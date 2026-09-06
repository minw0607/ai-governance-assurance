#!/usr/bin/env python3
"""Validate library metadata, links, control references, and root-catalog consistency.

Checks performed:

1. Front matter parses as YAML and conforms to schema/metadata.schema.json.
2. artifact_id values are unique across the library.
3. Local Markdown links resolve (fenced code blocks excluded).
4. Control identifiers referenced in prose are defined in control-objectives.md.
5. The root README catalog agrees with each artifact's own version and status.
6. The README artifact-count badge matches the real count.
7. last_reviewed dates are not older than the staleness window (warning only).
8. The generated control coverage matrix is current.

Usage:
    python3 scripts/validate-library.py [--stale-days N] [--no-staleness]
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml jsonschema")

try:
    import jsonschema
except ImportError:  # pragma: no cover
    sys.exit("jsonschema is required: pip install pyyaml jsonschema")

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "metadata.schema.json"
CONTROLS_PATH = ROOT / "governance" / "control-framework" / "control-objectives.md"
README_PATH = ROOT / "README.md"

CONTENT_ROOTS = (
    "governance",
    "assessments",
    "testing",
    "checklists",
    "templates",
    "mappings",
    "references",
)

DEFAULT_STALE_DAYS = 120

LINK_RE = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
CONTROL_REF_RE = re.compile(
    r"(?<![A-Za-z0-9-])((?:GOV|DATA|SEC|QUAL|HUM|TPRM|AGT|OPS)-\d{2})(?![A-Za-z0-9-])"
)
CONTROL_DEF_RE = re.compile(
    r"^### ((?:GOV|DATA|SEC|QUAL|HUM|TPRM|AGT|OPS)-\d{2}) — ", re.M
)
# | [Title](path.md) | description | 0.1.0 | Draft |
README_ROW_RE = re.compile(
    r"\|\s*\[([^\]]+)\]\(([^)]+\.md)\)\s*\|[^|]*\|\s*(\d+\.\d+\.\d+)\s*\|\s*(\w+)\s*\|"
)
BADGE_RE = re.compile(r"Artifacts-(\d+)%20documents")


def split_front_matter(text: str) -> tuple[str | None, str]:
    """Return (front_matter_yaml, body). front_matter is None when absent."""
    if text.startswith("---\n") and "\n---\n" in text[4:]:
        raw, body = text[4:].split("\n---\n", 1)
        return raw, body
    return None, text


def strip_code_fences(text: str) -> str:
    """Blank out fenced code blocks so example links are not treated as real ones."""
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else line)
    return "\n".join(out)


def check_links(path: Path, text: str, errors: list[str]) -> None:
    relative = path.relative_to(ROOT)
    for target in LINK_RE.findall(strip_code_fences(text)):
        target = target.strip().split()[0].strip("<>")
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        local = unquote(target.split("#", 1)[0])
        if local and not (path.parent / local).resolve().exists():
            errors.append(f"{relative}: broken local link '{target}'")


def check_controls(path: Path, body: str, defined: set[str], errors: list[str]) -> None:
    relative = path.relative_to(ROOT)
    for control in sorted(set(CONTROL_REF_RE.findall(strip_code_fences(body)))):
        if control not in defined:
            errors.append(
                f"{relative}: references undefined control objective '{control}'"
            )


def normalize_dates(value):
    """YAML parses bare ISO dates into date objects; the schema types them as strings."""
    if isinstance(value, dict):
        return {k: normalize_dates(v) for k, v in value.items()}
    if isinstance(value, list):
        return [normalize_dates(v) for v in value]
    if isinstance(value, dt.date):
        return value.isoformat()
    return value


def validate_metadata(
    path: Path,
    raw: str,
    schema: dict,
    identifiers: dict[str, Path],
    errors: list[str],
    warnings: list[str],
    stale_before: dt.date | None,
) -> None:
    relative = path.relative_to(ROOT)
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        errors.append(f"{relative}: front matter is not valid YAML ({exc.__class__.__name__})")
        return
    if not isinstance(data, dict):
        errors.append(f"{relative}: front matter must be a YAML mapping")
        return

    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.Draft202012Validator.FORMAT_CHECKER
    )
    for error in sorted(
        validator.iter_errors(normalize_dates(data)), key=lambda e: list(e.path)
    ):
        location = ".".join(str(p) for p in error.path) or "(root)"
        errors.append(f"{relative}: metadata invalid at {location}: {error.message}")

    artifact_id = data.get("artifact_id")
    if isinstance(artifact_id, str):
        if artifact_id in identifiers:
            errors.append(
                f"{relative}: duplicate artifact_id '{artifact_id}' also used by "
                f"{identifiers[artifact_id].relative_to(ROOT)}"
            )
        else:
            identifiers[artifact_id] = path

    reviewed = data.get("last_reviewed")
    if stale_before and isinstance(reviewed, dt.date) and reviewed < stale_before:
        warnings.append(
            f"{relative}: last_reviewed {reviewed.isoformat()} is older than the review window"
        )


def check_readme_catalog(files: list[Path], errors: list[str]) -> None:
    """The root catalog advertises versions and statuses; they must be real."""
    readme = README_PATH.read_text(encoding="utf-8")

    for title, target, version, status in README_ROW_RE.findall(readme):
        path = ROOT / target
        if not path.exists():
            errors.append(f"README.md: catalog row '{title}' points at missing file '{target}'")
            continue
        raw, _ = split_front_matter(path.read_text(encoding="utf-8"))
        if raw is None:
            errors.append(
                f"README.md: catalog row '{title}' advertises version {version}/{status}, "
                f"but {target} has no front matter to validate it against"
            )
            continue
        data = yaml.safe_load(raw) or {}
        actual_version = str(data.get("version", ""))
        actual_status = str(data.get("status", ""))
        if actual_version != version:
            errors.append(
                f"README.md: '{title}' shows version {version}, {target} declares {actual_version}"
            )
        if actual_status.lower() != status.lower():
            errors.append(
                f"README.md: '{title}' shows status {status}, {target} declares {actual_status}"
            )

    badge = BADGE_RE.search(readme)
    if not badge:
        errors.append("README.md: artifact-count badge not found or not in the expected format")
    elif int(badge.group(1)) != len(files):
        errors.append(
            f"README.md: artifact badge claims {badge.group(1)} documents, library contains {len(files)}"
        )


def check_coverage_matrix(errors: list[str]) -> None:
    script = ROOT / "scripts" / "build-coverage-matrix.py"
    if not script.exists():
        return
    result = subprocess.run(
        [sys.executable, str(script), "--check"], capture_output=True, text=True
    )
    if result.returncode != 0:
        errors.append(f"control coverage matrix: {result.stdout.strip() or 'stale'}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stale-days", type=int, default=DEFAULT_STALE_DAYS)
    parser.add_argument("--no-staleness", action="store_true")
    args = parser.parse_args()

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    defined_controls = set(CONTROL_DEF_RE.findall(CONTROLS_PATH.read_text(encoding="utf-8")))
    stale_before = (
        None
        if args.no_staleness
        else dt.date.today() - dt.timedelta(days=args.stale_days)
    )

    identifiers: dict[str, Path] = {}
    errors: list[str] = []
    warnings: list[str] = []
    artifacts: list[Path] = []

    paths: list[Path] = []
    for directory in CONTENT_ROOTS:
        root = ROOT / directory
        if root.exists():
            paths.extend(sorted(root.rglob("*.md")))

    for path in paths:
        text = path.read_text(encoding="utf-8")
        raw, body = split_front_matter(text)
        relative = path.relative_to(ROOT)

        if raw is None:
            # Front matter is required everywhere except catalog pages, where it is optional.
            if path.name.lower() != "readme.md":
                errors.append(f"{relative}: missing YAML front matter")
        else:
            artifacts.append(path)
            validate_metadata(path, raw, schema, identifiers, errors, warnings, stale_before)

        check_links(path, text, errors)
        check_controls(path, body, defined_controls, errors)

    for extra in (README_PATH, ROOT / "CONTRIBUTING.md", ROOT / "CHANGELOG.md"):
        if extra.exists():
            check_links(extra, extra.read_text(encoding="utf-8"), errors)

    check_readme_catalog(artifacts, errors)
    check_coverage_matrix(errors)

    for warning in warnings:
        print(f"warning: {warning}")

    if errors:
        print("Library validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Validated {len(paths)} Markdown files, {len(artifacts)} artifacts, "
        f"{len(identifiers)} identifiers, and {len(defined_controls)} control objectives."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

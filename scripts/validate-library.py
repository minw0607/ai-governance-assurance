#!/usr/bin/env python3
"""Validate controlled front matter and local Markdown links."""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
CONTENT_ROOTS = ("governance", "assessments", "testing", "checklists", "templates", "mappings", "references")
REQUIRED = ("schema_version", "artifact_id", "title", "artifact_class", "artifact_type", "status", "version", "last_reviewed")
CLASSES = {"governance", "assessment", "testing", "checklist", "template", "mapping", "reference"}
STATUSES = {"draft", "active", "deprecated", "archived"}
LINK_RE = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")


def scalar(front_matter: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*[\"']?([^\n\"']+)[\"']?\s*$", front_matter)
    return match.group(1).strip() if match else None


def validate_file(path: Path, identifiers: dict[str, Path]) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    relative = path.relative_to(ROOT)
    if path.name.lower() != "readme.md":
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            errors.append(f"{relative}: missing YAML front matter")
        else:
            front_matter = text.split("\n---\n", 1)[0][4:]
            values = {key: scalar(front_matter, key) for key in REQUIRED}
            for key, value in values.items():
                if not value:
                    errors.append(f"{relative}: missing required field '{key}'")
            artifact_id = values.get("artifact_id")
            if artifact_id:
                if artifact_id in identifiers:
                    errors.append(f"{relative}: duplicate artifact_id '{artifact_id}' also used by {identifiers[artifact_id].relative_to(ROOT)}")
                identifiers[artifact_id] = path
            if values.get("artifact_class") and values["artifact_class"] not in CLASSES:
                errors.append(f"{relative}: invalid artifact_class '{values['artifact_class']}'")
            if values.get("status") and values["status"] not in STATUSES:
                errors.append(f"{relative}: invalid status '{values['status']}'")
            if values.get("version") and not re.fullmatch(r"\d+\.\d+\.\d+", values["version"]):
                errors.append(f"{relative}: version must use X.Y.Z")
            if values.get("last_reviewed"):
                try:
                    dt.date.fromisoformat(values["last_reviewed"])
                except ValueError:
                    errors.append(f"{relative}: last_reviewed must be ISO YYYY-MM-DD")

    for target in LINK_RE.findall(text):
        target = target.strip().split()[0].strip("<>")
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        local = unquote(target.split("#", 1)[0])
        if local and not (path.parent / local).resolve().exists():
            errors.append(f"{relative}: broken local link '{target}'")
    return errors


def main() -> int:
    identifiers: dict[str, Path] = {}
    errors: list[str] = []
    files: list[Path] = []
    for directory in CONTENT_ROOTS:
        root = ROOT / directory
        if root.exists():
            files.extend(sorted(root.rglob("*.md")))
    for path in files:
        errors.extend(validate_file(path, identifiers))
    if errors:
        print("Library validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {len(files)} Markdown files and {len(identifiers)} artifact identifiers.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

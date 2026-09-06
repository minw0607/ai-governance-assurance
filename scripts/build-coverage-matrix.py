#!/usr/bin/env python3
"""Regenerate the control coverage matrix from control references in the library.

The matrix is a derived artifact: it indexes every control objective defined in
control-objectives.md against every other artifact that references it. Run this
after adding, renaming, or removing control references.

    python3 scripts/build-coverage-matrix.py [--check]

--check exits non-zero if the committed matrix is stale, for use in CI.
"""

from __future__ import annotations

import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / "governance" / "control-framework" / "control-objectives.md"
TARGET = ROOT / "governance" / "control-framework" / "control-coverage-matrix.md"

CONTROL_RE = re.compile(r"(?<![A-Za-z0-9-])((?:GOV|DATA|SEC|QUAL|HUM|TPRM|AGT|OPS)-\d{2})(?![A-Za-z0-9-])")
DEFINITION_RE = re.compile(r"^### ((?:GOV|DATA|SEC|QUAL|HUM|TPRM|AGT|OPS)-\d{2}) — (.+)$", re.M)

GROUPS = [
    ("GOV", "1. Governance and lifecycle"),
    ("DATA", "2. Data, privacy, and intellectual property"),
    ("SEC", "3. Architecture, security, and supply chain"),
    ("QUAL", "4. Model and system quality"),
    ("HUM", "5. Human oversight, transparency, and use"),
    ("TPRM", "6. Third-party risk"),
    ("AGT", "7. Agentic AI"),
    ("OPS", "8. Monitoring, incidents, and change"),
]

CLASS_LABEL = {
    "checklists": "checklist",
    "testing": "testing",
    "templates": "template",
    "mappings": "mapping",
    "governance": "governance",
    "assessments": "assessment",
    "references": "reference",
}


def defined_controls() -> dict[str, str]:
    return dict(DEFINITION_RE.findall(SOURCE.read_text(encoding="utf-8")))


def label(relative: str) -> str:
    """Build a link label that stays unambiguous across similarly named files."""
    parts = pathlib.Path(relative).parts
    stem = pathlib.Path(relative).stem
    topic = parts[1].replace("-", " ") if len(parts) > 2 else stem.replace("-", " ")
    if stem == "scenario-library":
        text = f"{topic} scenarios"
    elif stem == "testing-guide":
        text = f"{topic} tests"
    elif stem == "README":
        text = f"{topic} catalog"
    else:
        text = stem.replace("-", " ")
    prefix = CLASS_LABEL.get(parts[0], parts[0])
    return f"[{prefix}: {text}](../../{relative})"


def strip_front_matter(text: str) -> str:
    """Control references in prose count; provenance labels in front matter do not."""
    if text.startswith("---\n") and "\n---\n" in text[4:]:
        return text[4:].split("\n---\n", 1)[1]
    return text


def collect_references() -> dict[str, set[str]]:
    references: dict[str, set[str]] = collections.defaultdict(set)
    for path in sorted(ROOT.rglob("*.md")):
        if any(part.startswith(".") for part in path.parts) or path == SOURCE or path == TARGET:
            continue
        relative = path.relative_to(ROOT).as_posix()
        for control in set(CONTROL_RE.findall(strip_front_matter(path.read_text(encoding="utf-8")))):
            references[control].add(relative)
    return references


def render(titles: dict[str, str], references: dict[str, set[str]]) -> str:
    lines = [
        "---",
        'schema_version: "1.0"',
        "artifact_id: GOV-CTRL-002",
        "title: Control Coverage Matrix",
        "artifact_class: governance",
        "artifact_type: control-framework",
        "domains:",
        "  - internal-control",
        "  - traceability",
        "  - assurance",
        "applies_to:",
        "  - generative-ai",
        "  - agentic-ai",
        "  - machine-learning",
        "industries:",
        "  - cross-industry",
        "lifecycle_stages:",
        "  - validation",
        "  - deployment",
        "  - operation",
        "status: draft",
        'version: "0.1.0"',
        "last_reviewed: 2026-09-05",
        "---",
        "",
        "# Control Coverage Matrix",
        "",
        "## Purpose",
        "",
        "This is the reverse index for the [Enterprise AI Control Objectives](control-objectives.md): "
        "for each objective, which library artifacts govern it, verify it, test it, and record its evidence.",
        "",
        "Use it two ways:",
        "",
        "- **Forward** — from a control objective, find the checklist that gates it, the scenarios that test it, "
        "and the template that records the result.",
        "- **Backward** — from a coverage question (\"what evidences `AGT-06`?\"), reach every artifact that "
        "touches it without reading the whole library.",
        "",
        "An objective with no testing coverage is a control that can be asserted but not demonstrated. "
        "Those are listed under [coverage gaps](#coverage-gaps).",
        "",
        "> **This file is generated.** Run `python3 scripts/build-coverage-matrix.py` after changing control "
        "references. `scripts/validate-library.py` fails if a referenced identifier is not defined, or if this "
        "file is stale.",
        "",
        "## Matrix",
    ]

    gaps: list[str] = []
    for prefix, heading in GROUPS:
        lines += ["", f"### {heading}", "", "| Objective | Title | Referenced by |", "|---|---|---|"]
        for control in sorted(c for c in titles if c.startswith(prefix + "-")):
            paths = sorted(references.get(control, ()))
            if paths:
                cell = "; ".join(label(p) for p in paths)
            else:
                gaps.append(control)
                cell = "*not referenced*"
            lines.append(f"| `{control}` | {titles[control]} | {cell} |")

    lines += ["", '<a id="coverage-gaps"></a>', "", "## Coverage gaps", ""]
    if gaps:
        lines.append(
            "These objectives are defined but not referenced by any checklist, scenario, template, or mapping. "
            "Each is either a genuine gap or an objective that should be merged:"
        )
        lines.append("")
        lines += [f"- `{control}` — {titles[control]}" for control in gaps]
    else:
        lines.append("Every control objective is referenced by at least one other artifact.")

    lines += [
        "",
        "## How to use this in an assurance engagement",
        "",
        "1. Determine applicable objectives from the [risk tier](../risk-tiering/ai-risk-tiering-framework.md) "
        "and system boundary — not every objective applies to every system.",
        "2. For each applicable objective, take the checklist item as the control expectation and the scenario "
        "as the test procedure.",
        "3. Record the result against the objective identifier using the "
        "[test-case](../../templates/test-case-template.md) and "
        "[findings](../../templates/findings-report-template.md) templates.",
        "4. Report coverage as *objectives tested / objectives applicable*, and state which applicable "
        "objectives were not tested and why.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    titles = defined_controls()
    if not titles:
        print(f"No control objectives found in {SOURCE.relative_to(ROOT)}", file=sys.stderr)
        return 1
    content = render(titles, collect_references())

    if "--check" in sys.argv:
        current = TARGET.read_text(encoding="utf-8") if TARGET.exists() else ""
        if current != content:
            print("Control coverage matrix is stale. Run: python3 scripts/build-coverage-matrix.py")
            return 1
        print("Control coverage matrix is current.")
        return 0

    TARGET.write_text(content, encoding="utf-8")
    referenced = sum(1 for c in titles if c in collect_references())
    print(f"Wrote {TARGET.relative_to(ROOT)}: {len(titles)} objectives, {referenced} referenced.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Contributing

Contributions should make the library more accurate, usable, and auditable. Open an issue before a large restructuring or taxonomy change.

## Editorial principles

- Organize by artifact purpose, then topic, then document.
- Distinguish legal requirements, supervisory guidance, voluntary standards, and internal good practice.
- Prefer primary and authoritative sources.
- State applicability limits and avoid presenting examples as universal requirements.
- Use testable language: identify the control objective, evidence, owner, cadence, and decision threshold.
- Preserve source attribution while rewriting content into a consistent library voice.
- Avoid vendor-specific UI instructions unless the artifact is explicitly product-specific and date-stamped.

## The root "Start here" table

New artifacts that answer a question a reader would actually arrive with should be added to the root README's **Start here** table, which is grouped by lifecycle stage: getting oriented, intake and approval, design and build, test and release, operate and change and respond, and prove and comply.

- Add the row to the stage at which the question arises, not the stage the artifact describes.
- Phrase the row as the reader's question in their words, not the artifact's title.
- Security questions belong in the stage where they arise rather than in a group of their own, because AI security is an overlay across the library rather than a stage of it.
- Where a stage grows past roughly five rows, route through an overlay or catalog page instead of adding a seventh row — the table is for finding the entry point, not for listing the library.
- Add a new stage only when a question genuinely fits none of the six; the catalog tables below the taxonomy exist for completeness.

## Metadata

Every substantive artifact must use the fields defined in [schema/metadata.md](schema/metadata.md). Use stable `artifact_id` values; do not recycle identifiers from retired artifacts.

Allowed status values are `draft`, `active`, `deprecated`, and `archived`.

## Control traceability

Artifacts reference the [control objectives](governance/control-framework/control-objectives.md) by identifier rather than restating them:

- checklist sections name the objectives their items evidence, and the lifecycle gate they serve;
- scenario entries name the objective they test;
- templates carry a control-objective field; and
- mappings carry a control-objective column.

A referenced identifier that is not defined fails validation. After changing control references, regenerate the coverage matrix:

```
python3 scripts/build-coverage-matrix.py
```

## Draft traceability

`source_artifacts` records which earlier working draft an artifact was consolidated from, using the `SRC-*` labels defined in the [register](references/source-register.md). It is an editorial trace, not a citation: authority for any regulatory, standards, or product statement is the primary source cited in the artifact itself.

Do not record filenames, paths, or personal references in metadata.

## Versioning

Use semantic versions for artifacts:

- **Patch:** clarity, typo, link, or non-substantive metadata correction.
- **Minor:** new procedure, control, section, or backward-compatible expansion.
- **Major:** changed scope, decision logic, scoring method, or control expectation.

A material regulatory or standards update normally requires at least a minor version and an entry in the root changelog.

## Review expectations

Before requesting review:

1. Run `python3 scripts/validate-library.py`.
2. Verify all links and source dates.
3. Confirm that examples are labeled as examples.
4. Check that legal and regulatory statements cite an authoritative source.
5. Confirm that no confidential, personal, or client information is included.

## Pull requests

Describe the purpose, affected artifacts, source updates, version changes, and validation performed. Use a draft pull request for substantial content migrations.

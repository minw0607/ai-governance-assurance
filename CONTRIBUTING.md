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

## Source provenance

Never record a source filename, path, organization, engagement, or person in the repository. Unpublished source material is referenced only by opaque `SRC-*` label in `source_artifacts`, and the label-to-file mapping stays local. Organization-specific, engagement-specific, and personally identifying content is excluded rather than generalized.

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

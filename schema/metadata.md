# Artifact Metadata Standard

Substantive Markdown artifacts begin with YAML front matter. The metadata supports discovery, independent versioning, review scheduling, and future catalog generation.

## Required fields

| Field | Purpose | Example |
|---|---|---|
| `schema_version` | Metadata contract version | `"1.0"` |
| `artifact_id` | Stable library identifier | `TEST-SEC-001` |
| `title` | Human-readable title | `Security Red Teaming Guide` |
| `artifact_class` | Primary purpose | `testing` |
| `artifact_type` | Document form | `testing-guide` |
| `status` | Lifecycle state | `draft` |
| `version` | Independent artifact version | `"0.1.0"` |
| `last_reviewed` | Most recent substantive review | `2026-08-17` |

## Recommended discovery fields

- `domains`: controlled risk or governance topics.
- `applies_to`: technologies such as `generative-ai`, `llm`, `rag`, and `agentic-ai`.
- `industries`: sector-specific applicability; use `cross-industry` when general.
- `deployment_models`: `api`, `managed-api`, `saas`, `on-premises`, or `hybrid`.
- `lifecycle_stages`: `intake`, `design`, `development`, `validation`, `deployment`, `operation`, or `retirement`.
- `source_artifacts`: provenance labels for migrated internal source material.

## Controlled artifact classes

`governance`, `assessment`, `testing`, `checklist`, `template`, `mapping`, and `reference`.

## Example

```yaml
---
schema_version: "1.0"
artifact_id: ASSESS-VENDOR-001
title: GenAI Vendor Assessment Framework
artifact_class: assessment
artifact_type: framework
domains:
  - third-party-risk
  - ai-governance
applies_to:
  - generative-ai
  - agentic-ai
industries:
  - financial-services
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
---
```

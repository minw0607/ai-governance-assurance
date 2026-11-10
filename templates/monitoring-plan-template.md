---
schema_version: "1.0"
artifact_id: TMPL-MON-001
title: AI Monitoring Plan Template
artifact_class: template
artifact_type: template
domains:
  - monitoring
  - metrics
  - incident-response
applies_to:
  - generative-ai
  - rag
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
  - deployment
  - operation
status: draft
version: "0.2.0"
last_reviewed: 2026-11-10
---

# AI Monitoring Plan

## Record

- System/use case and risk tier:
- Production owner / risk reviewer:
- Validated baseline and release version:
- Monitoring start / review cadence:

## Measures and actions

| Risk | Control objective | Metric or review | Segment | Source | Cadence | Threshold | Response | Owner |
|---|---|---|---|---|---|---|---|---|

Use the identifiers from the [control objectives](../governance/control-framework/control-objectives.md) (for example `OPS-01`, `QUAL-03`, `AGT-03`) so monitoring coverage can be reconciled against the control framework.

Cover each of the five measure categories as applicable, so a gap is visible as an empty category rather than an absent line:

| Category | Typical measures |
|---|---|
| Performance | Task success, accuracy, factuality, retrieval quality, severe-error and abstention rates, completion rates |
| Risk and compliance | Policy violations, sensitive-data exposure, unauthorized access attempts, regulatory and contractual breaches |
| Model behavior | Hallucination rate, unexpected or out-of-scope output, bias indicators, behavioral drift, abnormal tool or destination use |
| Operational | Availability, latency, error and retry rates, usage trends, cost and resource consumption, per-agent attribution |
| Human oversight | Escalation, override and abstention rates, complaint and appeal volume with outcomes, reviewer feedback and reported difficulty |

Also include identity, provider change, and documentation completeness where applicable. Set the cadence per measure from the system's risk tier — see [minimum assurance by tier](../governance/risk-tiering/ai-risk-tiering-framework.md) — rather than applying one frequency across the portfolio.

## Sampling and evaluation

[Define production sampling, privacy safeguards, evaluator calibration, human review, uncertainty, and retention.]

## Alerts and incidents

[Define severity, notification, containment, fallback, rollback, kill switch, evidence preservation, and regulatory/customer escalation.]

## Change and reassessment triggers

[List model/provider, prompt, retrieval, data, tool, permission, use, scale, law, incident, and threshold changes that require regression or reassessment.]

## Reporting and governance

[Define dashboards, recipients, decision forum, issue aging, exceptions, and plan review.]

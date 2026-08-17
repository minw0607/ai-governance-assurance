---
schema_version: "1.0"
artifact_id: ASSESS-READY-002
title: AI Governance Readiness Scoring Guide
artifact_class: assessment
artifact_type: scoring-guide
domains:
  - governance-readiness
  - scoring
applies_to:
  - generative-ai
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - GenAI MRM Survey with Heatmap v2.xlsx
---

# AI Governance Readiness Scoring Guide

## Item scoring

| Response | Score |
|---|---:|
| Yes / fully implemented with evidence | 1.00 |
| Partially implemented or inconsistently evidenced | 0.50 |
| No / not implemented | 0.00 |
| Not applicable with approved rationale | Excluded |

For autonomy maturity, use: advisory only `1.00`, human-in-the-loop `0.75`, human-on-the-loop `0.50`, fully autonomous `0.25`. This is a control-readiness indicator, not a statement that advisory systems are always low risk or autonomous systems are always unacceptable.

## Category weighting

Suggested starting weights:

| Category | Weight |
|---|---:|
| Governance and inventory | 15% |
| Autonomy and human oversight | 20% |
| Data and privacy | 20% |
| Performance and hallucination | 20% |
| Explainability and auditability | 15% |
| Third-party and vendor risk | 10% |

Adjust weights before assessment based on organizational context. Calculate category scores from applicable items, then the weighted overall score.

## Interpretation

| Score | Indicative maturity |
|---:|---|
| 0.80–1.00 | Strong controls; validate operating effectiveness and continue improvement |
| 0.60–0.79 | Moderate; address inconsistency, evidence gaps, and coverage |
| 0.40–0.59 | Elevated risk; prioritize remediation and restrict higher-risk use |
| Below 0.40 | High risk; foundational governance is not ready for material deployment |

Scores do not replace review of critical gaps. A single missing control may be decisive when it relates to prohibited use, sensitive data, consequential action, or legal obligation.

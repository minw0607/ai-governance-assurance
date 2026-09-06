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
  - SRC-MRM-01
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

## Interpretation and approval authority

An enterprise readiness score that does not change what the organization is allowed to do is a report, not a control. The band therefore carries two things: an indicative maturity view, and a ceiling on the [risk tier](../../governance/risk-tiering/ai-risk-tiering-framework.md) that may be approved at [stage gate G1](../../governance/lifecycle/stage-gates.md).

<a id="readiness-and-approval-authority"></a>

| Score | Indicative maturity | Max tier approvable under normal authority | Additional conditions above that tier |
|---:|---|---|---|
| 0.80–1.00 | Strong controls; validate operating effectiveness and continue improvement | Tier 1 | — |
| 0.60–0.79 | Moderate; address inconsistency, evidence gaps, and coverage | Tier 2 | Tier 1 also requires named compensating controls for the deficient categories and a shortened reassessment interval |
| 0.40–0.59 | Elevated risk; prioritize remediation and restrict higher-risk use | Tier 3 | Tier 1 and Tier 2 also require a dated remediation plan, or approval as a time-boxed pilot with a restricted population and restricted data |
| Below 0.40 | High risk; foundational governance is not ready for material deployment | Tier 4 | Material deployment deferred; permit only isolated experimentation on synthetic or public data |

**Approval authority is set by the tier, not by this table.** The [minimum assurance by tier](../../governance/risk-tiering/ai-risk-tiering-framework.md#minimum-assurance-by-tier) table already fixes who approves each tier — Tier 1 requires executive or risk-committee approval at every readiness band, including the highest. The right-hand column above is *additional* to that authority, never a substitute for it and never a relaxation of it.

Scores do not replace review of critical gaps. A single missing control may be decisive when it relates to prohibited use, sensitive data, consequential action, or legal obligation.

**Category scores govern, not just the overall score.** Use the category most relevant to the proposed use case. A customer-facing assistant over regulated records is constrained by the data and privacy category, whatever the weighted total says; an agent with write access is constrained by autonomy and human oversight. A strong overall score built on weak performance in the category that matters for this use case does not support approval (`GOV-02`, `GOV-06`).

**Restriction is not the only response.** A low band can also be met by narrowing scope — smaller population, non-regulated data, advisory-only output, shorter approval expiry — so that the use case moves to a tier the organization is ready to govern.

**This mapping is a configurable starting point, not a standard.** No regulation or framework prescribes a readiness-to-tier relationship. Set the bands, tiers, and escalation authority to the organization's risk appetite before the first assessment, approve them through the governance forum (`GOV-04`), and record the agreed mapping with the assessment so results cannot be reinterpreted after the fact.


## Related artifacts

- [Readiness Assessment Checklist](checklist.md)
- [Control Objectives](../../governance/control-framework/control-objectives.md)
- [Risk Tiering Framework](../../governance/risk-tiering/ai-risk-tiering-framework.md)

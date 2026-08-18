---
schema_version: "1.0"
artifact_id: ASSESS-VENDOR-003
title: AI Vendor Assessment Scoring Guide
artifact_class: assessment
artifact_type: scoring-guide
domains:
  - third-party-risk
  - scoring
  - risk-acceptance
applies_to:
  - generative-ai
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
  - procurement
  - validation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - GenAI Vendor Assessment Framework.docx
---

# AI Vendor Assessment Scoring Guide

## Criterion score

| Score | Rating | Evidence-based definition |
|---:|---|---|
| 4 | Fully meets | Requirement is satisfied with current, relevant, independently supportable evidence and no material gap |
| 3 | Substantially meets | Requirement is largely satisfied; minor limitations have low residual risk and defined remediation |
| 2 | Partially meets | Material gap or uncertainty exists; compensating controls and enhanced oversight are required |
| 1 | Minimally meets | Significant weakness, weak evidence, or limited customer control; use requires exceptional justification |
| 0 | Does not meet | Requirement is not satisfied or evidence contradicts the assertion |
| N/A | Not applicable | Applicability rationale is documented and approved; excluded from denominator |

## Evidence confidence

Record confidence separately from control score:

- **High:** current primary evidence, tested or independently assured.
- **Moderate:** credible documentation with limited validation.
- **Low:** self-attestation, incomplete scope, stale evidence, or unresolved contradiction.

A high control score with low confidence remains an assessment gap.

## Weighting

Weight domains based on the proposed use. For example, a confidential enterprise knowledge assistant should emphasize data boundaries, identity, retrieval, and change management; a transaction agent should emphasize authorization, action controls, traceability, resilience, and kill-switch capability.

Calculate the weighted average only after blockers and evidence confidence are reviewed. Do not let strengths in unrelated domains offset a mandatory failure.

## Decision bands

| Weighted score | Indicative conclusion |
|---:|---|
| 3.50–4.00 | Strong control posture; proceed subject to use-case testing and standard conditions |
| 3.00–3.49 | Generally adequate; close material gaps and confirm conditions |
| 2.50–2.99 | Conditional; compensating controls, restricted scope, and enhanced monitoring required |
| 2.00–2.49 | Weak; pilot or low-risk use only with explicit risk acceptance |
| Below 2.00 | Unacceptable absent fundamental remediation |

The decision owner may be more conservative based on tier, blockers, low evidence confidence, or concentration risk.

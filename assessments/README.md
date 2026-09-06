---
schema_version: "1.0"
artifact_id: ASSESS-CAT-000
title: Assessments Catalog and Readiness Model
artifact_class: assessment
artifact_type: catalog
domains:
  - readiness
  - ai-governance
  - assurance
applies_to:
  - generative-ai
  - llm
  - rag
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
  - intake
  - design
  - validation
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-23
---

# Assessments

Assessment artifacts answer: **What should be evaluated before, during, or after adoption?**

In practice this is the question most organizations call **"AI readiness."** That term carries at least three distinct meanings, and conflating them is the most common source of confusion in enterprise discussions.

## What "AI readiness" means here

| Sense | Question | Owner | Measured in | In this library |
|---|---|---|---|---|
| **Adoption readiness** | Can we get value from this? Data foundations, platform, talent, use-case pipeline, change management. | CIO / CDO | Capability | **Out of scope** — see below |
| **Governance readiness** | Can we control this? Inventory, classification, ownership, oversight, prohibited use, escalation. | Risk and compliance | Maturity | [Governance Readiness Assessment](readiness-assessment/checklist.md) (enterprise); [Use-Case Assessment](use-case-assessment/checklist.md) (per system) |
| **Assurance readiness** | Can we *demonstrate* it to a third party — regulator, auditor, certification body, enterprise customer? | Internal audit / second line | Evidence | [Examination Readiness](../checklists/examination-readiness.md); [Agentic AI Audit Readiness](../checklists/agentic-ai-audit-readiness.md) |

The three fail independently. High adoption readiness with low governance readiness produces fast deployment and a growing undocumented inventory. High governance readiness with low assurance readiness produces controls that are designed but cannot be evidenced when an examiner asks for a sample.

**Adoption readiness is deliberately out of scope.** This library covers governance, control, and evidence. It does not assess data-platform maturity, talent, or the commercial case for adoption, and a strong score here does not indicate that an organization is equipped to deliver AI value.

## Two levels of governance readiness

Readiness is assessed at two levels, and they answer different questions on different cadences.

| | Enterprise level | Use-case level |
|---|---|---|
| Artifact | [Governance Readiness Assessment](readiness-assessment/checklist.md) | [Use-Case Assessment](use-case-assessment/checklist.md) |
| Question | Is the organization ready to govern AI at all? | Is *this* use permitted, and at what tier and review depth? |
| Nature | Scored maturity, weighted across categories | Intake decision — permit, restrict, or reject |
| Output | A band (see the [scoring guide](readiness-assessment/scoring-guide.md)) | A tier, a control set, and an approval |
| Cadence | Periodic; annually or after material change | Per use case, at [stage gate G1](../governance/lifecycle/stage-gates.md) |
| Control objectives | `GOV-03`, `GOV-04`, `GOV-05` | `GOV-01`, `GOV-02` |

The levels are coupled: enterprise readiness constrains what use cases may be approved. A weak enterprise score is not a report to be filed — it limits the risk tier the organization can responsibly take on. That coupling is defined in the [readiness scoring guide](readiness-assessment/scoring-guide.md#readiness-and-approval-authority).

## Distinguish assessments from gates

A **readiness assessment** is a scored maturity view at a point in time. A **gate** is a binary decision at a lifecycle step. They are different artifact classes for a reason:

- Treating a gate as a score lets `0.7` ship.
- Treating a score as a gate turns maturity assessment into an audit, and candour in the responses disappears.

Gates live in [checklists](../checklists/README.md): [pre-deployment](../checklists/pre-deployment.md), [production readiness](../checklists/production-readiness.md), and the audit- and examination-readiness checklists. Note that "readiness" in those filenames means *readiness of a system or an evidence package* — a gate — not organizational maturity.

## Catalog

| Assessment | Level | Purpose |
|---|---|---|
| [Governance Readiness Assessment](readiness-assessment/checklist.md) | Enterprise | Scored governance, data, quality, oversight, and agentic-AI maturity |
| [Readiness Scoring Guide](readiness-assessment/scoring-guide.md) | Enterprise | Item scoring, category weighting, interpretation bands, and approval coupling |
| [Use-Case Assessment](use-case-assessment/checklist.md) | Use case | Intake, inherent-risk assessment, and tier determination at gate G1 |
| [Vendor Assessment Framework](vendor-assessment/framework.md) | Supplier | Risk-based assessment for AI and foundation-model vendors |
| [Vendor Questionnaire](vendor-assessment/questionnaire.md) | Supplier | Evidence-oriented due-diligence questions |
| [Vendor Scoring Guide](vendor-assessment/scoring-guide.md) | Supplier | Domain weighting and interpretation |

Assessment results should identify evidence, gaps, residual risk, ownership, and decisions. A completed questionnaire without evidence is not an assurance conclusion.

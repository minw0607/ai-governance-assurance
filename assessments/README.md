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
last_reviewed: 2026-09-05
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

## Worked examples

The figures, organizations, and outcomes below are invented to illustrate how the artifacts interact. They are not benchmarks and not recommendations.

### Example 1 — the three senses fail independently

| | Adoption | Governance | Assurance | What it looks like in practice |
|---|---|---|---|---|
| Retailer, 18 months into a copilot rollout | Strong | Weak | Weak | Deployment is fast and popular. Nobody can answer "how many AI systems do we have?" because there is no inventory and embedded vendor features were never registered. The first real incident is also the first time anyone assembles a system boundary. |
| Regional bank with a mature model-risk function | Weak | Strong | Moderate | Policies, forums, tiering, and prohibited uses are all in place before there is much to govern. The programme is well run and is increasingly described internally as an obstacle, because governance got ahead of adoption. |
| Insurer preparing for its first regulatory examination | Moderate | Strong | Weak | Human review is required by policy and reviewers do perform it. When the examiner asks for evidence that the control operated across a sample of Q2 decisions, the review left no durable record. The control was designed, never evidenced. |

The third row is the most common surprise. Governance readiness measures whether a control exists; assurance readiness measures whether you can prove it operated. Passing the [readiness assessment](readiness-assessment/checklist.md) does not imply passing the [examination-readiness checklist](../checklists/examination-readiness.md).

### Example 2 — the ceiling, and why the category score governs

An organization assesses at **0.62 overall**. Per the [interpretation and approval authority table](readiness-assessment/scoring-guide.md#readiness-and-approval-authority), that band makes Tier 2 approvable under normal authority. Category scores are uneven:

| Category | Score |
|---|---:|
| Governance and inventory | 0.80 |
| Autonomy and human oversight | 0.75 |
| **Data and privacy** | **0.48** |
| Performance and hallucination | 0.65 |
| Explainability and auditability | 0.55 |

A proposed customer-facing assistant answers questions over regulated customer records. It classifies as **Tier 2**.

Reading the overall score alone, this is approvable. But the category that dominates this use case is data and privacy at `0.48`, a band that supports only **Tier 3**. The use case is therefore *not* approvable under normal authority, despite a comfortable overall score. The `0.62` was carried by categories that have little to do with the risk this system actually presents.

Three legitimate paths from here, none of which is re-tiering the use case downward:

1. **Escalate** — approve at Tier 2 with a dated remediation plan for the data and privacy gaps, plus named compensating controls and a shortened reassessment interval.
2. **Reduce scope** — run against a non-regulated corpus for an internal population, advisory-output only. The use case genuinely becomes Tier 3 and is approvable now, with the regulated corpus deferred to a later gate.
3. **Defer** — close the data and privacy gaps first, reassess, then bring the original scope back to G1.

Path 2 is the one most often missed. The ceiling is meant to shape use cases, not merely block them.

### Example 3 — the levels are independent in both directions

A strong enterprise score does not approve a weak use case. An organization at **0.85** proposes an agent with write access to a payments system and no tested kill switch. Enterprise readiness permits Tier 1; the [use-case assessment](use-case-assessment/checklist.md) still fails at G1 on `AGT-02` (consequential-action gating) and `AGT-03` (execution trace and intervention).

Enterprise readiness sets the ceiling. It never substitutes for the use-case gate.

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

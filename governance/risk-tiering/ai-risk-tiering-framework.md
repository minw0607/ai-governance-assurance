---
schema_version: "1.0"
artifact_id: GOV-RISK-001
title: AI Risk Tiering Framework
artifact_class: governance
artifact_type: framework
domains:
  - risk-tiering
  - impact-assessment
  - control-calibration
applies_to:
  - generative-ai
  - agentic-ai
  - machine-learning
industries:
  - cross-industry
lifecycle_stages:
  - intake
  - design
  - validation
status: draft
version: "0.3.0"
last_reviewed: 2026-09-18
source_artifacts:
  - SRC-AGT-01
  - SRC-VEND-01
  - SRC-POL-01
---

# AI Risk Tiering Framework

## Objective

Classify AI use cases consistently so governance, testing, approval, and monitoring are proportionate to potential harm. Tiering is an informed decision, not a purely mechanical score.

## Classification dimensions

Assess each dimension using the highest credible impact under intended use and reasonably foreseeable misuse:

| Dimension | Lower-risk indicators | Higher-risk indicators |
|---|---|---|
| Decision impact | Drafting or administrative support | Credit, employment, healthcare, safety, legal, eligibility, or regulatory decisions |
| Human oversight | Output is optional and readily verified | Automation bias, ineffective review, or no meaningful intervention |
| Autonomy | No tools or external actions | Multi-step action, write access, transactions, code execution, or external communication |
| Data | Public or synthetic data | Sensitive, regulated, confidential, biometric, or large-scale personal data |
| Scale and exposure | Small internal pilot | Public-facing, enterprise-wide, high-volume, or vulnerable populations |
| Reversibility | Error is cheap and readily corrected | Irreversible, delayed, systemic, or difficult-to-detect harm |
| Model uncertainty | Bounded task with reliable ground truth | Open-ended task, emergent behavior, weak observability, or unverifiable output |
| Dependency | Isolated assistance | Embedded in critical processes or relied upon by downstream systems |

## Tiers

| Tier | Description | Illustrative uses |
|---|---|---|
| Tier 1 — Critical | Failure could cause severe legal, financial, safety, rights, or systemic harm; or the system can take consequential autonomous action | High-impact decisions, autonomous financial transactions, safety-critical control, privileged agents with irreversible actions |
| Tier 2 — High | Material decisions or sensitive operations with meaningful human oversight and containment | Decision support, customer-facing advice, production code generation, agents with bounded write access |
| Tier 3 — Moderate | Limited impact, reversible outcomes, and effective review | Internal summarization, analysis support, controlled knowledge assistants |
| Tier 4 — Low | Minimal exposure, no sensitive data, no consequential action | Isolated experimentation with synthetic/public data, low-impact drafting |

## Mandatory escalation factors

Escalate to at least Tier 2 when the system:

- affects access to essential services or protected rights;
- processes sensitive or regulated data at material scale;
- communicates externally without pre-publication review;
- generates production code or security configuration;
- uses retrieval over confidential repositories;
- can invoke tools with write, delete, transaction, identity, or communication privileges; or
- is difficult to observe, interrupt, or roll back.

Also escalate to at least Tier 2 when an agent uses persistent cross-session memory, can create or delegate to other agents, relies on externally managed MCP/A2A servers or tools, or can continue long-running work without contemporaneous review.

Escalate to Tier 1 when credible failure could create severe or irreversible harm, or when privileged autonomy is combined with untrusted input and sensitive data.

Tier 1 indicators for agentic systems include open-ended or recursive delegation, administrative or security-control authority, autonomous high-value transactions, cross-tenant reach, safety-critical action, inability to reconstruct material actions, or inability to contain and reconcile partially completed work.

## Agentic risk decision factors

For an agentic use case, record separately:

- highest autonomy mode and maximum duration without human intervention;
- reachable read, write, execute, communicate, transact, delete, identity, and administrative authority;
- credential and delegated-authority model, including parent/child propagation;
- tool, MCP/A2A, data, memory, network, destination, tenant, and environment reach;
- maximum steps, recursion/delegation depth, concurrency, cost, data volume, and transaction value;
- observability, intervention window, kill scope, rollback/compensation, and authoritative reconciliation; and
- credible combined failure involving untrusted input, sensitive data, privileged tools, persistent state, and external action.

## Minimum assurance by tier

| Requirement | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Documented use-case and impact assessment | Full | Full | Abbreviated | Basic |
| Architecture, data-flow, and threat modeling | Required | Required | Risk-based | Basic boundary review |
| Independent challenge | Independent validation | Independent review | Peer or second-line review | Owner approval |
| Adversarial and misuse testing | Comprehensive | Required | Targeted | As needed |
| Fairness and rights-impact testing | Required when relevant | Required when relevant | Risk-based | Normally not applicable |
| Production monitoring | Continuous or near-real-time for critical controls | Defined metrics and alerts | Periodic sampling | Basic incident monitoring |
| Change-triggered reassessment | Required | Required | Material changes | Scope changes |
| Approval authority | Executive/risk committee | Senior accountable owner plus risk | Business and technical owners | Designated owner |

## Shared-service tier inheritance

Tiering is a property of a **use case**. A shared AI service — one deployed system used by several teams or business units for different purposes — has no use case of its own; it has a portfolio of them.

For decisions that act on the service as a whole — change classification, testing depth, monitoring, and approval authority — the service **inherits the highest tier among its registered consuming use cases**. The inheriting tier is recomputed whenever a consumer is onboarded, retired, or re-tiered.

| Question | Tier that governs |
|---|---|
| How is this consumer's own use approved, controlled, and reviewed? | That consumer's assigned tier |
| How is a change to the shared service classified, tested, and approved? | The highest registered consumer tier |
| What assurance must the shared service itself carry? | The highest registered consumer tier |
| May a new consumer be onboarded at a tier above the service's current assurance? | Not until the service is assured at that tier |

Two consequences follow:

- A platform team cannot hold a lower tier than the business it serves. Onboarding a Tier 1 consumer raises the service to Tier 1 for change and assurance purposes, with the [minimum assurance](#minimum-assurance-by-tier) and approval authority that implies.
- Where the inherited tier is unaffordable, the remedy is to separate the consumer onto its own instance, configuration, or service — not to re-tier the consumer downward to fit the shared platform (`GOV-02`, `GOV-06`).

Record the inherited tier, the consumer it derives from, and the date on the service's inventory record. See the [AI Change Management Policy](../policies/change-management.md#shared-ai-services) for the resulting change requirements (`OPS-05`).

## Enterprise readiness ceiling

The tier an organization *assigns* is a property of the use case. The tier it may *approve* is additionally bounded by its own governance maturity: see [readiness and approval authority](../../assessments/readiness-assessment/scoring-guide.md#readiness-and-approval-authority). Where the two conflict, the assigned tier stands and the approval is escalated, scope-reduced, or deferred — never re-tiered downward to fit the available authority (`GOV-02`, `GOV-06`).

## Decision record

Record the tier, dimension-level rationale, assumptions, unresolved questions, required controls, approval authority, date, and reassessment triggers. The tier must be reconsidered when use, users, data, autonomy, model/provider, scale, or external obligations change.

## Related artifacts

- [Use-Case Assessment](../../assessments/use-case-assessment/checklist.md)
- [AI Lifecycle Stage Gates](../lifecycle/stage-gates.md)
- [Control Coverage Matrix](../control-framework/control-coverage-matrix.md)
- [Risk Assessment Template](../../templates/risk-assessment-template.md)

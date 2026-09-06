---
schema_version: "1.0"
artifact_id: ASSESS-USE-001
title: AI Use-Case Assessment Checklist
artifact_class: assessment
artifact_type: checklist
domains:
  - use-case-intake
  - impact-assessment
  - risk-tiering
applies_to:
  - generative-ai
  - agentic-ai
  - machine-learning
industries:
  - cross-industry
lifecycle_stages:
  - intake
  - design
status: draft
version: "0.2.0"
last_reviewed: 2026-08-18
source_artifacts:
  - SRC-AGT-01
  - SRC-POL-01
  - SRC-AUD-01
---

# AI Use-Case Assessment Checklist

## How to use this assessment

This is the **intake instrument** for [stage gate G1 — Intake and classify](../../governance/lifecycle/stage-gates.md). Completing it produces the G1 exit evidence: the intake record, prohibited-use determination, system-boundary description, and risk-tier rationale. The intake obligation itself is set by the [acceptable-use policy](../../governance/policies/acceptable-use.md); G1 defines when it happens; this checklist is what gets filled in.

Assess **use-case-level readiness** — whether this specific use is permitted and at what depth of review. Enterprise-level readiness is assessed separately in the [governance readiness assessment](../readiness-assessment/checklist.md), and it constrains the tier that may be approved here; see [readiness and approval authority](../readiness-assessment/scoring-guide.md#readiness-and-approval-authority).

Control objectives: `GOV-01` (approved use-case intake) and `GOV-02` (risk classification). Record the result using the [risk assessment template](../../templates/risk-assessment-template.md).

## Purpose and ownership

- [ ] Business problem, intended outcome, and alternatives are documented.
- [ ] Business and technical owners are named.
- [ ] Intended users, affected people, and decision recipients are identified.
- [ ] Success, failure, and stop criteria are measurable.
- [ ] Intended uses, prohibited uses, and foreseeable misuse are documented.

## Impact and dependency

- [ ] Consequences of inaccurate, harmful, delayed, unavailable, or manipulated output are assessed.
- [ ] The role of AI in decisions is clear: inform, recommend, rank, decide, or act.
- [ ] Human review is meaningful, timely, trained, and authorized.
- [ ] Reversibility, scale, vulnerable populations, and downstream reliance are evaluated.
- [ ] The [risk tier](../../governance/risk-tiering/ai-risk-tiering-framework.md) and rationale are recorded.

## Data and privacy

Apply the [AI Data Security & Governance Framework](../../governance/data-security-governance/framework.md) and [classification control matrix](../../governance/data-security-governance/data-classification-control-matrix.md) to the proposed processing pattern.

- [ ] Data sources, classifications, rights, lineage, regions, and retention are identified.
- [ ] Sensitive or regulated data use is necessary and approved.
- [ ] Training, improvement, logging, and provider reuse terms are understood.
- [ ] Data minimization, deletion, legal hold, and data-subject processes are designed.
- [ ] Data quality, representativeness, integrity, poisoning, and evaluation-contamination risks are assessed.
- [ ] RAG permissions, vector/index segregation, agent memory, and tool-data boundaries are designed where applicable.

## Architecture and security

- [ ] Models, prompts, retrieval, memory, tools, connectors, identities, and providers are mapped.
- [ ] Trust boundaries and untrusted content paths are threat-modeled.
- [ ] Least privilege, output validation, action authorization, logging, and secrets controls are defined.
- [ ] Fallback, containment, rollback, and kill-switch mechanisms are feasible.

## Agentic AI applicability

Complete this section when the system plans, uses tools, maintains state, delegates, communicates, or changes an external environment.

- [ ] Autonomy level, action authority, maximum duration, success/stop conditions, and prohibited actions are explicit.
- [ ] Human and workload identities, delegated authority, approval points, segregation of duties, and revocation are designed.
- [ ] Tool, MCP/A2A, server, schema, extension, agent, and downstream dependencies are inventoried and versioned.
- [ ] Memory, inter-agent context, action/state integrity, idempotency, reconciliation, and compensation are addressed.
- [ ] Maximum steps, retries, recursion/delegation depth, concurrency, cost, data volume, transaction value, and destinations are bounded.
- [ ] Long-horizon, adversarial, multi-agent, partial-failure, containment, recovery, and evidence-reconstruction tests are planned.

## Legal, rights, and conduct

- [ ] Applicable jurisdictions, sector rules, contracts, records duties, and disclosure obligations are identified.
- [ ] Discrimination, accessibility, intellectual-property, consumer, workforce, and contestability impacts are assessed.
- [ ] Legal or compliance interpretations are confirmed by accountable specialists.

## Assurance and operation

- [ ] Evaluation methods reflect the actual workflow and plausible failures.
- [ ] Acceptance thresholds and approval authority are defined before testing.
- [ ] Monitoring metrics, sampling, incidents, feedback, and change triggers are established.
- [ ] Vendor assessment and exit plan are complete where applicable.

## Decision

Record approval, conditions, rejected alternatives, unresolved risks, required evidence, owner, expiry/review date, and triggers for reassessment.

Confirm before approving that the assigned tier is within the band the current [enterprise readiness score](../readiness-assessment/scoring-guide.md#readiness-and-approval-authority) supports. Where it is not, either escalate to the authority that band requires, narrow the scope until the use case falls to a supportable tier, or defer.

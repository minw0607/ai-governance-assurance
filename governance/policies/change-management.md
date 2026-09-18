---
schema_version: "1.0"
artifact_id: GOV-POL-006
title: AI Change Management Policy
artifact_class: governance
artifact_type: policy
domains:
  - change-management
  - configuration-management
  - regression-testing
  - shared-services
applies_to:
  - generative-ai
  - rag
  - agentic-ai
  - machine-learning
industries:
  - cross-industry
lifecycle_stages:
  - development
  - deployment
  - operation
  - retirement
status: draft
version: "0.2.0"
last_reviewed: 2026-09-18
source_artifacts:
  - SRC-POL-01
  - SRC-TEST-01
---

# AI Change Management Policy

## Policy objective

Changes to AI behavior, data, access, or operating context must be identified, assessed, tested, approved, released, monitored, and reversible where practicable.

## Change scope

Changes include models and providers; versions and parameters; prompts and guardrails; retrieval sources, indexes, embeddings, and chunking; tools, permissions, connectors, and memory; application code; data schemas; user groups; intended use; scale; monitoring; and provider-controlled SaaS updates.

Scope also includes the **platform and infrastructure the system runs on**, which can move behavior without any change to the model or the prompt:

- inference runtime, serving stack, SDK/client library, and API version;
- compute, accelerator, region, availability zone, and failover target;
- container images, operating system, and dependency upgrades;
- orchestration, queueing, caching, batching, and concurrency settings;
- gateway, proxy, load balancer, timeout, retry, and truncation behavior;
- quota, rate-limit, and cost-control configuration;
- identity provider, authentication, and authorization integration;
- network, egress, and data-residency routing; and
- logging, tracing, and observability pipelines that carry the evidence.

Treat an infrastructure change as material whenever it can alter output, latency, availability, truncation, tool-call reliability, permission resolution, or the completeness of the audit trail — not because it is labelled infrastructure rather than AI.

## Requirements

1. **Record:** link each material change to an owner, rationale, affected components, risk assessment, and release record.
2. **Classify:** determine whether the change is standard, material, or emergency based on potential effect—not implementation size alone.
3. **Assess:** evaluate impact on legal obligations, data, security, performance, fairness, human oversight, and downstream processes.
4. **Test:** run targeted and regression tests with pre-defined acceptance criteria.
5. **Approve:** use authority commensurate with the system's tier and change impact.
6. **Release:** use staged rollout, version pinning, canarying, feature flags, or restricted cohorts when available.
7. **Monitor:** compare post-change behavior with baseline and investigate threshold breaches.
8. **Recover:** maintain rollback, fallback, containment, or disablement procedures.

For SaaS systems without version pinning, compensate with provider-change monitoring, golden test sets, increased sampling, restricted high-impact use, and rapid disablement. See the [Regression Testing Guide](../../testing/regression-testing/testing-guide.md).

## Shared AI services

A **shared AI service** is one deployed AI system used by more than one team, department, or business for materially different purposes. The requirements above assume a single system with a single owner, a single risk tier, and a single approver. A shared service breaks all three assumptions: one change made by the platform owner lands simultaneously on consumers who did not request it, cannot test it, and may not survive it.

The following requirements apply in addition to the requirements above (`OPS-05`).

### Consumer register

The platform owner must maintain, as part of the inventory record (`GOV-05`), a register of every consuming use case: consuming team, business owner, purpose, risk tier, data classes in use, acceptance criteria owner, notification contact, and whether the consumer can be held on the prior version independently.

A consumer that is not registered cannot be impact-assessed, notified, or tested. Unregistered consumption is a governance failure in its own right, not a reason to proceed.

### Inherited tier

A shared service inherits the **highest risk tier among its registered consuming use cases** for the purposes of change classification, testing depth, and approval authority. See [shared-service tier inheritance](../risk-tiering/ai-risk-tiering-framework.md#shared-service-tier-inheritance).

The platform team's own view of the change is not the governing view. A model upgrade that is routine for an internal drafting assistant is a Tier 1 change if one registered consumer uses the same service for eligibility decisions.

### Responsibility split

| Responsibility | Platform owner | Consuming business owner |
|---|---|---|
| Classify the change and determine the inherited tier | Accountable | Consulted |
| Maintain the shared golden suite and platform-level baseline | Accountable | Contributes cases |
| Define use-case acceptance criteria and the consumer test set | Consulted | Accountable |
| Execute consumer acceptance testing in the test window | Supports | Accountable |
| Accept or reject the change for that use case | Informed | Accountable |
| Obtain release approval at the inherited tier's authority | Responsible | Consulted |
| Sequence rollout, hold, and roll back | Accountable | Consulted |
| Monitor post-change behavior for that use case | Provides segmented data | Accountable |

Approval authority for the change itself is not the platform owner's to hold; it sits where the [RACI](../operating-model/roles-and-decision-rights.md) places it for the inherited tier. The platform owner must not accept upgrade risk on a consuming business owner's behalf. Silence from a consumer within the test window is not acceptance; it is an unassessed consumer, and must be treated as a hold or an explicit, recorded risk acceptance at the inherited tier.

## Pre-upgrade sequence for a shared service

Before launching any upgrade to a shared AI service — model version, provider, prompt, retrieval, tooling, or platform and infrastructure:

1. **Enumerate.** Take the affected consumers from the consumer register. Record any consumer discovered during the change that was not registered.
2. **Classify.** Determine materiality and the inherited tier. Where consumers differ in tier, the highest governs (`GOV-02`, `OPS-03`).
3. **Assess.** Evaluate the change against each consumer's obligations, data classes, human-oversight design, and downstream processes — not against the service in the abstract.
4. **Notify.** Give consumers the proposed change, the intended date, what is expected to move, what is not guaranteed to hold, the test window, the hold and objection route, and the fallback position. Notice period and test window should scale with the inherited tier.
5. **Test.** Run the shared golden suite against the production-intended configuration, and give each consumer the same window to run its own acceptance set (`QUAL-06`, `RGS-09`).
6. **Consolidate.** Apply the partial-failure rule below. Report results per consumer; never report a single averaged score across consumers.
7. **Approve.** Obtain release approval at the inherited tier's authority, plus per-consumer acceptance from each consuming business owner.
8. **Sequence.** Roll out in ascending order of consumer risk tier — lowest tier first — with a defined soak period and hold point between stages.
9. **Recover.** Verify rollback against the prior validated baseline before the first stage, or, where rollback is unavailable, follow the non-reversible change requirements below.
10. **Monitor.** Compare post-change behavior with the pre-change baseline **segmented by consumer** for a defined period, with named owners and thresholds per use case.

### Partial failure

The normal outcome of a shared-service upgrade is that some consumers pass and some do not. Decide in advance, and record the decision:

- A failure against any consumer's pre-agreed acceptance criteria blocks the upgrade **for that consumer**.
- Where the service cannot run split versions, a blocking failure for any consumer blocks the upgrade **entirely** until remediated, waived with compensating controls, or the affected consumer is deliberately suspended or restricted with recorded approval.
- A failure in a higher-tier consumer is never offset by passes in lower-tier consumers. An aggregate pass rate that hides a severe failure in one business unit is not an acceptable basis for release.
- Where a consumer is upgraded ahead of others, record the resulting version divergence in the inventory: two consumers on different baselines are two configurations to monitor, test, and evidence.

## Changes that cannot be rolled back

Rollback is a control only while the prior state remains available. It does not survive a retired model version, a withdrawn API version, a decommissioned region, or an irreversible schema or index migration.

When the prior state will become unavailable on a date the organization does not control:

- Treat the deprecation or end-of-life notice as the **start** of a change, not a notification of one, and open the change record on receipt (`TPRM-03`).
- Work back from the provider's deadline to set the internal cutover date, leaving time for consumer testing, remediation, and re-test — not the deadline itself.
- Identify the fallback that replaces rollback: an alternative version or provider, a degraded but acceptable configuration, a manual workflow, or disablement of the affected use case.
- Decide the disposition of any consumer that cannot pass acceptance before the deadline — restrict, suspend, migrate, or accept with conditions and an expiry — **before** the deadline, at the inherited tier's authority (`GOV-06`).
- Where the deadline will pass with a consumer unremediated, record it as an exception with a named owner and a closure date, not as an operational surprise.

Advance-notice periods, version availability during a test window, and rollback support are procurement requirements, not assumptions. See the [Third-Party Risk Policy](third-party-risk.md) and the [Vendor Questionnaire](../../assessments/vendor-assessment/questionnaire.md).

## Related artifacts

- [AI Lifecycle Stage Gates](../lifecycle/stage-gates.md) — change-to-gate routing, including shared services
- [AI Risk Tiering Framework](../risk-tiering/ai-risk-tiering-framework.md) — shared-service tier inheritance
- [Roles and Decision Rights](../operating-model/roles-and-decision-rights.md) — change approval authority
- [Regression Testing Guide](../../testing/regression-testing/testing-guide.md) and [scenario library](../../testing/regression-testing/scenario-library.md) — `RGS-01` onward
- [AI Ongoing Monitoring Checklist](../../checklists/ongoing-monitoring.md) and [Pre-Deployment Checklist](../../checklists/pre-deployment.md)

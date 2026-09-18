---
schema_version: "1.0"
artifact_id: CHECK-PRE-001
title: AI Pre-Deployment Checklist
artifact_class: checklist
artifact_type: checklist
domains:
  - pre-deployment
  - control-design
applies_to:
  - generative-ai
  - rag
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
  - design
  - validation
  - deployment
status: draft
version: "0.2.0"
last_reviewed: 2026-09-18
source_artifacts:
  - SRC-AUD-01
---

# AI Pre-Deployment Checklist

## How to use this checklist

**Lifecycle gate:** G2–G4 (design, build, validate) — see [AI Lifecycle Stage Gates](../governance/lifecycle/stage-gates.md).

Each section lists the [control objectives](../governance/control-framework/control-objectives.md) its items are intended to evidence. A checked box is not evidence; record the artifact, owner, date, and result against the named objective using the [test-case](../templates/test-case-template.md) and [findings](../templates/findings-report-template.md) templates.

**Relationship to production readiness.** This gate establishes that the design and behavior have been **validated** — evidence comes from the validation environment, including failure paths that cannot safely be exercised in production. The same control topics reappear in the [production readiness checklist](production-readiness.md) at G5, where they demand a different thing: evidence from the **production configuration**. The repetition is deliberate; completing one does not satisfy the other.


## Governance

**Control objectives:** GOV-01, GOV-02, GOV-04, GOV-05, TPRM-01, TPRM-02

- [ ] Use case, owners, intended users, affected parties, and prohibited uses are documented.
- [ ] Risk tier and applicable obligations are approved.
- [ ] Inventory record, architecture, data flow, dependencies, and lifecycle status are current.
- [ ] Vendor assessment and contract conditions are complete.

## Data and privacy

**Control objectives:** DATA-01, DATA-02, DATA-03, DATA-04, DATA-05, DATA-07, QUAL-04

- [ ] Data sources, rights, classifications, lineage, regions, retention, and deletion are approved.
- [ ] Provider training/reuse and logging terms match policy.
- [ ] Retrieval and connector permissions have been tested with negative cases.
- [ ] Sensitive test data is synthetic or separately approved.

## Security and resilience

**Control objectives:** SEC-01, SEC-02, SEC-03, SEC-04, SEC-05, SEC-06, OPS-02

- [ ] Threat model includes prompt injection, poisoning, output handling, supply chain, identity, and abuse.
- [ ] Least privilege, secrets, tool authorization, output validation, rate limits, and logging are implemented.
- [ ] Failure, timeout, dependency, fallback, rollback, and kill-switch behavior is tested in the validation environment, including failure paths that cannot safely be induced in production.
- [ ] Incident playbooks and escalation contacts are ready.

## Performance and impact

**Control objectives:** QUAL-01, QUAL-02, QUAL-03, QUAL-05, HUM-01, GOV-06

- [ ] Use-case-specific acceptance criteria were defined before execution.
- [ ] Functional, factuality, safety, fairness, privacy, workflow, and agentic tests are complete as applicable.
- [ ] Critical findings are closed or explicitly accepted with conditions.
- [ ] Human review is meaningful and tested for realistic workload.

## Operation

**Control objectives:** OPS-01, OPS-03, HUM-02, HUM-03, SEC-05

- [ ] Monitoring metrics, thresholds, sampling, alerts, owners, and response actions are approved.
- [ ] Change and regression process covers provider-controlled updates and platform/infrastructure changes made below the application layer.
- [ ] Users are trained on limitations, verification, prohibited use, and incident reporting.
- [ ] Records are reproducible and retained according to policy.

## Upgrading a shared service

**Control objectives:** OPS-05, OPS-03, QUAL-06, GOV-02, TPRM-03

Use this section when the system already runs and the change — model version, provider, prompt, retrieval, tooling, or platform and infrastructure — will reach more than one consuming team. It is the G4 revalidation for an upgrade, not a second release gate; see the [AI Change Management Policy](../governance/policies/change-management.md#pre-upgrade-sequence-for-a-shared-service).

- [ ] The consumer register is current and reconciled against actual usage; consumers found outside it are recorded and registered.
- [ ] The inherited tier is recomputed from the highest registered consumer and governs classification, testing depth, and approval authority.
- [ ] Each consumer's obligations, data classes, oversight design, and downstream processes were assessed — not the service in the abstract.
- [ ] Every registered consumer received notice of the change, the date, what may move, the test window, and the objection route.
- [ ] The shared core suite ran against the production-intended configuration, and each consumer ran its own acceptance set in the same window.
- [ ] Results are reported per consuming use case against pre-agreed criteria; no release decision rests on an averaged score across consumers.
- [ ] The partial-failure rule was applied and the decision recorded, including any consumer deliberately restricted, suspended, or held on the prior version.
- [ ] Each consuming business owner accepted for their own use case, or the consumer is explicitly held; silence was not treated as acceptance.
- [ ] Release is approved at the inherited tier's authority.
- [ ] Rollout is sequenced lowest consumer tier first, with defined soak periods and hold points.
- [ ] Rollback to the prior validated baseline was verified before the first stage — or, where the prior state will be withdrawn, a rehearsed migration plan, a named fallback, and a dated disposition for every consumer exist instead.
- [ ] Post-change monitoring is defined **per consumer**, with named owners and thresholds, for a defined period.
- [ ] Any resulting version divergence between consumers is recorded in the inventory as separate configurations to monitor and test.

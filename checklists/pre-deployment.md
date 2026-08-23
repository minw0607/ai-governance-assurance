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
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - SRC-AUD-01
---

# AI Pre-Deployment Checklist

## How to use this checklist

**Lifecycle gate:** G2–G4 (design, build, validate) — see [AI Lifecycle Stage Gates](../governance/lifecycle/stage-gates.md).

Each section lists the [control objectives](../governance/control-framework/control-objectives.md) its items are intended to evidence. A checked box is not evidence; record the artifact, owner, date, and result against the named objective using the [test-case](../templates/test-case-template.md) and [findings](../templates/findings-report-template.md) templates.

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
- [ ] Failure, timeout, dependency, fallback, rollback, and kill-switch behavior is tested.
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
- [ ] Change and regression process covers provider-controlled updates.
- [ ] Users are trained on limitations, verification, prohibited use, and incident reporting.
- [ ] Records are reproducible and retained according to policy.

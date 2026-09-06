---
schema_version: "1.0"
artifact_id: CHECK-PROD-001
title: AI Production Readiness Checklist
artifact_class: checklist
artifact_type: release-gate
domains:
  - production-readiness
  - release-management
applies_to:
  - generative-ai
  - rag
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
  - deployment
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - SRC-TEST-01
---

# AI Production Readiness Checklist

## How to use this checklist

**Lifecycle gate:** G5 (approve and deploy) — see [AI Lifecycle Stage Gates](../governance/lifecycle/stage-gates.md).

Each section lists the [control objectives](../governance/control-framework/control-objectives.md) its items are intended to evidence. A checked box is not evidence; record the artifact, owner, date, and result against the named objective using the [test-case](../templates/test-case-template.md) and [findings](../templates/findings-report-template.md) templates.

**Relationship to pre-deployment.** The [pre-deployment checklist](pre-deployment.md) established that the design was validated. This gate establishes that the **deployed production configuration** matches what was validated and that the controls operate there, with evidence retained. Where a topic appears in both, this gate asks for production evidence, not a restatement of the validation result.


## Release package

**Control objectives:** GOV-05, OPS-03, QUAL-06, GOV-06

- [ ] Approved versions of model/provider, prompts, retrieval, tools, policies, application, and evaluator are identified.
- [ ] Test plan, cases, raw results, findings, remediations, and limitations are linked.
- [ ] Approval conditions and residual risks are visible to operators and owners.
- [ ] Production configuration matches the validated configuration.

## Operational controls

**Control objectives:** SEC-02, SEC-05, SEC-06, OPS-01

- [ ] Identity, permissions, network, secrets, logging, retention, and alerting have production evidence.
- [ ] Dashboards and alerts are tested end to end.
- [ ] Capacity, rate limits, latency, cost budgets, and abuse controls are configured.
- [ ] Dependency failure and degraded-mode behavior are understood.

## Data security and governance

**Control objectives:** DATA-01, DATA-02, DATA-03, DATA-04, DATA-05, DATA-06, QUAL-04, TPRM-02

- [ ] Material data sources and derived assets have current owners, purpose, classification, provenance, rights, quality, regions, and retention records.
- [ ] Actual connectors, indexes, permissions, service identities, providers, logs, and memory match the approved data/control-flow design.
- [ ] Provider training/improvement, retention, human review, subprocessor, region, deletion, and exit terms align with configuration and approval.
- [ ] Permission, isolation, leakage, poisoning, retention, correction/deletion, backup/restore, and recovery tests passed for applicable data paths.
- [ ] Open data-quality, privacy, security, IP, or rights findings are remediated or explicitly accepted by authorized owners.

## Human and customer controls

**Control objectives:** HUM-01, HUM-02, HUM-03

- [ ] Review, approval, correction, appeal, escalation, and disclosure mechanisms work.
- [ ] Users receive limitations, verification duties, and support channels.
- [ ] Customer-facing content and decisions use required review and recordkeeping.

## Recovery

**Control objectives:** OPS-02, AGT-03, AGT-04, AGT-07

- [ ] Rollback, fallback, disablement, credential revocation, and kill switch are re-tested against the production configuration, with operator, timing, and result retained as evidence.
- [ ] On-call ownership and severity classification include AI-specific failures.
- [ ] Recovery preserves evidence and prevents duplicate or incomplete agent actions.

## Decision

**Control objectives:** GOV-04, GOV-06

- [ ] Accountable business, technical, risk, security, privacy, and compliance approvals are complete as required by tier.
- [ ] Release scope, cohort, date, conditions, monitoring period, and next review are recorded.

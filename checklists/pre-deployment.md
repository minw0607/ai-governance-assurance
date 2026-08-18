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
  - GenAI Audit Checklist v3.xlsx
---

# AI Pre-Deployment Checklist

## Governance

- [ ] Use case, owners, intended users, affected parties, and prohibited uses are documented.
- [ ] Risk tier and applicable obligations are approved.
- [ ] Inventory record, architecture, data flow, dependencies, and lifecycle status are current.
- [ ] Vendor assessment and contract conditions are complete.

## Data and privacy

- [ ] Data sources, rights, classifications, lineage, regions, retention, and deletion are approved.
- [ ] Provider training/reuse and logging terms match policy.
- [ ] Retrieval and connector permissions have been tested with negative cases.
- [ ] Sensitive test data is synthetic or separately approved.

## Security and resilience

- [ ] Threat model includes prompt injection, poisoning, output handling, supply chain, identity, and abuse.
- [ ] Least privilege, secrets, tool authorization, output validation, rate limits, and logging are implemented.
- [ ] Failure, timeout, dependency, fallback, rollback, and kill-switch behavior is tested.
- [ ] Incident playbooks and escalation contacts are ready.

## Performance and impact

- [ ] Use-case-specific acceptance criteria were defined before execution.
- [ ] Functional, factuality, safety, fairness, privacy, workflow, and agentic tests are complete as applicable.
- [ ] Critical findings are closed or explicitly accepted with conditions.
- [ ] Human review is meaningful and tested for realistic workload.

## Operation

- [ ] Monitoring metrics, thresholds, sampling, alerts, owners, and response actions are approved.
- [ ] Change and regression process covers provider-controlled updates.
- [ ] Users are trained on limitations, verification, prohibited use, and incident reporting.
- [ ] Records are reproducible and retained according to policy.

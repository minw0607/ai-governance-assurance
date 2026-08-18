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
  - GenAI Testing Procedures v2.docx
---

# AI Production Readiness Checklist

## Release package

- [ ] Approved versions of model/provider, prompts, retrieval, tools, policies, application, and evaluator are identified.
- [ ] Test plan, cases, raw results, findings, remediations, and limitations are linked.
- [ ] Approval conditions and residual risks are visible to operators and owners.
- [ ] Production configuration matches the validated configuration.

## Operational controls

- [ ] Identity, permissions, network, secrets, logging, retention, and alerting have production evidence.
- [ ] Dashboards and alerts are tested end to end.
- [ ] Capacity, rate limits, latency, cost budgets, and abuse controls are configured.
- [ ] Dependency failure and degraded-mode behavior are understood.

## Data security and governance

- [ ] Material data sources and derived assets have current owners, purpose, classification, provenance, rights, quality, regions, and retention records.
- [ ] Actual connectors, indexes, permissions, service identities, providers, logs, and memory match the approved data/control-flow design.
- [ ] Provider training/improvement, retention, human review, subprocessor, region, deletion, and exit terms align with configuration and approval.
- [ ] Permission, isolation, leakage, poisoning, retention, correction/deletion, backup/restore, and recovery tests passed for applicable data paths.
- [ ] Open data-quality, privacy, security, IP, or rights findings are remediated or explicitly accepted by authorized owners.

## Human and customer controls

- [ ] Review, approval, correction, appeal, escalation, and disclosure mechanisms work.
- [ ] Users receive limitations, verification duties, and support channels.
- [ ] Customer-facing content and decisions use required review and recordkeeping.

## Recovery

- [ ] Rollback, fallback, disablement, credential revocation, and kill switch are tested.
- [ ] On-call ownership and severity classification include AI-specific failures.
- [ ] Recovery preserves evidence and prevents duplicate or incomplete agent actions.

## Decision

- [ ] Accountable business, technical, risk, security, privacy, and compliance approvals are complete as required by tier.
- [ ] Release scope, cohort, date, conditions, monitoring period, and next review are recorded.

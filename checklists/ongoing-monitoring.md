---
schema_version: "1.0"
artifact_id: CHECK-MON-001
title: AI Ongoing Monitoring Checklist
artifact_class: checklist
artifact_type: checklist
domains:
  - ongoing-monitoring
  - performance
  - incident-management
applies_to:
  - generative-ai
  - rag
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - SRC-TEST-01
  - SRC-VEND-01
---

# AI Ongoing Monitoring Checklist

## How to use this checklist

**Lifecycle gate:** G6 (operate, monitor, and change) — see [AI Lifecycle Stage Gates](../governance/lifecycle/stage-gates.md).

Each section lists the [control objectives](../governance/control-framework/control-objectives.md) its items are intended to evidence. A checked box is not evidence; record the artifact, owner, date, and result against the named objective using the [test-case](../templates/test-case-template.md) and [findings](../templates/findings-report-template.md) templates.

At the cadence defined in the monitoring plan:

## Fitness for purpose

**Control objectives:** OPS-01, QUAL-02, QUAL-03, QUAL-06

- [ ] Task success, factuality, abstention, severe-error, and user-impact measures remain within thresholds.
- [ ] Results are segmented by use case, risk group, language, channel, and severity where relevant.
- [ ] Production samples are reviewed against current authoritative evidence.
- [ ] Limitations and user workarounds have not changed the effective use case.

## Security, privacy, and safety

**Control objectives:** SEC-03, SEC-05, DATA-02, DATA-04, QUAL-05, OPS-02

- [ ] Prompt-injection, leakage, policy, identity, and tool-use events are reviewed.
- [ ] Permission and data-source changes have propagated correctly.
- [ ] Sensitive data, retention, deletion, and cross-border controls remain effective.
- [ ] New threat intelligence and known attacks are added to regression coverage.

## Agentic operation

**Control objectives:** AGT-01, AGT-02, AGT-03, AGT-04, AGT-07

- [ ] Unauthorized, duplicate, excessive, failed, and human-overridden actions are trended.
- [ ] Tool permissions, credentials, memory, delegation, budgets, and kill switch are reviewed.
- [ ] Trace completeness and recovery outcomes meet requirements.

## Change and vendor

**Control objectives:** OPS-03, TPRM-03, SEC-04

- [ ] Model, prompt, retrieval, tool, application, evaluator, and provider changes are reconciled.
- [ ] Release notes, incidents, deprecations, subprocessors, and service performance are reviewed.
- [ ] Golden-suite regression results are current.
- [ ] Concentration and exit assumptions remain viable.

## Governance

**Control objectives:** GOV-05, GOV-06, OPS-04

- [ ] Findings, incidents, exceptions, risk acceptances, and remediation aging are reviewed.
- [ ] Inventory, tier, owners, approvals, and documentation remain current.
- [ ] Threshold breaches have documented decisions and follow-up.
- [ ] The next monitoring period and reassessment triggers are recorded.

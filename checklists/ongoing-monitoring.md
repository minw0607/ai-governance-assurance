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
version: "0.3.0"
last_reviewed: 2026-10-06
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
- [ ] Each agent security event is classified as alerting with a named responder and response path, or as log-only; denials, fallbacks, and limit breaches are reviewed alongside successful activity.
- [ ] Per-agent usage, cost, and limit attribution is reviewed, and automatic containment for runaway execution is confirmed operative.

## Change and vendor

**Control objectives:** OPS-03, OPS-05, TPRM-03, SEC-04

- [ ] Model, prompt, retrieval, tool, application, evaluator, and provider changes are reconciled.
- [ ] Platform and infrastructure changes — runtime, SDK/API version, compute, region, images, orchestration, gateway, quota, identity, observability — are reconciled against the approved baseline.
- [ ] Release notes, incidents, deprecations, subprocessors, and service performance are reviewed.
- [ ] Deprecation and end-of-life dates for components in use are tracked, with an internal cutover date set back from each deadline.
- [ ] Golden-suite regression results are current.
- [ ] Concentration and exit assumptions remain viable.

For a shared service:

- [ ] The consumer register matches actual usage, and the inherited tier is current.
- [ ] Post-change quality, safety, and error measures are trended **per consuming use case**, not only in aggregate.
- [ ] Any version divergence between consumers is recorded, time-bounded, and closing.
- [ ] Consumers held on a prior version, or running with conditions after a failed acceptance, have owners and closure dates.

## Governance

**Control objectives:** GOV-05, GOV-06, OPS-04

- [ ] Findings, incidents, exceptions, risk acceptances, and remediation aging are reviewed.
- [ ] Inventory, tier, owners, approvals, and documentation remain current.
- [ ] Threshold breaches have documented decisions and follow-up.
- [ ] The next monitoring period and reassessment triggers are recorded.

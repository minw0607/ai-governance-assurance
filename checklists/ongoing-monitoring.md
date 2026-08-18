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
  - GenAI Testing Procedures v2.docx
  - GenAI Vendor Assessment Framework.docx
---

# AI Ongoing Monitoring Checklist

At the cadence defined in the monitoring plan:

## Fitness for purpose

- [ ] Task success, factuality, abstention, severe-error, and user-impact measures remain within thresholds.
- [ ] Results are segmented by use case, risk group, language, channel, and severity where relevant.
- [ ] Production samples are reviewed against current authoritative evidence.
- [ ] Limitations and user workarounds have not changed the effective use case.

## Security, privacy, and safety

- [ ] Prompt-injection, leakage, policy, identity, and tool-use events are reviewed.
- [ ] Permission and data-source changes have propagated correctly.
- [ ] Sensitive data, retention, deletion, and cross-border controls remain effective.
- [ ] New threat intelligence and known attacks are added to regression coverage.

## Agentic operation

- [ ] Unauthorized, duplicate, excessive, failed, and human-overridden actions are trended.
- [ ] Tool permissions, credentials, memory, delegation, budgets, and kill switch are reviewed.
- [ ] Trace completeness and recovery outcomes meet requirements.

## Change and vendor

- [ ] Model, prompt, retrieval, tool, application, evaluator, and provider changes are reconciled.
- [ ] Release notes, incidents, deprecations, subprocessors, and service performance are reviewed.
- [ ] Golden-suite regression results are current.
- [ ] Concentration and exit assumptions remain viable.

## Governance

- [ ] Findings, incidents, exceptions, risk acceptances, and remediation aging are reviewed.
- [ ] Inventory, tier, owners, approvals, and documentation remain current.
- [ ] Threshold breaches have documented decisions and follow-up.
- [ ] The next monitoring period and reassessment triggers are recorded.

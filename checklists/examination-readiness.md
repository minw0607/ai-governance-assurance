---
schema_version: "1.0"
artifact_id: CHECK-EXAM-001
title: AI Examination and Audit Readiness Checklist
artifact_class: checklist
artifact_type: checklist
domains:
  - examination-readiness
  - audit
  - evidence
applies_to:
  - generative-ai
  - rag
  - agentic-ai
industries:
  - financial-services
  - cross-industry
lifecycle_stages:
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - SRC-AUD-01
---

# AI Examination and Audit Readiness Checklist

## How to use this checklist

**Lifecycle gate:** G6 (examination or audit of an operating portfolio) — see [AI Lifecycle Stage Gates](../governance/lifecycle/stage-gates.md).

Each section lists the [control objectives](../governance/control-framework/control-objectives.md) its items are intended to evidence. A checked box is not evidence; record the artifact, owner, date, and result against the named objective using the [test-case](../templates/test-case-template.md) and [findings](../templates/findings-report-template.md) templates.

Use this checklist to assess both **design** and **operating effectiveness**. For each item, identify the policy/control, owner, population, sample, evidence, test result, exception, and conclusion.

## Governance and lifecycle

**Control objectives:** GOV-01, GOV-02, GOV-03, GOV-04, GOV-05, GOV-06

- [ ] Demonstrate a recent use case from request through risk review, approval, deployment, and monitoring.
- [ ] Reperform risk classification and compare it with the recorded tier.
- [ ] Show approved policies, training, attestations, prohibited uses, and exception records.
- [ ] Reconcile the AI inventory to deployed systems, vendors, connectors, and discovered shadow AI.
- [ ] Trace model/provider, prompt, retrieval, tool, and configuration changes to testing, approval, and rollback readiness.
- [ ] Show governance roles, committee decisions, issue aging, and escalation.

## Data security and privacy

**Control objectives:** DATA-01, DATA-02, DATA-03, DATA-04, DATA-05, DATA-06, DATA-07

- [ ] Demonstrate source allow/block controls and retrieval permission boundaries.
- [ ] Sample data classifications, labels, access reviews, and least-privilege enforcement.
- [ ] Inspect secrets, service identities, rotation, and tool credentials.
- [ ] Trace sensitive data through prompts, retrieval, outputs, logs, retention, and deletion.
- [ ] Demonstrate data-subject, re-indexing, backup, residency, and transfer controls where applicable.

## Model/system risk and quality

**Control objectives:** QUAL-01, QUAL-02, QUAL-03, QUAL-04, QUAL-05, QUAL-06

- [ ] Show the evaluation framework, benchmark rationale, acceptance thresholds, and recent results.
- [ ] Reperform selected factuality, retrieval, safety, fairness, privacy, and adversarial tests.
- [ ] Review independent challenge, limitations, findings, approvals, and remediation closure.
- [ ] Compare production monitoring with validated baselines and investigate drift.
- [ ] Verify model/system documentation accurately reflects production configuration and use.

## Runtime security and monitoring

**Control objectives:** SEC-01, SEC-02, SEC-03, SEC-04, SEC-05, SEC-06, OPS-01

- [ ] Execute a controlled prompt-injection scenario and trace prevention, containment, detection, and response.
- [ ] Inspect output validation, DLP, logging, correlation, alert thresholds, and incident tickets.
- [ ] Review rate limits, cost controls, continuity, fallback, recovery tests, and service-level results.
- [ ] Sample user training, in-product warnings, and high-impact review workflows.

## Agentic AI

**Control objectives:** AGT-01, AGT-02, AGT-03, AGT-04, AGT-05, AGT-06, AGT-07

- [ ] Reconcile agent tools and permissions to approved tasks and identities.
- [ ] Trace a complete agent run from goal through planning, tool calls, approvals, state, and outcome.
- [ ] Test gated action, malicious tool output, memory isolation, failure recovery, and kill switch.
- [ ] Review task-success, tool-accuracy, unauthorized-action, retry, cost, drift, and trace-completeness metrics.
- [ ] For multi-agent systems, examine delegation, conflict, provenance, and resource arbitration.

## Walkthrough package

**Control objectives:** HUM-01, HUM-02, OPS-02, OPS-03

Prepare a concise evidence index containing inventory, governance charter, policies, recent approvals, architecture/data flows, tiering, assessments, test reports, monitoring, incidents, change records, exceptions, training, vendor evidence, and remediation tracking.

## Rating

**Control objectives:** GOV-06

- **Low issue:** control exists and evidence supports consistent operation.
- **Moderate issue:** control exists but coverage, consistency, or monitoring is incomplete.
- **High issue:** control is missing or ineffective, or the gap creates material exposure.

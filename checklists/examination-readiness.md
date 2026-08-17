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
  - GenAI Audit Checklist v3.xlsx
---

# AI Examination and Audit Readiness Checklist

Use this checklist to assess both **design** and **operating effectiveness**. For each item, identify the policy/control, owner, population, sample, evidence, test result, exception, and conclusion.

## Governance and lifecycle

- [ ] Demonstrate a recent use case from request through risk review, approval, deployment, and monitoring.
- [ ] Reperform risk classification and compare it with the recorded tier.
- [ ] Show approved policies, training, attestations, prohibited uses, and exception records.
- [ ] Reconcile the AI inventory to deployed systems, vendors, connectors, and discovered shadow AI.
- [ ] Trace model/provider, prompt, retrieval, tool, and configuration changes to testing, approval, and rollback readiness.
- [ ] Show governance roles, committee decisions, issue aging, and escalation.

## Data security and privacy

- [ ] Demonstrate source allow/block controls and retrieval permission boundaries.
- [ ] Sample data classifications, labels, access reviews, and least-privilege enforcement.
- [ ] Inspect secrets, service identities, rotation, and tool credentials.
- [ ] Trace sensitive data through prompts, retrieval, outputs, logs, retention, and deletion.
- [ ] Demonstrate data-subject, re-indexing, backup, residency, and transfer controls where applicable.

## Model/system risk and quality

- [ ] Show the evaluation framework, benchmark rationale, acceptance thresholds, and recent results.
- [ ] Reperform selected factuality, retrieval, safety, fairness, privacy, and adversarial tests.
- [ ] Review independent challenge, limitations, findings, approvals, and remediation closure.
- [ ] Compare production monitoring with validated baselines and investigate drift.
- [ ] Verify model/system documentation accurately reflects production configuration and use.

## Runtime security and monitoring

- [ ] Execute a controlled prompt-injection scenario and trace prevention, containment, detection, and response.
- [ ] Inspect output validation, DLP, logging, correlation, alert thresholds, and incident tickets.
- [ ] Review rate limits, cost controls, continuity, fallback, recovery tests, and service-level results.
- [ ] Sample user training, in-product warnings, and high-impact review workflows.

## Agentic AI

- [ ] Reconcile agent tools and permissions to approved tasks and identities.
- [ ] Trace a complete agent run from goal through planning, tool calls, approvals, state, and outcome.
- [ ] Test gated action, malicious tool output, memory isolation, failure recovery, and kill switch.
- [ ] Review task-success, tool-accuracy, unauthorized-action, retry, cost, drift, and trace-completeness metrics.
- [ ] For multi-agent systems, examine delegation, conflict, provenance, and resource arbitration.

## Walkthrough package

Prepare a concise evidence index containing inventory, governance charter, policies, recent approvals, architecture/data flows, tiering, assessments, test reports, monitoring, incidents, change records, exceptions, training, vendor evidence, and remediation tracking.

## Rating

- **Low issue:** control exists and evidence supports consistent operation.
- **Moderate issue:** control exists but coverage, consistency, or monitoring is incomplete.
- **High issue:** control is missing or ineffective, or the gap creates material exposure.

---
schema_version: "1.0"
artifact_id: GOV-LIFE-001
title: AI Lifecycle Stage Gates
artifact_class: governance
artifact_type: procedure
domains:
  - lifecycle-management
  - approval-gates
  - evidence-management
applies_to:
  - generative-ai
  - agentic-ai
  - machine-learning
industries:
  - cross-industry
lifecycle_stages:
  - intake
  - design
  - development
  - validation
  - deployment
  - operation
  - retirement
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - GenAI Policies - Example.docx
  - GenAI Audit Checklist v3.xlsx
  - GenAI Vendor Assessment Framework.docx
---

# AI Lifecycle Stage Gates

## Purpose

This procedure defines the decisions and evidence required to move an AI system through its lifecycle. It is designed for use with the [risk-tiering framework](../risk-tiering/ai-risk-tiering-framework.md), [control objectives](../control-framework/control-objectives.md), assessments, testing guides, and release checklists.

## Gate rules

1. Each gate has a named decision owner and a recorded outcome: approve, approve with conditions, return for remediation, reject, suspend, or retire.
2. Approval applies only to the documented use, users, data, system boundary, version strategy, and action authority.
3. Evidence depth is calibrated by risk tier, but required control outcomes may not be omitted without an applicability rationale or approved exception.
4. Conditions and exceptions must have an owner, due date, monitoring, and expiry.
5. A material change or threshold breach sends the system back to the earliest affected gate.

## G0 — Discover and register

**Decision:** Is the capability visible, assigned, and subject to governance?

### Entry triggers

- business intake, procurement, development, experiment, or vendor feature enablement;
- discovery through SaaS, browser, network, cloud, API, expense, or access monitoring;
- identification of AI embedded in an existing application; or
- discovery of an unregistered production dependency.

### Required activities

- Create a provisional inventory record and stable identifier.
- Record discovery source, business area, capability, provider, environment, and lifecycle status.
- Name a provisional business owner and technical contact.
- Restrict or suspend unapproved use when exposure is material.
- Route to G1 within a defined service level.

### Exit evidence

- provisional inventory record;
- owner acceptance or escalation for orphaned capability; and
- decision to proceed to intake, restrict, reject, or investigate.

## G1 — Intake and classify

**Decision:** Is the use permitted, and what risk tier and review path apply?

### Required activities

- Define intended purpose, users, affected parties, decisions, benefits, alternatives, and foreseeable misuse.
- Define the AI system boundary, including model, prompts, retrieval, tools, human review, and downstream actions.
- Check prohibited and restricted uses.
- Identify sensitive data, regulated processes, external communication, high-impact decisions, and vulnerable populations.
- Classify autonomy and action privileges.
- Assign an inherent risk tier and mandatory escalation factors.
- Determine required assessments, reviewers, approval authority, and evidence plan.

### Exit evidence

- completed use-case intake and impact assessment;
- prohibited-use determination;
- system-boundary description;
- risk-tier decision and rationale;
- review-routing plan and accountable owners; and
- decision to proceed, revise, restrict, or reject.

## G2 — Design and assess

**Decision:** Can the proposed design meet the applicable control requirements?

### Required activities

- Document architecture, trust boundaries, identities, data flows, providers, models, retrieval, memory, tools, and downstream systems.
- Establish outcome requirements, failure taxonomy, acceptance criteria, and human-oversight design.
- Complete privacy, data, security threat, legal/compliance, records, vendor, and rights-impact reviews as applicable.
- Define provider version strategy, rollback, degraded mode, recovery, and exit.
- Map control objectives to implementation, owner, evidence, and planned test.
- Resolve design-blocking findings before build or acquisition commitment.

### Exit evidence

- approved architecture and data-flow diagrams;
- control applicability matrix;
- domain assessments and vendor due diligence;
- requirements and measurable acceptance criteria;
- human-oversight and transparency design;
- test strategy and monitoring design; and
- design decision record.

## G3 — Build, acquire, and configure

**Decision:** Was the approved design implemented under controlled conditions?

### Required activities

- Use approved models, services, data sources, tools, connectors, and dependencies.
- Separate development, evaluation, and production identities and environments.
- Apply code review, dependency and secret scanning, provenance, configuration, and supply-chain controls.
- Version prompts, policies, retrieval indexes, tool schemas, guardrails, and evaluation datasets.
- Implement logging, correlation, rollback, kill switch, rate/transaction limits, and safe failure.
- Track deviations from the approved design and route material deviations back to G2.

### Exit evidence

- implementation and configuration baseline;
- component and provider inventory, including SBOM where applicable;
- data lineage and approved-source record;
- secure-development and review evidence;
- operational procedures and draft runbooks; and
- build-complete attestation from the technical owner.

## G4 — Validate and independently challenge

**Decision:** Does evidence demonstrate fitness for intended use and acceptable residual risk?

### Required activities

- Execute use-case-specific functional, factuality, safety, fairness, privacy, security, resilience, integration, agentic, and regression tests as applicable.
- Test normal, edge, ambiguous, adversarial, out-of-scope, and failure scenarios.
- Validate human oversight, permissions, logging, rollback, incident detection, recovery, and evidence reconstruction.
- Compare results with preapproved acceptance criteria and prior baselines.
- Document limitations, residual uncertainty, findings, and remediation.
- Obtain independent challenge or validation based on risk tier.

### Exit evidence

- approved test plan and traceable test cases;
- datasets, tools, configurations, raw outputs, and reproducible results;
- findings and remediation evidence;
- limitation and residual-risk statement;
- independent review report where required; and
- recommendation to approve, condition, restrict, or reject.

## G5 — Approve and deploy

**Decision:** May the system enter production, under which constraints, and for how long?

### Required activities

- Complete the [production-readiness checklist](../../checklists/production-readiness.md).
- Verify that production matches the validated baseline.
- Confirm monitoring thresholds, alert routes, incident and rollback readiness, support ownership, and recovery.
- Resolve critical findings and document any accepted residual findings.
- Define progressive rollout, user groups, volume, geography, action limits, and approval expiry.
- Train users and human reviewers; issue required notices and instructions.

### Exit evidence

- signed readiness record;
- production configuration and release identifier;
- residual-risk acceptance and conditions;
- monitoring and incident plans;
- rollout and rollback plans;
- user/reviewer training and communication; and
- formal deployment approval.

## G6 — Operate, monitor, and change

**Decision:** Does the system remain within its approved use and risk envelope?

### Required activities

- Monitor outcomes, quality, safety, fairness, privacy, security, human overrides, agent actions, resilience, provider changes, and cost.
- Review complaints, appeals, near misses, incidents, and control exceptions.
- Reconcile deployed models, prompts, retrieval, tools, and permissions with inventory and baselines.
- Perform periodic control, vendor, access, and monitoring reviews based on tier.
- Classify changes before release and run regression or targeted revalidation.
- Suspend, restrict, or roll back when thresholds or approval conditions fail.

### Periodic review record

- current use, users, tier, owner, versions, and dependencies;
- KPI/KRI trends against thresholds;
- incidents, overrides, complaints, and findings;
- changes and provider notices;
- exceptions and overdue actions;
- monitoring and control-effectiveness conclusion; and
- decision to continue, condition, reassess, suspend, or retire.

## G7 — Retire

**Decision:** Has the system been decommissioned without residual access, action, data, or dependency risk?

### Required activities

- Identify downstream processes, users, integrations, records, and replacement needs.
- Stop new activity and communicate the retirement date.
- Revoke user, service, API, connector, tool, agent, and vendor access.
- Disable schedules, queues, triggers, endpoints, memory, and autonomous workflows.
- Archive required evidence and dispose of prompts, logs, embeddings, indexes, training data, and other records according to policy.
- Verify that no shadow copy or unsupported dependency remains active.
- Close contracts or update vendor scope where applicable.

### Exit evidence

- approved retirement plan and impact assessment;
- access and integration revocation evidence;
- data and records disposition record;
- dependency-owner confirmation;
- updated inventory status and retirement date; and
- post-retirement verification.

## Change-to-gate routing

| Change or event | Earliest gate normally revisited |
|---|---|
| New purpose, affected population, or high-impact decision | G1 |
| New data category, geography, provider, architecture, or tool | G2 |
| Implementation deviation or new dependency | G3 |
| Model/prompt/retrieval update affecting behavior | G4 |
| Production configuration or rollout change | G5 |
| Threshold breach, incident, drift, or repeated override | G4 or G6 based on root cause |
| End of business need or unsupported provider | G7 |

## Gate-performance measures

- Intake-to-tier and tier-to-decision cycle time.
- Percentage of gates returned for incomplete evidence.
- Conditional approvals and overdue conditions by tier.
- Production releases that differ from validated baselines.
- Material changes deployed without prior classification.
- Reassessments triggered and completed within required time.
- Retired systems with residual credentials, integrations, or inventory discrepancies.

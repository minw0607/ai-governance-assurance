---
schema_version: "1.0"
artifact_id: GOV-OPS-001
title: AI Governance Roles and Decision Rights
artifact_class: governance
artifact_type: operating-model
domains:
  - accountability
  - governance-forums
  - three-lines
applies_to:
  - generative-ai
  - agentic-ai
  - machine-learning
industries:
  - cross-industry
lifecycle_stages:
  - intake
  - design
  - validation
  - deployment
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - GenAI Policies - Example.docx
  - GenAI Audit Checklist v3.xlsx
  - GenAI MRM Survey with Heatmap v2.xlsx
---

# AI Governance Roles and Decision Rights

## Purpose

This operating model assigns accountability for AI decisions and prevents approval gaps, self-review, and orphaned systems. Titles may differ across organizations; the required outcomes and segregation of duties are more important than the label.

## Role accountabilities

### Governing body or delegated board committee

- Approves enterprise AI risk appetite and receives material exposure reporting.
- Challenges management on high-impact uses, concentration, incidents, exceptions, and overdue remediation.
- Confirms executive accountability and adequate resources.

### Executive accountable owner

- Owns the enterprise AI governance mandate and implementation effectiveness.
- Sponsors policy, portfolio reporting, and cross-functional escalation.
- Accepts residual risk only within formally delegated authority.

### AI governance function

- Maintains the framework, taxonomy, inventory standard, intake, and committee process.
- Routes reviews, records decisions, monitors conditions and expiry, and reports portfolio risk.
- Challenges incomplete inventory, inconsistent tiering, and overdue governance activity.
- Does not assume the business owner's accountability for use-case outcomes.

### Business owner

- Owns the business purpose, affected parties, benefits, outcome requirements, and residual risk.
- Ensures users follow the approved use and that human oversight is effective.
- Funds remediation, monitoring, and retirement.
- Stops or restricts use when approval conditions are no longer met.

### Technical owner

- Owns architecture, implementation, identities, configuration, deployment, observability, resilience, and change execution.
- Maintains the production baseline and technical evidence.
- Ensures deployed components match the approved boundary.

### Model or AI product owner

- Maintains model/system documentation, performance requirements, limitations, evaluation, and monitoring.
- Coordinates provider/model changes and regression evidence.
- May be combined with the technical owner when responsibilities remain explicit.

### Data owner and data steward

- Authorize data use and establish quality, lineage, classification, access, retention, and deletion requirements.
- Verify that retrieval and downstream use preserve source permissions and restrictions.

### Information security

- Defines threat-modeling, identity, secrets, network, logging, vulnerability, incident, and resilience requirements.
- Reviews adversarial testing and validates that prompts or model behavior are not treated as authorization controls.

### Privacy

- Determines privacy-assessment requirements and challenges purpose, minimization, provider use, retention, residency, notices, rights, and deletion.
- Confirms that memory, embeddings, logs, and test data are included in the privacy boundary.

### Legal and compliance

- Identifies applicable obligations and advises on prohibited or restricted use, disclosures, contracts, intellectual property, consumer protection, and recordkeeping.
- Does not certify technical effectiveness outside its competence.

### Third-party risk and procurement

- Conduct due diligence, establish contractual protections, track provider dependencies, and maintain exit options.
- Escalate material vendor changes, incidents, control limitations, and concentration risk.

### Independent reviewer or validator

- Challenges conceptual suitability, data, implementation, test design, results, limitations, monitoring, and residual risk.
- Documents scope, methods, evidence, findings, and limitations.
- Must not report to the person whose delivery objective depends on approval when independence is required.

### Operations and incident management

- Own production procedures, on-call response, containment, recovery, and runbook exercises.
- Tag AI incidents and preserve model, prompt, retrieval, tool, action, and approval evidence.

### Internal audit

- Independently assesses whether governance and controls are designed and operating effectively.
- Evaluates first- and second-line performance rather than operating their controls.

### End users and human reviewers

- Use the system only within approved purposes and data rules.
- Verify outputs, protect confidential information, report unexpected behavior, and document material overrides.
- Remain accountable for decisions assigned to them.

## Governance forums

| Forum | Minimum authority | Core inputs | Typical cadence |
|---|---|---|---|
| Board / executive risk forum | Risk appetite, material exposure, critical exceptions and incidents | Portfolio risk, Tier 1 uses, concentration, incidents, overdue issues | Quarterly and event-driven |
| AI governance committee | Higher-risk approvals, exceptions, suspension, cross-functional standards | Intake and tiering, validation, residual risk, monitoring, incidents | Monthly and urgent sessions |
| AI review working group | Review routing, lower-tier decisions, readiness and action tracking | Intake records, assessments, evidence status, change requests | Weekly or biweekly |
| Architecture / security / privacy / data forums | Domain-specific design decisions and exceptions | Architecture, data flows, threat/privacy assessments, test evidence | Existing enterprise cadence |
| Change authority | Production release, emergency changes, rollback | Change classification, regression, approvals, recovery plan | Per release |

### Forum decision record

Every material forum decision should capture:

- system and use-case identifiers;
- decision requested and authority basis;
- materials reviewed and their versions;
- participants, conflicts, recusals, and quorum;
- decision, rationale, dissent, and unresolved uncertainty;
- conditions, remediation, owner, due date, and expiry;
- required monitoring and escalation triggers; and
- date and approving authority.

## Decision-rights matrix

`A` = accountable decision owner; `R` = responsible for preparing or operating; `C` = consulted/challenger; `I` = informed. Organizations should tailor names while preserving accountability and independence.

| Decision or activity | Executive / committee | Business owner | Technical / product owner | AI governance / risk | Security / privacy / legal / data | Independent assurance | Internal audit |
|---|---|---|---|---|---|---|---|
| Set AI risk appetite | A | C | C | R | C | I | I |
| Register use case | I | A | R | R | I | I | I |
| Define intended use and outcome criteria | I | A/R | C | C | C | I | I |
| Assign initial risk tier | I | A | C | R/C | C | I | I |
| Approve Tier 1 use | A | R | R | C | C | C | I |
| Approve Tier 2 use | A or delegated A | R | R | C | C | C/R | I |
| Approve Tier 3/4 use | I | A | R | C | C as applicable | I | I |
| Approve architecture and data use | I | C | R | C | A by domain | C | I |
| Design and execute testing | I | A | R | C | C | C or R if independent | I |
| Accept validation findings | A by tier | A/R | R | C | C | R | I |
| Accept residual risk | A by tier | R | C | C | C | I | I |
| Approve material change | A by tier | R | R | C | C | C | I |
| Operate and monitor | I | A | R | C | C | I | I |
| Declare and contain incident | I or A if material | A | R | C | R/C | I | I |
| Approve exception | A by originating authority | R | R | C | C | I | I |
| Suspend or retire use | A for Tier 1/material event | A/R | R | C | C | I | I |
| Audit governance effectiveness | I | C | C | C | C | I | A/R |

## Segregation-of-duties rules

- A developer must not be the sole approver of production readiness.
- The business owner must not delegate residual-risk accountability to a vendor or validation team.
- Independent reviewers must disclose prior design or implementation involvement.
- Privileged tool access, production deployment, and approval should not rest with one individual for higher-risk systems.
- The person granting an exception should have authority at least equal to the original requirement owner.
- Internal audit must not own the inventory, tiering, validation, monitoring, or exception process it later audits.

## Escalation triggers

Escalate outside normal cadence when:

- a prohibited or potentially unlawful use is proposed or discovered;
- credible harm is severe, systemic, difficult to reverse, or affects vulnerable people;
- a Tier 1 system lacks required independent evidence;
- an agent obtains or attempts authority beyond its approved scope;
- sensitive data exposure, discriminatory impact, or material misinformation occurs;
- a provider change invalidates the approval basis;
- a critical control is unavailable or repeatedly overridden;
- an exception, validation finding, or incident remediation becomes overdue; or
- ownership is disputed or the system is operating without a current approval.

## Effectiveness measures

- Percentage of inventory records with named accountable owners.
- Percentage of decisions with complete authority and evidence records.
- Approval cycle time by risk tier and control function.
- Actions overdue, average action age, and repeat findings.
- Exceptions nearing expiry or renewed more than once.
- Meeting cadence, quorum, and decision-condition closure.
- Systems suspended or restricted because approval conditions failed.

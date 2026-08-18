---
schema_version: "1.0"
artifact_id: GOV-INV-001
title: AI Inventory Minimum Data Standard
artifact_class: governance
artifact_type: standard
domains:
  - ai-inventory
  - system-of-record
  - lifecycle-management
applies_to:
  - generative-ai
  - agentic-ai
  - machine-learning
industries:
  - cross-industry
lifecycle_stages:
  - intake
  - design
  - deployment
  - operation
  - retirement
status: draft
version: "0.3.0"
last_reviewed: 2026-08-18
source_artifacts:
  - Agentic_AI_Auditing_Framework.docx
  - GenAI Policies - Example.docx
  - GenAI Audit Checklist v3.xlsx
  - GenAI MRM Survey with Heatmap v2.xlsx
---

# AI Inventory Minimum Data Standard

## Purpose

The AI inventory is the authoritative register of AI systems and use cases. It supports ownership, risk classification, review routing, aggregate exposure analysis, change control, incident response, and retirement. It must describe the full system rather than functioning only as a list of statistical models.

## Record structure

An organization may maintain separate linked records for a use case, system, model, vendor service, agent, and deployment. At minimum, relationships must be explicit enough to answer:

- Which business use depends on which deployed system?
- Which models, prompts, retrieval sources, tools, and vendors affect the outcome?
- Who owns the outcome, technology, data, and controls?
- What is approved, at which risk tier, under which conditions, and until when?
- What changed, what is monitored, and what must be contained during an incident?

## Required fields

### A. Identity and ownership

| Field | Requirement |
|---|---|
| Inventory identifier | Stable, unique, and never reused |
| System and use-case name | Human-readable name with separate aliases where needed |
| Record type | Use case, AI system, model, vendor service, agent, component, or deployment |
| Business unit and process | Owning area and process in which output or action is used |
| Business owner | Accountable for intended use, outcomes, and residual risk |
| Technical owner | Accountable for implementation and operation |
| Product/model owner | Accountable for behavior, limitations, evaluation, and monitoring |
| Control owners | Security, privacy, data, compliance, vendor, validation, and operations contacts as applicable |

### B. Purpose and impact

| Field | Requirement |
|---|---|
| Intended use | Specific tasks, decisions, users, and business outcome |
| Prohibited use | Explicit uses, users, data, or decisions outside approval |
| Affected parties | Employees, customers, applicants, public, vulnerable groups, or other stakeholders |
| Decision influence | Informational, drafting, recommendation, ranking, decision support, or decision execution |
| Human oversight | Advisory, human-in-the-loop, human-on-the-loop, or autonomous |
| Action authority | None, read, write, execute, communicate, transact, delete, or administer |
| Impact and reversibility | Credible harm, scale, detectability, correction, appeal, and rollback |

### C. Lifecycle and governance status

| Field | Requirement |
|---|---|
| Lifecycle status | Proposed, experiment, development, validation, approved, production, restricted, suspended, retired, or rejected |
| Risk tier | Current tier and rationale reference |
| Applicable requirements | Legal classification, policy/control set, and applicability decisions |
| Approval | Decision, authority, date, conditions, and expiry/review date |
| Exceptions | Open exceptions, compensating controls, owner, due date, and expiry |
| Independent review | Required status, reviewer, scope, date, result, and next due date |

### D. Model and provider

| Field | Requirement |
|---|---|
| Model/provider | Legal provider and product/service name |
| Model identifier | Provider model ID, family, or internal registry ID |
| Version strategy | Pinned, managed update, release channel, or internal version |
| Adaptation | Prompt-only, RAG, fine-tuned, trained, distilled, or ensemble |
| Model limitations | Known limitations and authoritative documentation link |
| Hosting/deployment | SaaS, API, cloud-managed, on-premises, device, or hybrid |
| Vendor dependencies | Subprocessors, model suppliers, vector databases, observability, and critical libraries |

### E. Prompt, retrieval, and data

| Field | Requirement |
|---|---|
| Prompt assets | System prompts, templates, policy instructions, versions, and repository links |
| Retrieval architecture | Sources, connectors, embeddings, indexes, rerankers, namespaces, and permission model |
| Data sources | Source owner, origin, purpose, lineage, quality, and authorization |
| Data asset records | Linked records for material datasets, corpora, indexes, evaluation sets, persistent memory, and derived artifacts under the [AI data framework](../data-security-governance/framework.md) |
| Data classification | Public, internal, confidential, restricted, personal, regulated, licensed, or other enterprise classes |
| Provider data use | Training/reuse, retention, deletion, residency, and cross-border terms |
| Logs and traces | Prompt/output/tool data captured, minimization, access, and retention |
| Training/fine-tuning data | Provenance, rights, representativeness, transformations, and version |
| Rights and disposition | Correction, restriction, withdrawal, deletion, legal hold, backup non-restoration, and verification process |

### F. Agentic components

| Field | Requirement |
|---|---|
| Agent/orchestrator | Agent identifier, objective, planner pattern, and parent/child relationship |
| Tool and protocol registry link | Tools, MCP/A2A clients/servers, endpoints, extensions, operations, owner, purpose, scope, environment, and risk |
| Version and schema baseline | Agent graph, protocol, SDK, server/tool, schema, extension, and deprecation status |
| Service identity | Credentials, authorization server, role, scopes/audiences, privileges, expiry/rotation, exchange pattern, and revocation owner |
| Delegated authority | Initiating human/workload, allowed delegation targets, maximum depth/duration, propagated authority, and termination |
| Action controls | Approval steps, limits, budgets, allowlists, circuit breakers, and rollback |
| Memory/state | Data stored, provenance, access, retention, correction, deletion, and checkpointing |
| Multi-agent coordination | Communication partners, context isolation, message integrity, conflict resolution, resource arbitration, and termination |
| Action/state integrity | Idempotency, deduplication, transaction boundaries, reconciliation, rollback/compensation, and orphan handling |
| Agent evidence | Correlation model for identity, purpose, versions, context references, approvals, calls, state changes, errors, and outcomes |

### G. Testing, monitoring, and operations

| Field | Requirement |
|---|---|
| Requirements and acceptance | Outcome criteria, failure taxonomy, and release thresholds |
| Test evidence | Current plan/results, dataset version, findings, and approval |
| Production baseline | Model, prompt, retrieval, tools, configuration, and release identifier |
| Monitoring | Metrics, thresholds, frequency, owner, alerts, and review cadence |
| Incident routing | Runbook, on-call owner, containment authority, and evidence location |
| Resilience | Dependencies, degraded mode, RTO/RPO where applicable, rollback, and recovery |
| Change history | Material changes, classification, tests, approval, and deployment date |

### H. Retirement

| Field | Requirement |
|---|---|
| Retirement trigger and date | Business, risk, performance, legal, or provider reason |
| Replacement/dependencies | Migration path and downstream owner confirmations |
| Access closure | Users, identities, keys, tools, connectors, endpoints, and schedules revoked |
| Data/records disposition | Archive, deletion, legal hold, and verification |
| Closure evidence | Final approval and post-retirement verification |

## Record ownership and updates

- The business owner is accountable for purpose, impact, users, approval scope, and continued need.
- The technical/product owner maintains component, version, deployment, monitoring, and change data.
- Control functions maintain their assessment, exception, and review fields.
- AI governance owns taxonomy, completeness rules, reconciliation, and reporting.
- Updates should occur before a lifecycle transition or material production change, not only during periodic certification.

## Reconciliation and shadow-AI discovery

At a risk-based cadence, reconcile the inventory with:

- procurement, contract, accounts-payable, and expense data;
- identity-provider applications, privileged identities, and access groups;
- API gateways, cloud subscriptions, model endpoints, and token usage;
- source repositories, CI/CD, model registries, and infrastructure-as-code;
- SaaS-management, CASB, DLP, browser, network, and DNS discovery;
- vector databases, embedding services, tool registries, and agent platforms;
- incident, change, privacy, vendor, and architecture records; and
- business attestations and user surveys.

Discrepancies must be assigned, risk assessed, and resolved. Material unapproved use should be restricted pending intake.

## Data-quality rules

- Required fields cannot be satisfied by placeholders such as “TBD” after production approval.
- Owners must be active named roles or groups, not departed individuals.
- Enumerated fields must use controlled values.
- Dates and versions must be machine-readable.
- Links must resolve to current evidence or explicitly archived records.
- A system may not be marked approved if approval is expired, conditions are unmet, or the production baseline is unknown.
- A retired system may not retain active identities, schedules, endpoints, or tool permissions without documented need.

## Inventory metrics

- Records complete by lifecycle status and risk tier.
- Production systems reconciled to technical discovery sources.
- Unregistered systems found and time to disposition.
- Records with missing, inactive, or disputed owners.
- Approvals, assessments, monitoring reviews, and exceptions due or overdue.
- Systems by provider, model family, sensitive-data class, business process, autonomy, and action privilege.
- Retired records with residual access or dependency exceptions.

## Minimum quarterly certification

For production systems, the business and technical owners should certify that:

- the intended use, users, data, autonomy, and dependencies remain accurate;
- the deployed baseline is represented correctly;
- approval conditions, testing, monitoring, and exceptions are current;
- incidents and material changes have been recorded; and
- continued use remains necessary and within risk appetite.

---
schema_version: "1.0"
artifact_id: CHECK-AGENT-002
title: Agentic AI Audit Readiness Checklist
artifact_class: checklist
artifact_type: checklist
domains:
  - agentic-ai
  - audit-readiness
  - evidence
applies_to:
  - agentic-ai
  - multi-agent-systems
industries:
  - cross-industry
lifecycle_stages:
  - validation
  - deployment
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-18
source_artifacts:
  - Agentic_AI_Auditing_Framework.docx
---

# Agentic AI Audit Readiness Checklist

## Scope and criteria

- [ ] Audit objective, period, population, risk tier, autonomy level, locations, and control criteria are approved.
- [ ] The unit of analysis is the full agent system, not only the model or vendor service.
- [ ] Business objective, prohibited uses, affected parties, maximum reachable impact, and residual-risk owner are documented.
- [ ] Design, implementation, operating-effectiveness, and outcome-effectiveness conclusions will be recorded separately.

## Architecture and inventory

- [ ] Production architecture and data/control-flow diagrams identify models, prompts, orchestration, data, retrieval, memory, tools, agents, protocols, identities, providers, logs, and downstream systems.
- [ ] Inventory records reconcile to deployed endpoints, service identities, gateways, tool/server catalogs, repositories, and provider accounts.
- [ ] Versions and baselines cover model, prompt/policy, retrieval, memory, tool/schema, agent graph, MCP/SDK, permissions, and monitoring.
- [ ] Unsupported, unowned, unknown, duplicate, shadow, or retired components have been resolved.

## Governance and accountability

- [ ] Business, technical, data, security, privacy, vendor, validation, operations, and audit responsibilities are assigned.
- [ ] Approval authority matches tier and autonomy; developers and agents cannot self-approve reserved matters.
- [ ] Exceptions state scope, compensating controls, owner, due date, expiry, and retest.
- [ ] Material change, incident, suspension, rollback, and retirement decision rights are explicit.

## Identity, tools, and action authority

- [ ] Human and workload identities, delegated authority, scopes, audiences, expiry, rotation, and revocation are documented.
- [ ] Each tool/server/action has an owner, purpose, version, integrity source, operations, data access, destinations, and risk classification.
- [ ] High-impact actions use deterministic authorization and exact-action approval where required.
- [ ] Self-escalation, self-approval, token misuse, cross-tenant action, replay, parameter substitution, and limit evasion have been tested.

## Data, retrieval, memory, and privacy

- [ ] Data classification, source authorization, lineage, minimization, residency, retention, deletion, and provider use are documented.
- [ ] Retrieval, memory, logs, and agent-to-agent context are isolated by the required user, tenant, role, case, environment, and region boundaries.
- [ ] Memory writes are provenance-aware, reviewable, correctable, expirable, and deletable.
- [ ] Sensitive content and credentials are excluded or minimized in prompts, context, tool arguments, memory, and traces.

## Testing and control effectiveness

- [ ] Requirements and failure modes trace to scenarios, metrics, acceptance criteria, and findings.
- [ ] Testing covers intended behavior, goal drift, permission boundaries, adversarial context, tool misuse, memory poisoning, delegation, loops, partial failure, and intervention.
- [ ] Long-horizon and multi-agent tests use the production-intended configuration and authoritative downstream outcome checks.
- [ ] Prior incidents, findings, exceptions, and material changes are included in regression coverage.
- [ ] Independent challenge and retesting are proportionate to tier.

## Observability and evidence

- [ ] Correlation links initiating identity, purpose, agent/model/configuration, retrieval/memory, authorization, approval, tool call, state change, and final outcome.
- [ ] Sampled runs can be reconstructed without relying on hidden chain-of-thought or agent self-report.
- [ ] Evidence is access-controlled, integrity-protected, retained appropriately, and minimized for privacy/security.
- [ ] Trace gaps, clock/correlation errors, disabled logging, and evidence export failure have been tested.

## Monitoring, resilience, and incidents

- [ ] Monitoring covers behavior, quality, permissions, tools/servers, data, drift, cost, loops, failures, overrides, and trace completeness.
- [ ] Thresholds, alerts, owners, response times, escalation, and recurring review are documented and evidenced.
- [ ] Agent, queue, tool/server, credential, endpoint, and child-task containment paths have been exercised.
- [ ] Rollback, compensation, idempotency, reconciliation, checkpoint recovery, and safe degraded mode have been tested.
- [ ] Incident exercises preserve evidence and address provider/customer notification and remediation.

## Third parties and protocol dependencies

- [ ] Provider due diligence and contracts address AI behavior, data use, security, changes, incidents, evidence, deletion, continuity, and exit.
- [ ] Assurance reports have been assessed for scope, period, exceptions, and complementary customer controls; they are not the sole control conclusion.
- [ ] MCP/A2A/protocol and SDK versions, enabled extensions, authentication model, deprecations, and migration obligations are current.
- [ ] External servers, tools, packages, agent cards/catalogs, and schemas are approved, monitored, and removable.

## Reporting and remediation

- [ ] Workpapers identify criteria, procedure, population/sample, evidence, result, limitation, conclusion, reviewer, and date.
- [ ] Findings distinguish root cause, condition, criteria, effect, risk, affected population, compensating controls, and reproducibility.
- [ ] Management actions have accountable owners, measurable outcomes, due dates, validation evidence, and retest criteria.
- [ ] Residual risk, scope limitations, unavailable evidence, and reliance on provider assertions are explicit.

---
schema_version: "1.0"
artifact_id: GOV-AGT-001
title: Agentic AI Governance and Assurance Profile
artifact_class: governance
artifact_type: control-profile
domains:
  - agentic-ai
  - autonomy
  - delegated-authority
  - assurance
applies_to:
  - agentic-ai
  - multi-agent-systems
  - llm
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
last_reviewed: 2026-08-18
source_artifacts:
  - Agentic_AI_Auditing_Framework.docx
  - GenAI Audit Checklist v3.xlsx
  - GenAI Testing Procedures v2.docx
---

# Agentic AI Governance and Assurance Profile

## Purpose

This profile applies the library's governance framework to AI systems that can pursue goals through planning, tool use, persistent or session state, delegation, communication, or external action. It does not replace the core governance, data, security, testing, or vendor requirements. It identifies where those requirements must be strengthened because the system can act rather than only generate content.

The unit of governance and assurance is the **full agent system**, including models, prompts, orchestration, tools, identities, data and retrieval, memory, policies, approvals, downstream systems, operators, providers, and evidence pipelines.

## Applicability

Apply this profile when any component can:

- select, sequence, or retry actions across multiple steps;
- invoke tools, APIs, code, connectors, robots, or other agents;
- read or modify persistent state or memory;
- send messages, publish content, transact, execute, delete, or administer;
- act using a human's or workload's delegated authority;
- continue work without contemporaneous human approval; or
- create child agents, delegate tasks, or communicate through A2A, MCP, or another protocol.

A chatbot without tools may still require GenAI controls, but it is not necessarily agentic. Marketing labels do not determine applicability; demonstrated architecture and reachable capability do.

## Governance principles

1. **Govern the system, not only the model.** Approval and testing cover every component that can influence an outcome or action.
2. **Bound delegated authority.** The agent receives only the identity, data, tools, operations, destinations, time, and transaction scope necessary for the approved task.
3. **Enforce controls outside model-controlled content.** Authorization, approval, schema validation, limits, and containment cannot depend solely on prompts or model refusal.
4. **Treat all context channels as potentially untrusted.** User input, retrieval, email, files, web content, tool results, memory, metadata, and other agents can carry instructions.
5. **Preserve accountable intervention.** Material actions must be observable, interruptible, recoverable, and attributable to an accountable human or workload identity.
6. **Assure behavior over time and across sequences.** Single-turn output testing is insufficient for long-horizon, stateful, or multi-agent behavior.
7. **Minimize evidence exposure.** Capture what is needed to reconstruct decisions and actions without creating an uncontrolled store of sensitive prompts, context, memory, or credentials.

## Autonomy and authority classification

Record the highest production mode and the maximum reachable authority, including failure and misuse paths.

| Level | Operating mode | Minimum governance expectation |
|---|---|---|
| A0 — Assist | Generates information; no tool or external action | Standard GenAI controls and human verification |
| A1 — Propose | Prepares a plan or exact action for human execution | Show evidence, limitations, and material parameters to the reviewer |
| A2 — Gated act | Executes only after approval of the specific material action | Deterministic authorization, approval integrity, expiry, and replay protection |
| A3 — Bounded autonomy | Executes approved classes of action within limits while monitored | Strong workload identity, least privilege, continuous telemetry, budgets, tested containment, and recovery |
| A4 — Extended autonomy | Pursues open-ended or long-running objectives with broad or consequential reach | Exceptional approval; independent assurance; narrow environments; continuous control evaluation; credible fallback and blast-radius limits |

The level does not replace risk tiering. A low-frequency A2 transaction may be more consequential than a high-volume A3 administrative workflow.

## Required governance record

The inventory and approval record must identify:

- business objective, success conditions, prohibited objectives, owner, users, and affected parties;
- autonomy level, action authority, credible maximum impact, reversibility, and intervention window;
- complete architecture and trust boundaries, including models, orchestration, retrieval, memory, tools, agents, protocols, providers, and downstream systems;
- human and workload identities, credential owners, delegated authority, approval points, and segregation of duties;
- tool and protocol inventory, versions, schemas, operations, data access, destinations, and provider status;
- memory and state purpose, provenance, isolation, retention, correction, deletion, and recovery;
- test baseline, scenario coverage, acceptance criteria, residual risk, approval conditions, and expiry;
- monitoring, incident, kill-switch, rollback, compensation, and retirement responsibilities; and
- evidence locations and retention/minimization rules.

## Twelve-domain control model

| Domain | Governing question | Required outcome |
|---|---|---|
| Use case and risk | What objective and impact are authorized? | Purpose, boundaries, tier, autonomy, affected parties, and prohibited uses are explicit |
| System boundary | What constitutes the production agent system? | Every material component, data flow, trust boundary, and dependency is inventoried and versioned |
| Accountability and lifecycle | Who may build, approve, operate, challenge, and stop it? | Decision rights, stage gates, exceptions, and change triggers are enforceable |
| Identity and tool authority | On whose behalf can the system act? | Human/workload identity, least privilege, approval, and revocation operate at action time |
| Data, privacy, retrieval, and memory | What information can influence or persist? | Classification, authorization, provenance, isolation, minimization, retention, and deletion are enforced |
| TEVV | How is intended and adverse behavior evaluated? | Risk-based requirements, long-horizon scenarios, independent challenge, and regression evidence support release |
| Observability and evidence | Can a material run be reconstructed? | Correlated decision-and-action traces support accountability without requiring hidden chain-of-thought |
| Monitoring and drift | What changes after release? | Behavior, tools, permissions, prompts, data, providers, cost, and configuration changes trigger action |
| Resilience and incident response | Can unsafe behavior be contained and corrected? | Limits, safe failure, isolation, revocation, rollback/compensation, and evidence preservation are exercised |
| Third-party risk | Which provider-controlled behaviors and changes matter? | Due diligence, contract, notification, testing access, concentration, and exit controls are proportionate |
| A2A/MCP and multi-agent | How is authority and context propagated between components? | Identities, protocols, delegation, context, schemas, chaining, and communication evidence are governed |
| Audit reporting and remediation | How is control effectiveness concluded and improved? | Criteria, results, findings, owners, dates, retesting, and residual risk are traceable |

## Minimum agentic control requirements

### Purpose, authority, and segregation

- Define an authorized goal envelope, prohibited actions, success conditions, stop conditions, and maximum duration.
- Prevent an agent from expanding its own privileges, altering its governing policy, approving its own material action, suppressing required evidence, or accepting its own exception.
- Require independent approval for production use and for material increases in autonomy, reach, data, or privilege.
- Bind each material action to the initiating user or approved workload purpose; revalidate authority at execution time.

### Tools and downstream action

- Maintain an approved tool registry with owner, version, integrity source, operations, parameters, data classes, destinations, environment, and risk.
- Separate read, write, execute, communicate, transact, delete, and administrative privileges.
- Validate model-selected tool names, schemas, arguments, recipients, resources, and returned content before use.
- Apply limits, allowlists, rate and cost budgets, dry runs, approval, idempotency, concurrency control, and compensating actions where relevant.

### Memory and state

- Prefer task or session state; require a documented need for persistent memory.
- Isolate state by user, tenant, role, case, environment, and region as applicable.
- Record source and confidence; prevent untrusted memory from changing identity, permissions, policy, approval, or other consequential facts without validation.
- Support correction, deletion, expiry, checkpoint recovery, and verification that restored state does not reintroduce prohibited data or actions.

### Observability and evidence

- Use correlation identifiers across requests, agent instances, models, policies, retrieval, tool calls, approvals, state changes, downstream actions, errors, and outcomes.
- Record decision and action evidence sufficient to reproduce material behavior. Do not require or retain private chain-of-thought; use externally meaningful rationale, selected evidence, policy decisions, and execution facts.
- Make material evidence tamper-evident or access-controlled and append-only where proportionate. Absolute immutability is not assumed when correction, deletion, legal hold, or privacy obligations apply.
- Restrict and minimize logs; exclude credentials and unnecessary content; test evidence export and reconstruction.

### Resilience and intervention

- Define maximum steps, time, retries, recursion, delegation depth, resource use, transaction value, and communication scope.
- Detect goal drift, unusual tools, permission changes, repeated failure, loops, resource spikes, trace gaps, and new communication partners.
- Test suspension of agents, queues, tools, protocol endpoints, jobs, and credentials, plus rollback or compensation of partially completed actions.
- Verify that the kill mechanism has a defined scope, authorized operator, independent path, exercise cadence, and recovery/reconciliation procedure.

## Assurance model

Assurance must distinguish four conclusions:

1. **Design effectiveness:** the control, owner, trigger, authority, evidence, exception path, and failure response are suitable for the risk.
2. **Implementation correctness:** the production-intended architecture and configuration implement the design.
3. **Operating effectiveness:** sampled actions, approvals, access reviews, alerts, changes, incidents, and exercises demonstrate sustained operation.
4. **Outcome effectiveness:** scenario and production evidence show the controls actually prevent, detect, contain, or correct the targeted failure.

The reviewer should remain independent of development and risk acceptance to the degree required by tier. Provider assertions and SOC reports are supporting evidence, not substitutes for system-specific testing or customer-control evaluation.

## Minimum assurance activities

- Confirm the inventory and architecture against deployed configuration and technical discovery.
- Trace every high-impact action from objective through identity, policy, approval, tool execution, resulting state, and reconciliation.
- Test intended performance, objective drift, boundary violations, adversarial context, tool misuse, memory poisoning, multi-agent delegation, loops, fail-safe behavior, and human intervention.
- Sample production runs, denied actions, overrides, changes, incidents, and monitoring exceptions.
- Exercise containment, credential revocation, queue cancellation, tool disablement, rollback/compensation, and evidence export.
- Reperform selected controls and reconcile evidence rather than relying only on walkthrough statements.

Use the [Agentic AI Scenario Library](../../testing/agentic-ai/scenario-library.md) and [Agentic AI Audit Workpaper Template](../../templates/agentic-ai-audit-workpaper-template.md) to document execution.

## Change triggers

Reassess tier, autonomy, controls, and tests before or promptly after:

- a new model, provider, orchestration framework, tool, MCP server, agent, memory type, data source, or protocol version;
- expanded write, execute, communicate, transact, delete, administrative, or cross-tenant authority;
- new users, affected parties, geography, volume, or business process;
- provider-controlled model or platform changes that may alter behavior or evidence;
- material changes to prompts, policies, schemas, permissions, routing, retrieval, or monitoring;
- a serious incident, control bypass, unexplained action, repeated loop, or trace failure; or
- evidence that actual behavior or use has moved outside the approved boundary.

## Related library requirements

This profile should be used with the [AI Governance Framework](../ai-governance-framework.md), [Risk Tiering Framework](../risk-tiering/ai-risk-tiering-framework.md), [AI Inventory Standard](../ai-inventory/minimum-data-standard.md), [Control Objectives](../control-framework/control-objectives.md), and [RAG, Vector, and Agent Data Security Standard](../data-security-governance/rag-vector-agent-data-security.md).

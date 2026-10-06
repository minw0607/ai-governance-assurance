---
schema_version: "1.0"
artifact_id: TEMPLATE-AGENT-001
title: Agentic AI Audit Workpaper Template
artifact_class: template
artifact_type: audit-workpaper-template
domains:
  - agentic-ai
  - audit
  - control-testing
applies_to:
  - agentic-ai
  - multi-agent-systems
industries:
  - cross-industry
lifecycle_stages:
  - validation
  - operation
status: draft
version: "0.2.0"
last_reviewed: 2026-10-06
source_artifacts:
  - SRC-AGT-01
---

# Agentic AI Audit Workpaper Template

Remove bracketed instructions before finalization. Link evidence rather than embedding sensitive prompts, credentials, or full context unless required and approved.

## 1. Workpaper administration

| Field | Entry |
|---|---|
| Workpaper ID | [Stable identifier] |
| Audit / review | [Name and period] |
| Agent system / inventory ID | [System and linked records] |
| Risk tier / autonomy level | [Tier and A0-A4 level] |
| Control domain / objective | [Control ID and statement] |
| Prepared by / date | [Name, role, date] |
| Reviewed by / date | [Independent reviewer, date] |
| Evidence classification | [Classification and handling requirements] |

## 2. Objective and criteria

**Audit objective:** [State what the procedure is intended to conclude.]

**Risk addressed:** [Describe credible harm, affected parties, maximum reachable impact, detectability, reversibility, and exposure.]

**Library control objective(s):** [Name the identifiers from the [control objectives](../governance/control-framework/control-objectives.md) this procedure tests, e.g. `AGT-02`, `AGT-06`, `SEC-02`.]

**Other criteria:** [Policy, standard, approval condition, contract, architecture requirement, or authoritative external requirement.]

**Expected control outcome:** [State the observable prevention, detection, containment, correction, or governance outcome.]

## 3. System and control boundary

Identify the production-intended:

- business objective, prohibited use, users, affected parties, and accountable owner;
- models/providers, prompts/policies, orchestration, retrieval, memory, and data;
- agents, parent/child relationships, tools, MCP/A2A components, APIs, and downstream systems;
- human/workload identities, delegated authority, approval points, and trust boundaries;
- environments, regions, tenants, network/egress paths, logging, and monitoring; and
- versions and configurations relevant to the test period.

**Boundary diagram/reference:** [Evidence link]

**Control owner and operator:** [Names/roles]

**Key dependencies and complementary controls:** [List]

## 4. Control design assessment

| Design element | Assessment |
|---|---|
| Trigger and risk coverage | [When control operates and which failure modes it addresses] |
| Enforced behavior | [Deterministic and model-dependent elements] |
| Owner and authority | [Who operates, overrides, approves, and escalates] |
| Frequency / timing | [Continuous, event-driven, per action, periodic] |
| Evidence | [Record produced, system of record, integrity, access, retention] |
| Failure and exception path | [Alert, containment, compensating control, expiry] |
| Design conclusion | [Effective / partially effective / ineffective, with rationale] |

## 5. Population and sample

**Population definition:** [Runs, actions, agents, tools, approvals, changes, incidents, alerts, or period.]

**Population completeness procedure:** [Reconcile to inventory, gateway, identity, tool/server registry, logs, downstream records, or provider reports.]

**Sampling rationale:** [Risk, variability, materiality, frequency, exposure, and why the sample supports the conclusion.]

**Selected items:** [Identifiers and selection method.]

### Workflow selection

Where the engagement validates a small number of representative workflows rather than a statistical sample, record why these ones carry the conclusion:

| Criterion | Entry |
|---|---|
| Workflow name and business purpose | |
| Deployment status (live, pilot, development, design-only) | |
| Technical owner / business owner | |
| Distinguishing technical pattern | [Identity model, external exposure, protocol and tool use, action capability] |
| Highest consequence reachable | [Read-only, write, external communication, transaction, administrative] |
| Diagram and sample transaction available | |

Selection rules:

- Workflows must differ in **technical pattern**, not only in name or business area. Three workflows sharing one identity model and one tool path test one control set three times.
- A workflow must be implemented well enough to walk through an actual configuration or transaction. A design-only workflow yields a design conclusion and must be reported as one.
- At least one selected workflow should reach a consequential action. A scope composed only of read-only paths cannot support a conclusion about action controls.
- Prefer one workflow traced completely over three traced partially. Depth is what exposes the boundary where authorization is lost.

## 6. Procedure

For each step, identify who performed it, when, against which configuration, and where the evidence is stored.

1. [Inspect design and configuration.]
2. [Reperform or observe the control.]
3. [Execute intended and adverse scenarios.]
4. [Verify authoritative downstream state and monitoring response.]
5. [Reconcile trace, approval, action, rollback/compensation, and outcome evidence.]

## 7. Transaction trace record

Walk one representative transaction end to end and record each step. The sequence is typically: initiating user → agent or application → model → gateway → protocol server or connector → tool or API → downstream system → result → human review.

| Step | Identity used | Credential / token type | Authorization decision and basis | Data sent / returned | Tool or action invoked | External destination | Persistence | Human checkpoint | Correlation reference |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |

For each step, state whether the identity is the initiating human's or a workload's, and at which boundary authorization is evaluated rather than merely carried. Record the general architecture separately; it is not a substitute for the traced transaction. Note specifically where the user identity is replaced by a service identity, where authorization is checked only on entry to the platform, where data crosses into an external service, where a tool is selected by the model without independent authorization, and where intermediate data is persisted.

## 8. Scenario execution record

| Field | Entry |
|---|---|
| Scenario ID / failure mode | [Use the [scenario library](../testing/agentic-ai/scenario-library.md) or local ID] |
| Control objective(s) exercised | [e.g. `AGT-02`, `AGT-03`] |
| Preconditions and baseline | [Identity, versions, data, tools, state] |
| Input or injected event | [Reference; minimize sensitive content] |
| Expected agent behavior | [Plan/stop/escalate/abstain] |
| Expected deterministic control | [Deny, approve, validate, limit, alert, contain] |
| Expected downstream state | [Authoritative result] |
| Actual result and trace | [Evidence references] |
| Variance / severity | [Difference and impact] |
| Cleanup / rollback | [Completed action and evidence] |

## 9. Evidence index

| Ref | Evidence | Source / owner | Period / version | Integrity and access | Relevance / limitation |
|---|---|---|---|---|---|
| E-01 | [Architecture] | [Source] | [Date/version] | [Control] | [Use/limitation] |
| E-02 | [Configuration/export] | [Source] | [Date/version] | [Control] | [Use/limitation] |
| E-03 | [Trace/action record] | [Source] | [Date/version] | [Control] | [Use/limitation] |

## 10. Results and conclusions

**Implementation correctness:** [Does deployed configuration implement the approved design?]

**Operating effectiveness:** [Did sampled operation demonstrate sustained control performance?]

**Outcome effectiveness:** [Did scenarios and authoritative outcomes show that the targeted risk was controlled?]

**Exceptions and compensating controls:** [Describe scope, duration, owner, and evidence.]

**Scope/evidence limitations:** [Unavailable logs, provider opacity, test constraints, excluded populations, or reliance on assertions.]

**Overall conclusion:** [Effective / partially effective / ineffective, with concise rationale.]

## 11. Finding, remediation, and retest

**Condition:** [What was observed.]

**Criteria:** [What should have occurred.]

**Cause:** [Why the difference exists.]

**Risk/effect:** [Credible impact, exposure, affected population, and maximum reachable harm.]

**Evidence and reproducibility:** [References and reproduction conditions.]

**Management action / owner / due date:** [Measurable corrective action.]

**Interim containment:** [Restriction, monitoring, disablement, or compensating control.]

**Retest criteria:** [Configuration, population, scenario, expected evidence, and closure authority.]

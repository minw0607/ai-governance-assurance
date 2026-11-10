---
schema_version: "1.0"
artifact_id: GOV-SEC-006
title: Identity and Access for AI Capabilities
artifact_class: governance
artifact_type: standard
domains:
  - ai-security
  - identity-and-access
  - entitlement-lifecycle
  - privileged-access
applies_to:
  - generative-ai
  - agentic-ai
  - rag
  - llm
industries:
  - cross-industry
lifecycle_stages:
  - design
  - development
  - deployment
  - operation
  - retirement
status: draft
version: "0.1.0"
last_reviewed: 2026-11-16
---

# Identity and Access for AI Capabilities

## Purpose

This library governs identity **inside** an AI system in detail: agent and workload identity, delegated authority, token exchange, least privilege at the tool boundary, and the non-human identity lifecycle. It has not covered the **interface to enterprise identity** — where AI entitlements actually come from, whether the controls that protect other applications reach the AI ones, and whether removing access removes it.

That interface is where most AI access failures originate, because the AI platform usually inherits whatever the enterprise directory already decided.

## Scope boundary

This standard does **not** assess or redesign an enterprise identity programme. Directory architecture, authentication platform selection, and enterprise entitlement design remain governed where they already are.

It covers only what AI access depends on: which identity facts drive AI authorization decisions, how AI entitlements are granted and removed, which privileged roles can change the AI security boundary, and whether identity monitoring reaches AI platforms and workload identities. Where a finding belongs to the enterprise programme rather than to an AI system, record it and route it there rather than absorbing it.

## 1. Identity-attribute authority

AI access decisions are usually made on identity attributes the AI platform did not author — group membership, role, department, practice or business area, employment status, manager, location.

- **Record which attributes AI authorization depends on**, and the authoritative system for each. An attribute with two authoritative systems has none.
- **Record how each attribute reaches the decision point**: automatically, on what interval, or by manual re-entry. Manual re-keying between an HR system of record, a directory, and a cloud identity provider is a control with a human error rate, not a synchronization.
- **AI entitlements are only as current as the upstream attribute.** Where a role or business-area change does not propagate, the AI platform enforces yesterday's entitlements correctly and indefinitely. State the propagation delay and treat exceeding it as a control failure, not a lag.
- **Name an owner for identity-data quality.** Attribute correctness is usually unowned precisely because it spans systems.
- **Account for identities that do not originate in the standard lifecycle** — cloud-only accounts, guests, contractors, vendor-support identities, and shared or departmental accounts. These are commonly outside joiner-mover-leaver processing while remaining inside the groups that grant AI access.
- **Distinguish planned automation from current state.** A roadmap item described in the present tense is the most common way an identity-flow walkthrough misleads.

## 2. Entitlement provenance

Establish, for each AI capability, how access is actually obtained. Four patterns recur and each defeats approval:

- **A license assignment is not an access approval.** Assigning a seat is a procurement action. Where assignment alone grants reach into enterprise content, the approval record for that reach does not exist.
- **A broad pre-existing group is not a scoped entitlement.** Enabling an AI capability for an existing directory group — everyone with an account, everyone in a region — grants it by default to a population nobody assessed, and the population changes without any AI decision.
- **Copying a colleague's access is not a role model.** Provisioning by cloning another account propagates whatever that account accumulated, including its own errors, and leaves no statement of what the access is for.
- **Movers are the weak case, not leavers.** Departures attract attention and tooling. A transfer between roles or business areas commonly adds the new entitlements and keeps the old ones, including AI platform access, content permissions, connected applications, and consents.

Record per capability: the granting mechanism, the approver, the scope granted, the review or expiry, the removal path, and where the evidence lives. A capability whose granting mechanism cannot be stated cannot be reviewed.

## 3. Authentication and session controls

- **Confirm each AI capability is behind the enterprise authentication, multi-factor, conditional-access and session controls**, by configuration rather than by assumption. "Where available" is not a control statement; maintain an exception register with owner, rationale, compensating control, and expiry.
- **Treat a local credential path as an exception.** An AI platform with its own sign-in sits outside enterprise authentication, conditional access, and session policy entirely, and will not appear in identity monitoring built around them.
- **Record which access paths carry which controls.** Browser, desktop application, mobile, and API paths to the same capability frequently differ, and the weakest path is the control.
- **State whether unmanaged devices can reach each capability**, and what applies if they can.
- **Do not exempt administrators or workload identities from stronger controls.** They are the identities whose compromise matters most and the ones most often excluded for convenience.

### Disabling an account is not terminating a session

Disabling a directory account stops **new** authentication. It does not, by itself, end sessions already established or invalidate tokens already issued. An AI platform session, a refresh token, or a connected application's grant can remain usable until it expires.

- Establish, per AI capability, what account disablement actually terminates and what survives it, and for how long.
- Where sessions survive, name the action that ends them and who may take it, and set token lifetimes against the revocation requirement rather than against convenience.
- Test this. The requirement is not a policy target but a measured end-to-end time from the disablement action to loss of access across the directory, the AI platforms, connected tools, and live sessions.
- Distinguish four separate times and report them separately: the **policy target**, the **directory propagation** interval, **application-level** entitlement removal, and **active-session** termination. A single number covering all four is almost always the first one.

## 4. Access review

- **Reviews must cover workload and agent identities**, not only people. A review population drawn from human accounts omits the identities with the broadest standing reach.
- **Define the frequency.** "Periodic" without an interval cannot be found non-compliant.
- **Review effective permissions, not assignments** — what the identity can reach, including inherited and transitive access.
- **Track findings to closure.** An identified and unresolved exception is a completed review only in the register.
- **Require a completed example.** A review process with no completed instance is a design, and must be reported as one.
- **Name an owner per granting group.** Where several groups grant access to the same capability, each needs an owner, or the review has no respondent.

## 5. Privileged roles that can change the AI security boundary

General privileged-access control is governed by `SEC-02` and enterprise standards. This section concerns the narrower set of privileges that can **alter AI authorization without changing the AI system**:

- granting or consenting to an application's access to enterprise data;
- registering an application or creating a workload identity;
- granting or expanding API permissions and scopes;
- administering an AI platform, its tenant settings, or its connectors;
- changing a workload identity's effective permissions;
- registering or enabling a protocol server, tool, or connector; and
- changing conditional-access, session, or exception configuration affecting AI paths.

Requirements:

- **Enumerate the roles holding these privileges** and who holds them, as a named list rather than a role description.
- **Prefer time-bound elevation to standing privilege.** Standing membership in a role that can grant an application access to enterprise content is a persistent path around every AI approval in this library.
- **Govern emergency and break-glass accounts explicitly**: how they are protected, how use is detected, and what review follows each use. An untested break-glass path is unevidenced; an unmonitored one is undetectable.
- **Set a service level for sensitive identity requests.** Where central provisioning is slow, teams build their own authorization — the custom model is a *symptom*, and the delay is the cause. Fixing one without the other reproduces it.
- **Make custom authorization models reviewable.** An authorization model implemented inside an application and never examined by the security function is an unassessed control, whatever its quality.

## 6. Delegated application consent

A consent grant — by a user or an administrator — gives an application standing access to enterprise data under the granting identity's authority. It is an access path that no AI approval in this library necessarily touched.

- **Inventory consent grants** reaching enterprise content, with the application, the granting identity, the scopes, and whether consent was user or administrative.
- **Restrict user consent** for scopes that reach enterprise content, and route them to an approval that names the data and the actions, per `AGT-01`.
- **Review grants on the access-review cycle**, and remove those whose purpose has lapsed. Consent persists after the person who granted it leaves.
- **Include service principals, connectors, and vendor-support identities** in the inventory. A capability the organization did not deploy can still reach its data.

## 7. Identity monitoring for AI paths

Identity monitoring commonly predates the AI platforms and does not reach them. Confirm coverage rather than assume inheritance; detections are specified in the [detection catalog](detection-catalog.md).

- Establish whether a new or changed consent grant, a workload identity reaching a new resource, an administrative change to an agent's permissions, or an anomalous or persistent session raises an **alert with a named responder** — or only a log entry (`SEC-05`).
- Confirm activity can be correlated between the initiating human and the workload identity performing the downstream action (`AGT-06`).
- Where an AI capability is vendor-operated and its identity telemetry is available only to the vendor, record that as a monitoring gap with a compensating control, not as covered.

## Minimum evidence

- attribute-authority record: attributes AI authorization depends on, authoritative system for each, propagation mechanism and delay, owner;
- per-capability entitlement record: granting mechanism, approver, scope, review or expiry, removal path, evidence location;
- authentication and session configuration per access path, with the exception register;
- tested end-to-end revocation times, reported separately for policy target, directory propagation, application removal, and session termination;
- completed access reviews including workload and agent identities, with exceptions tracked to closure;
- the enumerated list of privileges able to change the AI security boundary, with holders and elevation model;
- break-glass protection, use detection, and post-use review records;
- consent-grant inventory with scopes, granting identity, and review date; and
- identity detection coverage for AI paths, with named responders.

## Related artifacts

- [AI Security Overlay](README.md)
- [Enterprise AI Control Objectives](../control-framework/control-objectives.md) — `SEC-02`, `AGT-01`, `AGT-06`, `DATA-02`
- [AI Security Detection Catalog](detection-catalog.md)
- [A2A, MCP, and Multi-Agent Control Standard](../agentic-ai/a2a-mcp-multi-agent-control-standard.md)
- [RAG, Vector, and Agent Data Security Standard](../data-security-governance/rag-vector-agent-data-security.md) — information barriers and permission synchronization
- [AI Governance Roles and Decision Rights](../operating-model/roles-and-decision-rights.md)

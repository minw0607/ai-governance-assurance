---
schema_version: "1.0"
artifact_id: GOV-SEC-004
title: AI Security Incident Response
artifact_class: governance
artifact_type: procedure
domains:
  - ai-security
  - incident-response
  - containment
applies_to:
  - generative-ai
  - agentic-ai
  - rag
  - llm
industries:
  - cross-industry
lifecycle_stages:
  - deployment
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-10-08
---

# AI Security Incident Response

## Purpose

`OPS-02` requires that AI incidents be detected, contained, investigated, reported, recovered, and used to improve controls. This artifact states what differs from a conventional security incident, because applying a standard playbook unchanged fails in predictable ways.

It extends the enterprise incident process; it does not replace it. Severity criteria, notification obligations, legal and regulatory analysis, and communications remain governed there.

## What differs

| Conventional assumption | What holds for an AI system |
|---|---|
| Stopping the service stops the harm | Dispatched, queued, scheduled, and child-agent work continues after the component is disabled |
| Reverting the release undoes the change | A deployment revert replaces what starts next; it neither stops running executions nor undoes completed actions |
| The affected data is in the system you contained | Content has propagated to indexes, caches, embeddings, memory, summaries, exports, and provider copies |
| Logs are a supporting record | The trace is frequently the *only* record of what the system decided and did |
| The actor is a person or a process | The actor may be the model, acting on instructions embedded in content nobody reviewed |
| Remediation is a patch | Remediation may require rebuilding an index, purging memory, or rotating a delegation model |

## Response sequence

### 1. Detect and declare

Entry points include a detection from the [catalog](detection-catalog.md), a user or reviewer report, a provider notification, a downstream data-integrity discrepancy, or an audit finding.

Declare on suspicion. An agent acting under borrowed authority can complete a great deal of work during the interval spent establishing whether an incident is real.

### 2. Preserve before you contain

Containment destroys evidence in AI systems more readily than in conventional ones — context windows, in-memory state, ephemeral environments, and provider-side logs with short retention.

Before acting, capture: the correlation identifiers for affected executions, the trace of decisions and tool calls, the retrieved context and its sources, the prompt and policy versions in force, the model and configuration identifiers, the tool and protocol definitions as they stood, approval records, and the downstream state as it is now.

Where an ephemeral environment is implicated, snapshot it before teardown. Scheduled teardown will otherwise destroy the evidence on its normal cycle.

### 3. Contain at the right scope

Establish what is running before deciding what to stop. Then contain in this order:

1. **Stop in-flight execution** — cancel running tasks, drain queues, suspend schedules and triggers, halt child agents. This is distinct from every other action here.
2. **Remove the capability** — disable the specific tool, server, connector, route, or action rather than the platform, where the implementation allows it.
3. **Revoke the authority** — invalidate the workload identity, delegations, tokens, and secrets. A disabled component whose credentials remain valid can still be driven by anything holding them.
4. **Isolate the content** — suppress retrieval from affected sources, indexes, caches, and memory. Suppression is reversible and is the right first move while scope is unknown.
5. **Hold the change surface** — freeze registration, enablement, and definition changes for the affected components so the picture stops moving during investigation.

Record which of these the implementation actually supports. Where the only available action is a platform-wide shutdown, that is the containment capability, and it is also a finding.

### 4. Establish scope

Scope questions specific to AI incidents:

- **What did it do?** Every action taken, not only the one detected. Reconstruct from the trace; where the trace is incomplete, say so and treat the gap as unbounded.
- **What did it read?** Which sources, compartments, and classifications entered context, and under whose authority.
- **What left?** Outputs, summaries, citations, tool arguments, external communications, exports, and telemetry. Derived disclosure counts: an aggregate that reveals restricted content is a disclosure.
- **Who is attributable?** The initiating human for each action, not only the service identity that performed it. Where only the service identity is recorded, attribution is a finding in its own right.
- **How far did content propagate?** Source, index, cache, embedding, memory, logs, exports, downstream systems, provider copies.
- **Is state consistent?** Partially completed, duplicated, and compensated actions reconciled against the authoritative downstream record — not against the agent's own report of what it did.
- **Is it still reachable?** Other agents, workflows, or consumers sharing the same tool, identity, index, or model route.

### 5. Eradicate and recover

- Remove the cause, not the symptom: the poisoned source, the unapproved tool, the over-scoped identity, the missing authorization check.
- Rebuild rather than clean where integrity cannot be established — an index, memory store, or environment of uncertain state is rebuilt from an approved baseline.
- Verify recovery does not reintroduce the problem: revoked identities, unsafe catalogs, poisoned memory, withdrawn versions, and pre-incident backups.
- Reconcile downstream state and correct records the system altered.
- Recover deliberately. Restoring service requires validation and reapproval at the tier's authority, not re-enablement (`OPS-03`).

### 6. Report and improve

Beyond the enterprise post-incident requirements, record:

- whether the threat model contained this path, and update it where it did not (`SEC-01`);
- the detection that fired, or the detection that should have existed, added to the [catalog](detection-catalog.md);
- a permanent regression case for the failure, so a future change cannot silently reintroduce it (`QUAL-06`);
- the containment actions the implementation could not perform, as remediation with an owner and date; and
- whether evidence was sufficient to reach these conclusions, and what instrumentation is needed if not.

## Roles and authority

Record, before an incident, who may act without further approval:

| Action | Authority to record |
|---|---|
| Declare an AI security incident | |
| Cancel in-flight agent execution | |
| Disable an agent, tool, server, or route | |
| Revoke a workload identity or delegation | |
| Suppress retrieval from a source or index | |
| Approve restoration of service | |

Containment authority that requires an approval chain is containment that will not happen in time. Name the role, not the person, and confirm out-of-hours coverage.

## Exercise

Tabletop and technical exercises should include: an injected instruction causing an unauthorized tool call; a poisoned retrieval source discovered after weeks of use; a credential compromise where a workload identity has broader reach than any user; a cascading child-agent fan-out; and an incident where the trace is incomplete. Exercise containment on running work, not at rest — see `AGS-14` and `AGS-16` in the [agentic scenario library](../../testing/agentic-ai/scenario-library.md).

## Related artifacts

- [AI Security Overlay](README.md)
- [AI Security Detection Catalog](detection-catalog.md)
- [AI Threat Modeling Method](threat-modeling-method.md)
- [A2A, MCP, and Multi-Agent Control Standard](../agentic-ai/a2a-mcp-multi-agent-control-standard.md) — limits, containment, and recovery
- [Enterprise AI Control Objectives](../control-framework/control-objectives.md) — `OPS-02`, `AGT-03`, `SEC-05`
- [Findings Report Template](../../templates/findings-report-template.md)

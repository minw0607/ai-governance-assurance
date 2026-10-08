---
schema_version: "1.0"
artifact_id: GOV-SEC-003
title: AI Security Detection Catalog
artifact_class: governance
artifact_type: standard
domains:
  - ai-security
  - detection-engineering
  - monitoring
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

# AI Security Detection Catalog

## Purpose

`SEC-05` requires that security events be reconstructable and `OPS-01` requires that indicators lead to action. Between them sits a gap most AI deployments fall into: the events are logged, and nothing happens when they occur.

This catalog states what to detect, what signal carries it, and what the response is. Detections are starting points to tailor, not a conformance list.

## Recording is not detecting

Three conditions must hold before a control is monitored rather than merely logged:

1. **The signal exists** — the event is emitted with enough fidelity to distinguish it from normal activity.
2. **A rule evaluates it** — with a threshold, a window, and a tuned false-positive rate.
3. **A named responder owns the outcome** — with a defined response path and a service level.

A detection missing the third condition is a dashboard. Record the responder in the [monitoring plan](../../templates/monitoring-plan-template.md), by role, with an escalation path.

Two further requirements apply across every detection below:

- **Log denials, failures, and fallbacks as completely as successes.** A telemetry set containing only what worked cannot show that a control held, and most of these detections fire on the denial.
- **Keep telemetry out of scope for disclosure.** Credentials, tokens, full prompts, sensitive tool arguments, and client content must not be captured to make a detection work. Where a detection needs content, detect on metadata, hashes, or classifications instead.

## Catalog

Each detection names the control objective it evidences. Severity is indicative; set it from the system's tier.

### 1. Authorization and access

| ID | Detect | Signal | Response |
|---|---|---|---|
| `DET-01` | Denied retrieval or tool call spike for one identity, agent, or session | Authorization decision logs, denial rate against baseline | Investigate intent; distinguish misconfiguration from probing (`DATA-02`, `AGT-01`) |
| `DET-02` | Cross-boundary access attempt — tenant, compartment, business unit, region, or environment | Boundary decision logs with the boundary named | Treat as potential disclosure; preserve evidence before remediating (`DATA-02`) |
| `DET-03` | Information-barrier decision, logged distinctly from an ordinary permission denial | Barrier evaluation events | Confirm the barrier held across derived and aggregate paths, not only document return (`DATA-02`) |
| `DET-04` | A denied authorization followed by the same call succeeding under a different identity | Correlated decision logs across identities within a window | Treat as privilege escalation until disproven; this is the signature of identity-fallback abuse (`AGT-06`) |
| `DET-05` | Delegated-identity failure followed by continuation under a workload identity | Token exchange failures correlated with subsequent calls | Verify the path is approved and the fallback identity bounded to the user's reach (`AGT-06`) |
| `DET-06` | Permission synchronization stale beyond the approved tolerance | Sync job status, reconciliation age | Fail closed for affected corpora; do not wait for the next cycle (`DATA-02`, `QUAL-04`) |

### 2. Untrusted content and injection

| ID | Detect | Signal | Response |
|---|---|---|---|
| `DET-07` | Instruction-like patterns in retrieved content, tool responses, or uploads | Content inspection at ingestion and at tool-response handling | Quarantine the source; assess what the agent did while it was trusted (`SEC-03`) |
| `DET-08` | Agent behavior diverging from its declared task — unexpected tool, destination, or recipient | Trace comparison against the agent's approved tool and destination set | Contain the execution; treat as possible injection or goal drift (`AGT-01`, `AGT-02`) |
| `DET-09` | Outbound content matching canary, secret, or sensitive-pattern signatures | Egress inspection on tool calls, external communication, and output | Block and investigate the full path, including summaries and citations (`DATA-03`) |
| `DET-10` | Unusual retrieval breadth, sequential enumeration, or export volume | Query shape and volume against role baseline | Assess for reconstruction of restricted attributes across authorized queries (`QUAL-04`) |

### 3. Action and approval integrity

| ID | Detect | Signal | Response |
|---|---|---|---|
| `DET-11` | Consequential action executed without a matching approval record | Join of action events to approval events; alert on the unmatched set | Reverse or compensate; establish whether the gate is enforced or instructed (`AGT-02`) |
| `DET-12` | Action parameters differing between approval and execution | Parameter hash at approval compared with execution | Treat as approval bypass; preserve both records (`AGT-02`) |
| `DET-13` | Approval replay, duplicate execution, or concurrent approval race | Approval identifier reuse, idempotency key collisions | Reconcile downstream state; verify single-use binding (`AGT-07`) |
| `DET-14` | A gated action reached through an alternative tool, alias, endpoint, or retry | Action-effect events without the corresponding gate event | Close the alternate path; re-test every route to the same effect (`AGT-02`) |
| `DET-15` | Agent attempting self-escalation, self-approval, policy change, or credential retrieval | Denied privileged operations attributed to an agent identity | Contain; these should be structurally impossible, so a single occurrence is a design finding (`AGT-06`) |

### 4. Identity and credentials

| ID | Detect | Signal | Response |
|---|---|---|---|
| `DET-16` | Non-human identity active after its agent was disabled or retired | Identity usage correlated against agent lifecycle state | Revoke immediately; this is the common residue of containment (`SEC-02`, `OPS-04`) |
| `DET-17` | One identity used by unrelated agents or workflows | Caller attribution per identity | Separate the identities; shared identities defeat attribution and least privilege (`SEC-02`) |
| `DET-18` | Long-lived static credential in use where short-lived was required | Credential type and age at authentication | Rotate and convert; record as an exception until closed (`SEC-02`) |
| `DET-19` | Token used against an unintended audience, or validation disabled | Audience and issuer validation outcomes | Verify the check is enabled; a disabled check is an exception with owner and expiry (`AGT-06`) |

### 5. Protocol, tool, and supply chain

| ID | Detect | Signal | Response |
|---|---|---|---|
| `DET-20` | New or changed server, tool, schema, description, alias, or parameter default | Registry diff against the approved baseline | Re-review before use; a description change can increase capability without a schema change (`AGT-01`, `SEC-04`) |
| `DET-21` | Call to an unapproved server, tool, endpoint, or destination | Allowlist enforcement denials | Investigate how the call was constructed; verify the allowlist is enforced, not advisory (`AGT-01`) |
| `DET-22` | Administrative change to registration, enablement, or permissions | Administrative audit records | Attribute to a person and an approval; absence of attribution is a control gap (`AGT-01`) |
| `DET-23` | Model, package, image, or adapter deployed without matching provenance | Deployment events joined to signature or attestation verification | Block promotion; treat unverifiable artifacts as untrusted (`SEC-04`) |

### 6. Resource, resilience, and environment

| ID | Detect | Signal | Response |
|---|---|---|---|
| `DET-24` | Runaway execution — step, recursion, delegation-depth, duration, or concurrency limit approached | Per-agent counters against configured limits | Automatic containment, not an alert awaiting a human (`SEC-06`, `AGT-05`) |
| `DET-25` | Cost or token consumption anomaly attributable to one agent or workflow | Per-agent usage against baseline and budget | Throttle or stop; an account-level quota is not an agent control (`SEC-06`) |
| `DET-26` | Sandbox or ephemeral environment exceeding its lifetime, or surviving failure | Environment lifecycle events against expected teardown | Force teardown; investigate persistence of files, credentials, and processes (`GOV-07`) |
| `DET-27` | Egress from an environment declared to have none | Network flow records against the declared policy | Treat the declared boundary as unverified until re-tested (`GOV-07`, `SEC-03`) |

### 7. Evidence integrity

| ID | Detect | Signal | Response |
|---|---|---|---|
| `DET-28` | Trace gap — a transaction missing steps, or a correlation chain that does not join | Completeness check against the expected step sequence | Investigate as potential evasion as well as instrumentation failure (`SEC-05`, `AGT-03`) |
| `DET-29` | Log source silent or degraded | Volume and heartbeat monitoring per source | Treat as a control outage with a response path, not a telemetry nuisance (`SEC-05`) |
| `DET-30` | Unauthorized access to, or modification of, audit records | Log-store access events | Preserve and escalate; evidence integrity is the basis of every other conclusion (`SEC-05`) |

## Coverage and tuning

- **Derive coverage from the threat model**, not from this list. Each boundary finding marked *implemented* should map to at least one detection, and each detection should trace to a credible failure. See the [AI Threat Modeling Method](threat-modeling-method.md).
- **Set thresholds above measured variance.** A detection tuned before a baseline exists will be disabled within a month.
- **Test the detection, not only the control.** Generate the condition and confirm the alert reaches the named responder. An untriggered rule is unverified, and a rule that has never fired should be checked for sensitivity before being trusted.
- **Review after change.** A model, prompt, tool, protocol, or platform change can silently remove the signal a detection depends on.

## Related artifacts

- [AI Security Overlay](README.md)
- [AI Threat Modeling Method](threat-modeling-method.md)
- [AI Security Incident Response](incident-response.md)
- [Enterprise AI Control Objectives](../control-framework/control-objectives.md) — `SEC-05`, `OPS-01`
- [Monitoring Plan Template](../../templates/monitoring-plan-template.md)
- [AI Ongoing Monitoring Checklist](../../checklists/ongoing-monitoring.md)

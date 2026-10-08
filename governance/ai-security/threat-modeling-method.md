---
schema_version: "1.0"
artifact_id: GOV-SEC-002
title: AI Threat Modeling Method
artifact_class: governance
artifact_type: methodology
domains:
  - ai-security
  - threat-modeling
  - secure-design
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
  - validation
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-10-08
---

# AI Threat Modeling Method

## Purpose

The library requires a threat model at `SEC-01` and references one at gate G2, in the pre-deployment checklist, and across the data-security and agentic standards. This artifact supplies the missing procedure: how to produce one for an AI-enabled system, and what distinguishes an adequate model from a threat list.

A generic threat list is not a threat model. A threat model is tied to **this** system's trust boundaries, names what is affected, and states which control prevents each failure today — with the residual exposure written down where no control does.

## Scope the model to a workflow, not a platform

Model a **workflow**: one business transaction, traced end to end. Platform-level models produce platform-level findings that no owner can act on.

Where several workflows exist, select them as the [audit workpaper](../../templates/agentic-ai-audit-workpaper-template.md) directs — different technical patterns rather than different business areas, implemented enough to walk through, and at least one that reaches a consequential action. One workflow modeled completely is worth more than three modeled partially.

## Step 1 — Trace the transaction

Walk the actual path and record each hop. A typical sequence is:

```
initiating user → agent or application → model → gateway
    → protocol server or connector → tool or API
    → downstream system → result → human review
```

For each step record the identity in use, the credential type, where authorization is evaluated, the data sent and returned, the destination, what persists, and the correlation reference. Use the trace record in the [audit workpaper](../../templates/agentic-ai-audit-workpaper-template.md).

Do not accept an architecture diagram in place of the trace. The diagram shows what was designed; the trace shows what executes.

## Step 2 — Mark the trust boundaries

A trust boundary is any point where data, instructions, or authority change hands. In AI systems the recurring ones are:

| Boundary | What crosses | What is commonly lost |
|---|---|---|
| Untrusted content → model context | Retrieved documents, web content, email, uploads, tool and protocol responses | The distinction between data and instruction |
| Model → tool selection | A chosen operation and its parameters | Independent authorization of the choice |
| User identity → workload identity | Delegated authority | The initiating user's permission ceiling, and attribution |
| Application → external service | Prompts, context, documents, parameters | Destination control and provider data-use limits |
| Source system → derived store | Content plus its security attributes | Barriers, labels, deletion and hold status |
| Agent → agent or child task | Goals, context, and authority | Delegation depth, scope, and provenance |
| Environment → environment | Code, configuration, data, credentials | Isolation between lab and production |

Mark each boundary on the trace. Boundaries are where threat modeling is productive; the steps between them rarely are.

## Step 3 — Ask the question at each boundary

At each boundary, ask one question and record a complete answer:

> **What is the most credible security failure at this point, what identity, data, or action would be affected, and what control prevents it today?**

The answer has four parts, and a model missing any part is incomplete:

1. **The failure**, stated as a mechanism rather than a category. "Indirect prompt injection" names a class; "a retrieved document instructs the agent to send its context to an external recipient, and the send tool is reachable without approval" names a failure.
2. **The impact** — which identity, dataset, action, or party is affected, and how badly.
3. **The control**, named specifically and located outside the model where it enforces anything. A system prompt is a mitigation of last resort, not a control.
4. **The evidence** that the control operates, or an explicit statement that none exists.

Where the fourth part is absent, the entry is a design assertion. Record it as such — see [eliciting evidence](../control-framework/control-objectives.md#eliciting-evidence).

## Step 4 — Work the threat set

Use this set as a prompt at each boundary, not as a checklist to complete. Identifiers resolve in the [OWASP LLM](../../mappings/owasp-genai.md) and [OWASP Agentic](../../mappings/owasp-agentic.md) mappings.

| Threat | The question it forces |
|---|---|
| Direct and indirect prompt injection | What untrusted content reaches context, and what can it cause? |
| Excessive agency | What can the system do that its task does not require? |
| Confused deputy | Where does a component act with more authority than its requester? |
| Unauthorized tool invocation | Who authorizes the tool call, independently of the model choosing it? |
| Credential and identity misuse | What happens when a credential is stolen, reused, replayed, or substituted? |
| Data egress | By which paths can content leave, including summaries, citations, and telemetry? |
| Derived-store disclosure | What can be retrieved from an index, cache, embedding, or memory that the source would deny? |
| Poisoning | What happens if a trusted source, index, memory, or tool definition is altered? |
| Malicious or changed protocol component | What if a server, tool, schema, or description changes under you? |
| Supply-chain compromise | What do you deploy that you did not build, and how is its integrity established? |
| Runaway execution and cost abuse | What stops a loop, a fan-out, or a recursive delegation, automatically? |
| Cross-session and cross-environment leakage | What separates sessions, tenants, compartments, and environments? |
| Evidence degradation | If this failed, could you prove what happened? |

Two framing rules keep the exercise honest:

- **Insiders and accidents count.** A model that considers only external attackers omits the authorized user reaching further than intended, and the misconfiguration that grants it.
- **The model is not a control.** Where the answer to "what prevents this" is that the model was instructed not to, the control is absent.

## Step 5 — Decide, record, and route

For each boundary finding, record: the credible failure, the affected identity or data, the control, its evidence state (**implemented, planned, or absent**), the residual exposure, the owner, and the route.

Then route each one:

- **Implemented with evidence** → carry into the test plan as a scenario to verify, not an assertion to repeat.
- **Implemented without evidence** → a testing obligation before release (`QUAL-02`, G4).
- **Planned** → a design-blocking finding if the exposure exceeds the tier's tolerance; otherwise a tracked condition with a date (`GOV-06`).
- **Absent and accepted** → an exception with owner, compensating control, expiry, and approval at the tier's authority. Silence is not acceptance.

Convert the findings into executable cases using the [agentic](../../testing/agentic-ai/scenario-library.md), [security red teaming](../../testing/security-red-teaming/scenario-library.md), and [privacy](../../testing/privacy-data-leakage/scenario-library.md) scenario libraries. A threat model that produces no tests has not been finished.

## When to redo it

Revisit the model when the trace changes, not on a calendar: a new tool, connector, or protocol component; a new data source or derived store; a change in identity or authorization model; an increase in autonomy or action authority; a new consumer or compartment; a model or platform change that alters behavior or limits; or an incident that revealed a path the model did not contain.

## Adequacy test

A threat model is adequate when a reviewer who did not build the system can answer, for each trust boundary, what could go wrong, what it would affect, what stops it, and how that is known. If the document cannot answer those four questions boundary by boundary, it is documentation rather than a threat model.

## Related artifacts

- [AI Security Overlay](README.md)
- [Enterprise AI Control Objectives](../control-framework/control-objectives.md) — `SEC-01`
- [AI Lifecycle Stage Gates](../lifecycle/stage-gates.md) — gate G2
- [Agentic AI Audit Workpaper](../../templates/agentic-ai-audit-workpaper-template.md) — trace record
- [AI Security Detection Catalog](detection-catalog.md)
- [Risk Assessment Template](../../templates/risk-assessment-template.md)

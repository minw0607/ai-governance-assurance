---
schema_version: "1.0"
artifact_id: GOV-AGT-002
title: A2A, MCP, and Multi-Agent Control Standard
artifact_class: governance
artifact_type: standard
domains:
  - agentic-ai
  - multi-agent-systems
  - model-context-protocol
  - identity-and-access-management
applies_to:
  - agentic-ai
  - multi-agent-systems
  - llm
industries:
  - cross-industry
deployment_models:
  - api
  - managed-api
  - saas
  - on-premises
  - hybrid
lifecycle_stages:
  - design
  - development
  - validation
  - deployment
  - operation
status: draft
version: "0.2.0"
last_reviewed: 2026-10-06
source_artifacts:
  - SRC-AGT-01
---

# A2A, MCP, and Multi-Agent Control Standard

## Purpose and scope

This standard governs agent-to-agent communication, Model Context Protocol (MCP) clients and servers, tool gateways, orchestration, delegated tasks, and other protocol-mediated agent interactions. It is protocol-neutral except where an implementation adopts MCP or another versioned specification.

MCP is one protocol surface, not a complete agent architecture or security boundary. The system owner remains accountable for application identity, authorization, tool safety, context handling, monitoring, and recovery across the full call chain.

## Required component and relationship register

Before production use, record:

- agent, orchestrator, client, server, gateway, tool, resource, prompt, extension, and downstream API identifiers;
- owner, operator, provider, environment, endpoint, deployment model, and support status;
- protocol and SDK name/version, enabled capabilities/extensions, schema version, and deprecation status;
- human and workload identities, authorization server, credential mechanism, scopes, audiences, expiry, rotation, and revocation owner;
- operations, data classes, destinations, action impact, approval requirements, budgets, and prohibited uses;
- trust boundaries, network paths, tenancy, regions, subprocessors, and egress controls;
- parent/child and delegation relationships, maximum depth, termination rules, and resource arbitration; and
- logging, monitoring, incident, fallback, rollback/compensation, and exit dependencies.

Unregistered or unsupported servers, tools, extensions, agents, or protocol versions must be denied or isolated pending review.

## Identity and authority

- Give every production agent and protocol component a stable workload identity distinct from display names and model-generated labels.
- Bind material actions to both the workload identity and the initiating human, service, case, or approved purpose where applicable.
- Use short-lived, audience-bound, least-privilege credentials. Validate the intended recipient and authorization at each trust boundary.
- Do not pass an inbound token unchanged to a downstream service when it was not issued for that service. Obtain a separate downstream token or use an approved exchange pattern.
- Keep credentials in trusted components; do not expose them to prompts, retrieved content, tool output, memory, or model-selected storage.
- Revalidate authority when the user, purpose, resource, tool, destination, transaction value, or risk changes.
- Deny self-escalation, self-approval, policy modification, credential retrieval, and exception creation by the agent.
- Support immediate revocation of a user delegation, workload identity, server, client, tool, endpoint, session/task, and child-agent authority.

### Fallback and attribution

Delegated user identity is not always available at the moment it is needed — the token expires, the exchange fails, the downstream service rejects the audience, or the call originates from a background task with no interactive user. What the system does next is a control decision, and it is frequently made implicitly by a library default:

- **Define the failure behavior explicitly.** When the initiating user's delegated identity cannot be used, the transaction fails closed unless continuing under a different identity is separately approved for that path. Silent substitution of a workload or service identity is not a fallback; it is an unapproved change of authority mid-transaction.
- **Bound the fallback identity.** Where continuing is approved, the substituting identity must not be able to reach data or actions beyond what the initiating user could reach. A service identity with broader standing permissions turns an authentication failure into a privilege escalation.
- **Never retry a denial under another identity.** A failed authorization is a result, not a transient error. Retrying the same call with a different or more privileged identity defeats the decision that was just made, and is indistinguishable from the attack it enables.
- **Preserve attribution downstream.** Where a workload identity performs the call, the initiating human must remain reconstructable in the downstream system's own records, not only in the calling application's logs. An action attributable only to a service identity cannot be investigated, attested, or defended.
- **Treat a disabled validation as an exception.** Audience, issuer, and scope validation that is switched off requires a recorded rationale, a compensating control, an owner, and an expiry — the same treatment as any other control exception. Confirm by configuration whether the check is enabled, rather than by whether the mechanism exists.
- **Document fallback behavior per integration.** Where different integrations behave differently on delegation failure, record each one. Undocumented divergence means the enterprise answer to "does it fail closed?" is unknown rather than yes.

## Server, tool, and schema governance

- Approve the publisher, source, integrity, version, ownership, vulnerability posture, permissions, data use, and support status of each server and tool.
- Retrieve catalogs and metadata only from approved endpoints. Treat server descriptions, tool names, schemas, annotations, prompts, resources, and metadata as untrusted input.
- Pin or constrain protocol, SDK, tool, schema, and extension versions in production; monitor deprecation and breaking changes.
- Compare catalog and schema changes with the approved baseline and require reassessment when operations, parameters, destinations, or privileges expand.
- Validate tool arguments and returned data against locally enforced schemas and business rules. Descriptive metadata cannot authorize an action.
- Apply allowlists, environment segregation, network egress restrictions, sandboxing, and content validation to third-party or high-risk tools.
- Treat registration as distinct from enablement. A newly registered server or tool must not become reachable by an agent until approval and technical checks are complete.
- Grant access at tool and operation granularity. Server-level access that exposes every tool the server offers is not least privilege, and it expands silently whenever the server adds a tool.
- Treat changes to tool descriptions, names, annotations, aliases, parameter defaults and overrides, authentication, and downstream permissions as capability changes subject to review. Capability can increase without the schema changing, because the description is what steers tool selection.
- Reconstruct administrative change history over registrations, enablement, permissions, and definitions: who changed what, when, and under which approval. Where the platform provides no native change history, determine whether source control, deployment pipeline, database, or administrative logs reconstruct it in full — and record the shortfall as a control gap where they do not, rather than treating the absence as covered.

## Context, provenance, and isolation

- Label the origin and trust level of user input, system policy, retrieved data, tool output, memory, inter-agent messages, and generated summaries.
- Preserve source and authorization provenance across transformations and agent handoffs.
- Enforce user, tenant, role, case, environment, and region boundaries outside the model.
- Pass the minimum context needed for the delegated task. Do not assume that a protocol provides centralized, trusted, or automatically authorized context sharing.
- Prevent lower-trust content from silently changing goals, permissions, approval state, destinations, security policy, or persistent memory.
- Validate and minimize content before it is written to memory, sent to another agent, or used as a tool argument.

## Delegation and multi-agent coordination

- Define which agents may delegate, to whom, for what task, with which authority, data, time, depth, and resource budget.
- Require each child agent to have an identifiable owner, runtime identity, task, parent, permissions, and termination condition.
- Propagate no more authority than the parent has and no more than the child requires. Delegation does not transfer accountability or residual-risk ownership.
- Prevent unbounded recursive delegation, circular task assignment, duplicated action, conflicting goals, hidden child creation, and uncontrolled spawning.
- Define conflict resolution, shared-resource locking, priority, cancellation, timeout, and orphaned-task handling.
- Authenticate communication partners and protect message integrity and replay resistance. Use mutual authentication where the selected transport and architecture support it; otherwise document equivalent strong controls.
- Treat optional trust or reputation scores only as supplementary signals; never substitute them for identity, authorization, provenance, and policy enforcement.

## Action and state integrity

- Use idempotency keys, deduplication, concurrency control, and state checks for retried or repeated material operations.
- Define transaction boundaries and expected intermediate states for multi-step workflows.
- Stop safely when a prerequisite, approval, tool, or downstream system fails; do not infer success from a model's self-report.
- Reconcile the claimed outcome with authoritative downstream state.
- Provide rollback or compensating action for partial completion where technically and legally feasible.
- Protect task handles, checkpoints, state references, and message identifiers from guessing, substitution, cross-user reuse, or stale replay.

## Observability and audit evidence

Use correlation identifiers to connect:

- initiating human/workload identity and approved purpose;
- agent, parent/child relationship, protocol client/server, endpoint, version, and tool;
- model, prompt/policy, retrieval, memory, schema, and relevant configuration versions;
- authorization, scope/audience validation, approval, rate/limit, and policy decisions;
- task creation, delegation, message exchange, tool arguments at an appropriate level, result, error, retry, and cancellation;
- downstream state change, reconciliation, rollback/compensation, and final outcome; and
- alerts, human intervention, exceptions, and incident records.

A single correlation identifier should connect that whole chain end to end — initiating user, agent, model, protocol call, tool action, approval, downstream state, and final result. Evidence spread across sources that cannot be joined does not reconstruct a transaction.

**Recording an event is not monitoring it.** For each agent-specific security event, establish whether it merely lands in a log or raises an alert with a named responder and a defined response path. Record denials, authorization failures, fallbacks, cancellations, and limit breaches as deliberately as successful activity: a log containing only what worked cannot show that a control held. Keep credentials, tokens, full prompts, sensitive tool arguments, and client content out of telemetry — observability must not become its own disclosure path.

Record externally meaningful decision and action evidence; do not require hidden chain-of-thought. Make material audit records tamper-evident or access-controlled and append-only where proportionate, while supporting lawful correction, deletion, legal hold, and retention. Exclude credentials and minimize sensitive content.

## Limits, containment, and recovery

- Enforce maximum duration, steps, retries, recursion, child agents, concurrent tasks, tokens, compute, cost, data volume, transaction value, and destinations.
- Set limits per agent and per workflow, with usage attributable to each. A provider or account-level quota bounds the bill; it does not bound an individual agent, and it is reached only after the behavior it was meant to stop has already run.
- Pair detection with automatic containment for runaway conditions. An alert on a recursive or looping execution that depends on a human to act is not a limit.
- Detect unexpected tools, servers, partners, scopes, schemas, context volume, delegation patterns, denial spikes, loops, and trace gaps.
- Provide independent control paths to disable a server, tool, agent, credential, queue, extension, or communication route.
- Exercise cancellation of long-running tasks and reconcile actions that completed before cancellation.
- Preserve evidence during containment and prevent recovery from restoring revoked identities, unsafe catalogs, poisoned memory, or unsupported versions.

### Rollback is not termination

Reverting a deployment and stopping work already in progress are different operations with different mechanisms, and treating one as the other leaves an incident running:

- **A rollback does not stop an execution.** Deploying the previous version replaces what *starts next*. Tasks already dispatched continue under the version that launched them, including long-running, queued, scheduled, and child-agent work.
- **Disabling a component does not revoke its identity.** An agent switched off whose workload identity, tokens, and secrets remain valid can still be invoked by anything else holding them, and its scheduled triggers may continue to fire.
- **Containment must be scoped.** Establish that an individual agent, server, tool, identity, route, or model path can be stopped — together with its in-flight executions — without taking down the platform. Where the only available action is a platform-wide shutdown, record that as the containment capability and as a limitation.
- **Name the authority and test the mechanism.** Record who may initiate containment without further approval, and exercise it on a running multi-step task rather than confirming that the control exists. A kill path that has been designed but never run is unevidenced.
- **Recover deliberately.** Restoring service after containment requires validation and reapproval, not merely re-enablement.

## Third-party and supply-chain controls

- Assess provider governance, secure development, vulnerability response, release practices, subprocessors, data use, incident support, evidence, and exit.
- Review independent assurance reports for scope, period, exceptions, complementary customer controls, and relevance. They are supporting evidence, not proof of effective agent controls in the deployed system.
- Maintain an alternative, degraded mode, or containment plan for provider-controlled changes and outages proportionate to impact.
- Revalidate after material provider, SDK, protocol, extension, server, tool, schema, or model changes.

## Minimum assurance tests

| Test area | Representative test | Required result |
|---|---|---|
| Identity | Use unknown, revoked, expired, substituted, or cross-tenant identity | Connection or action denied and recorded |
| Audience and token use | Present a token for the wrong server or attempt downstream passthrough | Token rejected; downstream access uses separately authorized credentials |
| Catalog integrity | Add or modify an unapproved server, tool, schema, annotation, or extension | Change blocked, quarantined, or routed for approval |
| Context isolation | Send another user's, tenant's, case's, or agent's context | No unauthorized disclosure or action |
| Delegation | Exceed depth, authority, time, or resource limits; create unknown child | Delegation denied or terminated with attributable evidence |
| Message integrity | Spoof, alter, duplicate, delay, or replay inter-agent messages | Invalid message rejected; duplicate action prevented |
| Tool safety | Manipulate operation, arguments, destination, or returned content | Local policy/schema enforcement prevents unsafe use |
| State integrity | Retry after timeout, partial failure, or ambiguous result | Idempotency, reconciliation, and recovery avoid duplicate or inconsistent action |
| Resource control | Cause loop, fan-out, high-cost retrieval, or long-running task | Budget/circuit breaker contains behavior and preserves evidence |
| Intervention | Disable agent/server/tool/credential during a multi-step task | New actions stop; partial actions are reconciled or compensated |
| Evidence | Reconstruct a sampled multi-agent run end to end | Identity, authority, context, calls, approvals, state, and outcome are complete and time-correlated |

## MCP implementation note

Record and govern the exact MCP specification and SDK version. The `2026-07-28` MCP release changed the protocol to a stateless core and introduced material authorization, discovery, task, extension, and deprecation changes. Requirements should follow the version actually deployed rather than assume a timeless MCP behavior.

For HTTP authorization, apply the current specification's resource and issuer validation, secure token storage, least privilege, and prohibition on unsafe token passthrough as applicable. Other transports require controls appropriate to their security model.

## Authoritative references

- [NIST: Summary Analysis of Responses Regarding Security Considerations for AI Agents](https://www.nist.gov/publications/summary-analysis-responses-request-information-regarding-security-considerations-ai)
- [NIST NCCoE: Software and AI Agent Identity and Authorization](https://www.nist.gov/news-events/news/2026/02/new-concept-paper-identity-and-authority-software-agents)
- [Model Context Protocol 2026-07-28 release](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification/)
- [OWASP Agentic Security Initiative](https://genai.owasp.org/initiatives/agentic-security-initiative/)

## Related artifacts

- [Agentic AI Governance and Assurance Profile](governance-and-assurance-profile.md)
- [Control Objectives (AGT series)](../control-framework/control-objectives.md)
- [Agentic AI Scenario Library](../../testing/agentic-ai/scenario-library.md)
- [OWASP Agentic Top 10 Mapping](../../mappings/owasp-agentic.md)
- [Agentic AI Checklist](../../checklists/agentic-ai.md)

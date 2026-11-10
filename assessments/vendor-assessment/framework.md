---
schema_version: "1.0"
artifact_id: ASSESS-VENDOR-001
title: GenAI and Agentic AI Vendor Assessment Framework
artifact_class: assessment
artifact_type: framework
domains:
  - third-party-risk
  - ai-governance
  - supply-chain
applies_to:
  - generative-ai
  - agentic-ai
  - foundation-models
industries:
  - financial-services
  - cross-industry
deployment_models:
  - api
  - managed-api
  - saas
lifecycle_stages:
  - intake
  - procurement
  - validation
  - operation
  - retirement
status: draft
version: "0.2.0"
last_reviewed: 2026-11-24
source_artifacts:
  - SRC-VEND-01
---

# GenAI and Agentic AI Vendor Assessment Framework

## Purpose

This framework evaluates whether an AI vendor and the proposed service can support the organization's intended use within defined risk tolerances. The assessment covers the service actually configured and deployed—not only the provider's general control environment.

## Assessment process

1. Define the use case, deployment model, data, users, integrations, autonomy, and risk tier.
2. Identify the provider, foundation-model provider, hosting platform, subprocessors, tools, and material dependencies.
3. Select the evidence requirements and assessment depth by risk.
4. Review evidence and test customer-controlled configurations.
5. Score criteria, record gaps, and identify compensating controls.
6. Decide: approve, approve with conditions, pilot only, defer, or reject.
7. Establish monitoring, reassessment triggers, and an exit plan.

## Assessment domains

| Domain | Assessment objective | Representative evidence |
|---|---|---|
| Governance and transparency | Understand ownership, intended use, model/system limitations, and internal assurance | System/model cards, governance charter, evaluation reports, known-issues register |
| Architecture and controllability | Understand components, boundaries, configurations, and deterministic controls | Architecture/data-flow diagrams, admin and API documentation, permission model |
| Data governance and privacy | Determine how customer data is processed, retained, isolated, reused, and deleted | DPA, privacy terms, retention/deletion procedure, subprocessor list, residency evidence |
| Security | Evaluate identity, isolation, supply chain, AI-specific threats, logging, and response | SOC/ISO reports, penetration and red-team summaries, incident procedures, audit-log samples |
| Quality and reliability | Determine whether performance is measurable, stable, and fit for the use case | Evaluation methodology, benchmarks, SLA, status history, capacity and resilience results |
| Change management | Determine whether changes are visible, controllable, testable, and reversible | Release notes, version policy, notification history, deprecation and rollback procedures |
| Agentic controls | Bound tool access, state change, memory, autonomy, and human approval | Tool registry, permission matrix, action policies, trace samples, kill-switch evidence |
| Compliance and assurance support | Support applicable obligations, auditability, rights, and examination | Contractual audit/cooperation rights, records capabilities, fairness and impact evidence |
| Supply-chain and concentration risk | Understand dependencies, substitution, and failure scenarios | Subprocessor/model inventory, continuity plan, dependency and exit analysis |

## Assessment depth

| Risk tier | Minimum approach |
|---|---|
| Tier 1 | Full evidence review, independent challenge, adversarial and use-case testing, contractual gap closure, executive risk decision, continuous monitoring |
| Tier 2 | Full questionnaire, evidence validation, targeted testing, second-line review, defined monitoring and exit plan |
| Tier 3 | Abbreviated evidence review, configuration testing, owner and risk approval, periodic monitoring |
| Tier 4 | Basic security/privacy/terms review, approved-use restriction, owner approval |

## SaaS and API distinctions

For SaaS, focus on automatic updates, tenant isolation, admin controls, permission inheritance, exportability, integrated data sources, and compensating monitoring. For API deployments, focus on model/version choice, application architecture, logging, output handling, rate limits, key management, retrieval, and customer-built controls.

### Vendor-operated AI platforms

Where the AI capability is operated by the provider, most controls in this library cannot be implemented by the customer — only verified, configured, or demanded contractually. Five questions determine whether the capability is governable at all, and a negative answer to any of them is a control limitation to record rather than a question to leave open.

**1. Can you see what is enabled?** Inventory requirements (`GOV-05`) assume the organization can enumerate its own systems. On a vendor-operated platform the inventory is bounded by what the administrative surface exposes. Establish whether an administrator can enumerate, for each tenant:

- every enabled capability, including agentic and tool-using features;
- external integrations, connectors, and the data sources each can reach;
- the actions the platform can take, distinguished from assistance it merely provides;
- access paths in use — browser, desktop or document integration, mobile, email, API; and
- usage and last-activity information per user and per capability.

A console showing users and licences and nothing else cannot support an inventory record. Where visibility is absent, the inventory entry is an assertion and must be marked as one.

**2. Are restrictions enforced or merely decided?** A capability the organization chose not to use may be prohibited in policy, hidden in the interface, or technically disabled — three different states frequently reported as one.

- Establish which configuration disables each restricted capability, and confirm it by attempting use rather than by reading the setting.
- Establish what prevents re-enablement: a vendor update that activates new features by default, an administrator acting without review, or a user-level setting.
- Treat a restriction that can revert without review as a temporary control with an owner, not as a control.
- Require that new tool-using or agentic functionality arrives disabled and passes review before exposure, and record whether the provider supports that.

**3. What can you contain yourself?** Determine, before an incident rather than during one, which of these the organization can perform independently and which require provider action:

| Containment action | Independent, or provider-dependent? |
|---|---|
| Suspend an individual user | |
| Terminate active sessions and invalidate issued tokens | |
| Disable one integration or connector | |
| Disable one agentic capability or action, not the whole platform | |
| Disable one access path, such as a document or email integration | |
| Cut the platform's access to a data source | |
| Suspend the tenant | |

Removing a licence is not containment: sessions, integrations, and credentials may remain usable. Where containment requires a support request, record the named emergency contact, the committed response time, and the fact that response depends on a party that may itself be involved in the event. Containment is complete only when activity is verified to have stopped, not when the request is submitted.

**4. What access does the provider hold?** Identify provider support identities, service principals, and connectors that can reach organizational data or administer the capability, and whether the organization can revoke them independently and during an incident. Access the organization cannot revoke is residual exposure, not a vendor control.

**5. Can you see and investigate activity?** Establish which activity the provider records, which of it the customer can obtain, how long it is retained, whether it can be exported into enterprise monitoring, and whether the provider's own telemetry raises an alert or only a log entry (`SEC-05`). Where investigation requires the provider, record that as a dependency with a service level. Visibility available only to the provider is a monitoring gap with a compensating control, never coverage.

### Assurance scope for agentic capability

An independent assurance report over a provider's conventional application is not assurance over its AI or agentic surface. Request the scope explicitly, and for the agentic capability specifically: prompt-injection and indirect-injection testing, tool and connector abuse testing, data-exposure and cross-tenant testing, and the remediation status of findings rather than their existence. Where the provider will not supply this, the gap is recorded against the capability — it does not become acceptable by being unobtainable.

## Decision rules

A numeric score supports consistency but cannot override disqualifying conditions. Potential blockers include unauthorized training use, inability to meet mandatory data restrictions, insufficient tenant or identity controls, unbounded high-impact autonomy, lack of material incident notification, or no feasible exit/containment capability.

Use the [questionnaire](questionnaire.md) and [scoring guide](scoring-guide.md). Retain cited evidence and record uncertainty explicitly.

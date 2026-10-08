---
schema_version: "1.0"
artifact_id: GOV-SEC-001
title: AI Security Overlay
artifact_class: governance
artifact_type: catalog
domains:
  - ai-security
  - information-security
  - threat-modeling
  - detection-engineering
  - incident-response
  - supply-chain
applies_to:
  - generative-ai
  - agentic-ai
  - rag
  - llm
  - machine-learning
industries:
  - cross-industry
lifecycle_stages:
  - design
  - development
  - validation
  - deployment
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-10-08
---

# AI Security Overlay

AI security is a **capability overlay across the library, not a separate artifact class**. Securing an AI system is not a parallel activity to governing it: the same control objectives, the same lifecycle gates, and the same evidence discipline apply, with additional requirements that arise because the system takes untrusted input, selects its own actions, reaches data through derived stores, and acts under borrowed authority.

This page is the security view over the library. Nothing here is unique to this page — it routes to where the requirement actually lives.

## Where to start

| Your question | Go to |
|---|---|
| What are the credible failures in *this* system, and which controls prevent them? | [AI Threat Modeling Method](threat-modeling-method.md) |
| What should we alert on, and who responds? | [AI Security Detection Catalog](detection-catalog.md) |
| Something has gone wrong — how do we contain and investigate it? | [AI Security Incident Response](incident-response.md) |
| Can we trust the model, weights, adapters, and packages we deploy? | [Model and AI Supply Chain Security](model-supply-chain.md) |
| How do we secure the lab and development environments? | [AI Development Environment Standard](../environments/ai-development-environment-standard.md) |
| Can a user or agent reach data they should not? | [RAG, Vector, and Agent Data Security Standard](../data-security-governance/rag-vector-agent-data-security.md) |
| An agent uses tools, protocols, or other agents — what changes? | [A2A, MCP, and Multi-Agent Control Standard](../agentic-ai/a2a-mcp-multi-agent-control-standard.md) |
| How do we test any of this adversarially? | [Security Red Teaming](../../testing/security-red-teaming/testing-guide.md) and [Privacy and Data Leakage](../../testing/privacy-data-leakage/testing-guide.md) |

## Security control objectives

The [control objectives](../control-framework/control-objectives.md) are the spine. Security draws principally on three families and parts of a fourth:

| Family | Objectives | Concern |
|---|---|---|
| `SEC` | `SEC-01`–`SEC-06` | Threat modeling and secure design, identity and secrets, input/output/tool boundary enforcement, software and model supply chain, logging and tamper resistance, resilience and cost |
| `DATA` | `DATA-01`–`DATA-07` | Authorized sources and lineage, classification and least privilege including information barriers, minimization and provider data use, retention and deletion, residency, integrity, training and evaluation data |
| `AGT` | `AGT-01`–`AGT-07` | Tool registry and least privilege, consequential-action gating, execution trace and intervention, memory and state, multi-agent coordination, agent identity and delegation, action and state integrity |
| `OPS` | `OPS-01`, `OPS-02`, `OPS-03`, `OPS-05` | Monitoring and threshold action, incident response, controlled change, shared-service change |

Twenty of the library's forty-three objectives sit in `SEC`, `DATA`, and `AGT`. Use the [coverage matrix](../control-framework/control-coverage-matrix.md) to find every artifact that evidences a given objective.

## Security by lifecycle gate

Security is not a pre-release check. The [stage gates](../lifecycle/stage-gates.md) place it as follows:

| Gate | Security activity |
|---|---|
| G1 Intake | Identify untrusted input, sensitive data, external communication, and action authority; set the tier |
| G2 Design | Threat model the architecture and trust boundaries; complete the security review; define the authorization model |
| G3 Build | Separate environments and identities; supply-chain and secret controls; implement boundary enforcement outside the model |
| G4 Validate | Adversarial and negative testing with release-blocking criteria; evidence from the validation environment |
| G5 Deploy | Re-verify against the production configuration; confirm detection, response ownership, and containment paths |
| G6 Operate | Detection and alerting with named responders; change and revalidation; periodic entitlement review |
| G7 Retire | Revoke identities and credentials; disable triggers, endpoints, and tools; dispose of derived stores |

## What the overlay deliberately does not provide

- **Product configuration.** Platform-specific settings date faster than the library can maintain them. Requirements are stated as outcomes; see [testing tools](../../references/testing-tools.md) for the position on tooling.
- **A general enterprise security programme.** Network, endpoint, identity platform, and application security remain governed by existing enterprise standards. This overlay covers what is *additional or different* because the system is AI-enabled.
- **Threat intelligence.** Specific attacker tradecraft changes continuously. The [OWASP LLM](../../mappings/owasp-genai.md) and [OWASP Agentic](../../mappings/owasp-agentic.md) mappings give the stable taxonomy; current technique detail belongs to a live source.

## Related artifacts

- [Enterprise AI Control Objectives](../control-framework/control-objectives.md)
- [AI Data Security & Governance](../data-security-governance/README.md)
- [Agentic AI Governance](../agentic-ai/README.md)
- [AI Risk Tiering Framework](../risk-tiering/ai-risk-tiering-framework.md)
- [Testing catalog](../../testing/README.md)

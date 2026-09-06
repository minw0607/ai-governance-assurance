---
schema_version: "1.0"
artifact_id: MAP-OWASPASI-001
title: OWASP Top 10 for Agentic Applications Mapping
artifact_class: mapping
artifact_type: security-mapping
domains:
  - owasp
  - agentic-security
  - genai-security
applies_to:
  - agentic-ai
  - llm
  - rag
industries:
  - cross-industry
lifecycle_stages:
  - design
  - validation
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-23
---

# OWASP Top 10 for Agentic Applications Mapping

## Scope

OWASP publishes two complementary lists. The [Top 10 for LLM Applications 2026](owasp-genai.md) governs the **model layer** — what the model is asked, what it emits, what it discloses. The Top 10 for Agentic Applications (`ASI01`–`ASI10`, announced 9 December 2025) governs the **actor layer** — what the agent decides, invokes, remembers, delegates, and changes.

Use this mapping when the system plans, uses tools, maintains state, delegates, communicates with other agents, or changes an external environment. Apply both lists; neither subsumes the other.

## Mapping

| ID | Risk | Library control objectives | Governance | Testing and verification |
|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | `AGT-02`, `AGT-03`, `HUM-03`, `SEC-03` | [Agentic Profile](../governance/agentic-ai/governance-and-assurance-profile.md) — objective, authority, and stop conditions | [Agentic Testing Guide](../testing/agentic-ai/testing-guide.md); [Scenario Library](../testing/agentic-ai/scenario-library.md); [Safety Testing](../testing/safety-alignment/testing-guide.md) |
| ASI02 | Tool Misuse and Exploitation | `AGT-01`, `AGT-02`, `SEC-03` | Tool registry, least privilege, and consequential-action gating | Tool-boundary and negative-authorization tests |
| ASI03 | Identity and Privilege Abuse | `AGT-06`, `SEC-02`, `DATA-02` | [A2A/MCP Standard](../governance/agentic-ai/a2a-mcp-multi-agent-control-standard.md) — workload identity and delegated authority | Delegation, impersonation, and permission-preservation tests |
| ASI04 | Agentic Supply Chain Vulnerabilities | `SEC-04`, `TPRM-01`, `TPRM-02`, `TPRM-03` | [Third-Party Risk Policy](../governance/policies/third-party-risk.md); protocol/version governance | [Regression Testing](../testing/regression-testing/testing-guide.md); provider- and server-change tests |
| ASI05 | Unexpected Code Execution | `SEC-03`, `AGT-01`, `SEC-01` | Sandboxing, egress control, and output-handling requirements | [Security Red Teaming](../testing/security-red-teaming/testing-guide.md) |
| ASI06 | Memory and Context Poisoning | `AGT-04`, `DATA-01`, `DATA-06`, `QUAL-04` | [RAG, Vector, and Agent Data Security](../governance/data-security-governance/rag-vector-agent-data-security.md) | Retrieval-poisoning, memory-persistence, and cross-session leakage tests |
| ASI07 | Insecure Inter-Agent Communication | `AGT-05`, `AGT-06`, `SEC-02` | [A2A/MCP Standard](../governance/agentic-ai/a2a-mcp-multi-agent-control-standard.md) — authenticated channels, replay resistance, schema governance | Protocol conformance, replay, and message-integrity tests |
| ASI08 | Cascading Failures | `AGT-05`, `AGT-07`, `SEC-06`, `OPS-02` | Resilience, blast-radius, and containment requirements | Fault-injection, partial-failure, and recovery scenarios |
| ASI09 | Human-Agent Trust Exploitation | `HUM-01`, `HUM-02`, `QUAL-03` | Effective human review; notice, explanation, and contestability | Over-reliance, deceptive-confidence, and review-workload tests |
| ASI10 | Rogue Agents | `GOV-05`, `AGT-01`, `AGT-03`, `OPS-01` | Inventory, shadow-AI discovery, and agent registration | Discovery, unregistered-agent detection, and kill-switch tests |

## Applying both lists together

A single agentic incident usually spans both layers. A prompt-injected document (`LLM01`) that redirects an agent's plan (`ASI01`) into an over-privileged tool call (`ASI02`) with a delegated credential (`ASI03`) is one chain, not four findings. Test the chain and record the demonstrated impact; map the finding to every category it traverses so coverage analysis stays honest.

## Use note

OWASP categories guide threat coverage; they do not replace system-specific threat modeling and they carry no legal or regulatory force. Assess demonstrated impact and control effectiveness across the whole application, including the deterministic controls outside the model.

## Authoritative sources

- [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [OWASP Agentic Security Initiative](https://genai.owasp.org/initiatives/agentic-security-initiative/)
- [OWASP GenAI Security Project](https://genai.owasp.org/)

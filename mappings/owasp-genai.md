---
schema_version: "1.0"
artifact_id: MAP-OWASP-001
title: OWASP GenAI Security Mapping
artifact_class: mapping
artifact_type: security-mapping
domains:
  - owasp
  - application-security
  - genai-security
applies_to:
  - llm
  - generative-ai
  - rag
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
  - design
  - validation
  - operation
status: draft
version: "0.2.0"
last_reviewed: 2026-08-18
---

# OWASP GenAI Security Mapping

## Current LLM application list

OWASP published the Top 10 for LLM Applications 2026 on August 3, 2026:

| ID | Risk | Primary library coverage |
|---|---|---|
| LLM01:2026 | Prompt Injection | Security red teaming, prompt management, tool authorization |
| LLM02:2026 | Sensitive Information Disclosure | Data policy, privacy/leakage testing, output controls |
| LLM03:2026 | Excessive Agency | Agentic policy, risk tiering, agentic testing and checklist |
| LLM04:2026 | Supply Chain | Vendor assessment, dependency integrity, change management |
| LLM05:2026 | Data and Model Poisoning | Data lineage, retrieval/memory testing, integrity monitoring |
| LLM06:2026 | Unbounded Consumption | Rate/action budgets, resilience, cost and abuse monitoring |
| LLM07:2026 | Misinformation | Factuality testing, source support, human verification |
| LLM08:2026 | Hidden Context Exposure | Prompt/instruction protection, minimization, access and leakage tests |
| LLM09:2026 | Vector and Embedding Weaknesses | RAG permission, retrieval, poisoning, deletion, and segmentation tests |
| LLM10:2026 | Improper Output Handling | Schema validation, encoding, downstream sanitization, transaction controls |

## Agentic systems

When an LLM becomes an actor with tools, memory, delegation, or state-changing capability, pair the LLM list with OWASP's agentic guidance. Apply the [Agentic AI Governance and Assurance Profile](../governance/agentic-ai/governance-and-assurance-profile.md), [A2A/MCP Standard](../governance/agentic-ai/a2a-mcp-multi-agent-control-standard.md), [Agentic AI Testing Guide](../testing/agentic-ai/testing-guide.md), and [Scenario Library](../testing/agentic-ai/scenario-library.md) to goal hijacking, tool misuse, privilege abuse, supply chain, code execution, memory/context poisoning, inter-agent communication, cascading failures, human trust exploitation, and rogue agents.

## Use note

OWASP categories guide threat coverage; they do not replace system-specific threat modeling. Test demonstrated impact and control effectiveness across the entire application.

## Authoritative sources

- [OWASP Top 10 for LLM Applications 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)
- [OWASP GenAI Security Project](https://genai.owasp.org/)
- [OWASP Agentic Security Initiative](https://genai.owasp.org/initiatives/agentic-security-initiative/)

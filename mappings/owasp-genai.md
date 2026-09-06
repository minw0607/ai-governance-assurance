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

| ID | Risk | Library control objectives | Primary library coverage |
|---|---|---|---|
| LLM01:2026 | Prompt Injection | `SEC-01`, `SEC-03`, `AGT-02` | [Security red teaming](../testing/security-red-teaming/testing-guide.md), [prompt management](../governance/policies/prompt-management.md), tool authorization |
| LLM02:2026 | Sensitive Information Disclosure | `DATA-02`, `DATA-03`, `QUAL-04` | [Data handling policy](../governance/policies/data-handling.md), [privacy/leakage testing](../testing/privacy-data-leakage/testing-guide.md), output controls |
| LLM03:2026 | Excessive Agency | `AGT-01`, `AGT-02`, `HUM-03` | [Agentic profile](../governance/agentic-ai/governance-and-assurance-profile.md), [risk tiering](../governance/risk-tiering/ai-risk-tiering-framework.md), [agentic testing](../testing/agentic-ai/testing-guide.md) and [checklist](../checklists/agentic-ai.md) |
| LLM04:2026 | Supply Chain | `SEC-04`, `TPRM-01`, `OPS-03` | [Vendor assessment](../assessments/vendor-assessment/framework.md), dependency integrity, [change management](../governance/policies/change-management.md) |
| LLM05:2026 | Data and Model Poisoning | `DATA-01`, `DATA-06`, `DATA-07`, `AGT-04` | [Data lineage](../governance/data-security-governance/data-lifecycle-standard.md), retrieval/memory testing, integrity monitoring |
| LLM06:2026 | Unbounded Consumption | `SEC-06`, `OPS-01` | Rate/action budgets, resilience, cost and abuse monitoring |
| LLM07:2026 | Misinformation | `QUAL-03`, `HUM-01` | [Factuality testing](../testing/hallucination-factuality/testing-guide.md), source support, human verification |
| LLM08:2026 | Hidden Context Exposure | `DATA-03`, `SEC-03`, `SEC-05` | [Prompt/instruction protection](../governance/policies/prompt-management.md), minimization, access and leakage tests |
| LLM09:2026 | Vector and Embedding Weaknesses | `QUAL-04`, `DATA-02`, `DATA-04` | [RAG, vector, and agent data security](../governance/data-security-governance/rag-vector-agent-data-security.md); permission, retrieval, poisoning, deletion, and segmentation tests |
| LLM10:2026 | Improper Output Handling | `SEC-03`, `AGT-07` | Schema validation, encoding, downstream sanitization, transaction controls |

## Agentic systems

When an LLM becomes an actor with tools, memory, delegation, or state-changing capability, pair this list with the **OWASP Top 10 for Agentic Applications** (`ASI01`–`ASI10`). The LLM list governs the model layer; the agentic list governs the actor layer.

See the [OWASP Top 10 for Agentic Applications Mapping](owasp-agentic.md) for the full `ASI01`–`ASI10` mapping to library control objectives, governance standards, and test coverage.

## Use note

OWASP categories guide threat coverage; they do not replace system-specific threat modeling. Test demonstrated impact and control effectiveness across the entire application.

## Authoritative sources

- [OWASP Top 10 for LLM Applications 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)
- [OWASP GenAI Security Project](https://genai.owasp.org/)
- [OWASP Agentic Security Initiative](https://genai.owasp.org/initiatives/agentic-security-initiative/)

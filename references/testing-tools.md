---
schema_version: "1.0"
artifact_id: REF-TOOLS-001
title: AI Testing Tools Reference
artifact_class: reference
artifact_type: tool-register
domains:
  - testing-tools
  - evaluation
  - red-teaming
applies_to:
  - generative-ai
  - rag
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
  - development
  - validation
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - GenAI Testing Procedures v2.docx
---

# AI Testing Tools Reference

Tools accelerate execution and evidence collection; they do not establish fitness for purpose without sound cases, ground truth, configuration, and review.

| Tool | Typical use | Link |
|---|---|---|
| Promptfoo | Prompt, model, and assertion-based evaluation | https://github.com/promptfoo/promptfoo |
| Garak | LLM vulnerability probing | https://github.com/NVIDIA/garak |
| PyRIT | Risk identification and red-team orchestration | https://github.com/Azure/PyRIT |
| Ragas | Retrieval and generation evaluation for RAG | https://github.com/explodinggradients/ragas |
| DeepEval | LLM evaluation and test orchestration | https://github.com/confident-ai/deepeval |
| LangSmith | Tracing, datasets, and evaluation | https://www.langchain.com/langsmith |
| Fairlearn | Fairness assessment and mitigation | https://github.com/fairlearn/fairlearn |
| Playwright | Browser automation for approved interface testing | https://playwright.dev/ |

## Selection considerations

- supported deployment modality and authentication;
- data handling and telemetry;
- repeatability and version pinning;
- evaluator transparency and calibration;
- raw evidence export;
- extensibility for organization-specific cases;
- maintenance, licensing, and supply-chain risk; and
- whether automation is permitted by the provider and organizational policy.

Record tool and plugin versions with test evidence. Revalidate tool-generated metrics after material upgrades.

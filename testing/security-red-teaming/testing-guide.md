---
schema_version: "1.0"
artifact_id: TEST-SEC-001
title: Security Red Teaming Guide for GenAI Systems
artifact_class: testing
artifact_type: testing-guide
domains:
  - security
  - red-teaming
  - adversarial-testing
applies_to:
  - llm
  - rag
  - generative-ai
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

# Security Red Teaming Guide for GenAI Systems

## Threat model first

Map trust boundaries, identities, sensitive data, retrieval, memory, model/provider, tools, output consumers, administrative interfaces, and supply-chain dependencies. A prompt-only exercise is not a system red team.

## Core LLM application coverage

Align scenarios to the current [OWASP Top 10 for LLM Applications 2026](../../mappings/owasp-genai.md): prompt injection, sensitive information disclosure, excessive agency, supply chain, data and model poisoning, unbounded consumption, misinformation, hidden context exposure, vector and embedding weaknesses, and improper output handling.

## Procedure

1. Define rules of engagement, test environment, prohibited actions, monitoring, data, and emergency contacts.
2. Enumerate direct, indirect, persistent, multimodal, encoded, and cross-session attack paths.
3. Test with the deployed defense visible to the red team; static attack sets alone overstate assurance.
4. Chain attacks across retrieval, tool output, memory, identity, and output rendering.
5. Attempt impact: unauthorized access/action, exfiltration, persistence, poisoning, code execution, fraud, control bypass, or resource exhaustion.
6. Validate containment, alerting, trace quality, incident response, revocation, and recovery.
7. Reproduce successful attacks, minimize them to root cause, and create regression cases.

## High-value scenarios

- malicious instructions in documents, email, web content, issue titles, tool results, and MCP metadata;
- invisible or multimodal content that bypasses text-only inspection;
- permission confusion across users, tenants, repositories, and tools;
- sensitive output rendered into active links, code, commands, SQL, or HTML;
- poisoned retrieval corpus, embeddings, fine-tuning data, or persistent memory;
- compromised or substituted model, dependency, tool, or connector;
- loops, expensive requests, high-volume actions, and denial of service; and
- an agent combining untrusted input, sensitive access, and external/state-changing capability.

## Findings

Rate the demonstrated business impact, reachable privilege, exploitability, persistence, detectability, and affected population. Record attack preconditions, full trace, defense behavior, root cause, and containment. Do not report jailbreak success as equivalent to material compromise unless a meaningful policy or system impact is demonstrated.

## Source

- [OWASP Top 10 for LLM Applications 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)

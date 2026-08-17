---
schema_version: "1.0"
artifact_id: GOV-POL-005
title: Prompt and Instruction Management Policy
artifact_class: governance
artifact_type: policy
domains:
  - prompt-management
  - configuration-management
  - security
applies_to:
  - generative-ai
  - rag
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
  - development
  - validation
  - deployment
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - GenAI Policies - Example.docx
---

# Prompt and Instruction Management Policy

## Policy objective

System prompts, templates, tool descriptions, memory instructions, retrieval instructions, and policy configurations are controlled production artifacts. They must be versioned, reviewed, tested, and protected according to risk.

## Requirements

- Assign an owner and stable identifier to production prompt and instruction artifacts.
- Store approved versions in controlled repositories with change history and rollback capability.
- Separate trusted instructions from untrusted content as far as the architecture permits.
- Do not place credentials, secrets, or unnecessary sensitive information in prompts.
- Define expected behavior, refusal/escalation rules, output schema, source-use requirements, and uncertainty handling.
- Test robustness across paraphrase, ambiguity, conflicting context, multilingual input, long context, indirect injection, and tool output.
- Treat tool descriptions, MCP server metadata, retrieved documents, and persistent memory as potential instruction channels.
- Require review and regression testing before material changes.
- Monitor for prompt leakage, injection, anomalous overrides, and unexpected output drift.

Prompt controls reduce risk but are not a substitute for least privilege, deterministic authorization, output validation, transaction controls, or human approval.

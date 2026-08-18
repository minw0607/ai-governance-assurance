---
schema_version: "1.0"
artifact_id: TEST-DESIGN-001
title: Use-Case-Driven AI Test Design
artifact_class: testing
artifact_type: methodology
domains:
  - test-design
  - evaluation
  - coverage
applies_to:
  - generative-ai
  - rag
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
  - development
  - validation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - GenAI Testing Comprehensive Guide v2.docx
  - SaaS Testing Automation UseCase Design.docx
---

# Use-Case-Driven AI Test Design

## Start with the decision

Generic benchmarks describe broad capability; they rarely establish fitness for a specific workflow. Begin with what the system must do, what it must never do, who relies on it, what evidence exists, and how failure causes harm.

## Six-step design method

1. Decompose the business workflow into tasks, decisions, handoffs, data sources, and controls.
2. Identify normal, boundary, adversarial, and degraded scenarios.
3. Select the appropriate test format.
4. Define expected behavior and failure indicators before execution.
5. Build representative, difficult, and severe-case coverage.
6. Prioritize by impact, likelihood, exposure, detectability, and control dependence.

## Test formats

### Ground-truth test

Use for extraction, calculation, classification, retrieval, or factual tasks with an authoritative answer. Record the source, acceptable variants, tolerances, and automatic failure conditions.

### Behavioral test

Use for safety, security, policy, escalation, refusal, or tool-use behavior. Define what the system should and should not do; avoid requiring a single exact wording.

### Comparative test

Use for consistency, fairness, change detection, or model/provider comparison. Control non-tested variables and define what differences are material.

### Workflow scenario

Use for multi-step tasks and agents. Define state, permissions, tool behavior, interruptions, approvals, expected trace, and final outcome.

## Query taxonomy

Include:

- direct fact extraction and definition;
- procedure and sequence;
- multi-source or multi-hop reasoning;
- paraphrase, repetition, follow-up, and long-conversation consistency;
- ambiguity, missing context, conflicting evidence, noise, jargon, and out-of-scope requests;
- numerical, tabular, temporal, and chart interpretation;
- unanswerable questions and false-premise traps; and
- adversarial, multilingual, encoded, multimodal, and indirect inputs where relevant.

## Generated test cases

AI may accelerate case generation, but humans must verify ground truth, severity, realism, duplication, and coverage. Keep generated cases separate from approved cases until review. Do not expose confidential production data to unapproved generation tools.

## Evaluation design

Prefer deterministic checks when possible. Use domain-expert review for consequential judgments. Calibrate rubrics with examples and inter-rater checks. If an LLM assists evaluation, retain its version and prompt, compare against a human-reviewed calibration set, and route ambiguous or severe cases to people.

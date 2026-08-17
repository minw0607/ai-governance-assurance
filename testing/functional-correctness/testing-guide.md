---
schema_version: "1.0"
artifact_id: TEST-FUNC-001
title: Functional Correctness Testing Guide
artifact_class: testing
artifact_type: testing-guide
domains:
  - functional-correctness
  - task-performance
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

# Functional Correctness Testing Guide

## Objective

Determine whether the system completes intended tasks accurately, completely, consistently, and within operational constraints.

## Procedure

1. Decompose each use case into observable tasks and outcomes.
2. Define authoritative ground truth, rubric, tolerance, or success state.
3. Stratify cases by frequency, difficulty, data type, user group, and business impact.
4. Include edge cases, missing information, conflicting input, and degraded dependencies.
5. Execute using production-equivalent prompts, parameters, retrieval, permissions, and tools.
6. Evaluate task completion, correctness, completeness, relevance, consistency, and latency.
7. Analyze failure clusters rather than relying only on aggregate pass rate.

## Metrics

Possible measures include exact or tolerance-aware accuracy, task success rate, extraction precision/recall, calculation error, rubric score, consistency under paraphrase, tool-selection accuracy, and completion within time/cost limits.

## Acceptance considerations

Set thresholds by task and impact. Require zero known critical failures where a single error can cause severe harm. For open-ended tasks, define minimum rubric performance and explicit conditions requiring human review or abstention.

## Evidence

Retain the dataset version, sources, case classification, execution configuration, raw output, evaluator, score, failure reason, and disposition.

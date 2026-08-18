---
schema_version: "1.0"
artifact_id: TEST-REG-001
title: AI Regression Testing and Change Detection Guide
artifact_class: testing
artifact_type: testing-guide
domains:
  - regression-testing
  - change-detection
  - model-drift
applies_to:
  - generative-ai
  - rag
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
  - deployment
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - GenAI Testing Procedures v2.docx
  - GenAI Policies - Example.docx
---

# AI Regression Testing and Change Detection Guide

## Change surfaces

Track model/provider versions, parameters, prompts, guardrails, retrieval corpus and index, embeddings, tools, permissions, memory policy, application code, evaluator, data schema, user group, and provider-controlled SaaS behavior.

## Golden suite

Maintain a risk-weighted set of:

- critical functional cases with authoritative outcomes;
- known failures and remediations;
- severe security, privacy, safety, and agentic boundary cases;
- representative workflow and user scenarios;
- unanswerable, ambiguous, and edge cases; and
- stability probes for model/provider behavior.

Version cases, expected behavior, sources, evaluator, and thresholds. Refresh stale cases without erasing historical comparability.

## Execution

1. Establish a reproducible baseline with configuration and raw evidence.
2. Run the suite before planned releases and after material provider or environmental changes.
3. Compare deterministic results, rubric scores, distributions, severe failures, latency, cost, and trace behavior.
4. Route material differences for human review; semantic similarity alone cannot determine equivalence.
5. Investigate whether the change comes from model behavior, retrieval, application, permissions, data, evaluator, or test instability.
6. Approve, restrict, roll back, compensate, or escalate according to pre-defined criteria.

## SaaS without version control

Monitor release notes and observed behavior, schedule recurring golden-suite execution, sample critical production outcomes, and maintain rapid disablement or workflow fallback. Record the first observed date and evidence when the provider version is unavailable.

## Alerting

Alert on new critical failures, material degradation by risk segment, increased attack success, unauthorized action, privacy breach, abnormal abstention/refusal, trace gaps, or threshold drift. Avoid using a single average that masks severe regressions.

---
schema_version: "1.0"
artifact_id: TEST-FACT-001
title: Hallucination and Factuality Testing Guide
artifact_class: testing
artifact_type: testing-guide
domains:
  - hallucination
  - factuality
  - rag-evaluation
applies_to:
  - generative-ai
  - rag
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

# Hallucination and Factuality Testing Guide

## Failure taxonomy

- fabricated fact, event, quotation, or number;
- unsupported claim relative to supplied context;
- fabricated or misrepresented citation;
- entity, time, unit, or jurisdiction confusion;
- failure to recognize unavailable or contradictory evidence; and
- retrieval failure presented as answer-generation failure, or vice versa.

## Test methods

### Ground-truth factual evaluation

Use versioned, authoritative questions and answers. Measure correctness and confident-but-wrong behavior separately. Include questions whose answer changes over time and record the cutoff date.

### RAG decomposition

Evaluate retrieval and generation separately:

- retrieval relevance, recall, ranking, permission correctness, and source freshness;
- answer faithfulness to retrieved context;
- citation existence and claim-level support; and
- behavior when evidence is missing, conflicting, or out of scope.

### Unanswerable and false-premise tests

Ask questions not supported by the authorized source set, containing incorrect premises, or requiring unavailable recency. The expected behavior may be abstention, clarification, or explicit uncertainty—not invention.

### Numerical and entity integrity

Test units, sign, period, aggregation, tables, cross-document entities, and source-to-output transcription. Small numerical errors may be material.

## Metrics

Track factual error rate, unsupported-claim rate, citation precision, citation coverage, appropriate-abstention rate, retrieval recall/precision, and severity-weighted error. Report confidence intervals or sample limitations when making rate claims.

## Controls and retesting

Findings may require improved sources, retrieval, prompt design, output schema, citation checks, uncertainty policy, restricted use, or human verification. Add every material failure to regression testing.

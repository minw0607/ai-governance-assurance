---
schema_version: "1.0"
artifact_id: TEST-FAIR-001
title: Bias and Fairness Testing Guide
artifact_class: testing
artifact_type: testing-guide
domains:
  - bias
  - fairness
  - civil-rights
applies_to:
  - generative-ai
  - agentic-ai
  - machine-learning
industries:
  - cross-industry
lifecycle_stages:
  - design
  - validation
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - GenAI Testing Procedures v2.docx
---

# Bias and Fairness Testing Guide

## Scope

Fairness is context-specific. Identify affected groups, relevant attributes and proxies, decision pathways, applicable law, legitimate business factors, and the type of harm before selecting metrics.

## Methods

### Counterfactual pairs

Hold decision-relevant facts constant while varying the tested attribute or proxy. Compare recommendation, rationale, tone, assumptions, requested evidence, escalation, and confidence. Review whether the pair is realistic and whether the proxy itself introduces confounding context.

### Outcome analysis

Where outputs influence decisions, compare selection, error, burden, escalation, and benefit rates across relevant groups. Use appropriate statistical uncertainty and investigate root causes rather than treating a threshold as a universal legal conclusion.

### Representation and stereotype testing

Evaluate generated content for omission, demeaning association, role stereotyping, dialect or language disadvantage, and harmful defaults.

### Workflow review

Assess human reliance, appeal, accessibility, data quality, proxy variables, and how AI-generated explanations affect decisions. A fair model output can still produce an unfair process.

## Evidence and action

Record dataset provenance, group definitions, sample limitations, metrics, practical significance, reviewer expertise, and mitigation. Escalate legal interpretations to qualified counsel. Retest mitigations and monitor real-world outcomes where lawful and feasible.

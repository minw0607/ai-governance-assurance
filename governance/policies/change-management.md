---
schema_version: "1.0"
artifact_id: GOV-POL-006
title: AI Change Management Policy
artifact_class: governance
artifact_type: policy
domains:
  - change-management
  - configuration-management
  - regression-testing
applies_to:
  - generative-ai
  - rag
  - agentic-ai
  - machine-learning
industries:
  - cross-industry
lifecycle_stages:
  - development
  - deployment
  - operation
  - retirement
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - GenAI Policies - Example.docx
  - GenAI Testing Procedures v2.docx
---

# AI Change Management Policy

## Policy objective

Changes to AI behavior, data, access, or operating context must be identified, assessed, tested, approved, released, monitored, and reversible where practicable.

## Change scope

Changes include models and providers; versions and parameters; prompts and guardrails; retrieval sources, indexes, embeddings, and chunking; tools, permissions, connectors, and memory; application code; data schemas; user groups; intended use; scale; monitoring; and provider-controlled SaaS updates.

## Requirements

1. **Record:** link each material change to an owner, rationale, affected components, risk assessment, and release record.
2. **Classify:** determine whether the change is standard, material, or emergency based on potential effect—not implementation size alone.
3. **Assess:** evaluate impact on legal obligations, data, security, performance, fairness, human oversight, and downstream processes.
4. **Test:** run targeted and regression tests with pre-defined acceptance criteria.
5. **Approve:** use authority commensurate with the system's tier and change impact.
6. **Release:** use staged rollout, version pinning, canarying, feature flags, or restricted cohorts when available.
7. **Monitor:** compare post-change behavior with baseline and investigate threshold breaches.
8. **Recover:** maintain rollback, fallback, containment, or disablement procedures.

For SaaS systems without version pinning, compensate with provider-change monitoring, golden test sets, increased sampling, restricted high-impact use, and rapid disablement. See the [Regression Testing Guide](../../testing/regression-testing/testing-guide.md).

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
version: "0.2.0"
last_reviewed: 2026-09-18
source_artifacts:
  - SRC-TEST-01
  - SRC-POL-01
---

# AI Regression Testing and Change Detection Guide

> **Scenarios:** executable cases with acceptance criteria are in the [scenario library](scenario-library.md) (`RGS-01` onward). Control objective identifiers resolve in the [Enterprise AI Control Objectives](../../governance/control-framework/control-objectives.md).

## Change surfaces

Track model/provider versions, parameters, prompts, guardrails, retrieval corpus and index, embeddings, tools, permissions, memory policy, application code, evaluator, data schema, user group, and provider-controlled SaaS behavior.

Track the **platform underneath** on the same footing: inference runtime and serving stack, SDK/client and API version, compute and accelerator, region and failover target, container and OS images, orchestration and concurrency settings, gateway timeout/retry/truncation behavior, quota and rate limits, identity and authorization integration, and the logging and tracing pipeline. These change outputs, latency, truncation, tool-call reliability, permission resolution, and evidence completeness without any model or prompt edit, and they are routinely released outside the AI change process.

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

## Shared services with multiple consuming teams

Where the system serves several teams or business units, one regression suite cannot speak for all of them. The platform owner does not know each consumer's authoritative outcomes, acceptance thresholds, or tolerable failure modes.

- **Split the suite.** The platform owner maintains a shared core — safety, security, privacy, agentic boundary, format, latency, cost, and stability probes. Each consuming team owns an acceptance set for its own use case, with its own criteria agreed before execution.
- **Make contribution a condition of onboarding.** A consumer with no acceptance set cannot be tested, and therefore cannot be told whether an upgrade is safe for it. Treat the set as part of the onboarding record, not as a favour.
- **Run both in the same window.** Give consumers the same production-intended configuration, the same period, and the same baseline reference that the shared suite used.
- **Report per consumer.** Publish results by consuming use case. A single averaged score across consumers hides exactly the failure that matters — a severe regression confined to one business unit.
- **Weight by tier, not by volume.** The largest consumer is not necessarily the most consequential one. A failure in a Tier 1 consumer is not offset by passes elsewhere.
- **Baseline per consumer.** Variance differs by use case; a threshold derived from the shared suite may be far too loose for a narrow, high-stakes consumer.

Scenario coverage for these cases is `RGS-09` onward.

## Non-reversible changes

Rollback works only while the prior state still exists. A retired model version, withdrawn API version, decommissioned region, or completed index migration removes it.

Open the change on receipt of the deprecation notice, set the internal cutover date by working back from the provider's deadline with time for consumer testing and remediation, rehearse the migration rather than the rollback, and name the fallback that replaces rollback — alternative version or provider, degraded configuration, manual workflow, or disablement. Decide the disposition of any consumer that cannot pass in time before the deadline, not on the day. See the [AI Change Management Policy](../../governance/policies/change-management.md#changes-that-cannot-be-rolled-back).

## Alerting

Alert on new critical failures, material degradation by risk segment, increased attack success, unauthorized action, privacy breach, abnormal abstention/refusal, trace gaps, or threshold drift. Avoid using a single average that masks severe regressions.

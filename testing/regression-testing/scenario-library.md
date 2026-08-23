---
schema_version: "1.0"
artifact_id: TEST-REG-002
title: Regression Testing Scenario Library
artifact_class: testing
artifact_type: scenario-library
domains:
  - regression
  - change-management
applies_to:
  - generative-ai
  - llm
  - rag
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
  - validation
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-23
---

# Regression Testing Scenario Library

## Purpose

Use this library to detect whether a change — yours or the provider's — moved behavior outside the validated envelope.

Scenarios are starting points, not a compliance list. Select and tailor them from the system's intended purpose, risk tier, data, users, and credible harm. Executing a scenario is not evidence of control effectiveness — the recorded result is.

Companion method guidance: [Regression Testing Guide](testing-guide.md). Control objective identifiers resolve in the [Enterprise AI Control Objectives](../../governance/control-framework/control-objectives.md).

## Scenario record

For each scenario, record the scenario ID, control objective, system and configuration baseline, inputs and variants, expected behavior, acceptance criterion agreed **before** execution, actual result with trace reference, severity, reproducibility, owner, and retest status. Use the [test-case template](../../templates/test-case-template.md).

## Scenarios

### RGS-01 — Provider model version change

**Control objective:** `OPS-03`, `TPRM-03`, `QUAL-06`

**Objective:** Detect behavior change when the provider updates or retires a model version.

**Exercise:** Re-run the frozen regression set against the new version before cutover. Compare accuracy, refusal, format conformance, latency, cost, and worst-case severity against the validated baseline.

**Pass evidence:** Per-dimension delta against baseline with a pre-agreed materiality threshold; explicit go/no-go decision recorded; the case where the prior version is retired without notice is covered by a documented fallback.

### RGS-02 — Silent provider-side change

**Control objective:** `OPS-03`, `TPRM-03`, `OPS-01`

**Objective:** Detect change to a pinned endpoint that was not announced.

**Exercise:** Run a small canary set on a scheduled cadence against the production endpoint and alert on drift in output distribution, refusal rate, format, latency, or token consumption.

**Pass evidence:** Canary cadence, drift metric, alert threshold, and at least one recorded alert investigation; a canary that has never fired should be checked for sensitivity.

### RGS-03 — Prompt and instruction change

**Control objective:** `OPS-03`, `QUAL-06`

**Objective:** Detect unintended effects of a prompt edit.

**Exercise:** Run the full regression set after any system-prompt, instruction, or policy-text change, including changes intended to be cosmetic.

**Pass evidence:** Full-set result compared to baseline; prompt version recorded in the test record; no prompt change reaches production without an associated run.

### RGS-04 — Retrieval corpus and index change

**Control objective:** `QUAL-04`, `DATA-06`, `OPS-03`

**Objective:** Detect quality or permission change after corpus or index modification.

**Exercise:** After document additions, deletions, re-chunking, embedding-model change, or index rebuild, re-run retrieval quality and permission-preservation cases.

**Pass evidence:** Retrieval hit rate and permission-test results before and after; embedding-model changes treated as major changes requiring full revalidation.

### RGS-05 — Tool, schema, and connector change

**Control objective:** `AGT-01`, `SEC-04`, `OPS-03`

**Objective:** Detect breakage or privilege change when a tool or protocol surface changes.

**Exercise:** On any tool addition, schema change, MCP or A2A version change, or connector permission change, re-run agentic authorization and action-integrity scenarios.

**Pass evidence:** Tool inventory diff, schema-compatibility result, and re-run authorization tests; version pinning verified for protocol surfaces.

### RGS-06 — Regression set health

**Control objective:** `QUAL-06`, `DATA-06`

**Objective:** Confirm the regression set still detects what it was built to detect.

**Exercise:** Periodically inject known-bad outputs or revert a known fix and confirm the set fails. Review for staleness, contamination, and coverage of newly discovered failure modes.

**Pass evidence:** Mutation or revert test result, dated staleness review, and evidence that every closed severe finding produced a permanent regression case.

### RGS-07 — Baseline and variance discipline

**Control objective:** `QUAL-06`

**Objective:** Distinguish real regression from run-to-run noise.

**Exercise:** Establish the baseline from multiple runs, not one. Set materiality thresholds above measured variance. Re-run before declaring a regression.

**Pass evidence:** Baseline with variance bounds, threshold derivation, and confirmation runs for any declared regression.

### RGS-08 — Rollback and fallback verification

**Control objective:** `OPS-02`, `OPS-03`

**Objective:** Confirm the system can return to the last validated state.

**Exercise:** Execute an actual rollback of model version, prompt, retrieval configuration, and tool set. Verify behavior matches the prior validated baseline and that in-flight work is handled safely.

**Pass evidence:** Timed rollback execution record, post-rollback regression run matching baseline, and documented handling of partially completed agent actions.


## Coverage note

The distinguishing risk in GenAI regression is that the most consequential changes are made by someone else. RGS-01 and RGS-02 are the scenarios most often missing from otherwise mature change processes.

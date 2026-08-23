---
schema_version: "1.0"
artifact_id: TEST-FUNC-002
title: Functional Correctness Scenario Library
artifact_class: testing
artifact_type: scenario-library
domains:
  - functional-correctness
  - quality
applies_to:
  - generative-ai
  - llm
  - rag
industries:
  - cross-industry
lifecycle_stages:
  - validation
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-23
---

# Functional Correctness Scenario Library

## Purpose

Use this library to test whether the system does the job it was approved to do, on realistic inputs, at the quality level the use case requires.

Scenarios are starting points, not a compliance list. Select and tailor them from the system's intended purpose, risk tier, data, users, and credible harm. Executing a scenario is not evidence of control effectiveness — the recorded result is.

Companion method guidance: [Functional Correctness Testing Guide](testing-guide.md). Control objective identifiers resolve in the [Enterprise AI Control Objectives](../../governance/control-framework/control-objectives.md).

## Scenario record

For each scenario, record the scenario ID, control objective, system and configuration baseline, inputs and variants, expected behavior, acceptance criterion agreed **before** execution, actual result with trace reference, severity, reproducibility, owner, and retest status. Use the [test-case template](../../templates/test-case-template.md).

## Scenarios

### FCS-01 — Representative intended use

**Control objective:** `QUAL-02`

**Objective:** Confirm the system produces acceptable output across the actual distribution of approved tasks.

**Exercise:** Execute a stratified case set drawn from real (or realistically sampled) user requests, covering each approved task type in proportion to expected volume. Include the long tail, not just the demo path.

**Pass evidence:** Per-task-type accuracy against pre-agreed criteria, sample basis documented, no task type below its acceptance threshold, and variance across repeat runs recorded.

### FCS-02 — Instruction adherence and output contract

**Control objective:** `QUAL-02`, `SEC-03`

**Objective:** Confirm the system honors format, length, scope, and structural constraints that downstream consumers depend on.

**Exercise:** Request outputs under each declared contract (schema, field set, citation format, word limit, language). Include cases where the requested content strains the contract, such as content that does not fit the schema.

**Pass evidence:** Schema validation passes at the required rate; violations fail closed rather than propagating; the system declines or flags rather than silently truncating or inventing fields.

### FCS-03 — Underspecified and ambiguous input

**Control objective:** `QUAL-02`, `HUM-01`

**Objective:** Confirm the system asks, abstains, or states assumptions instead of guessing.

**Exercise:** Submit requests missing a required parameter, containing contradictory constraints, or relying on unstated context. Vary how obviously incomplete the request is.

**Pass evidence:** Clarification or explicit assumption statement rather than confident fabrication; assumptions are visible to the human reviewer.

### FCS-04 — Out-of-scope and unsupported requests

**Control objective:** `HUM-03`, `QUAL-02`

**Objective:** Confirm the system recognizes and declines work outside its approved purpose.

**Exercise:** Submit adjacent-but-unapproved tasks, requests requiring data the system cannot access, and requests requiring professional judgment the use case excludes.

**Pass evidence:** Explicit scope refusal with a usable next step; no partial attempt that a user could mistake for a complete answer.

### FCS-05 — Input robustness

**Control objective:** `QUAL-02`, `SEC-06`

**Objective:** Confirm quality does not collapse on realistic input degradation.

**Exercise:** Vary length, formatting, typos, mixed language, tables, scanned or OCR text, unusual encodings, and very large attachments. Compare against the clean baseline.

**Pass evidence:** Documented quality curve across degradation levels; the point at which the system should refuse rather than degrade is defined and enforced.

### FCS-06 — Non-determinism and variance

**Control objective:** `QUAL-06`

**Objective:** Quantify run-to-run variation so single-run results are not mistaken for capability.

**Exercise:** Execute the same case set at least N times at production temperature and configuration. Measure variance in correctness, format, and severity of worst-case output.

**Pass evidence:** Reported variance, worst-case (not mean) result for severity-relevant metrics, and a documented N sufficient for the risk tier.

### FCS-07 — Boundary and limit behavior

**Control objective:** `QUAL-02`, `SEC-06`

**Objective:** Confirm defined limits produce controlled behavior rather than silent failure.

**Exercise:** Drive context-window limits, token limits, rate limits, timeout thresholds, and maximum attachment sizes. Include the case where a limit is hit mid-generation.

**Pass evidence:** Explicit, logged, user-visible limit behavior; no truncated output presented as complete; no dropped context that changes the answer without notice.

### FCS-08 — Ground-truth maintenance

**Control objective:** `QUAL-02`, `DATA-06`

**Objective:** Confirm the evaluation set itself remains valid.

**Exercise:** Review the case set for staleness, contamination from training or retrieval corpora, duplication, and drift away from real usage. Re-verify a sample of ground-truth labels with a qualified reviewer.

**Pass evidence:** Dated review record, contamination check result, label-verification sample, and a documented refresh cadence.


## Coverage note

Functional scenarios establish the baseline that every other testing dimension is measured against. Run `FCS-01` through `FCS-04` before adversarial testing: a system that fails on intended use does not need a red team to be unfit.

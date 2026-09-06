---
schema_version: "1.0"
artifact_id: TEST-INT-002
title: Integration and Workflow Scenario Library
artifact_class: testing
artifact_type: scenario-library
domains:
  - integration
  - workflow
  - human-factors
applies_to:
  - generative-ai
  - rag
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
  - validation
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-09-05
---

# Integration and Workflow Scenario Library

## Purpose

Use this library to test the system as deployed in the real work process — including the humans, the handoffs, and the systems of record.

Scenarios are starting points, not a compliance list. Select and tailor them from the system's intended purpose, risk tier, data, users, and credible harm. Executing a scenario is not evidence of control effectiveness — the recorded result is.

Companion method guidance: [Integration and Workflow Testing Guide](testing-guide.md). Control objective identifiers resolve in the [Enterprise AI Control Objectives](../../governance/control-framework/control-objectives.md).

## Scenario record

For each scenario, record the scenario ID, control objective, system and configuration baseline, inputs and variants, expected behavior, acceptance criterion agreed **before** execution, actual result with trace reference, severity, reproducibility, owner, and retest status. Use the [test-case template](../../templates/test-case-template.md).

## Scenarios

### IWS-01 — End-to-end workflow completion

**Control objective:** `QUAL-02`, `HUM-01`

**Objective:** Confirm the full process produces the intended business outcome.

**Exercise:** Execute the workflow from real trigger to authoritative system-of-record state, using production-intended identities, permissions, and integrations. Verify the downstream record, not the interface confirmation.

**Pass evidence:** Authoritative downstream state verified for each path; interface success without corresponding record state is a finding.

### IWS-02 — Human review under realistic workload

**Control objective:** `HUM-01`

**Objective:** Determine whether human oversight is effective at production volume, not in principle.

**Exercise:** Observe reviewers handling production-representative volume and time pressure. Measure time per item, catch rate for seeded errors, and override behavior.

**Pass evidence:** Seeded-error catch rate at realistic throughput; time per item compared with the time the task actually requires; a control that only works at low volume is recorded as ineffective at design volume.

### IWS-03 — Automation bias and anchoring

**Control objective:** `HUM-01`, `QUAL-03`

**Objective:** Determine whether the AI suggestion displaces independent judgment.

**Exercise:** Seed confidently-worded incorrect suggestions. Compare reviewer decisions against a control condition without the suggestion, or without its rationale.

**Pass evidence:** Difference in error rate between conditions; where anchoring is material, the mitigation (withholding rationale, requiring independent conclusion first) is tested rather than asserted.

### IWS-04 — Degraded and fallback operation

**Control objective:** `SEC-06`, `OPS-02`

**Objective:** Confirm the business process continues safely when the AI component is unavailable or degraded.

**Exercise:** Induce provider outage, timeout, rate limiting, partial response, and retrieval unavailability. Verify the documented manual or fallback path actually functions and that staff know it.

**Pass evidence:** Fallback executed end to end with timings; no silent degradation presented to the user as a normal result; staff awareness confirmed rather than assumed.

### IWS-05 — Partial failure and idempotency

**Control objective:** `AGT-07`, `OPS-02`

**Objective:** Confirm interrupted work does not leave inconsistent or duplicated state.

**Exercise:** Interrupt mid-workflow at each state-changing step — network failure, timeout, crash, user abandonment. Retry the same operation. Inspect downstream records.

**Pass evidence:** No duplicate or orphaned records; retries demonstrably idempotent; compensating actions logged and verifiable.

### IWS-06 — Identity and permission propagation

**Control objective:** `SEC-02`, `DATA-02`, `AGT-06`

**Objective:** Confirm the requesting user's authority is enforced at every downstream hop.

**Exercise:** Execute the workflow as identities with differing entitlements, including a deliberately under-privileged one, and verify each integration enforces the user's authority rather than a shared service account.

**Pass evidence:** Effective permission at each hop documented; any hop enforcing service-account authority where user authority is required is a finding.

### IWS-07 — Record reconstruction and auditability

**Control objective:** `SEC-05`, `AGT-03`

**Objective:** Confirm a completed transaction can be reconstructed after the fact.

**Exercise:** Select a completed workflow instance and reconstruct, from retained records alone, what was requested, what was retrieved, what the system proposed, who approved, what changed, and when.

**Pass evidence:** Complete reconstruction from the evidence store within the retention period; each unreconstructable element identified with its missing record type.

### IWS-08 — User comprehension and disclosure

**Control objective:** `HUM-02`, `HUM-03`

**Objective:** Confirm users understand what the system did and what they remain responsible for.

**Exercise:** Test whether AI involvement, limitations, verification duties, and escalation routes are conveyed at the point of use. Verify comprehension with actual users, not by confirming the notice exists.

**Pass evidence:** Comprehension evidence from real users; correction, appeal, and support routes exercised end to end and confirmed to reach a human.


## Coverage note

A system that passes every model-level test can still fail in production because the reviewer has eight seconds per item, the fallback path was never exercised, or the record of decision does not reconstruct. These scenarios are where those failures surface.

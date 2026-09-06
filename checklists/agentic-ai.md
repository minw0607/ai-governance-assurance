---
schema_version: "1.0"
artifact_id: CHECK-AGENT-001
title: Agentic AI Control Checklist
artifact_class: checklist
artifact_type: checklist
domains:
  - agentic-ai
  - autonomy
  - tool-governance
applies_to:
  - agentic-ai
  - multi-agent-systems
industries:
  - cross-industry
lifecycle_stages:
  - design
  - validation
  - deployment
  - operation
status: draft
version: "0.2.0"
last_reviewed: 2026-08-18
source_artifacts:
  - SRC-AGT-01
  - SRC-TEST-01
  - SRC-AUD-01
---

# Agentic AI Control Checklist

## How to use this checklist

**Lifecycle gate:** G2–G6 (agentic overlay; applies at every gate once agentic capability is present) — see [AI Lifecycle Stage Gates](../governance/lifecycle/stage-gates.md).

Each section lists the [control objectives](../governance/control-framework/control-objectives.md) its items are intended to evidence. A checked box is not evidence; record the artifact, owner, date, and result against the named objective using the [test-case](../templates/test-case-template.md) and [findings](../templates/findings-report-template.md) templates.

## Purpose and authority

**Control objectives:** AGT-02, GOV-01, GOV-02, HUM-03

- [ ] Agent goal, allowed scope, success condition, prohibited actions, and termination condition are explicit.
- [ ] Every tool/action has an owner, business purpose, and read/write/delete/transact/execute classification.
- [ ] User authority is propagated and revalidated at action time.
- [ ] The agent cannot expand its own privileges, change governing policy, approve its own material action, or authorize its own exception.

## Privilege and action

**Control objectives:** AGT-01, AGT-02, AGT-06, SEC-02, SEC-03

- [ ] Credentials are held and scoped by trusted application components, not model-controlled content.
- [ ] Least privilege, parameter validation, rate/action budgets, and destination restrictions are enforced deterministically.
- [ ] Irreversible, external, privileged, or high-impact actions require the defined approval.
- [ ] Reviewers see the exact action and material parameters before approval.

## Context, tools, and memory

**Control objectives:** AGT-01, AGT-04, AGT-06, DATA-01, DATA-02, QUAL-04

- [ ] Untrusted input paths include retrieval, email, files, web, tool output, MCP metadata, messages, and memory.
- [ ] Tool/package identity, version, integrity, and provenance are verified.
- [ ] A2A/MCP clients, servers, extensions, SDK/protocol versions, tool schemas, endpoints, and owners are registered and approved.
- [ ] Tokens are scope- and audience-bound, validated at each trust boundary, and not passed unchanged to unauthorized downstream services.
- [ ] Memory writes are classified, logged, bounded, reviewable, and deletable.
- [ ] Cross-user, cross-session, and cross-agent contamination is tested.

## Reliability and coordination

**Control objectives:** AGT-05, AGT-07, SEC-06, QUAL-06

- [ ] Loops, retries, duplicates, concurrency, partial failure, and state recovery are controlled.
- [ ] Delegation limits, provenance, recursion, conflicts, and shared resources are governed.
- [ ] Child agents have distinct identities, bounded authority, parent/task linkage, termination conditions, and maximum delegation depth.
- [ ] Completion is verified against system state rather than accepted from self-report alone.

## Observability and recovery

**Control objectives:** AGT-03, SEC-05, OPS-01, OPS-02

- [ ] Planning, tool calls, approvals, state changes, errors, and final outcomes are reconstructable.
- [ ] Alerts cover unauthorized action, repeated failure, budget breach, anomalous tools, and trace gaps.
- [ ] Kill switch, credential revocation, containment, rollback/compensation, and checkpoint recovery are tested.
- [ ] Material runs can be reconstructed from decision and action evidence without relying on hidden chain-of-thought.
- [ ] Audit evidence is integrity-protected, access-controlled, minimized, exportable, and retained under an approved schedule.

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
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - GenAI Testing Procedures v2.docx
  - GenAI Audit Checklist v3.xlsx
---

# Agentic AI Control Checklist

## Purpose and authority

- [ ] Agent goal, allowed scope, success condition, prohibited actions, and termination condition are explicit.
- [ ] Every tool/action has an owner, business purpose, and read/write/delete/transact/execute classification.
- [ ] User authority is propagated and revalidated at action time.

## Privilege and action

- [ ] Credentials are held and scoped by trusted application components, not model-controlled content.
- [ ] Least privilege, parameter validation, rate/action budgets, and destination restrictions are enforced deterministically.
- [ ] Irreversible, external, privileged, or high-impact actions require the defined approval.
- [ ] Reviewers see the exact action and material parameters before approval.

## Context, tools, and memory

- [ ] Untrusted input paths include retrieval, email, files, web, tool output, MCP metadata, messages, and memory.
- [ ] Tool/package identity, version, integrity, and provenance are verified.
- [ ] Memory writes are classified, logged, bounded, reviewable, and deletable.
- [ ] Cross-user, cross-session, and cross-agent contamination is tested.

## Reliability and coordination

- [ ] Loops, retries, duplicates, concurrency, partial failure, and state recovery are controlled.
- [ ] Delegation limits, provenance, recursion, conflicts, and shared resources are governed.
- [ ] Completion is verified against system state rather than accepted from self-report alone.

## Observability and recovery

- [ ] Planning, tool calls, approvals, state changes, errors, and final outcomes are reconstructable.
- [ ] Alerts cover unauthorized action, repeated failure, budget breach, anomalous tools, and trace gaps.
- [ ] Kill switch, credential revocation, containment, rollback/compensation, and checkpoint recovery are tested.

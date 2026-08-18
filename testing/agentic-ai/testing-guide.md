---
schema_version: "1.0"
artifact_id: TEST-AGENT-001
title: Agentic AI Testing Guide
artifact_class: testing
artifact_type: testing-guide
domains:
  - agentic-ai
  - tool-use
  - autonomous-systems
applies_to:
  - agentic-ai
  - multi-agent-systems
  - llm
industries:
  - cross-industry
lifecycle_stages:
  - development
  - validation
  - deployment
  - operation
status: draft
version: "0.2.0"
last_reviewed: 2026-08-18
source_artifacts:
  - Agentic_AI_Auditing_Framework.docx
  - GenAI Testing Procedures v2.docx
  - GenAI Audit Checklist v3.xlsx
---

# Agentic AI Testing Guide

Use this guide with the [Agentic AI Governance and Assurance Profile](../../governance/agentic-ai/governance-and-assurance-profile.md). Select and document concrete tests through the [Agentic AI Assurance Scenario Library](scenario-library.md).

## Objective

Evaluate whether an agent can achieve authorized goals without exceeding permissions, losing goal integrity, creating uncontrolled side effects, or becoming unrecoverable.

## Required test areas

### Tool selection and arguments

Test correct tool choice, schema adherence, parameter validation, tool errors, timeouts, stale data, malicious tool output, and unavailable dependencies.

### Identity and privilege

Verify per-tool and per-action least privilege, credential separation, token refresh/revocation, tenant boundaries, and resistance to requests that exceed the user's authority.

### Action control

Test read, write, delete, transact, execute, and communicate actions separately. High-impact actions should require deterministic authorization and, where required, human confirmation of the exact action.

### Goal integrity

Inject conflicting instructions through user input, retrieval, memory, tool output, messages, and other agents. Confirm that the agent preserves the authorized goal or stops safely.

### Planning and completion

Test ambiguous goals, excessive decomposition, loops, duplicate actions, premature completion, hidden assumptions, and unsatisfied success conditions.

### Memory and state

Test poisoning, sensitive retention, cross-user contamination, instruction-bearing writes, deletion, state loss, checkpoint recovery, and idempotent resume.

### Multi-agent coordination

Test delegation authority, provenance, conflicting goals, recursive delegation, message spoofing, duplicated work, shared-resource conflict, and termination.

### Observability and recovery

Verify reconstructable traces, correlation IDs, alerts, budgets, circuit breakers, kill switch, rollback, compensation, and post-incident evidence.

Require externally meaningful decision and action evidence—identity, authorized purpose, configuration, context references, policy decisions, approvals, calls, state changes, and outcomes. Hidden chain-of-thought is neither required nor a substitute for operational evidence.

### Protocol and delegated authority

For A2A, MCP, or other protocol-mediated systems, test component registration, protocol/SDK/schema version, workload identity, scope and audience validation, unsafe token passthrough, untrusted metadata, delegation depth, message spoofing/replay, child-agent authority, cancellation, and inter-agent traceability. Apply the [A2A, MCP, and Multi-Agent Control Standard](../../governance/agentic-ai/a2a-mcp-multi-agent-control-standard.md).

## Scenario severity

Prioritize combinations of untrusted input, sensitive access, and external or state-changing capability. Test maximum reachable impact, not only the agent's intended happy path.

## Metrics

Track task success, correct tool use, unauthorized-action rate, approval bypass, attack success, loop/duplicate rate, recovery success, trace completeness, cost/resource limits, and human-intervention rate.

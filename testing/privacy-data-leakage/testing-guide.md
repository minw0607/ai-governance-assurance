---
schema_version: "1.0"
artifact_id: TEST-PRIV-001
title: Privacy and Data Leakage Testing Guide
artifact_class: testing
artifact_type: testing-guide
domains:
  - privacy
  - data-leakage
  - access-control
applies_to:
  - generative-ai
  - rag
  - agentic-ai
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

# Privacy and Data Leakage Testing Guide

## Test surfaces

- prompts, outputs, feedback, logs, analytics, and cached context;
- retrieval sources, embeddings, vector indexes, and permission synchronization;
- fine-tuning, evaluation, and abuse-monitoring datasets;
- cross-user, cross-session, workspace, tenant, and region boundaries;
- tools, connectors, external URLs, rendering, and covert output channels; and
- persistent memory and multi-agent communication.

## Procedure

1. Create synthetic canary data with known ownership and classification.
2. Establish users, groups, tenants, repositories, and regions with positive and negative permissions.
3. Test direct requests, indirect retrieval, aggregation, inference, encoding, and prompt-injection-assisted exfiltration.
4. Change and revoke permissions; measure propagation and cache behavior.
5. Exercise retention, deletion, export, legal hold, and data-subject workflows.
6. Verify that logs and evaluator systems do not create secondary leakage.
7. Test alerts, investigation evidence, containment, credential revocation, and deletion verification.

## Expected results

Unauthorized content is not retrieved, inferred, rendered, logged, or exposed through tool calls. Authorized data is limited to the approved purpose and minimization rules. Access and deletion changes propagate within documented service levels.

Use real sensitive data only when necessary, approved, and protected. A successful synthetic canary leak should be treated as a control failure even if no production record was exposed.

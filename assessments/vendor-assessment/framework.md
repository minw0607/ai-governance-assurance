---
schema_version: "1.0"
artifact_id: ASSESS-VENDOR-001
title: GenAI and Agentic AI Vendor Assessment Framework
artifact_class: assessment
artifact_type: framework
domains:
  - third-party-risk
  - ai-governance
  - supply-chain
applies_to:
  - generative-ai
  - agentic-ai
  - foundation-models
industries:
  - financial-services
  - cross-industry
deployment_models:
  - api
  - managed-api
  - saas
lifecycle_stages:
  - intake
  - procurement
  - validation
  - operation
  - retirement
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - GenAI Vendor Assessment Framework.docx
---

# GenAI and Agentic AI Vendor Assessment Framework

## Purpose

This framework evaluates whether an AI vendor and the proposed service can support the organization's intended use within defined risk tolerances. The assessment covers the service actually configured and deployed—not only the provider's general control environment.

## Assessment process

1. Define the use case, deployment model, data, users, integrations, autonomy, and risk tier.
2. Identify the provider, foundation-model provider, hosting platform, subprocessors, tools, and material dependencies.
3. Select the evidence requirements and assessment depth by risk.
4. Review evidence and test customer-controlled configurations.
5. Score criteria, record gaps, and identify compensating controls.
6. Decide: approve, approve with conditions, pilot only, defer, or reject.
7. Establish monitoring, reassessment triggers, and an exit plan.

## Assessment domains

| Domain | Assessment objective | Representative evidence |
|---|---|---|
| Governance and transparency | Understand ownership, intended use, model/system limitations, and internal assurance | System/model cards, governance charter, evaluation reports, known-issues register |
| Architecture and controllability | Understand components, boundaries, configurations, and deterministic controls | Architecture/data-flow diagrams, admin and API documentation, permission model |
| Data governance and privacy | Determine how customer data is processed, retained, isolated, reused, and deleted | DPA, privacy terms, retention/deletion procedure, subprocessor list, residency evidence |
| Security | Evaluate identity, isolation, supply chain, AI-specific threats, logging, and response | SOC/ISO reports, penetration and red-team summaries, incident procedures, audit-log samples |
| Quality and reliability | Determine whether performance is measurable, stable, and fit for the use case | Evaluation methodology, benchmarks, SLA, status history, capacity and resilience results |
| Change management | Determine whether changes are visible, controllable, testable, and reversible | Release notes, version policy, notification history, deprecation and rollback procedures |
| Agentic controls | Bound tool access, state change, memory, autonomy, and human approval | Tool registry, permission matrix, action policies, trace samples, kill-switch evidence |
| Compliance and assurance support | Support applicable obligations, auditability, rights, and examination | Contractual audit/cooperation rights, records capabilities, fairness and impact evidence |
| Supply-chain and concentration risk | Understand dependencies, substitution, and failure scenarios | Subprocessor/model inventory, continuity plan, dependency and exit analysis |

## Assessment depth

| Risk tier | Minimum approach |
|---|---|
| Tier 1 | Full evidence review, independent challenge, adversarial and use-case testing, contractual gap closure, executive risk decision, continuous monitoring |
| Tier 2 | Full questionnaire, evidence validation, targeted testing, second-line review, defined monitoring and exit plan |
| Tier 3 | Abbreviated evidence review, configuration testing, owner and risk approval, periodic monitoring |
| Tier 4 | Basic security/privacy/terms review, approved-use restriction, owner approval |

## SaaS and API distinctions

For SaaS, focus on automatic updates, tenant isolation, admin controls, permission inheritance, exportability, integrated data sources, and compensating monitoring. For API deployments, focus on model/version choice, application architecture, logging, output handling, rate limits, key management, retrieval, and customer-built controls.

## Decision rules

A numeric score supports consistency but cannot override disqualifying conditions. Potential blockers include unauthorized training use, inability to meet mandatory data restrictions, insufficient tenant or identity controls, unbounded high-impact autonomy, lack of material incident notification, or no feasible exit/containment capability.

Use the [questionnaire](questionnaire.md) and [scoring guide](scoring-guide.md). Retain cited evidence and record uncertainty explicitly.

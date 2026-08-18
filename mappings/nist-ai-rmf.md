---
schema_version: "1.0"
artifact_id: MAP-NIST-001
title: NIST AI RMF Mapping
artifact_class: mapping
artifact_type: framework-mapping
domains:
  - nist-ai-rmf
  - ai-governance
  - risk-management
applies_to:
  - generative-ai
  - agentic-ai
  - machine-learning
industries:
  - cross-industry
lifecycle_stages:
  - intake
  - design
  - development
  - validation
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
---

# NIST AI RMF Mapping

## Current status

NIST AI RMF 1.0 remains a voluntary framework. NIST states that version 1.0 is being revised. NIST AI 600-1, the Generative AI Profile released in July 2024, remains a companion profile focused on GenAI risks and actions.

## Function mapping

| NIST AI RMF function | Library implementation |
|---|---|
| Govern | [Governance framework](../governance/ai-governance-framework.md), policies, roles, inventory, risk appetite, exceptions, and accountability |
| Map | [Use-case assessment](../assessments/use-case-assessment/checklist.md), context, affected parties, impacts, data, dependencies, and risk tier |
| Measure | [Testing framework](../testing/testing-framework/enterprise-genai-testing.md), evaluation evidence, thresholds, independent challenge, and uncertainty |
| Manage | Production gates, [monitoring](../checklists/ongoing-monitoring.md), findings, incident response, change, residual risk, and retirement |

## Generative AI Profile themes

The library addresses GenAI-specific concerns through:

- content provenance and unsupported claims;
- data privacy, intellectual property, and information integrity;
- harmful bias and human-AI configuration;
- information security, prompt injection, poisoning, and misuse;
- value-chain, provider, and component integration; and
- pre-deployment testing, incident disclosure, and ongoing monitoring.

## Use note

AI RMF categories should be traced to concrete controls, owners, evidence, and decisions. A claim of alignment without implementation evidence is not assurance.

## Authoritative sources

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST AI 600-1: Generative Artificial Intelligence Profile](https://doi.org/10.6028/NIST.AI.600-1)
- [NIST AI Resource Center](https://airc.nist.gov/)

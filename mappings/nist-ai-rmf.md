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

## Category and subcategory mapping

Function-level alignment is too coarse to support assurance. This table maps AI RMF categories to the library [control objectives](../governance/control-framework/control-objectives.md) that produce testable evidence.

| AI RMF category | Theme | Library control objectives |
|---|---|---|
| GOVERN 1 | Policies, processes, procedures, and practices | `GOV-03`, `GOV-06` |
| GOVERN 2 | Accountability structures, roles, and authority | `GOV-04` |
| GOVERN 3 | Workforce diversity, equity, inclusion, and accessibility | `QUAL-05`, `HUM-02` |
| GOVERN 4 | Organizational culture, risk tolerance, and communication | `GOV-03`, `GOV-06` |
| GOVERN 5 | Engagement with relevant AI actors and affected communities | `HUM-02` |
| GOVERN 6 | Third-party software, data, and supply chain | `TPRM-01`, `TPRM-02`, `TPRM-03`, `SEC-04` |
| MAP 1 | Context, intended purpose, and categorization | `GOV-01`, `GOV-02` |
| MAP 2 | System capabilities, targeted usage, goals, and requirements | `QUAL-01`, `QUAL-02` |
| MAP 3 | Benefits and costs of AI capabilities | `GOV-01`, `QUAL-01` |
| MAP 4 | Risks and benefits mapped for third-party components | `TPRM-01`, `SEC-04`, `DATA-01` |
| MAP 5 | Impacts to individuals, groups, communities, and society | `QUAL-05`, `HUM-02`, `GOV-02` |
| MEASURE 1 | Appropriate methods and metrics identified and applied | `QUAL-02`, `QUAL-06` |
| MEASURE 2 | Trustworthiness characteristics evaluated | `QUAL-03`, `QUAL-04`, `QUAL-05`, `SEC-01`, `DATA-03` |
| MEASURE 3 | Mechanisms for tracking identified risks over time | `OPS-01`, `QUAL-06` |
| MEASURE 4 | Feedback about efficacy of measurement gathered and assessed | `OPS-01`, `HUM-01` |
| MANAGE 1 | Risks prioritized, responded to, and managed | `GOV-06`, `OPS-03` |
| MANAGE 2 | Strategies to maximize benefits and minimize negative impacts | `HUM-01`, `HUM-03`, `AGT-02` |
| MANAGE 3 | Third-party risks and benefits managed | `TPRM-02`, `TPRM-03` |
| MANAGE 4 | Post-deployment monitoring, response, recovery, and communication | `OPS-01`, `OPS-02`, `OPS-04`, `SEC-05` |

Subcategory identifiers (`GOVERN 1.1`, `MEASURE 2.7`, and so on) should be recorded on the individual [test case](../templates/test-case-template.md) or [monitoring plan](../templates/monitoring-plan-template.md) entry, not maintained as a static table here — subcategory wording changes between AI RMF revisions and a stale crosswalk is worse than none.

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

---
schema_version: "1.0"
artifact_id: MAP-EUAIA-001
title: EU AI Act Implementation Mapping
artifact_class: mapping
artifact_type: regulatory-mapping
domains:
  - eu-ai-act
  - regulation
  - conformity
applies_to:
  - ai-systems
  - general-purpose-ai
  - generative-ai
industries:
  - cross-industry
lifecycle_stages:
  - intake
  - design
  - deployment
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
---

# EU AI Act Implementation Mapping

## Applicability first

Determine the organization's role (provider, deployer, importer, distributor, product manufacturer, or authorized representative), geographic nexus, AI-system classification, intended purpose, and whether the output is used in the EU. Obligations differ materially by role and classification.

## Current timeline

As of this review:

- prohibited-practice and definition provisions began applying on **2 February 2025**;
- governance and general-purpose AI obligations began applying on **2 August 2025**;
- Commission enforcement of GPAI obligations and Article 50 transparency obligations began on **2 August 2026**;
- following the AI Omnibus that entered into force in July 2026, rules for specified Annex III high-risk areas apply from **2 December 2027**; and
- rules for high-risk AI embedded in regulated products apply from **2 August 2028**.

Check transitional provisions for models or systems placed on the market before the relevant dates.

## Library mapping

| AI Act theme | Library artifacts |
|---|---|
| Classification and prohibited practices | [Use-case assessment](../assessments/use-case-assessment/checklist.md), [risk tiering](../governance/risk-tiering/ai-risk-tiering-framework.md), acceptable use |
| Risk and quality management | Governance framework, risk assessment, testing framework, findings and monitoring |
| Data governance | Data handling policy, lineage, quality, privacy, and deletion evidence |
| Technical documentation and records | Inventory, architecture, templates, traceability, change and examination readiness |
| Transparency and human oversight | Use boundaries, disclosures, reviewer authority, contestability, and training |
| Accuracy, robustness, cybersecurity | Functional, factuality, security, privacy, regression, and agentic testing |
| GPAI/provider and value-chain duties | Vendor assessment, documentation, model information, data/copyright considerations, incidents and downstream support |
| Post-market monitoring and incidents | Monitoring plan, incident response, thresholds, remediation, and reassessment |

## Use note

This mapping is not a legal determination or conformity assessment. The regulation and implementing materials evolve; confirm the current official text, harmonized standards, guidelines, and enforcement position.

## Authoritative sources

- [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [European Commission AI Act overview and current timeline](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Navigating the AI Act](https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act)
- [AI Omnibus enters into force](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force)

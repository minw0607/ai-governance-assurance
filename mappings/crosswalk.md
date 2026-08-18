---
schema_version: "1.0"
artifact_id: MAP-CROSS-001
title: Cross-Framework AI Governance Themes
artifact_class: mapping
artifact_type: crosswalk
domains:
  - crosswalk
  - control-mapping
applies_to:
  - generative-ai
  - agentic-ai
  - machine-learning
industries:
  - cross-industry
lifecycle_stages:
  - intake
  - design
  - validation
  - operation
status: draft
version: "0.2.0"
last_reviewed: 2026-08-18
---

# Cross-Framework AI Governance Themes

This crosswalk identifies common implementation themes; it does not claim requirement equivalence.

| Control theme | NIST AI RMF | EU AI Act | SR 26-2 | OWASP GenAI | Library anchor |
|---|---|---|---|---|---|
| Governance and accountability | Govern | Governance, quality management | Governance and controls | Program-level governance | [Governance framework](../governance/ai-governance-framework.md) |
| Context and classification | Map | Roles, prohibited/high-risk/GPAI classification | Purpose, exposure, materiality | Architecture and threat context | [Use-case assessment](../assessments/use-case-assessment/checklist.md) |
| Inventory and documentation | Govern/Map | Technical documentation and records | Inventory and documentation | Asset/supply-chain awareness | Governance framework and templates |
| Risk measurement and testing | Measure | Accuracy, robustness, cybersecurity, conformity evidence | Development testing, validation, outcomes analysis | Adversarial testing | [Testing framework](../testing/testing-framework/enterprise-genai-testing.md) |
| Data governance and privacy | Map/Measure/Manage | Data governance and fundamental rights | Inputs and data limitations | Disclosure, poisoning, vector weaknesses | [AI Data Security & Governance](../governance/data-security-governance/README.md) |
| Human oversight and action control | Govern/Manage | Human oversight and transparency | Effective challenge and appropriate use | Excessive agency | Agentic guide and checklist |
| Monitoring and incident response | Manage | Post-market monitoring and incidents | Ongoing monitoring | Detection, response, resource abuse | Monitoring checklist and template |
| Change and lifecycle | Govern/Manage | Substantial modification and lifecycle duties | Changes, deterioration, redevelopment | Supply-chain and configuration change | Change policy and regression testing |
| Third-party risk | Govern/Map/Manage | Value-chain roles and cooperation | Vendor products | Supply chain | Vendor assessment framework |

## Interpretation cautions

- NIST AI RMF is voluntary and currently under revision.
- EU AI Act applicability is legal- and role-specific.
- SR 26-2 explicitly excludes generative and agentic AI, even though its principles may inform internal practices.
- OWASP focuses on security risk and does not cover the full governance or legal landscape.

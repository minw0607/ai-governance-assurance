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

| Control theme | Library control objectives | NIST AI RMF | ISO/IEC 42001 | EU AI Act | SR 26-2 | OWASP GenAI |
|---|---|---|---|---|---|---|
| Governance and accountability | `GOV-03`, `GOV-04`, `GOV-06` | Govern | Cl. 5; A.2, A.3 | Governance, quality management | Governance and controls | Program-level governance |
| Context and classification | `GOV-01`, `GOV-02` | Map | Cl. 4, 6; A.5 | Roles, prohibited/high-risk/GPAI classification | Purpose, exposure, materiality | Architecture and threat context |
| Inventory and documentation | `GOV-05` | Govern/Map | Cl. 7; A.4 | Technical documentation and records | Inventory and documentation | Asset/supply-chain awareness |
| Risk measurement and testing | `QUAL-01`–`QUAL-06` | Measure | Cl. 8; A.6 | Accuracy, robustness, cybersecurity, conformity evidence | Development testing, validation, outcomes analysis | Adversarial testing (`LLM01`, `LLM07`) |
| Data governance and privacy | `DATA-01`–`DATA-07` | Map/Measure/Manage | A.7 | Data governance and fundamental rights | Inputs and data limitations | `LLM02`, `LLM05`, `LLM09` |
| Runtime security | `SEC-01`–`SEC-06` | Measure/Manage | Cl. 8; A.6 | Cybersecurity and robustness | Model implementation controls | `LLM01`, `LLM06`, `LLM08`, `LLM10` |
| Human oversight and action control | `HUM-01`–`HUM-03`, `AGT-02` | Govern/Manage | A.8, A.9 | Human oversight and transparency | Effective challenge and appropriate use | `LLM03` (Excessive Agency); `ASI01`, `ASI09` |
| Agentic identity and coordination | `AGT-01`, `AGT-03`–`AGT-07` | Govern/Measure/Manage | A.6, A.9 | Substantial modification and oversight duties | Out of scope; internal governance choice | `ASI02`–`ASI08`, `ASI10` |
| Monitoring and incident response | `OPS-01`, `OPS-02` | Manage | Cl. 9; A.6 | Post-market monitoring and incidents | Ongoing monitoring | Detection, response, resource abuse |
| Change and lifecycle | `OPS-03`, `OPS-04` | Govern/Manage | Cl. 10; A.6 | Substantial modification and lifecycle duties | Changes, deterioration, redevelopment | `LLM04` supply-chain and configuration change |
| Third-party risk | `TPRM-01`–`TPRM-03` | Govern/Map/Manage | A.10 | Value-chain roles and cooperation | Vendor products | `LLM04`, `ASI04` |

Control objective identifiers resolve in the [Enterprise AI Control Objectives](../governance/control-framework/control-objectives.md). Full per-framework detail is in the [NIST](nist-ai-rmf.md), [ISO/IEC 42001](iso-iec-42001.md), [EU AI Act](eu-ai-act.md), [SR 26-2](sr-26-2.md), [OWASP LLM](owasp-genai.md), and [OWASP Agentic](owasp-agentic.md) mappings.

## Interpretation cautions

- NIST AI RMF is voluntary and currently under revision.
- EU AI Act applicability is legal- and role-specific.
- SR 26-2 explicitly excludes generative and agentic AI, even though its principles may inform internal practices.
- OWASP focuses on security risk and does not cover the full governance or legal landscape.
- ISO/IEC 42001 Annex A controls are selective, not mandatory; applicability is set by the organization's own risk treatment and recorded in a Statement of Applicability.
- Column entries indicate related intent, not requirement equivalence. A single library control objective may only partially satisfy a framework requirement, and vice versa.

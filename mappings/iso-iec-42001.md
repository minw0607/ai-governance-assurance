---
schema_version: "1.0"
artifact_id: MAP-ISO42001-001
title: ISO/IEC 42001 AI Management System Mapping
artifact_class: mapping
artifact_type: standards-mapping
domains:
  - iso-42001
  - management-system
  - certification
applies_to:
  - artificial-intelligence
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
  - deployment
  - operation
  - retirement
status: draft
version: "0.1.0"
last_reviewed: 2026-09-05
---

# ISO/IEC 42001 AI Management System Mapping

## What this standard is

ISO/IEC 42001:2023 specifies requirements for an **AI management system (AIMS)** — the organizational system for establishing, implementing, maintaining, and improving responsible AI. It is certifiable, and it is the standard most often requested in customer due diligence and procurement.

Two structural points drive how this library maps to it:

- **Clauses 4–10 are requirements.** An AIMS must satisfy them to conform. They are about the management system itself: context, leadership, planning, support, operation, evaluation, improvement.
- **Annex A controls are selective.** Clause 6.1.3 requires the organization to determine the controls its risk treatment needs and then compare that set against Annex A to confirm nothing relevant was overlooked. Applicability and exclusions are recorded in a **Statement of Applicability (SoA)**.

This library supplies control content and evidence practices. It does **not** constitute an AIMS, and using it does not confer or imply certification.

## Clause 4–10 mapping

| Clause | Requirement theme | Library implementation |
|---|---|---|
| 4 — Context of the organization | Internal/external issues, interested parties, AIMS scope, organizational role (provider, developer, deployer, user) | [AI Governance Framework](../governance/ai-governance-framework.md); [Use-Case Assessment](../assessments/use-case-assessment/checklist.md) role and boundary determination |
| 5 — Leadership | AI policy, leadership commitment, roles, responsibilities, authorities | [Roles and Decision Rights](../governance/operating-model/roles-and-decision-rights.md); [GenAI Policy Suite](../governance/policies/README.md); `GOV-03`, `GOV-04` |
| 6 — Planning | Risk and opportunity, AI risk assessment and treatment, AI system impact assessment, objectives, SoA | [AI Risk Tiering Framework](../governance/risk-tiering/ai-risk-tiering-framework.md); [Risk Assessment Template](../templates/risk-assessment-template.md); `GOV-02`, `GOV-06` |
| 7 — Support | Resources, competence, awareness, communication, documented information | [Roles and Decision Rights](../governance/operating-model/roles-and-decision-rights.md); `GOV-03`, `GOV-05` |
| 8 — Operation | Operational planning and control, risk assessment/treatment execution, impact assessment execution | [AI Lifecycle Stage Gates](../governance/lifecycle/stage-gates.md); [Control Objectives](../governance/control-framework/control-objectives.md); [Pre-Deployment](../checklists/pre-deployment.md) and [Production Readiness](../checklists/production-readiness.md) checklists |
| 9 — Performance evaluation | Monitoring, measurement, analysis, internal audit, management review | [Ongoing Monitoring](../checklists/ongoing-monitoring.md); [Monitoring Plan Template](../templates/monitoring-plan-template.md); [Examination Readiness](../checklists/examination-readiness.md); `OPS-01` |
| 10 — Improvement | Nonconformity, corrective action, continual improvement | [Findings Report Template](../templates/findings-report-template.md); `GOV-06`, `OPS-02`, `OPS-03` |

## Annex A control-group mapping

Annex A groups A.2–A.10 contain 38 controls. This table maps each group to the library control objectives that carry equivalent intent, so an SoA entry can cite concrete, testable content.

| Annex A group | Title | Library control objectives | Primary library artifacts |
|---|---|---|---|
| A.2 | Policies related to AI | `GOV-03` | [GenAI Policy Suite](../governance/policies/README.md); [Acceptable Use](../governance/policies/acceptable-use.md) |
| A.3 | Internal organization | `GOV-04`, `GOV-06` | [Roles and Decision Rights](../governance/operating-model/roles-and-decision-rights.md) |
| A.4 | Resources for AI systems | `GOV-05`, `DATA-01`, `SEC-04` | [AI Inventory Minimum Data Standard](../governance/ai-inventory/minimum-data-standard.md) |
| A.5 | Assessing impacts of AI systems | `GOV-01`, `GOV-02`, `QUAL-05`, `HUM-02` | [Risk Tiering](../governance/risk-tiering/ai-risk-tiering-framework.md); [Risk Assessment Template](../templates/risk-assessment-template.md) |
| A.6 | AI system life cycle | `QUAL-01`–`QUAL-06`, `OPS-03`, `OPS-04` | [Stage Gates](../governance/lifecycle/stage-gates.md); [Enterprise GenAI Testing](../testing/testing-framework/enterprise-genai-testing.md) |
| A.7 | Data for AI systems | `DATA-01`–`DATA-07`, `QUAL-04` | [AI Data Security & Governance](../governance/data-security-governance/README.md); [Training and Evaluation Data Governance](../governance/data-security-governance/training-evaluation-data-governance.md) |
| A.8 | Information for interested parties | `HUM-02` | [Findings Report Template](../templates/findings-report-template.md); disclosure requirements in the [governance framework](../governance/ai-governance-framework.md) |
| A.9 | Use of AI systems | `HUM-01`, `HUM-03`, `AGT-02` | [Acceptable Use](../governance/policies/acceptable-use.md); [Agentic AI Checklist](../checklists/agentic-ai.md) |
| A.10 | Third-party and customer relationships | `TPRM-01`, `TPRM-02`, `TPRM-03` | [Vendor Assessment Framework](../assessments/vendor-assessment/framework.md); [Third-Party Risk Policy](../governance/policies/third-party-risk.md) |

## Coverage gaps

This library is control- and assurance-oriented. An organization pursuing certification must add AIMS machinery that is intentionally out of scope here:

- a documented AIMS scope statement and AI policy approved by top management;
- a Statement of Applicability with justified inclusions and exclusions;
- an internal audit programme and management review records;
- competence and awareness records for personnel in AIMS roles; and
- documented-information control (versioning, approval, distribution, retention) for the AIMS itself.

## Use note

Mapping is not conformity. Group-level correspondence identifies where to look; each Annex A control has its own text and implementation guidance in ISO/IEC 42001 and ISO/IEC 42005, and applicability is determined by the organization's own risk treatment. Obtain the standard and assess against its actual wording.

## Authoritative sources

- [ISO/IEC 42001:2023](https://www.iso.org/standard/42001)
- [ISO/IEC 23894:2023 — AI risk management guidance](https://www.iso.org/standard/77304.html)
- [ISO/IEC JTC 1/SC 42 catalog](https://www.iso.org/committee/6794475/x/catalogue/)

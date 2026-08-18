---
schema_version: "1.0"
artifact_id: REF-SRC-002
title: Source-to-Library Coverage Map
artifact_class: reference
artifact_type: traceability-map
domains:
  - provenance
  - migration
  - coverage
applies_to:
  - library
industries:
  - cross-industry
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
---

# Source-to-Library Coverage Map

## Purpose

This map records how the supplied source documents were curated into the library. “Migrated” means the underlying concept is represented, not that the source text was copied verbatim. Stale legal conclusions, fixed numerical thresholds, product UI instructions, and unsupported claims are not carried forward without review.

## Coverage status

- **Detailed:** concepts are represented in operational artifacts with requirements, evidence, or procedures.
- **Baseline:** core concepts are present, but additional depth or examples may still be useful.
- **Deferred:** intentionally excluded from the core library because the material is implementation-specific, volatile, duplicative, or needs separate review.
- **Superseded:** replaced by current authoritative information or corrected scope.

## GenAI Policies - Example.docx

| Source section | Curated destinations | Status and decision |
|---|---|---|
| Executive summary and policy architecture | [AI Governance Framework](../governance/ai-governance-framework.md); policy suite | Detailed; converted from one large policy document into framework, policies, standards, and procedures |
| Acceptable use, user responsibility, intake, attestations, enforcement, exceptions | [Acceptable Use](../governance/policies/acceptable-use.md); [Stage Gates](../governance/lifecycle/stage-gates.md); [Roles and Decision Rights](../governance/operating-model/roles-and-decision-rights.md) | Detailed; fixed examples and organization-specific forms generalized |
| Data classification, regulated data, prompt/output handling, retention, cross-border | [Data Handling](../governance/policies/data-handling.md); [Control Objectives](../governance/control-framework/control-objectives.md) | Detailed; legal applicability and exact retention periods left for tailoring |
| Model definition, inventory, development, validation, monitoring, change, retirement | [AI Inventory Standard](../governance/ai-inventory/minimum-data-standard.md); [Model Risk Policy](../governance/policies/model-risk-management.md); [Stage Gates](../governance/lifecycle/stage-gates.md) | Detailed; legacy SR 11-7 conclusions superseded by the current SR 26-2 scope note |
| Third-party assessment, contracts, monitoring | Vendor assessment framework/questionnaire/scoring; [Third-Party Risk Policy](../governance/policies/third-party-risk.md) | Detailed |
| Prompt security, effectiveness, versioning, grounding | [Prompt Management](../governance/policies/prompt-management.md); security and factuality testing guides | Detailed |
| Technical security standards | [Control Objectives](../governance/control-framework/control-objectives.md); security, privacy, and agentic testing guides | Detailed; fixed cryptographic versions, rotation periods, and numeric alert examples treated as tailoring inputs rather than universal requirements |
| Testing and validation standards | Enterprise testing framework and nine testing guides | Detailed; brittle universal pass rates excluded |
| Monitoring, incident response, continuous improvement | [AI Governance Framework](../governance/ai-governance-framework.md); ongoing monitoring and examination checklists | Detailed; fixed notification timelines not generalized |
| Prohibited and restricted uses | [Acceptable Use](../governance/policies/acceptable-use.md); [Risk Tiering](../governance/risk-tiering/ai-risk-tiering-framework.md) | Baseline; organizations must map current law and risk appetite |
| Governance structure and RACI | [Roles and Decision Rights](../governance/operating-model/roles-and-decision-rights.md) | Detailed |
| LLM change-management appendix | [Change Management](../governance/policies/change-management.md); regression testing; stage-gate change routing | Detailed |
| AI inventory and agentic-AI appendix | [AI Inventory Standard](../governance/ai-inventory/minimum-data-standard.md); [Agentic AI Testing](../testing/agentic-ai/testing-guide.md); control objectives | Detailed |
| Credit-underwriting case study | Risk tiering, human oversight, fairness, evidence, and lifecycle controls | Baseline; source assertions tied to superseded guidance were not retained as current requirements |

## GenAI Audit Checklist v3.xlsx

| Workbook area | Curated destinations | Status and decision |
|---|---|---|
| Governance and lifecycle controls | [Control Objectives](../governance/control-framework/control-objectives.md); [Stage Gates](../governance/lifecycle/stage-gates.md); examination checklist | Detailed; design and operating-effectiveness distinction retained |
| Data security and privacy | Data policy, privacy testing, production/examination checklists, control objectives | Detailed |
| Model risk and quality | Testing framework, factuality/fairness/RAG methods, readiness assessment, control objectives | Detailed |
| Runtime security and monitoring | Security red teaming, ongoing monitoring, incident and resilience controls | Detailed |
| Agentic AI governance | Agentic testing, agentic checklist, inventory and control objectives | Detailed |
| Walkthrough prompts | Examination readiness and control-objective assurance procedures | Detailed; walkthrough topics generalized into reusable procedures |
| Low/medium/high issue interpretation | Readiness and vendor scoring guides; findings template | Baseline; ratings remain indicative rather than universal |

## GenAI MRM Survey with Heatmap v2.xlsx

| Workbook area | Curated destinations | Status and decision |
|---|---|---|
| Inventory and scope | Readiness assessment; AI inventory standard | Detailed |
| Use and autonomy | Risk tiering; agentic controls; readiness assessment | Detailed |
| Data, privacy, IP, performance, hallucination, explainability, vendor, accountability | Readiness checklist and control objectives | Detailed |
| Response scoring and category weights | [Readiness Scoring Guide](../assessments/readiness-assessment/scoring-guide.md) | Detailed; presented as a configurable starting point |
| SR 11-7 / MRM theme labels | [SR 26-2 Mapping](../mappings/sr-26-2.md) | Superseded; no claim that the current guidance directly applies to GenAI or agentic AI |

## GenAI Vendor Assessment Framework.docx

| Source section | Curated destinations | Status and decision |
|---|---|---|
| Purpose, scope, risk tiers, assessment requirements | Vendor assessment framework | Detailed |
| Eight assessment domains and key questions | Vendor questionnaire and control objectives | Detailed |
| Criterion/domain/overall scoring | Vendor scoring guide | Detailed |
| Predeployment and ongoing documentation | Vendor framework and monitoring plan template | Detailed |
| Monitoring dimensions and escalation triggers | Vendor framework, third-party policy, ongoing monitoring checklist | Detailed |
| SaaS versus API considerations | Vendor framework and testing modality guidance | Baseline |
| SR 11-7 appendix | SR 26-2 mapping | Superseded |

## GenAI Testing Procedures v2.docx

| Source section | Curated destinations | Status and decision |
|---|---|---|
| Philosophy, modality, sampling, documentation | Enterprise testing framework | Detailed |
| Functional correctness | Functional testing guide | Detailed |
| Hallucination and factuality | Hallucination/factuality testing guide | Detailed |
| Security and adversarial testing | Security red-teaming guide | Detailed |
| Safety and alignment | Safety/alignment guide | Detailed |
| Bias and fairness | Bias/fairness guide | Detailed |
| Privacy and leakage | Privacy/data-leakage guide | Detailed |
| Integration and workflow | Integration/workflow guide | Detailed |
| Agentic testing | Agentic-AI testing guide | Detailed |
| Regression and change detection | Regression testing guide | Detailed |
| Product-specific quick references | Testing tools reference | Deferred where product configuration or UI is volatile |

## GenAI Testing Comprehensive Guide v2.docx

| Source section | Curated destinations | Status and decision |
|---|---|---|
| Automation spectrum and execution/evaluation split | Use-case-driven test design; testing framework | Detailed at methodology level |
| Test case format types | Use-case-driven test design; test case template | Detailed |
| Query taxonomy | Use-case-driven test design | Detailed |
| Six-step methodology and prioritization | Use-case-driven test design; test plan template | Detailed |
| Product-specific automation | Testing tools reference | Deferred where login, selectors, rate limits, or interface behavior is volatile |

## SaaS Testing Automation UseCase Design.docx

| Source section | Curated destinations | Status and decision |
|---|---|---|
| SaaS automation spectrum | Testing framework and tools reference | Baseline |
| LLM-assisted evaluation | Use-case-driven test design and findings template | Detailed at control-design level |
| Business-use-case decomposition | Use-case-driven test design | Detailed |
| End-to-end workflow | Test plan and test case templates | Detailed |
| Specific product automation code | Testing tools reference | Deferred from core methods |

## Guide Automation Engineer.docx

| Source section | Curated destinations | Status and decision |
|---|---|---|
| Role, dependencies, execution outputs | Testing tools reference and test evidence concepts | Baseline |
| Browser automation, authentication state, selectors, waiting, screenshots, rate limits | None in core governance library | Deferred; suitable for a separate implementation playbook maintained against a specific product/version |
| Troubleshooting and file-output conventions | Testing tools reference | Baseline |

## Remaining enhancement opportunities

- Add sector-specific overlays without changing the cross-industry core.
- Develop product/version-specific automation playbooks in a clearly time-stamped implementation area.
- Add machine-readable control-to-framework mappings at the individual control-objective level.
- Add example completed evidence packages and case studies using synthetic organizations and data.
- Convert selected checklists and assessment models into reusable spreadsheets while retaining the Markdown source of truth.

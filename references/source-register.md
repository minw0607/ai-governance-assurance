---
schema_version: "1.0"
artifact_id: REF-SRC-001
title: Source Register and Migration Decisions
artifact_class: reference
artifact_type: source-register
domains:
  - provenance
  - migration
applies_to:
  - library
industries:
  - cross-industry
status: draft
version: "0.5.0"
last_reviewed: 2026-08-19
---

# Source Register and Migration Decisions

The library was curated from a set of unpublished working drafts held locally. Those drafts are referenced only by opaque source label; no source file, filename, or binary is published in this repository, and the label-to-file mapping is maintained locally.

Every public artifact in this library is independently rewritten in repository-native Markdown. Source material was used to identify topics, control themes, and structure. Published wording, control objectives, evidence expectations, and regulatory statements were re-derived and re-verified against the primary sources cited in each artifact. Section-level traceability is maintained in the [Source-to-Library Coverage Map](source-coverage-map.md).

Nothing in this library reproduces confidential, proprietary, client, or employer information. Where source material contained organization-specific, engagement-specific, or personally identifying context, that content was excluded rather than generalized.

| Source label | Material type | Primary use | Migration decision |
|---|---|---|---|
| SRC-POL-01 | Policy draft | Governance, policy, roles, data, change | Decomposed into a framework, operating model, lifecycle, inventory and control standards, plus modular policies; outdated regulatory assertions corrected |
| SRC-VEND-01 | Assessment draft | Vendor tiers, domains, questionnaire, scoring | Split into framework, questionnaire, and scoring guide |
| SRC-TEST-01 | Procedure draft | Enterprise testing dimensions and procedures | Decomposed into independent testing methodologies |
| SRC-TEST-02 | Guide draft | Test formats, automation, query taxonomy | Consolidated into use-case-driven test design; brittle product instructions excluded |
| SRC-AUD-01 | Checklist draft | Control objectives, evidence, walkthroughs | Curated into control objectives, stage gates, inventory requirements, and examination/lifecycle checklists |
| SRC-MRM-01 | Survey draft | Readiness questions and weighted scoring | Migrated into readiness checklist and scoring guide; SR 11-7 framing updated |
| SRC-SAAS-01 | Design draft | SaaS automation and test design | Reused for modality and test-design principles; product UI details deferred |
| SRC-AUTO-01 | Runbook draft | Product-specific automation execution | Deferred from the library because selectors, interfaces, and authentication flows are implementation-specific and time-sensitive |
| SRC-AGT-01 | Framework draft | Agentic governance, audit modules, A2A/MCP controls, scenarios, evidence requests, and workpapers | Curated into an agentic governance and assurance profile, protocol control standard, scenario library, audit-readiness checklist, workpaper template, and targeted enhancements to tiering, inventory, controls, assessments, glossary, and catalogs |
| SRC-M365-01 | Sample report draft | Product-oriented sample audit report and framework application | Rewritten and reorganized as a wholly synthetic, GitHub-native example aligned to the governance framework, data-security standard, agentic profile, control objectives, scenario library, and findings template |

## Material updates during migration

- SR 26-2 replaced SR 11-7 in April 2026 and explicitly excludes generative and agentic AI.
- OWASP's 2026 LLM Top 10 replaced the 2025 list in August 2026.
- EU AI Act dates were updated for the AI Omnibus that entered into force in July 2026.
- NIST AI RMF 1.0 is identified as under revision; NIST AI 600-1 remains the GenAI companion profile.

## Data security and governance corrections

The data-security source material had strong control intent, but several examples required qualification before becoming reusable standards:

- Fixed prompt, output, log, training-data, or model-artifact retention periods were not adopted as universal requirements. Retention must follow purpose, applicable law, authoritative records schedules, contracts, investigations, legal holds, and minimization.
- The source's “25 months for credit denials” attribution to FCRA was corrected. The 25-month application-record requirement is generally in [Regulation B, 12 CFR 1002.12](https://www.consumerfinance.gov/rules-policy/regulations/1002/12/), with scope, business-credit, investigation, and other qualifications.
- Example algorithms, protocol versions, credential-rotation periods, alert counts, and test sample sizes were treated as tailoring inputs. Current enterprise security standards and risk-based test design control these values.
- A DPA, no-training clause, and encryption do not alone authorize external AI processing. Purpose, data rights, provider features, retention, human review, subprocessors, location, isolation, incident response, deletion, and exit also require review.
- Masking, tokenization, pseudonymization, embeddings, and synthetic data were not treated as automatically anonymous or outside privacy/confidentiality obligations.
- Deletion was expanded from vector removal into source-to-derived lineage, suppression, re-indexing, cache/log/memory/provider handling, backup non-restoration, model-impact assessment, and verification.

## Agentic AI curation corrections

- “Reasoning traceability” was translated into externally meaningful decision-and-action evidence. The library does not require hidden chain-of-thought.
- “Immutable lineage” was translated into proportionate tamper-evident or access-controlled append-only evidence that remains compatible with minimization, correction, deletion, legal hold, and retention obligations.
- Mutual authentication and trust scoring were not treated as universal standalone requirements. Strong workload identity, authenticated channels, authorization, provenance, policy enforcement, and replay resistance are required; mutual authentication and trust/risk signals depend on architecture and protocol support.
- MCP is treated as a versioned protocol surface, not a complete security architecture. The deployed specification, SDK, extensions, authorization model, servers, tools, and schemas must be recorded and governed.
- SOC and similar assurance reports are supporting third-party evidence, not proof that the deployed agent system's controls operate effectively.

## Microsoft 365 Copilot sample curation corrections

- The report is explicitly identified as synthetic framework illustration, not actual client work, assurance, attestation, certification, legal advice, or evidence about a real organization or tenant.
- Core Microsoft 365 Copilot capabilities were distinguished from separately enabled web, external-agent, connector, and Copilot Studio paths; processing, contractual, identity, logging, and control boundaries must be assessed against the deployed configuration.
- Agentic applicability is capability-based. Additional controls apply when tools, triggers, state, autonomy, delegated authority, workload identities, inter-agent communication, or external actions are present.
- Product capability and documentation are not treated as evidence that a control is implemented or effective. Licensing, configuration, event coverage, evidence completeness, and operating effectiveness require validation.
- Product-specific assertions and source references were checked against current official Microsoft documentation as of 2026-08-19 and must be revalidated when the example is tailored.

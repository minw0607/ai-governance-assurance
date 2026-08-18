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
version: "0.3.0"
last_reviewed: 2026-08-18
---

# Source Register and Migration Decisions

The library was curated from locally supplied source documents. The original binaries are intentionally not published in the repository; they remain local inputs for provenance and future review. Detailed section-level traceability is maintained in the [Source-to-Library Coverage Map](source-coverage-map.md).

| Source artifact | Primary use | Migration decision |
|---|---|---|
| GenAI Policies - Example.docx | Governance, policy, roles, data, change | Decomposed into a comprehensive framework, operating model, lifecycle, inventory and control standards, plus modular policies; outdated regulatory assertions corrected |
| GenAI Vendor Assessment Framework.docx | Vendor tiers, domains, questionnaire, scoring | Split into framework, questionnaire, and scoring guide |
| GenAI Testing Procedures v2.docx | Enterprise testing dimensions and procedures | Decomposed into independent testing methodologies |
| GenAI Testing Comprehensive Guide v2.docx | Test formats, automation, query taxonomy | Consolidated into use-case-driven test design; brittle product instructions excluded |
| GenAI Audit Checklist v3.xlsx | Control objectives, evidence, walkthroughs | Curated into control objectives, stage gates, inventory requirements, and examination/lifecycle checklists |
| GenAI MRM Survey with Heatmap v2.xlsx | Readiness questions and weighted scoring | Migrated into readiness checklist and scoring guide; SR 11-7 framing updated |
| SaaS Testing Automation UseCase Design.docx | SaaS automation and test design | Reused for modality and test-design principles; product UI details deferred |
| Guide Automation Engineer.docx | Product-specific automation execution | Deferred from core library because selectors, interfaces, and authentication flows are implementation-specific and time-sensitive |

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

---
schema_version: "1.0"
artifact_id: REF-SRC-001
title: Initial Source Register and Migration Decisions
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
version: "0.1.0"
last_reviewed: 2026-08-17
---

# Initial Source Register and Migration Decisions

The first library release was curated from locally supplied source documents. The original binaries are intentionally not published in the repository; they remain local inputs for provenance and future review.

| Source artifact | Primary use | Migration decision |
|---|---|---|
| GenAI Policies - Example.docx | Governance, policy, roles, data, change | Decomposed into modular policies; outdated regulatory assertions corrected |
| GenAI Vendor Assessment Framework.docx | Vendor tiers, domains, questionnaire, scoring | Split into framework, questionnaire, and scoring guide |
| GenAI Testing Procedures v2.docx | Enterprise testing dimensions and procedures | Decomposed into independent testing methodologies |
| GenAI Testing Comprehensive Guide v2.docx | Test formats, automation, query taxonomy | Consolidated into use-case-driven test design; brittle product instructions excluded |
| GenAI Audit Checklist v3.xlsx | Control objectives, evidence, walkthroughs | Curated into examination and lifecycle checklists |
| GenAI MRM Survey with Heatmap v2.xlsx | Readiness questions and weighted scoring | Migrated into readiness checklist and scoring guide; SR 11-7 framing updated |
| SaaS Testing Automation UseCase Design.docx | SaaS automation and test design | Reused for modality and test-design principles; product UI details deferred |
| Guide Automation Engineer.docx | Product-specific automation execution | Deferred from core library because selectors, interfaces, and authentication flows are implementation-specific and time-sensitive |

## Material updates during migration

- SR 26-2 replaced SR 11-7 in April 2026 and explicitly excludes generative and agentic AI.
- OWASP's 2026 LLM Top 10 replaced the 2025 list in August 2026.
- EU AI Act dates were updated for the AI Omnibus that entered into force in July 2026.
- NIST AI RMF 1.0 is identified as under revision; NIST AI 600-1 remains the GenAI companion profile.

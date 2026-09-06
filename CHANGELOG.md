# Changelog

All notable library-level changes are recorded here. Individual artifacts retain independent versions in their metadata.

## [Unreleased]

### Changed

- Provenance framing corrected throughout: the library is the author's own original work, and `SRC-*` labels are an editorial trace to earlier working drafts rather than a record of external sources. Removed the statement that the library was curated from unpublished drafts held locally, along with the related language in the coverage map, contributing guide, and metadata standard.
- Emoji added to root README section headings, with explicit HTML anchors for the two badge targets so heading links do not depend on emoji slug behaviour.

- Restored the standard project disclaimer used across the author's other repositories, replacing the variant introduced in 0.3.0.

- The pre-deployment and production-readiness checklists share five control topics. The distinction between them — validated design versus production-configuration evidence — was real but undocumented, so the two read as duplicative. Each now states the relationship explicitly, and the one genuinely identical item pair (recovery and kill-switch testing) is differentiated by the evidence each gate demands.

## [0.3.0] - 2026-08-23

### Added

- Root README "Start here" section routing by question rather than by folder, with an explicit note disambiguating the four meanings the word "readiness" carries in and around this library (governance, assurance, release, adoption).
- Readiness model in the assessments catalog: the three senses of "AI readiness" (adoption, governance, assurance), which artifact serves each, and adoption readiness declared explicitly out of scope.
- Readiness-to-approval coupling in the readiness scoring guide: enterprise readiness band sets a ceiling on the risk tier approvable at gate G1, with category scores governing over the weighted total, and the mapping labelled a configurable starting point rather than a standard.
- Control coverage matrix: a generated reverse index from every control objective to the checklists, scenarios, templates, and mappings that evidence it, with an explicit coverage-gap list.
- Scenario libraries for functional correctness, factuality, security red teaming, safety and alignment, bias and fairness, privacy and data leakage, integration and workflow, and regression testing — each with stable scenario identifiers, acceptance criteria, and control-objective references.
- OWASP Top 10 for Agentic Applications (`ASI01`–`ASI10`) mapping, paired with the existing LLM Top 10 mapping as the actor layer to its model layer.
- ISO/IEC 42001 mapping covering clauses 4–10 and Annex A control groups A.2–A.10, with an explicit statement of the AIMS machinery the library does not supply.
- `scripts/build-coverage-matrix.py` to generate the coverage matrix, with a `--check` mode for CI.
- Front matter for the data-security, agentic-AI, policy, and templates catalog pages so their advertised versions are validatable.
- Related-artifact footers on leaf documents that previously had no outbound internal links.

### Changed

- The use-case assessment is now identified as the intake instrument for stage gate G1, with reciprocal links from G1, the acceptable-use policy, and the risk-tiering framework, so intake is specified once rather than described in four places.
- Root README "how to use the library" now starts at enterprise readiness rather than assuming it.
- Control objective identifiers are now referenced throughout the library: checklist sections, scenario entries, template fields, and every framework mapping. Checklists also name the lifecycle stage gate they serve.
- Crosswalk rebuilt around library control objectives and extended with an ISO/IEC 42001 column.
- NIST AI RMF mapping extended from four functions to category level.
- OWASP LLM mapping gained a control-objective column and now defers agentic coverage to the dedicated `ASI` mapping.
- `scripts/validate-library.py` rewritten: YAML front matter is parsed with a real parser and validated against `schema/metadata.schema.json`, control references are checked against their definitions, the root README catalog is reconciled against artifact metadata, the artifact-count badge is verified, code fences are excluded from link checking, and `last_reviewed` staleness is reported.
- Source provenance is recorded by opaque `SRC-*` label only; no source filename appears in the repository, and the disclaimer now describes provenance accurately rather than claiming public-source-only derivation.

### Fixed

- README catalog showed stale versions for the vendor questionnaire and the Copilot example, and advertised versions for four catalog pages that carried no metadata.
- README artifact-count badge was wrong (`53` against an actual 61 at the time).


### Added

- A GitHub-native, wholly synthetic Microsoft 365 Copilot audit assessment report demonstrating application of the governance framework, data-security standard, agentic profile, control objectives, scenario library, and findings template; no source-document binary is published.
- Agentic AI Governance and Assurance Profile covering the full agent-system boundary, autonomy, delegated authority, assurance, and evidence.
- A2A, MCP, and Multi-Agent Control Standard covering identity, authorization, protocol/version governance, context, delegation, action/state integrity, and resilience.
- Agentic AI scenario library, audit-readiness checklist, and audit workpaper template.
- Integrated AI Data Security & Governance Framework covering lifecycle, ownership, control domains, evidence, metrics, and assurance.
- AI data lifecycle and classification-to-use standards.
- Dedicated RAG, vector, connector, agent-memory, and tool-data security requirements.
- Training and evaluation data governance requirements for provenance, rights, quality, representativeness, contamination, segregation, and reproducibility.

### Changed

- Re-authored the Microsoft 365 Copilot sample as a native Markdown report with current product boundaries, capability-based agentic applicability, delegated authority, web and connector paths, audit evidence, public-release suitability, and explicit no-client-work/no-sponsorship disclosures.
- Added a cross-library technology and capability overlay catalog to make agentic-AI applicability visible without changing the purpose-first taxonomy.
- Expanded risk tiering, inventory, control objectives, use-case/vendor assessment, testing, glossary, mappings, and provenance for agentic systems.
- Curated the agentic AI auditing source draft while keeping organization-specific context and source identifiers out of the public library.
- Added data security and governance to the root taxonomy and governance catalogs.
- Reconciled the new standards to the supplied policies, audit checklist, MRM survey, vendor framework, and testing procedure.
- Corrected source examples that presented fixed retention periods, cryptographic settings, or incomplete provider conditions as universal requirements.

## [0.2.0] - 2026-08-17

### Added

- Repository taxonomy diagram and classification dimensions in the root catalog.
- Detailed roles, governance forums, decision rights, segregation-of-duties, and escalation model.
- Eight-gate lifecycle procedure with entry, evidence, decision, and exit requirements.
- AI inventory minimum data standard covering system, model, retrieval, agent, data, approval, monitoring, and retirement fields.
- Enterprise AI control framework with control objectives, evidence expectations, and assurance procedures.
- Section-level source-to-library coverage map for the supplied DOCX and XLSX materials.

### Changed

- Expanded the AI Governance Framework from a high-level lifecycle outline into a comprehensive operating and assurance model.
- Deepened source traceability and clarified which volatile product instructions and legacy legal assertions were deferred or superseded.

## [0.1.0] - 2026-08-17

### Added

- Initial purpose-first library taxonomy.
- Metadata standard and automated validation.
- Curated governance, assessment, testing, checklist, template, mapping, and reference artifacts.
- Current mapping notes for NIST AI RMF, SR 26-2, the EU AI Act, and OWASP GenAI guidance.

### Changed

- Replaced legacy SR 11-7 assertions with the current SR 26-2 scope and explicit GenAI/agentic-AI caveat.
- Updated OWASP mapping to the 2026 Top 10 for LLM Applications.
- Updated EU AI Act dates to reflect the AI Omnibus timeline in force in July 2026.

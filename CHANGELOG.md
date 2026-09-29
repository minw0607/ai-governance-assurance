# Changelog

All notable library-level changes are recorded here. Individual artifacts retain independent versions in their metadata.

## [Unreleased]

### Added

- Information barriers as a first-class control: a mandatory restriction that overrides an otherwise-valid grant, distinguished from ordinary access control by being imposed rather than granted, applying retroactively to content already held in derived stores, and constraining cross-compartment aggregation and summarization rather than only document return. Covered in the RAG/vector/agent standard (§4.4), `DATA-02`, the minimum test suite, privacy scenario `PRS-09`, the data-security framework's segregation rule, and two glossary entries.
- Security metadata mapping as a required architecture record: for each source attribute that constrains access — ACLs, compartment restrictions, barrier indicators, classification, deletion status, preservation status — the field carrying it downstream and the component enforcing it. An attribute with no carrier is not enforced downstream whatever the source system does; an attribute carried but never evaluated is not enforced either.
- Evidence-elicitation guidance extending the existing design/implementation/operating/outcome ladder: a named mechanism is an assertion rather than an outcome, probes are made one issue at a time, controls need paired allowed and denied results from the same run, revocation is tested separately from never-granted, and the effectiveness level the evidence actually supports is recorded.
- Two-key approval for governed data assets: the AI approval does not substitute for the asset owner's approval, which must name the permitted data and actions rather than the agent alone, with recertification on change of purpose, owner, or scope. Wired through `AGT-01`, the RACI, a segregation-of-duties rule, and the G2 and G5 gates.

- Shared-service change management throughout the governance chain: a service used by more than one team or business unit now has an explicit consumer register, an inherited risk tier, a split of responsibility between platform owner and consuming business owner, and a named pre-upgrade sequence — enumerate, classify, assess, notify, test, aggregate, approve, sequence, recover, monitor.
- Control objective `OPS-05` — Shared-service change and consumer impact, with evidence and assurance procedure, wired through the stage gates, risk-tiering framework, change policy, both change checklists, and the regression scenario library.
- Shared-service tier inheritance in the risk-tiering framework: for change classification, testing depth, and approval authority, a shared service inherits the highest tier among its registered consuming use cases, and an unaffordable inherited tier is resolved by separating the consumer rather than re-tiering it downward.
- Partial-failure decision rule for shared-service upgrades: a failure against any consumer's pre-agreed criteria blocks the upgrade for that consumer, a higher-tier failure is never offset by lower-tier passes, and version divergence between consumers is recorded as separate configurations to monitor and test.
- Requirements for changes that cannot be rolled back — provider deprecation and end-of-life — covering when the change record opens, how the internal cutover date is derived from the provider deadline, the fallback that replaces rollback, and the dated disposition of consumers that cannot pass in time.
- "Upgrading a shared service" section in the pre-deployment checklist, as the G4 revalidation for an upgrade rather than a second release gate, plus a root README routing row for it.
- Regression scenarios `RGS-09`–`RGS-12`: shared-service upgrade across consuming teams, partial failure and version divergence, platform and infrastructure change, and forced deprecation with migration rehearsal.
- Shared-services and non-reversible-change sections in the regression testing guide, including how to split a golden suite between a platform-owned core and consumer-owned acceptance sets.
- Inventory fields for consuming use cases and inherited tier, with a rule that a shared service may not be marked approved on an incomplete consumer register.
- RACI rows for approving a shared-service change and accepting one for a single consuming use case, and a segregation rule barring a platform owner from accepting a change on a consuming business owner's behalf.
- Vendor questionnaire coverage of committed advance-notice periods, prior-version availability during a test window, customer ability to defer or stage a change, infrastructure changes made without a version change, and post-migration rollback support.

### Changed

- `DATA-04` and the data lifecycle standard now treat preservation and deletion as conflicting obligations that meet in the derived stores: whether a hold extends to embeddings, indexes, caches, summaries, and agent memory is determined and recorded in advance rather than settled by whichever process runs first; in-scope derivatives are suppressed rather than destroyed, and hold status reconciles between source and downstream stores on the same cadence as permissions.
- `AGT-06` and the agentic control checklist now separate establishing identity from establishing the authorization basis. Correct delegated identity does not show that the downstream decision evaluates current source restrictions rather than permissions captured at ingestion — the failure mode that passes a casual review.
- Examination readiness now asks for artifacts rather than topics, with control conclusions citing an artifact and a date rather than an interview alone.
- Change scope now covers the platform and infrastructure the system runs on — runtime, SDK and API version, compute, region, images, orchestration, gateway timeout and truncation behavior, quota, identity integration, and the observability pipeline — treated as material whenever it can alter output, availability, permission resolution, or trace completeness. Previously the scope stopped at application code, leaving the substrate outside the AI change process.
- `OPS-03` extended to name platform and infrastructure changes, with an assurance procedure that reaches below the application layer.
- Stage-gate change-to-gate routing gained rows for onboarding a consumer to a shared service, platform and infrastructure change, and provider deprecation notices — the last opening at the notice rather than the deadline. G6 activities and the periodic review record now cover consumer notification, inherited tier, and version divergence.
- Ongoing monitoring now trends quality and error measures per consuming use case rather than only in aggregate, and tracks deprecation dates with internal cutover dates set back from each deadline.

## [0.3.0] - 2026-09-05

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

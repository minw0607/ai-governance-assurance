# Changelog

All notable library-level changes are recorded here. Individual artifacts retain independent versions in their metadata.

## [Unreleased]

### Added

- **Vendor-operated AI platforms** in the vendor assessment framework, expanding the existing one-paragraph SaaS and API section. Where the provider operates the capability, most controls in this library cannot be implemented by the customer — only verified, configured, or demanded contractually — so five questions determine whether the capability is governable at all, and a negative answer is a control limitation to record rather than a question to leave open.
- **Administrative visibility as a bound on inventory.** `GOV-05` assumes an organization can enumerate its own systems; on a provider-operated platform the inventory is bounded by what the administrative surface exposes. A console showing users and licences cannot support an inventory record, and where visibility is absent the entry is an assertion and is marked as one. Visibility must also distinguish capabilities that generate output from those that invoke tools, reach external systems, or take actions.
- **Restriction enforcement**, separating three states routinely reported as one: prohibited in policy, hidden in the interface, and technically disabled. Restrictions are confirmed by attempting use rather than by reading the setting, and what prevents re-enablement — a provider update activating features by default, an administrator acting without review, or a user-level setting — must be established. A restriction that can revert without review is a temporary control with an owner, not a control.
- **Independent containment determination**, settled during assessment rather than during an event: a table of seven containment actions, each marked independent or provider-dependent. Removing a licence is not containment, because sessions, tokens, integrations and credentials may remain usable; where the only available action is suspending the tenant, that is the containment capability and its collateral impact belongs in the decision; and where containment requires a support request, response depends on a party that may itself be involved in the event. Containment is complete when activity is verified to have stopped, not when the request is submitted.
- **Provider-held access**: support identities, service principals and connectors that can reach organizational data or administer the capability, and whether they can be revoked independently and during an incident. Access the organization cannot revoke is residual exposure, not a vendor control.
- **Assurance scope for agentic capability**: an independent report over a provider's conventional application is not assurance over its AI or agentic surface. Prompt and indirect injection, tool and connector abuse, data exposure and cross-tenant testing are requested specifically, with the remediation status of findings rather than their existence — and a gap the provider will not close does not become acceptable by being unobtainable.
- Fourteen questionnaire questions as a new section on vendor-operated platform control, covering administrative enumeration, restriction enforcement and reversion, the seven containment actions, emergency contact and response commitment, provider-held identities, log availability, retention and export, provider-side alerting, investigation dependency, agentic test evidence, and what interface deletion actually deletes.
- `DET-34` — a capability recorded as restricted becoming available, or a new provider feature appearing without review.
- A section in the AI incident response procedure on containing a capability the organization does not operate, including preserving provider-side records early because retention is set by the provider, may be shorter than the investigation, and may not survive the tenant action taken to contain.

### Changed

- `TPRM-01` now requires administrative visibility, restriction enforcement, independent containment, provider-held access and obtainable activity records to be established before approval of a provider-operated capability, with an assurance procedure that attempts use of a capability recorded as restricted. `TPRM-02` adds a named emergency contact and committed response time where containment depends on the provider, and customer access to records sufficient to investigate. `TPRM-03` verifies that restricted capabilities remain disabled after provider updates and that provider-held support access is still required and still revocable.

### Added

- **Identity and Access for AI Capabilities** (`GOV-SEC-006`). The library governed identity *inside* an AI system in detail — agent and workload identity, delegated authority, token exchange, non-human identity lifecycle — and said nothing about the interface to enterprise identity, which is where AI entitlements originate and where most AI access failures start, because the platform inherits whatever the directory already decided. Covers attribute authority, entitlement provenance, authentication and session controls, access review, boundary privileges, delegated consent, and identity monitoring for AI paths, with an explicit scope boundary: it does not assess or redesign an enterprise identity programme, and a finding belonging there is routed rather than absorbed.
- **Disabling an account is not terminating a session.** Disabling a directory account stops new authentication; it does not end sessions already established or invalidate tokens already issued, so an AI platform session or connected grant can remain usable until expiry. The library already made this point for agents — disabling a component does not revoke its identity — but never for people. Four times must now be reported separately rather than as one number: policy target, directory propagation, application-level removal, and active-session termination.
- **Entitlement provenance**, naming four patterns that each defeat approval: a license assignment treated as an access approval; an AI capability enabled for a broad pre-existing directory group, granting it by default to a population nobody assessed and which changes without any AI decision; provisioning by copying a colleague's account, which propagates that account's accumulated errors; and movers, who commonly gain new entitlements while keeping the old ones, where leavers attract attention and tooling.
- **Privileges that can change the AI security boundary** as a distinct enumeration from privileged access generally: granting consent, registering an application, granting API permissions, administering a platform or its connectors, changing a workload identity's permissions, registering a protocol server or tool, and changing conditional-access or session configuration on AI paths. Time-bound elevation preferred to standing privilege, break-glass governed explicitly, and a service level for sensitive identity requests — because where central provisioning is slow, teams build their own authorization, so the custom model is the symptom and the delay is the cause.
- **Delegated application consent** as a standing access path under the granting identity's authority that no AI approval necessarily touched, with inventory, user-consent restriction, review on the access-review cycle, and service principals, connectors and vendor-support identities in scope. Consent persists after the person who granted it leaves.
- Detections `DET-31` (new or changed consent grant), `DET-32` (workload identity reaching a resource for the first time, where scope creep becomes visible), and `DET-33` (session still usable after its account was disabled).
- Identity items in the agentic audit-readiness checklist covering tested revocation, per-capability granting mechanism, boundary privileges, consent inventory, and reviews of effective rather than assigned permissions.

### Changed

- `SEC-02` now requires AI capabilities to inherit enterprise authentication, session and conditional-access controls or carry a recorded exception, and requires that removing access removes it including sessions and tokens already issued. Its assurance procedure disables an account to establish what actually ends, takes a transfer to test whether prior entitlements were removed as well as new ones added, and traces each capability's granting mechanism for access conferred with no approval record.

### Added

- Synthetic content against a human control, as scenario `SRS-11` and a threat-set entry in the threat-modeling method: a control whose last line is a person judging whether what they were shown is genuine can be defeated with no weakness in the model, the prompt, or the tools. `HUM-01` and `AGT-02` now require the gate to rest on an authenticated channel and independently verifiable facts, and any control relying on human detection of generated content to be recorded as a residual exposure rather than a mitigation. The threat-modeling method gains a companion to "the model is not a control": human judgement of authenticity is not one either.
- Human-oversight monitoring section in the ongoing monitoring checklist, and a five-category measure taxonomy in the monitoring plan template — performance, risk and compliance, model behavior, operational, human oversight — so a gap shows as an empty category rather than an absent line. `OPS-01` now names human-oversight indicators in the monitored set, which it previously omitted, and requires escalation, override, abstention, complaint and appeal measures to carry sources, thresholds and responses rather than be read at a meeting. A reviewer population that never overrides and never escalates is recorded as a finding.
- Glossary entry for *generated explanation*.

### Changed

- `HUM-02` now requires a model-generated explanation to be presented as generated content rather than as an account of how the system reached its result, with the basis of each explanation established — retrieved sources, recorded policy decisions and execution facts, or the model's own narration — and a generated rationale not relied upon as evidence of reasoning in notices, reviewer displays, appeal responses, or control records. The library already measured whether generated rationale anchors a reviewer; it had stated only that hidden chain-of-thought is not *required*, never that a generated explanation is not *proof*.

### Changed

- Root README "Start here" table restructured into six lifecycle stages — getting oriented, intake and approval, design and build, test and release, operate and change and respond, prove and comply — so a reader navigates by where they are rather than scanning eighteen ungrouped rows. All rows retained; none added or removed. Security questions are distributed across the stages at which they arise rather than grouped, because AI security is an overlay across the library rather than a stage of it.
- Each "Start here" stage carries an icon (🔭 🚦 🏗️ 🚀 ⚙️ 🧾), chosen to stay distinct from the section-header icons used elsewhere in the README.
- `CONTRIBUTING.md` records how to extend the table: add to the stage where the question arises rather than where the artifact sits, phrase the row as the reader's question rather than the artifact's title, and route through an overlay once a stage grows past roughly five rows instead of listing the library.

## [0.4.0] - 2026-11-01

### Added

- **AI Control Operating Model** (`GOV-OPS-002`), covering the question the library had no artifact class for: how the control set is operated across a growing portfolio without the effort growing with it. Tiering for depth allocation, inherited and local controls, attaching to existing enterprise processes rather than running a parallel one, producing evidence rather than collecting it, an activity-based operating rhythm, programme metrics, and the sequence for standing the model up on one system before templating it.
- **Inherited and local controls** as a named distinction. A control implemented once in a shared platform is inherited by every use case built on it; a control specific to one system is local. Each use case records the split with the providing component, because nothing is inherited by assumption and "we assumed the platform handles that" is otherwise discovered during an incident rather than before one. A local control built twice is a platform control that has not been built yet. Glossary entry distinguishes an *inherited control* from an *inherited tier*, which are unrelated.
- **Control ownership principles** in roles and decision rights: exactly one accountable role per control and never a committee — a committee can approve a control but cannot own one; the owner is a role rather than a person; inherited and local accountability split; a data owner for every source; a human sponsor for every non-human identity, with joiner-mover-leaver treatment; an internal owner for vendor-provided AI, because the provider secures the model while the organization owns what it reaches; ownership moving in the register the same day a role holder changes; and exceptions carrying an owner and an expiry. Paired with six observable signs that ownership is not working, written as conditions to search for rather than wait for.
- **Programme metrics** distinct from gate-performance and decision-effectiveness measures, including the ratio of controls inherited from the platform rather than rebuilt per use case — which should climb, since a flat ratio across a growing portfolio means each project is re-solving solved problems — non-human identities with no human sponsor at a target of zero, time to revoke access after a role change, and controls recorded as inherited but not evidenced at the platform.
- **Stage ownership table** in the RAG, vector, and agent standard: for each pipeline stage, the decision it forces, the typical accountable owner, and the recurring failure that settles there when the stage is unowned.
- Decision-rights rows for maintaining the control library, building and operating platform-level inherited controls, sponsoring a non-human identity, producing pre-release evidence, re-testing after material change, and owning a vendor-provided capability internally.

### Changed

- `GOV-04` now requires exactly one accountable role per control, with inherited controls recorded as such and evidenced at the platform; its assurance procedure selects inherited controls to confirm platform evidence and use-case scope, and searches for controls with no owner, several owners, a committee as owner, or a register owner who no longer holds the role.

- **AI security overlay** (`governance/ai-security/`), following the pattern the agentic-AI catalog already established: security is a capability overlay across the library rather than a separate artifact class. The overlay routes by security question, maps the twenty `SEC`/`DATA`/`AGT` objectives of forty-four, places security at each lifecycle gate, and states what it deliberately does not provide — product configuration, a general enterprise security programme, and threat intelligence.
- **AI Threat Modeling Method** (`GOV-SEC-002`), filling the library's largest security gap: `SEC-01` and gate G2 required a threat model and nothing said how to produce one. Scopes to a workflow rather than a platform, traces the transaction, marks the seven recurring AI trust boundaries, asks one question at each, and routes findings by evidence state — implemented, planned, or absent — into tests or exceptions. A threat model that produces no tests is unfinished, and a generic threat list is not a threat model.
- **AI Security Detection Catalog** (`GOV-SEC-003`): thirty detections across authorization, untrusted content, action and approval integrity, identity, supply chain, resources, and evidence integrity — each with signal, response, and objective. Recording an event is not monitoring it: a detection without a named responder and a response path is a dashboard.
- **AI Security Incident Response** (`GOV-SEC-004`), stating what differs from a conventional incident — disabling a component does not stop dispatched work, reverting a release does not undo completed actions, affected content has already propagated to indexes and caches, the trace is often the only record of what happened, and the actor may be the model acting on instructions nobody reviewed. Preserve before containing, since containment destroys AI evidence more readily than conventional evidence.
- **Model and AI Supply Chain Security Standard** (`GOV-SEC-005`), extending `SEC-04` to the artifacts an AI system consumes but does not build: base models, weights, adapters, tokenizers, embedding models, datasets, prompts, protocol components, frameworks, and evaluation harnesses — including a compromised judge model, which approves everything else. Treats deserialization of model artifacts as code execution unless the format forbids it, and governs an adapter as a distinct artifact because alignment properties do not survive modification automatically.
- **AI Development Environment Standard** (`GOV-ENV-001`) and control objective **`GOV-07` — Contained experimentation**. The library previously required environment separation in one line at G3 and used "sandbox" only for tool-execution control. Adds the containment contract across identity, data, egress, inbound paths, actions, isolation, reversibility, resource limits, observability and lifetime; teardown behavior on completion, failure, timeout and abandonment; experiment conduct including kill criteria set before starting; and governed promotion, because prompts, evaluation sets, indexes, adapters and conclusions each carry contamination out. Experimentation is distinguished from piloting: the boundary is use, not infrastructure, so an environment can be perfectly isolated and still host production use.

- Identity fallback and attribution requirements in the A2A/MCP standard, `AGT-06`, the agentic checklists, and scenario `AGS-15`: where delegated user identity cannot be used the transaction fails closed unless an approved exception bounds the substituting identity to the initiating user's reach; a denied authorization is never retried under another identity; the initiating human stays reconstructable in the downstream system's own records rather than only in the calling application's logs; and audience or issuer validation that is switched off is an exception with a rationale, compensating control, owner, and expiry. Fallback behavior is documented per integration, because undocumented divergence means the enterprise answer to "does it fail closed?" is unknown rather than yes.
- "Rollback is not termination" in the A2A/MCP standard, with supporting coverage in `AGT-03`, `RGS-08`, `AGS-14`, `AGS-16`, and both agentic checklists: reverting a deployment replaces what starts next and does not stop dispatched, queued, scheduled, or child-agent work; disabling a component does not revoke its identity or suspend its triggers; containment must be demonstrated at component rather than platform scope, exercised on a running task, with a named authority.
- Workflow selection criteria and an end-to-end transaction trace record in the agentic audit workpaper: selected workflows must differ in technical pattern rather than name, be implemented enough to walk through, and include at least one consequential path — and one workflow traced completely beats three traced partially. The trace grid captures identity, credential type, authorization decision and basis, data exchanged, tool invoked, external destination, persistence, human checkpoint, and correlation reference per step.
- Scenario `AGS-15` (identity fallback and downstream attribution) and `AGS-16` (containment scope and in-flight termination).
- Non-human identity lifecycle requirements in `SEC-02` and the audit-readiness checklist: a named owner, approved purpose, effective permissions, review date, and retirement path for each, with explicit search for identities shared across unrelated agents, long-lived static credentials, and credentials still valid after the agent they served was retired.
- Glossary entry for *confused deputy*.

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

- Root README repositioned toward AI security: the subtitle and taxonomy line lead with security, a security badge links the overlay, and six "Start here" rows route security questions that previously had no entry point.
- Gate G0 now routes experimentation that cannot yet define purpose, users, or acceptance criteria to a contained environment rather than through intake or around it — the structural reason unregistered AI use appears as a discovery trigger. G3 requires separation to the containment contract; change-to-gate routing sends an experiment that acquires real users back to G1 and a promoted artifact to G2 or G3, never directly to production.
- The acceptable-use policy now prohibits real sensitive data, production credentials, or real users in an uncontained environment regardless of how the activity is labelled.
- `SEC-01`, `SEC-04`, `SEC-05`, and `OPS-02` now point to the method, standard, catalog, and procedure that implement them.
- Tool and server governance in the A2A/MCP standard now separates registration from enablement, requires access at tool and operation granularity rather than server level, treats changes to tool descriptions, names, annotations, aliases, parameter defaults, authentication, and downstream permissions as capability changes subject to review — capability can increase without the schema changing, because the description is what steers tool selection — and requires administrative change history over registration, enablement, definitions, and permissions to be reconstructable or recorded as a gap rather than presumed covered.
- `AGS-04` and the agentic checklist now test whether a restriction is enforced or merely instructed: a write attempted through a "read-only" agent, an approval requirement living in a tool permission rather than the system prompt, and alternative paths to a gated action through another tool, alias, endpoint, parameter, or retry.
- `SEC-05` and the A2A/MCP observability section now distinguish recording an event from monitoring it. Each agent security event is classified as alerting with a named responder and response path or as log-only; denials, fallbacks, and limit breaches are recorded as completely as successes; one correlation identifier spans the full chain; and telemetry must not become its own disclosure path for credentials, prompts, tool arguments, or client content.
- `SEC-06` and the A2A/MCP limits section now require limits to bind per agent or workflow with attributable usage, and runaway or recursive execution to be stopped automatically. A provider or account-level quota bounds the bill, not an individual agent, and is reached only after the behavior it was meant to stop has already run; an alert that depends on a human to act is not a limit.
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

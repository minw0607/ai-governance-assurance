---
schema_version: "1.0"
artifact_id: GOV-FWK-001
title: AI Governance Framework
artifact_class: governance
artifact_type: framework
domains:
  - ai-governance
  - enterprise-risk
  - lifecycle-management
applies_to:
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
version: "0.3.0"
last_reviewed: 2026-08-18
source_artifacts:
  - Agentic_AI_Auditing_Framework.docx
  - GenAI Policies - Example.docx
  - GenAI Audit Checklist v3.xlsx
  - GenAI MRM Survey with Heatmap v2.xlsx
  - GenAI Vendor Assessment Framework.docx
  - GenAI Testing Procedures v2.docx
---

# AI Governance Framework

## 1. Purpose and intended outcomes

This framework establishes the enterprise operating model for governing AI systems from discovery through retirement. It converts principles into decision rights, lifecycle gates, minimum controls, required evidence, escalation paths, and assurance activities.

The framework is designed to produce five outcomes:

1. **Complete visibility:** the organization knows which AI systems, use cases, models, prompts, retrieval sources, tools, agents, and vendors it relies upon.
2. **Risk-proportionate decisions:** the depth of assessment, testing, approval, monitoring, and independent challenge reflects impact and uncertainty.
3. **Controlled operation:** deterministic controls constrain data access, tool use, external actions, and failure propagation.
4. **Traceable accountability:** material decisions, system behavior, exceptions, changes, and incidents can be reconstructed.
5. **Continuous assurance:** monitoring and change triggers keep the approval basis current after deployment.

This is an enterprise control framework, not a legal conclusion. Each organization must identify applicable obligations and tailor control ownership, approval authority, evidence retention, and risk thresholds.

## 2. Scope and system boundary

The framework applies to internally developed, acquired, embedded, experimental, and production AI capabilities, including:

- traditional predictive and machine-learning models;
- foundation models and generative AI accessed through APIs or SaaS products;
- prompt templates, system instructions, guardrails, and evaluation configurations;
- retrieval-augmented generation, embeddings, indexes, rerankers, and connected repositories;
- fine-tuned, adapted, or domain-specific models and their training data;
- agents, orchestration workflows, memory stores, tool registries, and multi-agent systems;
- AI-enabled features embedded in business applications or third-party platforms; and
- AI used by risk, compliance, validation, audit, or other assurance functions.

The governed object is the **AI system and use case**, not only the underlying model. The boundary must include data, prompts, retrieval, orchestration, interfaces, human decisions, downstream actions, monitoring, and third parties.

## 3. Normative language

- **Must** denotes a minimum requirement unless an approved exception exists.
- **Should** denotes expected practice that may be tailored with documented rationale.
- **May** denotes an optional practice.
- **Material change** means a change capable of altering risk, performance, rights impact, security, data use, or the basis of approval.

## 4. Governing principles

1. **Accountable ownership:** every system and use case has named business, technical, and control owners.
2. **Risk proportionality:** assurance depth is driven by impact, data, autonomy, exposure, uncertainty, dependency, and reversibility.
3. **Lifecycle control:** approval is conditional and time-bounded; material changes and threshold breaches trigger reassessment.
4. **Evidence over assertion:** claims about safety, quality, security, or compliance require reproducible evidence.
5. **Defense in depth:** model behavior and prompts are not authorization boundaries; deterministic controls constrain access and action.
6. **Human authority:** human oversight must be meaningful, informed, timely, and able to prevent or reverse material harm.
7. **Independent challenge:** review independence and competence increase with risk and consequence.
8. **Transparency and contestability:** people receive appropriate notice, explanations, correction paths, and escalation mechanisms.
9. **Data stewardship:** data is authorized, minimized, traceable, protected, retained, and deleted according to sensitivity and purpose.
10. **Safe failure:** systems fail predictably, preserve evidence, and support containment, rollback, and recovery.

## 5. Governance architecture

### 5.1 Policy hierarchy

| Layer | Purpose | Library artifacts |
|---|---|---|
| Principles and risk appetite | Defines acceptable outcomes and prohibited exposure | This framework; acceptable-use policy; risk-tiering framework |
| Policies | States mandatory organizational rules | Data handling, model risk, third-party risk, prompt, and change policies |
| Standards and control objectives | Defines the minimum control condition | [AI control objectives](control-framework/control-objectives.md); [AI Data Security & Governance](data-security-governance/README.md) |
| Procedures and methods | Explains how assessments, testing, monitoring, and escalation are performed | Assessment and testing libraries; [lifecycle stage gates](lifecycle/stage-gates.md) |
| Evidence and records | Demonstrates design and operating effectiveness | Checklists, templates, inventories, approvals, logs, test results, and findings |

Requirements should be inherited from enterprise security, privacy, data, records, third-party, software-development, operational-risk, legal, and internal-audit frameworks. AI governance supplements those frameworks where probabilistic behavior, foundation-model dependency, retrieval, or autonomy creates additional risk.

### 5.2 Lines of accountability

| Accountability layer | Primary responsibility | Independence expectation |
|---|---|---|
| Governing body / executive management | Sets risk appetite, assigns executive accountability, and receives material risk reporting | Independent of delivery priorities |
| First line: business and technology | Owns intended use, design, implementation, controls, testing, operation, and residual risk | May not self-approve matters reserved for independent review |
| Second line: risk, compliance, privacy, security, and AI governance | Sets policy, challenges classification and evidence, monitors aggregate exposure, and approves within delegated authority | Sufficient authority and separation from delivery |
| Independent validation / assurance | Tests assumptions, outcomes, and control evidence for higher-risk systems | Separate from design and implementation; competence matched to risk |
| Third line: internal audit | Assesses governance design and operating effectiveness | Does not replace first-line ownership or second-line oversight |

Smaller organizations may combine roles, but must document conflicts, compensating review, escalation, and final decision authority. Detailed responsibilities and forum design are in [Roles and Decision Rights](operating-model/roles-and-decision-rights.md).

### 5.3 Governance forums

At minimum, the operating model should define:

- an executive or board-level forum for risk appetite and material exposure;
- an AI governance or risk committee for higher-risk approvals, exceptions, incidents, and portfolio oversight;
- a working-level intake and review forum for classification and control routing;
- existing security, privacy, data, third-party, architecture, and change forums that review their domains; and
- a clear route for urgent decisions when the normal cadence is too slow.

Each forum must have a charter, quorum, delegated authority, membership, cadence, escalation rules, required inputs, decision record, and action-tracking process.

## 6. Governance lifecycle and stage gates

The lifecycle operates through eight control gates. A gate may be lightweight for low-risk experimentation or formal and independently challenged for a critical use case. Gate evidence is cumulative: later approvals rely on the continued validity of earlier decisions.

| Gate | Decision | Required minimum evidence | Typical decision owner |
|---|---|---|---|
| G0 Discover and register | Is the capability visible and owned? | Inventory record, owner, status, source of discovery | AI governance / inventory steward |
| G1 Intake and classify | Is the use permitted and what risk tier applies? | Intended use, prohibited-use check, impact analysis, boundary, tier rationale | Business owner with risk challenge |
| G2 Design and assess | Can the design meet control requirements? | Architecture and data flows, privacy/threat/vendor assessments, oversight, acceptance criteria | Design authority and control functions |
| G3 Build or acquire | Was implementation controlled? | Approved components, configuration baseline, lineage, secure-development and supply-chain evidence | Technical owner |
| G4 Validate and challenge | Does evidence support the intended use and residual risk? | Test plan/results, limitations, findings, independent review where required | Independent reviewer / control function |
| G5 Approve and deploy | May the system enter production and under what conditions? | Readiness checklist, residual risk, monitoring, rollback, approvals, expiry | Delegated approval authority |
| G6 Operate, monitor, and change | Does continued use remain within the approved envelope? | Monitoring, incidents, feedback, change records, periodic review | Business and technical owners with oversight |
| G7 Retire | Has use ceased safely and completely? | Dependency analysis, access revocation, data/evidence disposition, inventory closure | Business and technical owners |

The full gate criteria, entry conditions, exit conditions, and required records are in [AI Lifecycle Stage Gates](lifecycle/stage-gates.md).

## 7. Risk classification and control calibration

Each use case must be assigned a risk tier before material development, procurement, or production use. The [AI Risk Tiering Framework](risk-tiering/ai-risk-tiering-framework.md) evaluates:

- impact on people, rights, safety, finances, legal obligations, and business operations;
- whether meaningful human review can detect and correct error;
- autonomy, tool privileges, transaction authority, and ability to communicate externally;
- sensitivity, provenance, and scale of data;
- user population, deployment scale, public exposure, and vulnerable groups;
- reversibility and detectability of harm;
- uncertainty, observability, and availability of ground truth; and
- downstream dependency and concentration risk.

Risk tiering must not become a score-only exercise. Mandatory escalation factors, prohibited uses, legal classifications, and credible worst-case outcomes override an average numerical result.

The tier determines approval authority, review independence, required assessments, test depth, release strategy, monitoring cadence, revalidation triggers, and evidence retention.

## 8. Enterprise AI inventory

The organization must maintain a centralized inventory covering all lifecycle states, including proposed, experimental, approved, suspended, retired, and rejected uses. The inventory must reconcile to actual deployments, vendor applications, access logs, procurement records, API gateways, cloud accounts, browser/SaaS discovery, and other shadow-AI detection sources.

The minimum record includes:

- stable system and use-case identifiers;
- business and technical ownership;
- intended users, affected parties, decisions, and prohibited uses;
- lifecycle status, risk tier, approval conditions, and expiry;
- model/provider identity and version strategy;
- prompts, retrieval, embeddings, tools, agents, memory, and downstream integrations;
- data sources, classifications, retention, residency, and provider-use terms;
- deployment modality and environments;
- human-oversight and action-authority level;
- assessment, test, monitoring, incident, exception, and change links; and
- dependencies, recovery approach, and retirement status.

Field definitions, record ownership, reconciliation checks, and completeness measures are in the [AI Inventory Minimum Data Standard](ai-inventory/minimum-data-standard.md).

## 9. Control domains

| Domain | Control intent | Illustrative evidence |
|---|---|---|
| Governance and accountability | Establish ownership, decision rights, risk appetite, and oversight | Charters, RACI, committee decisions, training, exceptions |
| Inventory and use-case management | Maintain complete visibility and approved scope | Inventory, intake record, discovery reconciliation, prohibited-use check |
| Data, privacy, and intellectual property | Authorize and protect data throughout the system | [AI data security and governance](data-security-governance/framework.md), data flows, lineage, classification, privacy assessment, deletion tests |
| Architecture and secure development | Build a controlled, resilient, and observable system | Threat model, architecture review, secure-development evidence, baseline |
| Model and system quality | Demonstrate fitness for the intended task and limits | Requirements, benchmarks, datasets, evaluation results, limitations |
| Safety, fairness, and rights impact | Identify and mitigate harmful or inequitable outcomes | Impact assessment, subgroup and safety tests, review and appeal evidence |
| Security and adversarial resilience | Prevent misuse, injection, leakage, poisoning, and unsafe output handling | Red-team results, access/tool controls, DLP tests, attack monitoring |
| Third-party and supply chain | Control provider, component, and concentration risk | Due diligence, contracts, SBOM, dependency monitoring, exit plan |
| Human oversight and transparency | Make review effective and interactions appropriately transparent | Review procedures, notices, explanations, override analysis, training |
| Agentic action and autonomy | Bound delegated authority and preserve intervention | Tool registry, permission matrix, limits, kill switch, execution trace |
| Monitoring, incidents, and resilience | Detect deterioration and contain failure | KPIs/KRIs, alerts, runbooks, exercises, recovery tests, postmortems |
| Change and configuration management | Keep the approval basis valid as components evolve | Version records, change classification, regression results, rollback |
| Records and assurance | Preserve reconstructable, reviewable evidence | Decision records, logs, evidence index, findings, remediation |

Detailed objectives, design expectations, operating-effectiveness tests, and evidence examples are in [Enterprise AI Control Objectives](control-framework/control-objectives.md).

## 10. Generative-AI control overlay

### 10.1 Prompt and instruction governance

- Version system prompts, reusable templates, policies, and evaluation configurations.
- Separate trusted instructions from untrusted content; do not rely on prompt secrecy for authorization.
- Test injection, jailbreak, prompt extraction, ambiguity, conflicting instructions, and multi-turn manipulation.
- Restrict sensitive data in prompts and log only what is necessary.

### 10.2 Retrieval and grounding

- Approve and classify retrieval sources; enforce source permissions at query time.
- Track document provenance, ingestion transformations, embedding/index versions, and deletion propagation.
- Test retrieval precision, recall, ranking, stale content, permission boundaries, and poisoning.
- Require citations or source traceability when the use case depends on factual grounding.

Implementation requirements are in the [RAG, Vector, and Agent Data Security Standard](data-security-governance/rag-vector-agent-data-security.md).

### 10.3 Output controls

- Validate structured outputs before downstream use.
- Apply context-appropriate grounding, uncertainty, refusal, content safety, and human review.
- Treat generated code, queries, commands, and documents as untrusted until validated.
- Define when the system must abstain, escalate, or revert to a deterministic process.

### 10.4 Foundation-model dependency

- Document provider terms, data use, retention, location, subprocessors, updates, and incident obligations.
- Decide whether to pin a version, accept managed updates, or use a hybrid release channel.
- Maintain regression tests and rollback alternatives for provider-driven changes.

## 11. Agentic-AI control overlay

Agentic systems require governance of delegated authority, not only output quality.

The [Agentic AI Governance and Assurance Profile](agentic-ai/governance-and-assurance-profile.md) defines the complete agent-system control and assurance model. Use the [A2A, MCP, and Multi-Agent Control Standard](agentic-ai/a2a-mcp-multi-agent-control-standard.md) when agents, tool servers, protocol clients, or delegated tasks communicate across a protocol boundary.

### 11.1 Autonomy classification

Record the highest permitted mode:

1. advisory only;
2. human-in-the-loop approval before action;
3. human-on-the-loop monitoring with intervention capability; or
4. fully autonomous execution under explicit limits and exception handling.

Higher autonomy increases required control strength and approval authority.

### 11.2 Tool and action governance

- Maintain a tool registry with owner, purpose, data access, read/write/execute scope, environment, and risk.
- Grant least privilege through separate service identities; prevent authority inheritance from untrusted content.
- Require step-up approval or dual authorization for consequential, irreversible, financial, identity, communication, or deletion actions.
- Use allowlists, limits, budgets, dry-run modes, circuit breakers, and idempotency where applicable.

### 11.3 Memory and state

- Define which facts may be stored, for whose benefit, for how long, and with what user controls.
- Apply encryption, access control, provenance, correction, retention, and deletion to memory and checkpoints.
- Prevent untrusted memory from silently changing goals, permissions, or policy.

### 11.4 Execution trace and intervention

- Capture the goal, plan state, model/provider version, inputs, retrieved context, tool calls, intermediate results, approvals, errors, outputs, and resulting actions under a correlation identifier.
- Provide kill-switch, credential revocation, queue suspension, and rollback capabilities.
- Test partial completion, duplicate execution, tool failure, poisoned observations, goal hijacking, and multi-agent conflict.

## 12. Human oversight

Human review is a control only when the reviewer:

- has authority and sufficient time to intervene;
- receives underlying evidence and limitations, not merely a confident answer;
- is trained to identify automation bias, hallucination, manipulation, and data-quality issues;
- can reject, correct, escalate, or reverse the outcome;
- is not pressured by volume or workflow design to rubber-stamp outputs; and
- has overrides and disagreements logged and analyzed.

The oversight design must state what is reviewed, at what point, by whom, using which information, against which criteria, and with what escalation. Effectiveness should be tested through exercises, sampled decisions, override analysis, and time-to-intervention metrics.

## 13. Approval and residual-risk acceptance

Production approval must identify:

- approved use, users, data, environments, models/providers, tools, and autonomy;
- risk tier and residual-risk statement;
- unresolved findings, compensating controls, and remediation dates;
- measurable acceptance criteria and monitoring thresholds;
- conditions, geographic or volume limits, and prohibited extensions;
- accountable approver and consulted control functions;
- approval date, expiry or review date, and reassessment triggers; and
- rollback, suspension, and retirement authority.

Approval is invalid if the deployed system materially differs from the reviewed configuration or if a critical prerequisite is not operating.

## 14. Monitoring and management information

Monitoring must combine system health, outcome quality, control performance, and portfolio risk.

### 14.1 System-level indicators

- task success, error taxonomy, factuality/groundedness, abstention, and user correction;
- safety, fairness, harmful-output, privacy, and security events;
- retrieval relevance, permission denials, stale sources, and citation support;
- agent success, unauthorized or failed tool calls, retries, duplicate actions, and intervention time;
- latency, availability, capacity, recovery, token use, and cost;
- drift in inputs, outputs, data, usage, and failure patterns; and
- overrides, complaints, appeals, incidents, and near misses.

### 14.2 Portfolio-level indicators

- inventory completeness and unregistered-system discoveries;
- use cases by tier, lifecycle status, business unit, provider, and autonomy;
- overdue approvals, assessments, reviews, and remediation;
- exceptions by age, cause, control domain, and tier;
- provider, model, connector, and data-source concentration;
- repeat incidents and control failures; and
- percentage of higher-risk systems with current independent review.

Each threshold must specify the action it triggers: investigation, increased sampling, change freeze, restricted use, rollback, suspension, reapproval, or executive escalation.

## 15. Incident, issue, and escalation management

AI incidents must be integrated into enterprise incident management and tagged for aggregate analysis. Scenarios should include:

- sensitive-data leakage or unauthorized retrieval;
- harmful, discriminatory, deceptive, or materially inaccurate output;
- prompt injection, compromised retrieval, unsafe output handling, or supply-chain compromise;
- unauthorized tool action, excessive agency, duplicate action, or financial loss;
- provider outage, silent model change, severe degradation, or loss of auditability; and
- failure of mandatory human review, notice, explanation, or appeal controls.

Response procedures must define severity, on-call ownership, containment authority, evidence preservation, legal/regulatory analysis, communication, recovery criteria, root-cause analysis, and post-incident improvement. Tabletop exercises should test both technical response and governance decisions.

Control deficiencies that do not meet incident criteria must enter issue management with severity, owner, due date, remediation validation, and escalation for overdue or risk-accepted items.

## 16. Change management and reassessment

### 16.1 Material changes

Examples include:

- a new model, provider, major version, fine-tuning method, or training dataset;
- new or materially changed data sources, retrieval logic, embeddings, or indexes;
- changes to prompts, policies, guardrails, or orchestration that affect behavior;
- new tools, write privileges, autonomy, memory, external communications, or transaction authority;
- expanded users, geography, scale, purpose, or affected population;
- new obligations, incidents, or evidence that invalidates prior assumptions; and
- performance, fairness, safety, or security degradation beyond approved limits.

Material changes require targeted or full reassessment, regression testing, updated documentation, and approval at the authority level appropriate to the resulting risk.

### 16.2 Non-material and emergency changes

Infrastructure patches, cosmetic changes, and bug fixes may use streamlined review only when evidence demonstrates no effect on behavior, access, data, action, or the approved control basis. The rationale must still be recorded.

Emergency procedures must define authorization, minimum checks, temporary controls, evidence, post-implementation review, and a deadline for retrospective testing and approval.

## 17. Exceptions and waivers

An exception request must identify the requirement, system, justification, alternatives, risk, affected parties, compensating controls, monitoring, owner, duration, approval authority, review date, and exit plan. It must confirm that legal obligations and non-delegable accountabilities are not being waived.

Exceptions must be time-bound, centrally registered, monitored, and escalated before expiry. Repeated exceptions should trigger root-cause analysis and possible policy or capability investment.

## 18. Evidence and records

Each system should maintain an evidence index linking:

- inventory and intake records;
- architecture, data-flow, threat, privacy, impact, and vendor assessments;
- risk-tier rationale and control applicability decisions;
- requirements, system documentation, prompts, configuration, and limitations;
- test plan, cases, datasets, raw results, findings, remediation, and independent review;
- approvals, conditions, exceptions, and risk acceptances;
- production baseline, monitoring, dashboards, reviews, and alert decisions;
- change, incident, complaint, appeal, and post-event records; and
- retirement, access revocation, data disposition, and dependency closure evidence.

Retention must follow applicable records, legal, contractual, privacy, and audit requirements. Auditability does not justify unlimited collection of sensitive prompts, outputs, traces, or test data.

## 19. Independent assurance

Assurance should address:

- **design effectiveness:** the control addresses the stated risk if performed as designed;
- **implementation:** the control exists in the deployed system and process;
- **operating effectiveness:** evidence shows consistent performance over a defined period; and
- **outcome effectiveness:** the control set keeps actual outcomes within approved limits.

Higher-risk reviews should include independent reproduction or challenge of material tests, sampling of decisions and changes, walkthroughs of live controls, and reconciliation between inventory, production, and evidence repositories.

Internal audit may use the [Examination Readiness Checklist](../checklists/examination-readiness.md) and the control objectives as a starting point, then tailor procedures to the actual risk profile.

## 20. Implementation roadmap

### Phase 1: Establish visibility and authority

- approve scope, principles, prohibited uses, and interim risk appetite;
- name executive, business, technical, and control owners;
- launch a minimum inventory and intake process;
- identify higher-risk and externally exposed systems; and
- establish escalation and emergency suspension authority.

### Phase 2: Standardize decisions and evidence

- implement tiering, stage gates, templates, and evidence indexing;
- define control applicability by tier;
- integrate vendor, privacy, security, architecture, and change reviews; and
- remediate critical and high-risk systems first.

### Phase 3: Operationalize assurance

- implement use-case-specific testing and production monitoring;
- establish independent challenge and portfolio reporting;
- exercise incident, rollback, and agent kill-switch procedures; and
- reconcile inventory to technical discovery sources.

### Phase 4: Improve and automate

- automate evidence collection, version reconciliation, and overdue-control reporting;
- calibrate thresholds using incidents, overrides, and monitoring history;
- measure control and human-oversight effectiveness; and
- retire redundant controls while preserving risk coverage.

## 21. Framework review

Review this framework at least annually and after material legal, regulatory, technology, incident, or risk-appetite changes. Confirm that taxonomy, stage gates, control objectives, approval authorities, evidence requirements, and monitoring measures remain effective across the current AI portfolio.

---
schema_version: "1.0"
artifact_id: GOV-DATA-001
title: AI Data Security & Governance Framework
artifact_class: governance
artifact_type: framework
domains:
  - data-governance
  - information-security
  - privacy
  - data-quality
  - intellectual-property
applies_to:
  - generative-ai
  - llm
  - rag
  - agentic-ai
  - machine-learning
industries:
  - cross-industry
deployment_models:
  - api
  - managed-api
  - saas
  - on-premises
  - hybrid
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
last_reviewed: 2026-08-18
source_artifacts:
  - GenAI Policies - Example.docx
  - GenAI Audit Checklist v3.xlsx
  - GenAI MRM Survey with Heatmap v2.xlsx
  - GenAI Vendor Assessment Framework.docx
  - GenAI Testing Procedures v2.docx
---

# AI Data Security & Governance Framework

## 1. Purpose

This framework defines how an organization should govern and protect data used by or produced through AI systems. It connects enterprise data governance, privacy, cybersecurity, records management, model risk, third-party risk, and AI assurance into one lifecycle.

The intended outcome is not merely protected storage. An organization should be able to demonstrate that AI data is:

- authorized for the intended use;
- traceable to accountable sources and transformations;
- suitable and sufficiently representative for the task;
- limited to what is necessary;
- protected according to sensitivity and threat exposure;
- used within legal, contractual, consent, and licensing boundaries;
- correctable, suppressible, retainable, and deletable as required; and
- continuously monitored for leakage, corruption, misuse, and drift.

## 2. Scope and system boundary

Apply this framework to data and data-derived artifacts throughout the AI value chain, including:

- prompts, system instructions, conversation state, and user-provided files;
- grounding sources, connector results, indexes, chunks, embeddings, and caches;
- pretraining, fine-tuning, alignment, evaluation, red-team, and monitoring datasets;
- labels, annotations, synthetic data, derived features, and benchmark answers;
- outputs, citations, tool parameters, tool results, and agent memory;
- telemetry, feedback, logs, traces, incident records, and human-review records;
- model weights or adapters when they may encode or expose governed data; and
- copies held by providers, subprocessors, backups, recovery systems, and downstream consumers.

The system boundary must show both **data flow** and **control flow**. Document identities, trust boundaries, providers, regions, stores, transformations, retrieval paths, tool calls, logging paths, and human decision points. A model endpoint alone is not an adequate AI system boundary.

## 3. Governing principles

### 3.1 Purpose before access

Existing access to a repository does not automatically authorize AI ingestion, retrieval, training, inference, monitoring, or secondary use. Record the intended purpose, compatible uses, prohibited uses, users, affected parties, and approval basis before processing begins.

### 3.2 Classification follows the data

Source classification, contractual restrictions, legal obligations, and access permissions must survive copying, chunking, embedding, caching, summarization, logging, export, and agent use. Derived artifacts inherit the highest applicable source restriction unless a documented process demonstrates that a different classification is justified.

### 3.3 Minimize every layer

Minimization applies separately to source ingestion, prompt/context construction, output, logging, memory, evaluation, and retention. Removing unnecessary data from a prompt does not cure unnecessary ingestion or excessive logging.

### 3.4 Deny by enforcement, not instruction alone

User training and model instructions are supporting controls. Sensitive-data boundaries must also be enforced through identity, authorization, connector policy, segmentation, DLP, filtering, tool constraints, network controls, and provider configuration.

### 3.5 Provenance is a control

For each material data asset, retain origin, owner, collection basis, rights, version, transformations, quality state, approval, consumers, and disposition. Provenance should support reconstruction of both a model or index build and a material output.

### 3.6 Privacy and security claims require evidence

Do not label data or a model “anonymous,” “de-identified,” “not retained,” “not used for training,” “region locked,” or “deleted” solely from marketing language or configuration intent. Validate the claim against contracts, architecture, configuration, tests, and operational evidence.

### 3.7 Controls scale with consequence and exposure

Control strength and independent review should reflect data sensitivity, affected population, decision consequence, autonomy, external exposure, provider dependency, reversibility, and detectability—not only model complexity.

## 4. Operating model and decision rights

| Role | Minimum accountability |
|---|---|
| Business/use-case owner | Defines purpose, necessity, approved users, consequences, and residual-risk acceptance within authority |
| AI system or model owner | Maintains system boundary, data dependencies, performance, changes, and lifecycle evidence |
| Data owner | Authorizes source use, classification, quality expectations, access rules, retention, and downstream use |
| Data steward | Maintains metadata, lineage, quality controls, issue resolution, and source-to-index reconciliation |
| Security | Defines threat model and technical control baseline; reviews architecture, identity, leakage, monitoring, and incident readiness |
| Privacy | Determines assessment needs, processing conditions, rights workflows, minimization, transfers, and privacy evidence |
| Legal/IP | Reviews rights, licenses, terms, confidentiality, regulated-use restrictions, and disputes |
| Records management | Defines authoritative retention and defensible disposition, including legal holds and restoration controls |
| Vendor owner/procurement | Maintains provider terms, subprocessors, locations, assurance evidence, changes, incidents, and exit obligations |
| Independent risk/assurance | Challenges design and tests operating and outcome effectiveness according to risk tier |

No single technical owner should unilaterally approve source rights, privacy applicability, security architecture, and residual risk for a material system. The [roles and decision-rights standard](../operating-model/roles-and-decision-rights.md) defines enterprise escalation and three-lines accountability.

## 5. AI data record

Maintain a record for each material source, dataset, corpus, index, evaluation set, and persistent memory store. At minimum, record:

1. stable identifier and descriptive name;
2. accountable owner and steward;
3. source system, provider, and collection method;
4. intended purpose and approved downstream uses;
5. data subjects or populations represented, if applicable;
6. classification, regulated-data flags, confidentiality, and contractual restrictions;
7. legal, consent, permission, or licensing basis requiring confirmation;
8. regions, providers, subprocessors, and transfer constraints;
9. lineage, transformations, filters, labels, chunking, and embedding versions;
10. quality dimensions, known gaps, representativeness, and bias limitations;
11. access model, service identities, segregation, and approved consumers;
12. retention trigger, period, legal-hold behavior, and deletion method;
13. associated model, prompt, index, agent, evaluation, and monitoring uses;
14. last review, material changes, incidents, and open exceptions; and
15. evidence location and disposition status.

This supplements the [AI inventory minimum data standard](../ai-inventory/minimum-data-standard.md); it does not create a disconnected register.

## 6. Control domains

### 6.1 Source authorization and rights

- Approve sources and explicitly block disallowed repositories, personal drives, uncontrolled internet sources, or unlicensed datasets.
- Confirm confidentiality, privacy, contract, consent, copyright, database rights, and usage restrictions relevant to the intended processing.
- Record whether data may be used for inference, retrieval, fine-tuning, evaluation, monitoring, or provider improvement; these are separate uses.
- Reassess when purpose, population, provider, model, modality, geography, or downstream use changes.

### 6.2 Classification and access

- Map enterprise classifications to AI processing patterns using the [classification and use matrix](data-classification-control-matrix.md).
- Use managed human and workload identities, least privilege, separation of duties, and periodic access review.
- Preserve source permissions at retrieval time and promptly propagate grants, revocations, and legal restrictions.
- Segregate customers, business units, environments, regions, and evaluation datasets where commingling would create unacceptable risk.

### 6.3 Data quality, integrity, and representativeness

- Define quality dimensions and thresholds based on the decision or task, not a generic completeness score.
- Test origin, accuracy, timeliness, consistency, duplication, missingness, label quality, coverage, and representativeness.
- Detect unauthorized source changes, ingestion failures, stale content, poisoned documents, and malicious annotations.
- Route threshold breaches to a named owner with documented impact analysis, remediation, and revalidation.

### 6.4 Privacy and data-subject impact

- Identify personal and sensitive data across inputs, derived data, outputs, logs, and model behavior.
- Determine when a privacy impact assessment or other jurisdiction-specific review is required.
- Document necessity, reasonable expectations, notices, rights handling, correction, objection, consent withdrawal, and automated-decision requirements as applicable.
- Treat anonymization as an evidence-based claim. Pseudonymized or masked data may remain personal or sensitive data.

### 6.5 Security architecture and leakage prevention

- Threat-model confidentiality, integrity, and availability across the AI value chain.
- Apply current organizational cryptographic and key-management standards rather than hardcoding an algorithm or protocol in this framework.
- Protect secrets and service identities in managed stores; prohibit credentials in prompts, training corpora, source code, or persistent agent memory.
- Control input, output, retrieval, tool, export, and logging paths with validation, DLP, segmentation, and monitoring appropriate to exposure.
- Test prompt injection, data exfiltration, cross-session/tenant leakage, poisoning, model extraction, and insecure downstream handling.

### 6.6 Provider and subprocessor governance

- Verify contract and configuration for data ownership, permitted use, model improvement, human review, retention, deletion, security, audit evidence, incident notice, location, subprocessors, and termination.
- Distinguish zero-retention or no-training configurations from default consumer or feedback settings.
- Validate isolation and administrative-access claims with architecture evidence and independent assurance where risk warrants.
- Reassess provider model, terms, regions, subprocessors, telemetry, and product-feature changes.

### 6.7 Retention, correction, deletion, and exit

- Base retention on purpose, legal and records requirements, investigations, contractual commitments, and minimization. Avoid universal durations.
- Map each source to downstream chunks, embeddings, indexes, caches, prompts, outputs, logs, memory, datasets, backups, and providers.
- Deletion must either remove the data or place it beyond use through a documented, time-bound, technically enforced process.
- When immediate backup deletion is infeasible, prevent deleted data from being restored into active processing and expire it through the approved backup lifecycle.
- Test provider termination and system retirement, including export, revocation, deletion attestation, residual copies, and dependency shutdown.

### 6.8 Monitoring and incident response

- Monitor unauthorized source use, label gaps, excessive access, DLP events, anomalous retrieval, data drift, quality failures, poisoning, rights failures, transfer deviations, and deletion-job failures.
- Correlate user, workload, model, index, prompt, retrieval, tool, output, and approval events without unnecessarily logging sensitive content.
- Extend incident playbooks to data leakage, poisoned corpora, compromised credentials, unlawful processing, provider exposure, and agent exfiltration.
- Preserve evidence, contain affected paths, assess downstream propagation, meet applicable notice duties, and verify remediation through regression testing.

## 7. Lifecycle control model

| Lifecycle point | Required decision | Minimum evidence |
|---|---|---|
| Intake | Is the purpose allowed and is the data necessary? | use-case record, preliminary data inventory, inherent-risk and applicability assessment |
| Design | Can the architecture preserve restrictions and meet rights, security, quality, and residency needs? | data-flow/control-flow diagrams, threat model, privacy review, classification mapping, provider review |
| Acquire/prepare | Are sources authorized, fit, and reproducible? | source approvals, rights records, lineage, quality profile, transformation code/configuration |
| Build/configure | Are training, retrieval, prompting, logging, and memory controls implemented? | access/configuration evidence, dataset/index manifests, secrets and environment controls |
| Validate | Do controls and outcomes work under representative and adversarial conditions? | quality, permission, leakage, deletion, poisoning, segregation, and recovery test results |
| Deploy | Is residual risk accepted and evidence complete? | approvals, exceptions, production configuration, monitoring and incident plans |
| Operate/change | Do data, permissions, providers, quality, and behavior remain within approval? | monitoring, access reviews, reconciliations, change impact, regression results, issues |
| Retire | Has use ceased and data been disposed of or retained under authority? | access revocation, export, deletion, backup/provider treatment, inventory closure |

Use the [AI lifecycle stage gates](../lifecycle/stage-gates.md) for enterprise gate ownership and escalation.

## 8. Assurance model

Assurance should distinguish four questions:

1. **Design effectiveness:** Would the control address the identified risk if performed as designed?
2. **Implementation:** Is it present across every relevant data path and store?
3. **Operating effectiveness:** Did it work consistently over the review period?
4. **Outcome effectiveness:** Did actual data use, quality, access, leakage, and disposition stay within approved limits?

Representative procedures include:

- trace an output to its source, transformations, permissions, model/index version, and approval;
- sample indexed content for approved source, classification, label, owner, and freshness;
- test allowed and denied retrieval using different users, tenants, regions, and recently changed permissions;
- inject synthetic canaries and verify prevention, detection, containment, and deletion;
- reconcile configured provider retention and training settings to contracts and observed behavior;
- execute correction/deletion through all active and recoverable stores;
- reproduce a dataset or index from versioned manifests and transformations;
- test source poisoning, malicious metadata, stale content, and integrity-monitoring alerts; and
- inspect exceptions for authority, compensating controls, expiry, and closure.

## 9. Metrics and escalation

Use denominators and risk context. Useful measures include:

- percentage of material AI data assets with current owner, purpose, classification, lineage, rights, and retention metadata;
- percentage of indexed content with valid source labels and permission mappings;
- unauthorized retrieval attempts and confirmed permission failures;
- sensitive-data detections by path, severity, false-negative review, and disposition;
- data-quality threshold breaches, time to containment, recurrence, and affected outputs;
- deletion requests completed across all stores, exceptions, and verification failures;
- provider settings or subprocessor changes awaiting assessment;
- stale, orphaned, or unapproved datasets/indexes/models; and
- critical data incidents, near misses, time to contain, and remediation aging.

Escalation thresholds must be risk-based and approved. A low aggregate error rate must not mask a critical cross-tenant disclosure, unlawful source, or failed deletion.

## 10. Tailoring and exceptions

Document which requirements apply, which do not, and why. Tailoring may strengthen or specialize the baseline; it must not silently remove a legal, contractual, or high-risk requirement. Exceptions require a defined owner, rationale, scope, compensating controls, residual risk, approval authority, expiration, monitoring, and closure evidence.

## 11. Source and standards basis

This framework curates the supplied source documents but deliberately does not carry forward their example retention periods, encryption versions, alert counts, or product-specific instructions as universal requirements.

Authoritative reference points reviewed for this version include:

- [NIST AI RMF 1.0 and AI 600-1 Generative AI Profile](https://www.nist.gov/itl/ai-risk-management-framework), including data privacy, information security, intellectual property, provenance, third-party, and decommissioning actions;
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20), including the Govern function and organization-wide cybersecurity outcomes;
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework/privacy-framework), which treats privacy risk across the data lifecycle and processing ecosystem;
- [NIST SP 800-218A](https://csrc.nist.gov/pubs/sp/800/218/a/final), an AI-specific secure development profile used with the Secure Software Development Framework;
- [EDPB Opinion 28/2024](https://www.edpb.europa.eu/documents/opinion-of-the-board-art-64/opinion-282024-on-certain-data-protection-aspects-related-to_en), which emphasizes case-specific analysis of AI-model anonymity and lawful processing;
- [EU AI Act, Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng), including data-governance, technical-record, and cybersecurity obligations where applicable; and
- [FTC Safeguards Rule](https://www.ftc.gov/legal-library/browse/rules/safeguards-rule) for financial institutions within FTC jurisdiction, including service-provider safeguarding responsibilities.

These references differ in legal force and scope. Mapping supports control design but does not establish applicability or compliance.

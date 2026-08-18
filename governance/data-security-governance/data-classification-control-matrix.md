---
schema_version: "1.0"
artifact_id: GOV-DATA-003
title: Data Classification and AI Use Control Matrix
artifact_class: governance
artifact_type: standard
domains:
  - data-classification
  - data-governance
  - privacy
  - information-security
applies_to:
  - generative-ai
  - llm
  - rag
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
  - intake
  - design
  - development
  - deployment
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-18
source_artifacts:
  - GenAI Policies - Example.docx
  - GenAI Audit Checklist v3.xlsx
  - GenAI MRM Survey with Heatmap v2.xlsx
---

# Data Classification and AI Use Control Matrix

## 1. Purpose

This matrix is a configurable baseline for deciding whether and how a data class may be used in common AI processing patterns. Replace the illustrative classification names with the organization's authoritative scheme; add sector, jurisdiction, contract, export-control, records, and purpose restrictions before adoption.

The matrix is not an automatic permission grant. A use must also have an approved purpose, owner, architecture, provider, users, retention, and risk decision.

## 2. Illustrative classification tiers

| Tier | Typical description | Examples | Default posture |
|---|---|---|---|
| Public | Approved for unrestricted public release | published reports, public websites, approved marketing | Allowed subject to source integrity, rights, and quality review |
| Internal | Non-public information with limited harm from authorized internal use | internal procedures, organization charts, general internal communications | Approved enterprise services and users only |
| Confidential | Material proprietary, personal, customer, or business information requiring controlled access | contracts, financials, customer files, employee information, source code | Case-specific approval with enforced access, minimization, and monitored data paths |
| Restricted | Highly sensitive, regulated, privileged, secret, credential, payment, health, identity, security, or similarly critical information | authentication secrets, full identifiers, regulated records, investigations, privileged advice | Prohibited by default; narrowly approved processing requires strong technical isolation and explicit accountable approval |

A record can carry multiple overlays, such as personal data, payment data, health data, export-controlled data, legal privilege, intellectual-property restrictions, or contractual confidentiality. Apply the strictest relevant condition.

## 3. Processing-pattern matrix

**Legend:** A = generally allowed under approved enterprise controls; C = conditional case-specific approval; P = prohibited by default; N/A = not applicable. “Conditional” never means approval by a developer alone.

| AI processing pattern | Public | Internal | Confidential | Restricted |
|---|:---:|:---:|:---:|:---:|
| Approved enterprise chat/SaaS with configured tenant controls | A | A | C | P/C |
| External consumer or unapproved AI service | A/C | P | P | P |
| Managed API with approved contract and architecture | A | A | C | P/C |
| On-premises or dedicated isolated deployment | A | A | C | C |
| RAG indexing and retrieval | A | A | C | C |
| Fine-tuning or continued training | A/C | C | C | P/C |
| Evaluation or red-team dataset | A | A | C | C |
| Full prompt/output content logging | A | C | C | P/C |
| Persistent user or agent memory | A | C | C | P |
| Autonomous agent tool access | A/C | C | C | P/C |
| Human feedback sent to provider | A/C | C | P/C | P |
| Public release of model output | A/C | C | C | P |

`P/C` means prohibited unless a formally defined exceptional pathway exists. If the organization does not establish such a pathway, treat it as prohibited.

## 4. Conditional-use requirements

Before approving a cell marked `C` or `P/C`, document and implement the applicable controls below.

### Purpose, rights, and privacy

- approved necessity and purpose, including secondary-use boundaries;
- source-owner authorization and confirmed confidentiality, contract, consent, copyright, license, and database-use conditions;
- privacy or impact assessment and lawful-processing analysis where applicable;
- notice, choice, rights, correction, and deletion handling;
- approved data locations, transfer mechanism, subprocessors, and residency configuration; and
- retention and disposition rule for every created copy and derived artifact.

### Architecture and provider

- approved service tier, endpoint, tenant, region, and feature settings;
- terms covering provider training/improvement, retention, human review, abuse monitoring, deletion, subprocessors, incident notice, and administrative access;
- isolation between customers, users, environments, and workloads;
- current organizational encryption, key-management, network, endpoint, and backup controls; and
- exit capability, including export, revocation, and deletion evidence.

### Identity and data path

- SSO or managed identity, MFA where required, least privilege, and periodic access review;
- source-permission preservation for RAG and connectors;
- DLP, masking/tokenization, input/output validation, and export controls appropriate to the data;
- secret detection and prohibition on credentials in prompts, corpora, outputs, or memory;
- logging that supports traceability without unnecessary sensitive content; and
- monitoring and incident response for unauthorized access, leakage, and anomalous use.

### Assurance

- permitted and denied access tests, including cross-user/tenant and recent permission changes;
- sensitive-data leakage and extraction tests using synthetic canaries;
- deletion and retention tests across indexes, caches, logs, memory, providers, and backups;
- provider configuration and contract reconciliation; and
- documented residual risk, approver, conditions, review date, and exception expiry.

## 5. AI-specific decision rules

### Prompts and context

- Do not paste complete records when a narrow field, reference, token, or summary is sufficient.
- Treat system prompts and hidden instructions as confidential configuration; do not place secrets in them.
- Redaction must be validated for the actual languages, formats, files, images, and identifiers in scope.
- A masked identifier may remain linkable; classify based on realistic re-identification and harm, not appearance.

### RAG and connectors

- Retrieval authorization must reflect current source permissions and purpose, not only index membership.
- Classifications and restrictions must remain attached to chunks and embeddings.
- Block unapproved repositories, personal locations, external shares, deleted sources, and stale permission replicas.
- Confidential or restricted corpora require poisoning controls and inspection of hidden or embedded instructions.

### Training and fine-tuning

- Approval for inference does not imply approval for training or fine-tuning.
- Confirm provenance, collection basis, rights, representativeness, quality, contamination, and removal/correction strategy.
- Assess whether personal or confidential information could be memorized or extracted from the resulting artifact.
- Apply stricter segregation and release controls to weights, adapters, checkpoints, and training logs where source data may be encoded.

### Logs, telemetry, and feedback

- Define necessary event fields before enabling content capture.
- Provider abuse monitoring, human review, feedback, and support diagnostics may create distinct data uses requiring review.
- Protect traces and retrieved content as production data, not ordinary operational metadata.
- Retention must be tied to purpose and authoritative schedules rather than convenience.

### Agent memory and tools

- Default memory to task- or session-bound unless persistence is justified and visible to the user.
- Store source, owner, sensitivity, purpose, timestamp, and expiry with persistent memory.
- Never persist authentication secrets, one-time codes, prohibited identifiers, or unrelated third-party information.
- Bind tool access to the acting identity, allowed records and fields, approved actions, and transaction limits.

## 6. Approval record

Each conditional decision should record:

| Field | Required content |
|---|---|
| Use case and processing pattern | What the AI system will do with the data |
| Data classes and overlays | Enterprise class plus personal, regulated, contractual, IP, geographic, or privilege flags |
| Sources and destinations | Systems, providers, stores, regions, tools, logs, and downstream recipients |
| Purpose and necessity | Why each data element and processing step is needed |
| Controls | Technical, contractual, procedural, and monitoring controls |
| Tests | Evidence that classification, permission, leakage, isolation, retention, and deletion controls work |
| Decision | Approver, conditions, residual risk, validity period, and reassessment triggers |

## 7. Important corrections from the source baseline

- A data-processing agreement plus encryption is not by itself sufficient approval for external AI processing.
- A fixed cryptographic algorithm or protocol version should live in the organization's maintained security standard, not a timeless AI matrix.
- Retention periods such as 90 days, three years, or seven years are examples, not universal AI requirements.
- “No training” must cover the relevant data categories and service features and be supported by both terms and configuration.
- Pseudonymization, masking, tokenization, and embeddings do not automatically remove privacy, confidentiality, or rights obligations.
- Data-subject deletion is conditional on applicable law and exceptions; the technical workflow should nevertheless support correction, suppression, deletion, and evidence across derived stores.

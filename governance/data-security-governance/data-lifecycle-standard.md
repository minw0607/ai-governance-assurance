---
schema_version: "1.0"
artifact_id: GOV-DATA-002
title: AI Data Lifecycle Standard
artifact_class: governance
artifact_type: standard
domains:
  - data-governance
  - privacy
  - information-security
  - records-management
applies_to:
  - generative-ai
  - llm
  - rag
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
version: "0.1.0"
last_reviewed: 2026-08-18
source_artifacts:
  - GenAI Policies - Example.docx
  - GenAI Audit Checklist v3.xlsx
  - GenAI MRM Survey with Heatmap v2.xlsx
---

# AI Data Lifecycle Standard

## 1. Objective

This standard defines minimum control activities and evidence for data from source approval through disposition. It should be applied to source data and to derived artifacts such as chunks, embeddings, labels, prompts, outputs, logs, memory, adapters, and evaluation results.

## 2. Lifecycle and lineage model

Document applicable stages and stores using the following chain:

```text
source or collection
  → transfer and landing
  → validation and classification
  → preparation and transformation
  → training / fine-tuning / indexing / configuration
  → prompt and context assembly
  → inference, retrieval, and tool use
  → output, action, and human review
  → logging, feedback, evaluation, and monitoring
  → retention, correction, deletion, archive, or retirement
```

Lineage must identify splits, joins, filters, copies, providers, regions, transformations, and derived assets. A diagram without stable asset identifiers and version evidence is not sufficient lineage for a material use case.

## 3. Stage requirements

### 3.1 Propose and authorize

Before acquiring or connecting data:

- define the business purpose, AI processing pattern, expected benefit, affected users or parties, and prohibited secondary uses;
- identify the source owner, intended data population, sensitive or regulated elements, and expected destinations;
- determine whether privacy, legal/IP, records, security, vendor, or sector review is required;
- assess whether a less data-intensive or non-AI alternative can meet the purpose; and
- record the approval, conditions, expiration or review trigger, and accountable owner.

**Evidence:** intake, purpose and necessity assessment, preliminary data-flow diagram, applicability review, source-owner approval, decision record.

### 3.2 Acquire, collect, or connect

- Use approved acquisition channels and authenticated connectors.
- Record source, collection method, date/time, terms, version, checksum or equivalent integrity reference, and chain of custody when material.
- Enforce source allowlists and explicit blocks; do not rely on a developer remembering which folders are out of scope.
- Separate development, test, evaluation, and production ingestion paths.
- Quarantine untrusted external data until validation and scanning are complete.

**Evidence:** connector configuration, source register, acquisition log, contract/license record, integrity record, quarantine result.

### 3.3 Classify and validate

- Apply enterprise classification and AI-specific use restrictions before downstream processing.
- Detect personal, sensitive, confidential, secret, credential, malware, and prohibited content as appropriate.
- Validate schema, format, completeness, duplication, corruption, and expected population.
- Identify whether data is structured, semi-structured, unstructured, multimodal, synthetic, labeled, or generated.
- Route ambiguous or conflicting classifications to the data owner; do not silently downgrade.

**Evidence:** classification result, scanning report, exception record, quality profile, owner resolution.

### 3.4 Prepare and transform

- Version transformation code, prompts, rules, filters, normalization, labeling, chunking, and sampling.
- Preserve a reproducible manifest of included and excluded records or source versions when feasible.
- Mask, tokenize, generalize, aggregate, or synthesize where this meets the approved purpose and risk model.
- Prevent transformation logs, temporary files, notebooks, and caches from becoming uncontrolled sensitive-data copies.
- Validate that de-identification reduces risk; do not assume masking or pseudonymization makes data anonymous.

**Evidence:** transformation version, manifest, quality comparison, privacy test, temporary-data disposition record.

### 3.5 Build, index, or configure

- Restrict builders, pipelines, service identities, and environments to approved data and destinations.
- Record dataset, model, embedding, index, prompt, parser, and configuration versions.
- Preserve source identifiers and permissions in chunks and index metadata.
- Scan for secrets, malware, prompt-injection content, corrupted labels, and unauthorized sources.
- Apply dataset and model-artifact access, encryption, backup, and export controls appropriate to classification.

**Evidence:** build manifest, access policy, environment configuration, scan results, dataset/model/index card, reproducibility test.

### 3.6 Prompt, context, retrieval, and tool use

- Construct the minimum context needed for the task.
- Enforce current user and workload permissions when querying source and index—not only when content was ingested.
- Treat retrieved documents, websites, messages, and tool results as untrusted instructions unless explicitly trusted by design.
- Prevent credentials, hidden system instructions, restricted metadata, and unrelated user/session content from entering prompts or outputs.
- Bind agent tools to approved identities, fields, records, actions, and transaction limits.

**Evidence:** context-building logic, permission tests, DLP rules, tool schema/allowlist, denied-event logs, synthetic leakage tests.

### 3.7 Output, action, and downstream use

- Classify outputs based on their content, source restrictions, intended audience, and decision consequence.
- Validate citations, transformations, and sensitive-data disclosure before material use.
- Apply output encoding, content-type validation, DLP, and downstream authorization before execution or export.
- Record when AI output materially influences a decision, communication, transaction, or record.
- Prevent feedback, copy/paste, exports, and user ratings from bypassing data-use restrictions.

**Evidence:** output controls, review/approval record, source references, action log, blocked or redacted event evidence.

### 3.8 Log, evaluate, and monitor

- Define necessary event fields before enabling full-content logging.
- Prefer identifiers, hashes, classifications, decision outcomes, and redacted excerpts where full content is unnecessary.
- Restrict access to prompts, outputs, retrieved content, traces, and feedback separately from general operational logs.
- Keep evaluation datasets independent from production traffic unless reuse is explicitly approved.
- Monitor quality, drift, unusual retrieval, sensitive-data events, access anomalies, poisoning indicators, and unexpected secondary use.

**Evidence:** log schema, redaction rules, access review, retention configuration, evaluation-data approval, monitoring thresholds and tickets.

### 3.9 Correct, restrict, delete, or retain

- Maintain a map from source records to derived artifacts and active consumers.
- Support correction or suppression where inaccurate source or derived data affects ongoing use.
- Execute approved deletion across active stores, indexes, caches, logs, memory, evaluation sets, provider copies, and downstream exports as applicable.
- Rebuild or incrementally update indexes when tombstoning alone could still permit retrieval.
- Respect legal holds and authoritative records schedules; document why a requested deletion cannot be completed immediately.
- For backups, prevent deleted data from returning to active use and expire it under the approved backup lifecycle.

**Evidence:** request and authority, affected-asset list, job logs, re-index result, post-deletion query test, provider confirmation, exception/hold record.

### 3.10 Retire and exit

- Stop ingestion, inference, retrieval, tool access, monitoring, and provider processing.
- Revoke human and machine identities, credentials, connectors, exports, and scheduled jobs.
- Export required records in a usable format and validate completeness.
- Dispose of or retain datasets, prompts, outputs, logs, indexes, memory, model artifacts, and backups under documented authority.
- Reconcile the AI and data inventories and close dependencies, exceptions, incidents, and residual vendor obligations.

**Evidence:** retirement plan, access revocation, export validation, disposition record, provider attestation, inventory closure approval.

## 4. Retention schedule requirements

Do not use a single default period for all AI artifacts. The schedule should identify:

| Artifact | Retention trigger | Decision factors |
|---|---|---|
| Source data | collection, source-system status, or record event | original purpose, authoritative system, contract, legal/records duties |
| Prompts and outputs | interaction, decision, or case closure | necessity, decision evidence, investigation, privacy exposure |
| Retrieved context | interaction or cache creation | reconstructability, source retention, leakage exposure |
| Embeddings and indexes | build, source deletion, or supersession | source restrictions, refresh cycle, deletion propagation |
| Training/fine-tuning data | build/release or model retirement | reproducibility, rights, personal data, model reconstruction needs |
| Evaluation and red-team data | test execution or supersession | benchmark integrity, evidence, synthetic/real data, contamination risk |
| Logs and traces | event or case closure | security investigation, audit evidence, data content, cost and access risk |
| Agent memory/state | task, session, case, or user relationship | user expectation, correction, continuity, consequence, secrets exposure |
| Model artifacts | release, replacement, or retirement | reproducibility, vulnerability, data encoding, contractual restrictions |

Each schedule entry must name the owner, repository, period or event rule, legal-hold behavior, deletion method, backup treatment, and verification evidence. Example periods in source documents are tailoring inputs only.

## 5. Change triggers

Reassess lifecycle controls when any of the following changes materially:

- purpose, user group, affected population, geography, or decision consequence;
- data source, classification, volume, schema, collection basis, license, or owner;
- model, provider, embedding model, parser, chunking, index, prompt, tool, or memory design;
- provider terms, training/retention settings, subprocessors, region, or administrative access;
- access model, connector scope, transfer path, storage, logging, or retention;
- observed quality, leakage, poisoning, rights failure, or incident pattern; or
- applicable law, regulatory guidance, contract, or enterprise policy.

Route changes through the [change-management policy](../policies/change-management.md) and perform risk-based regression testing.

## 6. Minimum assurance tests

At deployment and on a risk-based cadence:

1. trace representative source records into transformations, prompts/retrieval, outputs, logs, and downstream stores;
2. compare approved sources with actual connected and indexed sources;
3. test recently granted and revoked permissions;
4. test cross-user, cross-session, cross-tenant, and cross-region boundaries;
5. inspect samples for classification, sensitive data, rights, quality, and freshness;
6. execute synthetic sensitive-data detection and exfiltration scenarios;
7. execute correction and deletion end to end;
8. reproduce a dataset or index from recorded versions;
9. confirm provider configurations and terms remain aligned; and
10. verify alerts create owned, timely, and closed actions.

Use synthetic or specially authorized test data. Never introduce real secrets or unapproved personal data merely to test the controls.

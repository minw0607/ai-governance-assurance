---
schema_version: "1.0"
artifact_id: GOV-DATA-004
title: RAG, Vector, and Agent Data Security Standard
artifact_class: governance
artifact_type: standard
domains:
  - rag-security
  - vector-security
  - agentic-ai
  - data-leakage
  - information-security
applies_to:
  - rag
  - llm
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
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
  - GenAI Testing Procedures v2.docx
  - GenAI Vendor Assessment Framework.docx
---

# RAG, Vector, and Agent Data Security Standard

## 1. Objective

This standard protects enterprise data when AI systems ingest sources, create chunks and embeddings, retrieve context, maintain memory, or call tools. It addresses a central AI risk: an application can respect model-level controls while still leaking, corrupting, or misusing data through retrieval and execution paths.

## 2. Required architecture record

Document:

- authoritative sources, owners, classifications, and approved connector scopes;
- ingestion services, parsers, OCR, transformations, chunking, metadata, and embedding models;
- vector, keyword, graph, cache, and source-document stores;
- namespaces, tenants, regions, environments, encryption/key boundaries, and backup paths;
- human and service identities at ingestion, retrieval, administration, and tool execution;
- permission synchronization and revocation timing;
- query rewriting, routing, retrieval, reranking, context assembly, and citation logic;
- model/provider endpoints, prompts, filters, logs, traces, feedback, and support paths;
- agent goals, memory, tools, action approval, transaction limits, and emergency stop; and
- deletion, re-indexing, disaster recovery, provider exit, and retirement flows.

Identify every point where untrusted content can influence instructions or where an identity boundary can be lost.

## 3. Source onboarding and ingestion

### 3.1 Source approval

- Maintain approved and blocked source lists with owner, purpose, scope, classification, rights, region, and review date.
- Do not broadly connect a repository when only a defined collection is necessary.
- Review externally shared folders, inherited permissions, personal drives, stale groups, and public links before ingestion.
- Separate source approval for search/retrieval from approval for training, evaluation, monitoring, or provider improvement.

### 3.2 Integrity and poisoning controls

- Authenticate source and connector; record version, timestamps, and integrity metadata appropriate to the risk.
- Quarantine and scan files, archives, markup, images, scripts, links, metadata, and hidden content.
- Detect prompt-like instructions, invisible text, encoded content, unexpected language, malicious links, and anomalous bulk changes.
- Restrict who can publish to trusted corpora; use review or dual control for high-impact knowledge sources.
- Alert on unusual source, author, permission, volume, deletion, or content-pattern changes.
- Maintain rollback to a known-good corpus or index.

### 3.3 Parsing and chunking

- Version parsers, OCR, cleaning, chunking, overlap, metadata extraction, and embedding configuration.
- Test tables, headers, footnotes, images, hidden fields, comments, tracked changes, and access labels; parsing can change meaning or expose hidden content.
- Preserve stable source, record, section, version, classification, owner, permission, and deletion identifiers in chunk metadata.
- Prevent chunks from combining content with incompatible permissions or classifications.
- Verify that generated summaries or enrichment do not become untraceable authoritative sources.

## 4. Identity and authorization

### 4.1 End-user authorization

- Bind retrieval to the authenticated user and approved purpose.
- Apply source authorization at query time or through an equally current, demonstrably equivalent enforcement mechanism.
- Test direct retrieval, semantic retrieval, metadata filters, query rewriting, citations, previews, exports, and cached answers.
- Do not let the model decide whether the user is entitled to data.

### 4.2 Workload and administrative access

- Use distinct managed identities for ingestion, retrieval, administration, evaluation, and agents.
- Scope service identities to required sources, namespaces, operations, fields, and environments.
- Protect vector-database, model-provider, connector, and tool credentials in approved secret stores.
- Restrict and monitor administrative search, bulk export, index snapshots, debugging, and support access.
- Revoke terminated, transferred, expired, and compromised identities promptly.

### 4.3 Permission synchronization

- Define authoritative source, synchronization mechanism, maximum acceptable delay, failure behavior, and owner.
- Fail closed or isolate affected content when permission synchronization is stale or unsuccessful for sensitive corpora.
- Propagate grants, revocations, document deletion, legal holds, external-share changes, and group changes.
- Reconcile indexed permission metadata to source permissions on a risk-based cadence.

## 5. Vector and index security

- Segregate tenants, customers, regions, environments, and materially different classifications using architecture appropriate to the threat model.
- Prevent unscoped similarity search, cross-namespace joins, metadata-filter bypass, and unauthorized index enumeration.
- Treat embeddings as governed derived data. They may reveal source membership or attributes and do not automatically constitute anonymous data.
- Restrict index snapshots, backups, exports, debug endpoints, and analytics replicas.
- Maintain index manifest, source coverage, embedding model/version, build time, freshness state, permissions state, and checksum or equivalent build reference.
- Detect orphaned chunks, missing labels, duplicate records, stale sources, excessive retrieval, and index/source count differences.
- Test restore and failover to ensure obsolete or deleted content does not reappear.

## 6. Retrieval and context construction

- Retrieve the minimum number and fields of sources needed for the task.
- Filter by current identity, purpose, tenant, classification, region, and lifecycle status before content reaches the model.
- Treat retrieved text as data, not trusted instructions; delimit it and maintain instruction hierarchy.
- Limit context size and prevent unrelated records, hidden metadata, secrets, system prompts, and internal identifiers from leaking into output.
- Preserve citations and stable source IDs so reviewers can verify grounding and authorization.
- Test conflicting, stale, malicious, deleted, mislabeled, and low-quality sources.
- Define fallback behavior when permission, integrity, freshness, or retrieval services fail; unsafe broadening is not an acceptable fallback.

## 7. Prompt injection and data exfiltration defenses

Use layered controls:

1. source trust and ingestion controls;
2. instruction/data separation and context labeling;
3. identity and retrieval authorization outside the model;
4. input, retrieved-content, output, and tool-parameter validation;
5. least-privilege tools and allowed operations;
6. DLP and sensitive-data detection across prompt, context, output, export, and logs;
7. transaction limits, approval gates, sandboxing, and egress controls; and
8. monitoring, incident containment, and regression testing.

Model refusal alone is not sufficient protection against indirect prompt injection or exfiltration.

## 8. Agent memory and state

### 8.1 Memory design

- Define memory purpose, scope, source, classification, visibility, write authority, retention, correction, and deletion.
- Prefer task/session memory; persistent memory requires explicit justification and user/owner expectations.
- Keep memory isolated by user, tenant, role, case, environment, and region as applicable.
- Record provenance and confidence; distinguish user-provided facts, system observations, inferences, and generated summaries.
- Expire or revalidate time-sensitive facts and permissions.

### 8.2 Memory safety

- Prevent credentials, one-time codes, authentication material, prohibited identifiers, and unrelated third-party data from persistent storage.
- Validate writes and defend against malicious or misleading memory insertion.
- Require higher assurance before memory can change permissions, approval state, financial details, identity attributes, or other consequential facts.
- Make correction and deletion effective across active memory, caches, replicas, logs, and restored state.
- Test cross-user, stale, conflicting, poisoned, and deleted-memory scenarios.

## 9. Agent tool and action data

- Bind each tool call to an accountable human or workload identity.
- Allow only approved tools, operations, resources, fields, destinations, and transaction limits.
- Validate parameters and returned data; do not pass unrestricted model-generated queries, code, paths, recipients, or URLs into privileged tools.
- Prevent the agent from escalating its own permissions, changing guardrails, retrieving credentials, or authorizing its own exception.
- Require approval or dual control for irreversible, financial, identity, external communication, deletion, administrative, or high-impact actions.
- Protect tool results from unrelated reuse in prompts, memory, logs, or subsequent agents.
- Log purpose, identity, input parameters at an appropriate level, approval, result, error, and downstream state change.

## 10. Logging and monitoring

Record enough to reconstruct material behavior while minimizing sensitive content:

- user/workload identity and tenant;
- request, session, model, prompt, index, embedding, source, and tool versions;
- source identifiers and authorization decision, not full retrieved text unless necessary and approved;
- policy, DLP, injection, validation, and approval decisions;
- model output classification and action outcome;
- memory reads/writes and state checkpoints; and
- exceptions, failures, overrides, and emergency stops.

Monitor for:

- denied and cross-boundary retrieval;
- unusual query breadth, export volume, or sequential enumeration;
- DLP detections and sensitive-output patterns;
- ingestion anomalies, source poisoning, label gaps, and permission drift;
- unexplained changes in retrieval sources or citation patterns;
- agent attempts to expand scope, bypass approval, call unapproved tools, or send data externally; and
- deletion, synchronization, backup, and restore failures.

## 11. Deletion and source change

When a source is corrected, restricted, deleted, or loses authorization:

1. identify all chunks, embeddings, metadata, keyword/graph entries, caches, generated summaries, evaluation copies, memory, logs, exports, and provider copies;
2. stop new retrieval and use;
3. delete, tombstone, suppress, or rebuild according to the approved procedure;
4. propagate changed permissions and invalidate caches;
5. prevent restoration from reintroducing the data;
6. query for residual retrieval using representative and adversarial prompts; and
7. retain evidence of authority, execution, exceptions, and verification.

## 12. Minimum test suite

| Test area | Representative scenarios | Expected evidence |
|---|---|---|
| Source scope | approved, blocked, personal, externally shared, deleted, and newly added sources | connector enforcement and denied-event logs |
| Permissions | allowed/denied users, nested groups, recent revocation, file/folder conflict, service identity | source-to-index authorization consistency |
| Isolation | user, session, tenant, business unit, environment, and region boundaries | no unauthorized retrieval or metadata disclosure |
| Injection | hidden text, document instructions, metadata, email thread, image/OCR, malicious link | unsafe instruction ignored/contained and event detected |
| Exfiltration | synthetic canaries, broad summaries, encoding, tool/export path, multi-turn extraction | prevention or detection with no unauthorized disclosure |
| Poisoning | altered trusted source, malicious new source, label manipulation, bulk change | quarantine, alert, rollback, and impact analysis |
| Quality | stale, conflicting, low-quality, missing, and deleted sources | appropriate ranking, warning, abstention, or exclusion |
| Memory | cross-user, stale, conflicting, malicious, correction, and deletion | isolation, provenance, lifecycle enforcement |
| Tools | unauthorized record/field/action, approval bypass, replay, duplicate, recipient change | enforced scope, approval, idempotency, and trace |
| Recovery | stale backup/index restore, provider outage, permission sync failure | safe degraded mode and no reappearance of restricted data |

Use synthetic canaries and multiple test identities. The source procedure's sample counts are examples; sample design should reflect attack diversity, system exposure, risk, and statistical purpose.

## 13. Required evidence package

- architecture and data/control-flow diagrams;
- source and connector register;
- chunk/index/embedding manifest and permission model;
- identity, namespace, region, and environment configuration;
- ingestion scanning and integrity results;
- injection, permission, isolation, leakage, poisoning, deletion, and recovery test results;
- memory and tool registry with scopes and approvals;
- logging schema, monitoring thresholds, alerts, and incident playbook;
- provider terms/configuration and subprocessor evidence; and
- open findings, exceptions, owners, dates, and residual-risk approval.

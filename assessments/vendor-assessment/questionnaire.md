---
schema_version: "1.0"
artifact_id: ASSESS-VENDOR-002
title: AI Vendor Assessment Questionnaire
artifact_class: assessment
artifact_type: questionnaire
domains:
  - third-party-risk
  - due-diligence
  - evidence-management
applies_to:
  - generative-ai
  - agentic-ai
  - foundation-models
industries:
  - cross-industry
deployment_models:
  - api
  - managed-api
  - saas
lifecycle_stages:
  - procurement
  - validation
  - operation
status: draft
version: "0.2.0"
last_reviewed: 2026-08-18
source_artifacts:
  - Agentic_AI_Auditing_Framework.docx
  - GenAI Vendor Assessment Framework.docx
---

# AI Vendor Assessment Questionnaire

For each response, record the vendor answer, evidence reference, assessor conclusion, gap, owner, and due date. Mark statements that cannot be independently supported as **unverified**.

## 1. Service and supply chain

1. Identify the legal entity, service, deployment model, hosting regions, foundation models, model providers, and material subprocessors.
2. Which components are shared, tenant-specific, customer-managed, or provider-managed?
3. What data and control-plane dependencies could affect service continuity or customer isolation?
4. How are model, tool, connector, plugin, and subprocessor changes communicated?
5. What exit, portability, deletion, and transition support is available?

## 2. Governance and transparency

6. Provide system/model cards describing intended uses, limitations, evaluations, and known failure modes.
7. Describe governance and approval for model and service releases.
8. Provide recent evaluation, red-team, safety, and remediation summaries relevant to the offered version.
9. How are customer-reported model failures investigated and communicated?
10. What information is available to support independent customer testing and audit?

## 3. Architecture and customer controls

11. Provide architecture and data-flow diagrams covering prompts, context, retrieval, tools, logs, telemetry, and storage.
12. Which parameters, guardrails, policies, regions, retention options, and model versions can the customer control?
13. Can the customer pin, stage, compare, or roll back model and service versions?
14. How are system instructions, retrieved data, user input, tool output, and memory separated or labeled?
15. What deterministic controls validate output and authorize downstream actions?

## 4. Data governance and privacy

16. Is customer content used for training, fine-tuning, evaluation, abuse monitoring, or service improvement? Identify defaults and opt-outs.
17. Where are prompts, outputs, files, embeddings, logs, feedback, and backups stored and processed?
18. What retention and deletion controls exist, and how is deletion verified across derived stores?
19. How is tenant, user, workspace, and data-source isolation enforced and tested?
20. How are data-subject, legal-hold, e-discovery, residency, and cross-border requirements supported?

## 5. Security

21. Describe SSO, MFA, RBAC, service identities, API authentication, key management, and privileged access.
22. Provide current independent assurance reports and the scope/limitations of those reports.
23. Describe testing for prompt injection, data exfiltration, insecure output handling, poisoning, excessive agency, and supply-chain compromise.
24. What customer-visible logs exist for prompts, retrieval, tool calls, administrative changes, policy events, and data access?
25. Describe vulnerability disclosure, incident severity, notification timelines, investigation support, and evidence preservation.

## 6. Quality, safety, and reliability

26. Which use-case-relevant quality, factuality, safety, fairness, and robustness measures are tracked?
27. How are evaluation datasets created, governed, protected from contamination, and refreshed?
28. What are service-level objectives, rate limits, degradation behavior, and continuity mechanisms?
29. How does the provider detect and respond to regressions or harmful behavior after release?
30. Which limitations require customer controls or human review?

## 7. Agentic AI

31. List every available tool/action and its read, write, delete, transact, communicate, or execute capability.
32. How are credentials scoped, refreshed, revoked, and kept outside model-controlled content?
33. Can customers require approval for sensitive actions and inspect the exact action before execution?
34. How are planning steps, tool calls, intermediate results, memory writes, and outcomes traced?
35. What controls address loops, duplicate action, state loss, goal hijacking, malicious tool output, and multi-agent conflict?
36. How can customers immediately suspend an agent, tool, connector, or credential?
37. Identify supported A2A/MCP or other agent protocols, clients, servers, SDKs, extensions, protocol versions, schemas, and deprecation commitments.
38. How are workload identity, scopes, token audiences, delegation, downstream token exchange, message integrity, replay resistance, and revocation enforced?
39. How are child agents identified, authorized, limited in depth/duration/resources, monitored, cancelled, and prevented from inheriting excessive authority?
40. What customer-visible evidence correlates initiating identity, agent/model/configuration, context references, authorization, approval, tool calls, state changes, errors, and outcomes?

## 8. Change and lifecycle management

41. What constitutes a material change and what notice is provided?
42. Provide recent release notes, deprecation notices, rollback examples, and customer-impact assessments.
43. How are preview features separated from generally available capabilities?
44. What reassessment and re-testing does the provider perform after changes?
45. What support periods and migration paths exist for retired models or APIs?

## 9. Contract and assurance

46. Do terms provide audit, regulatory cooperation, incident notification, data-use restriction, deletion, subprocessor notice, service level, and termination rights?
47. Who owns customer prompts, outputs, fine-tuning artifacts, evaluations, and derived configurations?
48. How does the provider support transparency, recordkeeping, impact assessment, accessibility, and contestability obligations?
49. Identify all requested controls the provider cannot meet and proposed alternatives.

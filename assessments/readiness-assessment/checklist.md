---
schema_version: "1.0"
artifact_id: ASSESS-READY-001
title: AI Governance Readiness Assessment
artifact_class: assessment
artifact_type: checklist
domains:
  - governance-readiness
  - model-risk
  - operational-readiness
applies_to:
  - generative-ai
  - agentic-ai
industries:
  - financial-services
  - cross-industry
lifecycle_stages:
  - intake
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - GenAI MRM Survey with Heatmap v2.xlsx
---

# AI Governance Readiness Assessment

Rate each scored item using the [scoring guide](scoring-guide.md) and retain evidence. Inventory questions provide context but do not receive maturity scores.

## A. Inventory and scope

- How many AI systems and use cases are documented, and how many are internal, vendor-provided, embedded, experimental, or retired?
- [ ] Inventory includes models, prompts, agents, retrieval, tools, owners, versions, data, risk tier, and lifecycle status.
- [ ] Embedded AI features and shadow-AI discovery are included.

## B. Use and autonomy

- Where is AI used and which processes or decisions depend on it?
- [ ] Autonomous or semi-autonomous actions are identified and bounded.
- [ ] Human oversight is defined based on impact and reversibility.
- [ ] Kill-switch and emergency-override mechanisms exist for agentic systems.

## C. Risk classification

- [ ] A common risk taxonomy and tiering method includes data, impact, autonomy, exposure, reversibility, and external obligations.
- [ ] Tier decisions are linked to minimum approval, testing, and monitoring requirements.

## D. Data, privacy, and intellectual property

- [ ] Regulated, sensitive, confidential, and licensed data use is identified.
- [ ] Provider training/reuse, retention, and deletion terms are controlled.
- [ ] Leakage prevention, data minimization, permission boundaries, and privacy rights are tested.

## E. Performance and validation

- [ ] Use-case-specific quality, factuality, safety, robustness, and task-success measures exist.
- [ ] Edge cases, ambiguity, adversarial input, and unanswerable cases are tested.
- [ ] Validation or independent challenge is proportionate to risk.

## F. Hallucination, fairness, and harm

- [ ] Grounding, citation, uncertainty, and human-review controls address unsupported output.
- [ ] Fairness and harmful-impact evaluation is performed where people or protected interests may be affected.
- [ ] Findings are linked to remediation, release decisions, and monitoring.

## G. Explainability and auditability

- [ ] The organization can reconstruct material inputs, model/provider version, retrieved sources, tool calls, approvals, and outputs.
- [ ] Records are understandable to reviewers and retained according to applicable requirements.

## H. Third-party and vendor governance

- [ ] Vendor assessment covers changes, data use, security, quality, incidents, dependencies, and exit.
- [ ] Contracts address material AI risks and provide necessary evidence and cooperation.

## I. Governance and accountability

- [ ] A designated executive owner, governance forum, and risk appetite exist.
- [ ] First-line ownership, second-line challenge, and independent assurance responsibilities are clear.
- [ ] Prohibited uses, exceptions, and escalation paths are formally defined.

## J. AI used within assurance functions

- [ ] When AI assists risk, compliance, validation, or audit, outputs receive effective human challenge.
- [ ] Assurance teams retain accountability and can reproduce their conclusions without relying on opaque AI assertions.

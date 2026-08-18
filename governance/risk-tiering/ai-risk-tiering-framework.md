---
schema_version: "1.0"
artifact_id: GOV-RISK-001
title: AI Risk Tiering Framework
artifact_class: governance
artifact_type: framework
domains:
  - risk-tiering
  - impact-assessment
  - control-calibration
applies_to:
  - generative-ai
  - agentic-ai
  - machine-learning
industries:
  - cross-industry
lifecycle_stages:
  - intake
  - design
  - validation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - GenAI Vendor Assessment Framework.docx
  - GenAI Policies - Example.docx
---

# AI Risk Tiering Framework

## Objective

Classify AI use cases consistently so governance, testing, approval, and monitoring are proportionate to potential harm. Tiering is an informed decision, not a purely mechanical score.

## Classification dimensions

Assess each dimension using the highest credible impact under intended use and reasonably foreseeable misuse:

| Dimension | Lower-risk indicators | Higher-risk indicators |
|---|---|---|
| Decision impact | Drafting or administrative support | Credit, employment, healthcare, safety, legal, eligibility, or regulatory decisions |
| Human oversight | Output is optional and readily verified | Automation bias, ineffective review, or no meaningful intervention |
| Autonomy | No tools or external actions | Multi-step action, write access, transactions, code execution, or external communication |
| Data | Public or synthetic data | Sensitive, regulated, confidential, biometric, or large-scale personal data |
| Scale and exposure | Small internal pilot | Public-facing, enterprise-wide, high-volume, or vulnerable populations |
| Reversibility | Error is cheap and readily corrected | Irreversible, delayed, systemic, or difficult-to-detect harm |
| Model uncertainty | Bounded task with reliable ground truth | Open-ended task, emergent behavior, weak observability, or unverifiable output |
| Dependency | Isolated assistance | Embedded in critical processes or relied upon by downstream systems |

## Tiers

| Tier | Description | Illustrative uses |
|---|---|---|
| Tier 1 — Critical | Failure could cause severe legal, financial, safety, rights, or systemic harm; or the system can take consequential autonomous action | High-impact decisions, autonomous financial transactions, safety-critical control, privileged agents with irreversible actions |
| Tier 2 — High | Material decisions or sensitive operations with meaningful human oversight and containment | Decision support, customer-facing advice, production code generation, agents with bounded write access |
| Tier 3 — Moderate | Limited impact, reversible outcomes, and effective review | Internal summarization, analysis support, controlled knowledge assistants |
| Tier 4 — Low | Minimal exposure, no sensitive data, no consequential action | Isolated experimentation with synthetic/public data, low-impact drafting |

## Mandatory escalation factors

Escalate to at least Tier 2 when the system:

- affects access to essential services or protected rights;
- processes sensitive or regulated data at material scale;
- communicates externally without pre-publication review;
- generates production code or security configuration;
- uses retrieval over confidential repositories;
- can invoke tools with write, delete, transaction, identity, or communication privileges; or
- is difficult to observe, interrupt, or roll back.

Escalate to Tier 1 when credible failure could create severe or irreversible harm, or when privileged autonomy is combined with untrusted input and sensitive data.

## Minimum assurance by tier

| Requirement | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Documented use-case and impact assessment | Full | Full | Abbreviated | Basic |
| Architecture, data-flow, and threat modeling | Required | Required | Risk-based | Basic boundary review |
| Independent challenge | Independent validation | Independent review | Peer or second-line review | Owner approval |
| Adversarial and misuse testing | Comprehensive | Required | Targeted | As needed |
| Fairness and rights-impact testing | Required when relevant | Required when relevant | Risk-based | Normally not applicable |
| Production monitoring | Continuous or near-real-time for critical controls | Defined metrics and alerts | Periodic sampling | Basic incident monitoring |
| Change-triggered reassessment | Required | Required | Material changes | Scope changes |
| Approval authority | Executive/risk committee | Senior accountable owner plus risk | Business and technical owners | Designated owner |

## Decision record

Record the tier, dimension-level rationale, assumptions, unresolved questions, required controls, approval authority, date, and reassessment triggers. The tier must be reconsidered when use, users, data, autonomy, model/provider, scale, or external obligations change.

---
schema_version: "1.0"
artifact_id: GOV-POL-001
title: Acceptable Use Policy for Generative and Agentic AI
artifact_class: governance
artifact_type: policy
domains:
  - acceptable-use
  - workforce-governance
  - prohibited-use
applies_to:
  - generative-ai
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
  - intake
  - deployment
  - operation
status: draft
version: "0.2.0"
last_reviewed: 2026-10-08
source_artifacts:
  - SRC-POL-01
---

# Acceptable Use Policy for Generative and Agentic AI

## Policy objective

AI must be used only for approved purposes, with appropriate protection of people, data, systems, and organizational obligations. This policy applies to employees, contractors, and third parties using AI on behalf of the organization.

## Required conduct

Users must:

- use only approved accounts, models, agents, connectors, and tools;
- complete required training before receiving access;
- follow data-classification and handling requirements;
- verify material outputs against authoritative evidence;
- identify AI-assisted content where required by policy or law;
- retain records for regulated or consequential activities;
- report suspected harmful output, security events, data leakage, and shadow AI; and
- respect intellectual-property, confidentiality, privacy, and contractual restrictions.

Builders and owners must additionally register the use case, maintain documentation, implement required controls, test before release, monitor in production, and obtain approval before material changes.

Experimentation, evaluation, and development of AI capability must take place in an environment meeting the containment contract in the [AI Development Environment Standard](../environments/ai-development-environment-standard.md). Using real sensitive data, production credentials, or real users in an uncontained environment is prohibited regardless of how the activity is labelled; an experiment that acquires real users making real decisions has become production use and must re-enter intake (`GOV-07`).

## Prohibited uses

Unless expressly authorized by applicable law and an approved governance process, users must not:

- place sensitive credentials, regulated data, or confidential records into unapproved AI services;
- use personal AI accounts for organizational data;
- evade security, monitoring, retention, or approval controls;
- represent unverified AI output as fact, professional advice, or an official organizational decision;
- make consequential decisions solely on AI output without required human authority;
- create deceptive, discriminatory, harassing, unlawful, or rights-infringing content;
- deploy autonomous actions outside documented permissions and approval boundaries; or
- conceal material AI use from reviewers, affected functions, or required disclosures.

## Intake and approval

New uses must document the business purpose, users, affected parties, data, providers, architecture, external obligations, human oversight, failure consequences, and success measures. Record this using the [use-case assessment checklist](../../assessments/use-case-assessment/checklist.md) at [stage gate G1](../lifecycle/stage-gates.md); do not maintain a separate intake form. Approval depth follows the [risk tier](../risk-tiering/ai-risk-tiering-framework.md), subject to the ceiling set by the current [enterprise readiness band](../../assessments/readiness-assessment/scoring-guide.md#readiness-and-approval-authority).

## Violations and exceptions

Access may be suspended during investigation. Confirmed violations are handled under applicable disciplinary and incident processes. Exceptions must be time-bound, documented, supported by compensating controls, and approved by the authority associated with the requirement.

---
schema_version: "1.0"
artifact_id: GOV-POL-004
title: Third-Party AI Risk Management Policy
artifact_class: governance
artifact_type: policy
domains:
  - third-party-risk
  - supply-chain
  - procurement
applies_to:
  - generative-ai
  - agentic-ai
  - foundation-models
industries:
  - cross-industry
lifecycle_stages:
  - intake
  - procurement
  - operation
  - retirement
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - GenAI Policies - Example.docx
  - GenAI Vendor Assessment Framework.docx
---

# Third-Party AI Risk Management Policy

## Policy objective

Third-party AI services must be assessed and governed according to the risks of the organization's actual use, including dependencies on foundation-model providers, data processors, tools, plugins, connectors, and hosting platforms.

## Requirements

- Complete risk-tiered due diligence before contract or production use.
- Identify the full service and data supply chain, including material subprocessors and model providers.
- Assess model/system documentation, data practices, security, privacy, performance, safety, availability, change management, concentration risk, and exit capability.
- Obtain evidence proportionate to risk; certifications alone do not establish AI control effectiveness.
- Define contractual requirements for data use, retention, deletion, incident notification, material changes, audit rights, regulatory cooperation, service levels, subprocessor changes, intellectual property, termination, and transition.
- Validate institution-specific configurations and use cases; vendor benchmark results do not replace internal testing.
- Monitor incidents, financial and operational health, model releases, deprecations, subprocessor changes, control attestations, service performance, and risk concentration.
- Maintain an exit plan covering data export/deletion, replacement, continuity, credentials, integrations, and retained records.

Use the [Vendor Assessment Framework](../../assessments/vendor-assessment/framework.md) and document unresolved evidence gaps as risks rather than assuming absence of risk.

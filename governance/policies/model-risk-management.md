---
schema_version: "1.0"
artifact_id: GOV-POL-003
title: AI Model and System Risk Management Policy
artifact_class: governance
artifact_type: policy
domains:
  - model-risk
  - system-risk
  - validation
applies_to:
  - generative-ai
  - agentic-ai
  - machine-learning
industries:
  - financial-services
  - cross-industry
lifecycle_stages:
  - design
  - development
  - validation
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-08-17
source_artifacts:
  - GenAI Policies - Example.docx
  - GenAI_MRM_Survey_with_Heatmap_v2.xlsx
---

# AI Model and System Risk Management Policy

## Scope note

Organizations should govern AI based on risk and function, not labels alone. In financial services, determine separately whether a component meets the institution's regulatory and policy definition of a model.

The U.S. interagency [SR 26-2 guidance](../../mappings/sr-26-2.md) superseded SR 11-7 in April 2026 and explicitly states that generative AI and agentic AI models are outside its scope. Its principles may still inform internal governance, but this policy does not represent them as direct GenAI requirements.

## Policy requirements

### Inventory and scope

Maintain an inventory of models, AI systems, use cases, providers, versions, prompts, retrieval components, tools, owners, risk tiers, dependencies, validation status, and lifecycle stage. Document which model-risk, technology-risk, privacy, security, conduct, consumer-protection, and operational-risk frameworks apply.

### Development and implementation

- Define intended use, performance objectives, limitations, and prohibited reliance.
- Document data, architecture, assumptions, model/provider selection, prompt and retrieval design, tool permissions, human oversight, and fallback.
- Establish evaluation criteria before testing.
- Separate model behavior controls from deterministic application and access controls.

### Independent challenge

The degree of independence, expertise, and rigor must be commensurate with risk. Review should examine conceptual suitability, evidence quality, data and retrieval, test design, limitations, outcomes, monitoring, and implementation controls. Independence does not require a single organizational form; conflicts and decision rights must be clear.

### Monitoring

Monitor fitness for purpose, data and retrieval changes, output quality, harmful outcomes, system and provider changes, user behavior, incidents, limitations, and aggregate dependencies. Define thresholds and actions before deployment.

### Limitations and use

Users and downstream systems must receive clear boundaries on appropriate use. Material limitations require controls, overlays, restricted use, additional review, or non-deployment. Output fluency is not evidence of reliability.

### Findings and exceptions

Findings must include severity, evidence, owner, due date, interim control, and closure criteria. Residual risk acceptance is time-bound and made by an authority with accountability for the affected business risk.

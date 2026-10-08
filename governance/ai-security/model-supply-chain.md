---
schema_version: "1.0"
artifact_id: GOV-SEC-005
title: Model and AI Supply Chain Security Standard
artifact_class: governance
artifact_type: standard
domains:
  - ai-security
  - supply-chain
  - provenance
  - integrity
applies_to:
  - generative-ai
  - agentic-ai
  - machine-learning
  - llm
industries:
  - cross-industry
lifecycle_stages:
  - design
  - development
  - validation
  - deployment
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-10-08
---

# Model and AI Supply Chain Security Standard

## Purpose

`SEC-04` requires control over the software and model supply chain. Conventional application supply-chain practice covers packages and images well. It does not cover the artifacts particular to AI systems, where the library has treated model artifacts mainly as a data-sensitivity concern.

This standard states what must be controlled across the artifacts an AI system consumes but does not build.

## What is in the supply chain

| Artifact | Why it carries risk |
|---|---|
| Base model, hosted or self-hosted | Behavior, safety properties, and training data are not verifiable by inspection |
| Model weights and checkpoints | Executable or deserializable formats can carry code; integrity is not self-evident |
| Adapters, fine-tunes, LoRA layers | Modify behavior and safety properties while appearing to be small assets |
| Tokenizers and preprocessing assets | Change input interpretation; a mismatch silently degrades behavior |
| Embedding models | Changing one invalidates every existing vector; also a derived-data exposure path |
| Datasets — training, fine-tuning, evaluation | Carry rights, poisoning, contamination, and representativeness risk |
| Prompts, system policies, guardrail configurations | Behavior-defining and frequently unversioned |
| Protocol servers, tools, connectors, extensions | Grant capability and reach; definitions are prompt-visible and change independently |
| Agent frameworks, SDKs, orchestration libraries | Determine identity, authorization, and limit enforcement |
| Container images, runtimes, accelerant libraries | Conventional surface, with AI-specific dependency depth |
| Evaluation harnesses and judge models | Determine whether anything else is trusted; a compromised judge approves everything |

## Requirements

### Provenance and integrity

- Record, for every artifact above: source, publisher, version or digest, acquisition date, licence and use restrictions, owner, and the approval under which it entered the environment.
- Verify integrity on acquisition and again at deployment, by signature or attestation where the publisher provides one and by digest pinning where they do not. Where neither is available, record the artifact as unverifiable and treat it as untrusted content.
- Pin by immutable digest rather than by mutable tag or alias for anything that reaches production. A tag that moves is a change that bypassed review.
- Reject artifacts from sources that cannot be reconciled to an approved publisher, including convenience mirrors and community re-uploads of otherwise approved models.

### Weight and artifact format risk

- Prefer formats that cannot carry executable content. Treat deserialization of model artifacts as code execution unless the format demonstrably forbids it.
- Load untrusted or newly acquired artifacts only in an isolated environment, per the [AI development environment standard](../environments/ai-development-environment-standard.md), before promotion.
- Scan artifacts for embedded payloads where tooling exists, and record that scanning is a partial control — absence of a detection is not evidence of integrity.

### Adapters and derived models

- Govern an adapter, fine-tune, or merged model as a distinct artifact with its own provenance, approval, and evaluation — not as a configuration of its base.
- Re-run safety, security, and quality evaluation after fine-tuning or merging. Alignment properties of the base model do not survive modification automatically.
- Record the lineage: base model and version, training or tuning data, method, operator, and date. An adapter of unknown lineage cannot be assessed.

### Hosted models and providers

- Establish what the provider commits to for version identity, notice periods, prior-version availability, and change without a version change. See the [vendor questionnaire](../../assessments/vendor-assessment/questionnaire.md) and the [third-party risk policy](../policies/third-party-risk.md).
- Treat a provider-side change as a supply-chain event subject to `OPS-03` and, where the service is shared, `OPS-05`.
- Record the complete inference path: endpoint, region, routing, gateway, and any intermediary that can observe or alter prompts and responses.

### Protocol components and tools

Server, tool, and schema governance is specified in the [A2A, MCP, and Multi-Agent Control Standard](../agentic-ai/a2a-mcp-multi-agent-control-standard.md). Two supply-chain points reinforce it:

- A tool definition is a supply-chain artifact. Its description, name, annotations, and parameter defaults steer model behavior and can increase capability without a schema change.
- A third-party protocol component is a dependency with reach, not a configuration. Assess its publisher, integrity, support status, and change practice as you would any deployed dependency.

### Datasets

Dataset provenance, rights, quality, contamination, and segregation are specified in the [training and evaluation data governance standard](../data-security-governance/training-evaluation-data-governance.md). Treat evaluation datasets as integrity-critical: a contaminated or leaked evaluation set invalidates every release decision made against it.

### Inventory and change

- Maintain the artifact inventory as part of the [AI inventory](../ai-inventory/minimum-data-standard.md), including the agent-to-model and agent-to-tool mapping, so the blast radius of any one artifact change is answerable.
- Monitor for publisher advisories, deprecations, withdrawn versions, and licence changes affecting artifacts in use.
- Revalidate after any material artifact change, with security regression as well as functional comparison (`QUAL-06`, `RGS-01`, `RGS-05`).

### Exit and continuity

- Record, for each externally sourced artifact, what happens if it becomes unavailable, withdrawn, or untrusted: an alternative, a retained approved copy where licensing permits, a degraded mode, or planned disablement.
- Retain the approved version of artifacts you can lawfully retain. An artifact that exists only at a publisher's discretion is a continuity dependency, not an asset.

## Minimum evidence

- artifact inventory with source, digest, version, owner, and approval;
- signature or attestation verification results, or recorded unverifiability;
- isolation evidence for artifacts loaded before promotion;
- lineage records for adapters, fine-tunes, and merged models;
- post-change evaluation results including security regression;
- agent-to-model and agent-to-tool mapping; and
- advisory monitoring records and exit position per artifact.

## Related artifacts

- [AI Security Overlay](README.md)
- [Enterprise AI Control Objectives](../control-framework/control-objectives.md) — `SEC-04`, `TPRM-01`, `OPS-03`
- [A2A, MCP, and Multi-Agent Control Standard](../agentic-ai/a2a-mcp-multi-agent-control-standard.md)
- [Training and Evaluation Data Governance Standard](../data-security-governance/training-evaluation-data-governance.md)
- [AI Development Environment Standard](../environments/ai-development-environment-standard.md)
- [Third-Party Risk Policy](../policies/third-party-risk.md)

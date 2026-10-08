---
schema_version: "1.0"
artifact_id: GOV-ENV-001
title: AI Development Environment Standard
artifact_class: governance
artifact_type: standard
domains:
  - ai-security
  - environment-segregation
  - experimentation
  - containment
applies_to:
  - generative-ai
  - agentic-ai
  - rag
  - llm
  - machine-learning
industries:
  - cross-industry
lifecycle_stages:
  - intake
  - design
  - development
  - validation
status: draft
version: "0.1.0"
last_reviewed: 2026-10-08
---

# AI Development Environment Standard

## Purpose

The library required environment separation in a single line at gate G3 and treated "sandbox" only as a tool-execution control. It had no standard for the lab, development, and ephemeral environments where AI capability is actually built and tried — which is where most AI work begins and where unapproved use originates.

This standard covers two things the library previously left to judgement: what an environment must guarantee before experimental work may happen in it (`GOV-07`), and what may cross back out.

> **Two senses of "sandbox."** Elsewhere in this library *sandboxing* means constraining a single tool or code execution at runtime (`SEC-03`, and the [A2A/MCP standard](../agentic-ai/a2a-mcp-multi-agent-control-standard.md)). Here it means an isolated environment in which people and agents work. Both are used; they are not the same control.

## Why experimentation needs its own gate

Gate G1 requires intended purpose, users, affected parties, and foreseeable misuse; gate G2 requires measurable acceptance criteria. An experiment exists precisely because those are not yet known. Without a sanctioned route, experimentation either cannot clear intake honestly or is waved through as "lightweight" with no boundary defined at all — which is why unregistered AI use appears as a discovery trigger at G0 rather than as an anomaly.

The remedy is not to exempt experimentation from governance. It is to make containment the price of not yet knowing: wide latitude inside a boundary that has been paid for in advance by removing what makes mistakes expensive.

## The containment contract

An environment may be used for AI experimentation only where all of the following hold. Record each as configuration, not intent.

| Dimension | Requirement |
|---|---|
| **Identity** | Separate tenant, subscription, or project, with separate service principals. No production credentials, including read-only ones — read access to production is an exfiltration path, not a convenience. |
| **Data** | Synthetic or properly de-identified by default. Real sensitive data requires separate explicit approval, and grants the environment the production controls for that dataset rather than exempting it. |
| **Egress** | Default-deny outbound, allowlisting only what the work requires. An environment described as having no egress must be verified against observed network flows, not against its design. |
| **Inbound** | No path from the environment into production systems: no write access, no shared queues, no shared schedulers, no callbacks. |
| **Actions** | Mock or simulated tools first; real tools read-only; write actions only against a seeded disposable copy. |
| **Isolation** | One person's or agent's environment cannot reach another's, the platform's secrets, or the hosting environment. State this as a tested property. |
| **Reversibility** | Rebuilt from code and disposable. An environment that cannot be destroyed and recreated has become undocumented production. |
| **Resource limits** | Hard caps on spend, tokens, runtime, concurrency, and recursion, set at the account or platform level rather than in application configuration — the level the bug cannot bypass. |
| **Observability** | Logging equal to production or better. Learning is the deliverable, and an unlogged experiment produces neither evidence nor conclusions. |
| **Lifetime** | An expiry date, with destruction as the default action on expiry. |

## Teardown

Teardown is where sandbox claims most often fail, because the failure is invisible when things go well.

Define and test what happens to files, credentials, running processes, in-memory state, and network connections on each of:

- **Completion** — the expected path.
- **Failure** — a crashed, errored, or killed workload. An environment that survives its own failure is an environment that persists indefinitely.
- **Timeout** — a workload that neither completes nor fails.
- **Abandonment** — a person who stops using it without closing it.

Requirements:

- Credentials issued to an ephemeral environment expire with it, and are not reusable after teardown.
- Storage is destroyed rather than detached, and is not shared between environments or reused without wiping.
- Teardown is verified, not assumed. Confirm by inspection that the environment, its storage, its identities, and its running work are gone.
- Teardown of an environment is distinct from reverting a deployment and from stopping work in flight. Where agents run in these environments, all three are separate operations — see [rollback is not termination](../agentic-ai/a2a-mcp-multi-agent-control-standard.md).

## Conducting the experiment

- **Write the hypothesis and the kill criteria before starting.** An experiment with no failure condition runs indefinitely and always "shows promise". Stopping must be a respectable outcome.
- **Fix the measure before seeing output**, as the scenario libraries require of any test.
- **Probe failure deliberately.** A demonstration of the intended path is an anecdote. Budget more effort for adversarial and edge cases than for the demonstration.
- **Log every run** with model, version, parameters, prompt version, and configuration. Reproducibility is the output.
- **Timebox, then decide explicitly**: proceed to intake, iterate against a new hypothesis, or stop.
- **Agents start low.** Begin at propose-only autonomy even where the target is bounded autonomy, and progress mock tools → real read-only tools → writes against a disposable copy. Never grant a lab agent an irreversible action; "it is only the sandbox" combined with one misconfigured credential is how lab agents reach production.

## What may leave

Promotion out of an experimental environment is a governed event, not a shortcut. Nothing is production-ready by virtue of having worked in a lab.

Each of these can carry contamination out:

| Artifact | What it can carry |
|---|---|
| Prompts and system policies | Real records used in tuning, embedded verbatim |
| Evaluation sets | Contamination — a set the model has seen is no longer a valid benchmark |
| Indexes and embeddings | Content ingested without permission filtering |
| Fine-tunes and adapters | Training data, and altered safety properties |
| Conclusions | Validity that does not transfer — a result on synthetic data may not hold on the real distribution |
| Configuration and infrastructure code | Permissive settings adopted for convenience in the lab |

Requirements:

- Route promotion through gate G2 or G3 according to what is being promoted; it does not enter production directly.
- Establish the provenance of any dataset, index, or prompt built in the lab before it is used in production, including whether permission filtering applied.
- Re-derive any evaluation set that has been exposed to the model under test.
- State the environments a conclusion was reached in, and whether it was reproduced on a production-intended configuration.
- Treat artifacts acquired or loaded in the lab under the [model and AI supply chain standard](../ai-security/model-supply-chain.md) before promotion.

## Experimentation is not piloting

The moment real users make real decisions from the output, or real counterparties are affected, the work has left the experimental environment: it is production with a small population. That requires the full gate path, participant notice, an opt-out, human review, and an incident route. Naming it a pilot does not change it.

The boundary is use, not infrastructure. An environment can be perfectly isolated and still be hosting production use.

## Minimum evidence

- environment register with owner, purpose, expiry, and the contract above recorded as configuration;
- isolation test results, including environment-to-environment, environment-to-secrets, and environment-to-host;
- egress policy with observed-flow verification;
- teardown test results for completion, failure, and timeout;
- data approval where real data is used, with the controls that accompany it;
- experiment records: hypothesis, kill criteria, runs with configuration, and the recorded decision; and
- promotion records with provenance and the gate the artifact re-entered at.

## Related artifacts

- [AI Security Overlay](../ai-security/README.md)
- [AI Lifecycle Stage Gates](../lifecycle/stage-gates.md) — G0, G2, G3
- [Enterprise AI Control Objectives](../control-framework/control-objectives.md) — `GOV-07`, `SEC-03`, `SEC-06`
- [Model and AI Supply Chain Security Standard](../ai-security/model-supply-chain.md)
- [Training and Evaluation Data Governance Standard](../data-security-governance/training-evaluation-data-governance.md)
- [AI Acceptable Use Policy](../policies/acceptable-use.md)

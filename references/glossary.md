---
schema_version: "1.0"
artifact_id: REF-GLOSS-001
title: AI Governance and Assurance Glossary
artifact_class: reference
artifact_type: glossary
domains:
  - terminology
applies_to:
  - generative-ai
  - agentic-ai
  - machine-learning
industries:
  - cross-industry
status: draft
version: "0.7.0"
last_reviewed: 2026-11-17
---

# AI Governance and Assurance Glossary

**Agentic AI:** An AI-enabled system that plans or selects actions and uses tools, memory, or other agents to pursue goals with some degree of autonomy.

**Agent-to-agent (A2A) communication:** A structured interaction in which one agent or agent-enabled component sends tasks, context, status, or results to another. A2A does not by itself establish identity, authority, or trusted context.

**Agent identity:** A stable workload identity used to authenticate and authorize an agent or agent-enabled component. It is distinct from an agent's human-readable name or model-generated persona.

**Agent system:** The complete operational system containing models, prompts, orchestration, data, retrieval, memory, tools, identities, approvals, agents, protocols, downstream applications, monitoring, and human roles.

**AI system:** A machine-based system that infers from inputs how to generate outputs such as predictions, content, recommendations, or decisions that can influence environments.

**Assurance:** Evidence-based confidence that governance, risk management, and controls are suitable and operating as intended.

**Compartment:** The unit a barrier separates — a matter, case, deal, engagement, client, or investigation — against which access and derivation are restricted.

**Delegated authority:** The limited permission for an agent or workload to act on behalf of a person, service, or business purpose. Delegation should identify scope, duration, resources, destinations, and revocation.

**Confused deputy:** A failure in which a component with broader authority performs an action on behalf of a requester who lacks that authority, because the component substitutes its own permissions for the requester's. In agent systems it typically arises where a workload or service identity acts for a user without constraining the action to what that user could do.

**Control plane:** The layer that governs AI systems rather than performing their work — registry and ownership, identity and scoped access, policy enforcement, observability, routing and cost, lifecycle state, and containment. The term is borrowed from networking and container orchestration. Its governance value is that controls implemented there are *inherited controls* for every system built on it; its governance risk is that it reaches the whole estate at once, and that a system which bypasses it appears governed because the registry lists it.

**Data plane:** The layer where the work happens — models answering, retrieval executing, tools being called, actions taken. This library's recurring requirement that authorization be enforced outside the model is a separation of these two layers: a decision the data plane makes about its own permissions is not a control.

**Decision and action trace:** Correlated operational evidence showing the authorized purpose, identity, versions, context references, policy/approval decisions, tool calls, state changes, errors, and outcomes. It does not require hidden chain-of-thought.

**Effective challenge:** Critical, objective analysis by people with appropriate expertise, independence, standing, and authority to influence decisions.

**Embedding:** A numerical representation used to capture aspects of similarity or meaning, often for search and retrieval.

**Foundation model:** A model trained on broad data that can be adapted or used across many downstream tasks.

**Generative AI:** AI that produces content such as text, images, audio, video, software, or structured data.

**Ground truth:** Authoritative evidence used to determine the expected result for an evaluation.

**Guardrail:** A model, policy, filter, rule, or application control intended to constrain input, output, or action. Guardrails vary in reliability and are not inherently security boundaries.

**Hallucination:** Output that is fabricated, unsupported, or inconsistent with authoritative evidence or supplied context.

**Human in the loop:** A person must review and authorize a decision or action before it takes effect.

**Human on the loop:** A person supervises operation and can intervene, but the system may act before review.

**Inherited control:** A control implemented once in a shared platform and relied upon by every use case built on it, rather than rebuilt per project. Distinct from an *inherited tier*, which is the risk tier a shared service takes from its highest-tier consumer. A control recorded as inherited must be evidenced at the platform; a use case that assumes inheritance without a record has no control.

**Generated explanation:** Model output describing how or why a result was reached. It is produced by the same process as any other output and is not an account of the system's internal computation: it may be fluent, plausible and wrong. Treat it as content requiring verification, never as evidence of reasoning, and keep it distinct from a *decision and action trace*, which records externally observable facts.

**Information barrier:** A mandatory restriction that prevents specified people from accessing specified information, overriding an otherwise-valid permission or role grant. Known in different sectors as an ethical wall, a Chinese wall, a conflicts screen, or a compartment. Unlike ordinary access control it is imposed rather than granted, commonly applies retroactively to content that already exists in derived stores, and constrains aggregation and summarization across compartments as well as direct retrieval.

**Large language model (LLM):** A model trained to process and generate language or related token sequences at scale.

**MCP:** Model Context Protocol, a versioned protocol for interactions between AI applications and servers exposing tools, resources, prompts, or extensions. The protocol is not itself an authorization or governance boundary.

**Memory:** Information retained by an agent or application beyond the immediate input, including session, task, episodic, semantic, profile, or long-term state. Memory must be governed as data and as a potential instruction channel.

**Model:** Use the definition required by the governing policy or authority. Regulatory definitions may exclude some generative or agentic systems.

**Model-assisted evaluation:** Use of one model to judge another system's output; it requires calibration and human oversight for consequential conclusions.

**Prompt injection:** Untrusted input changes model behavior in a way the application developer did not intend, including through direct, retrieved, tool, multimodal, or persistent content.

**RAG:** Retrieval-augmented generation, in which external information is retrieved and supplied as context for generation.

**Residual risk:** Risk remaining after controls and treatments are applied.

**Tamper-evident evidence:** Records protected so unauthorized alteration can be detected. Tamper-evidence is not synonymous with permanent immutability and should coexist with lawful retention, correction, deletion, and legal-hold processes.

**Workload identity:** A non-human identity assigned to software, a service, an agent, or a job for authentication, authorization, and accountability.

**Risk tier:** A category used to calibrate governance and assurance depth based on potential impact and exposure.

**System prompt:** Higher-priority instructions supplied by the application or provider. It may influence behavior but should not be treated as a secret or an enforceable authorization boundary.

**TEVV:** Test, evaluation, verification, and validation activities used to assess system requirements, performance, and risk.

**Tool:** An external capability an AI system can invoke, such as search, code execution, database access, messaging, file operations, or transactions.

## Related artifacts

- [Standards Landscape](standards-landscape.md)
- [Control Objectives](../governance/control-framework/control-objectives.md)
- [Agentic AI Governance and Assurance Profile](../governance/agentic-ai/governance-and-assurance-profile.md)

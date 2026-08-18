# AI Data Security & Governance

This collection translates the [AI Data Handling and Privacy Policy](../policies/data-handling.md) into an operating framework and implementation standards. It covers data used or created during acquisition, prompting, retrieval, training, evaluation, logging, monitoring, and retirement.

| Resource | Use |
|---|---|
| [AI Data Security & Governance Framework](framework.md) | Scope, principles, lifecycle, ownership, control domains, evidence, and assurance model |
| [AI Data Lifecycle Standard](data-lifecycle-standard.md) | Required controls from source approval through deletion and retirement |
| [Data Classification and AI Use Control Matrix](data-classification-control-matrix.md) | A configurable decision matrix for prompts, RAG, fine-tuning, logs, agent memory, and external services |
| [RAG, Vector, and Agent Data Security Standard](rag-vector-agent-data-security.md) | Permission preservation, ingestion integrity, vector security, memory, tools, and leakage prevention |
| [Training and Evaluation Data Governance Standard](training-evaluation-data-governance.md) | Provenance, rights, quality, representativeness, contamination, segregation, and reproducibility |

## Relationship to other artifact classes

- **Policy:** the [data-handling policy](../policies/data-handling.md) states mandatory organizational rules.
- **Governance standards:** this collection defines how those rules should operate and what evidence should exist.
- **Assessment:** the [use-case](../../assessments/use-case-assessment/checklist.md) and [vendor](../../assessments/vendor-assessment/framework.md) assessments determine exposure and control applicability.
- **Testing:** the [privacy and data leakage](../../testing/privacy-data-leakage/testing-guide.md) and [security red-teaming](../../testing/security-red-teaming/testing-guide.md) guides test the implemented controls.
- **Checklists:** release and monitoring checklists verify that required evidence is complete and current.

These documents provide a cross-industry control baseline, not a legal conclusion. Organizations must tailor classifications, retention periods, cryptographic requirements, transfer mechanisms, and approval authorities to applicable law, contract, risk appetite, and architecture.

---
schema_version: "1.0"
artifact_id: GOV-DATA-005
title: Training and Evaluation Data Governance Standard
artifact_class: governance
artifact_type: standard
domains:
  - training-data
  - evaluation-data
  - data-quality
  - provenance
  - intellectual-property
applies_to:
  - generative-ai
  - llm
  - machine-learning
  - rag
  - agentic-ai
industries:
  - cross-industry
lifecycle_stages:
  - design
  - development
  - validation
  - deployment
  - operation
  - retirement
status: draft
version: "0.1.0"
last_reviewed: 2026-08-18
source_artifacts:
  - GenAI Policies - Example.docx
  - GenAI MRM Survey with Heatmap v2.xlsx
  - GenAI Testing Procedures v2.docx
  - GenAI Vendor Assessment Framework.docx
---

# Training and Evaluation Data Governance Standard

## 1. Objective

This standard governs data used to train, fine-tune, adapt, align, evaluate, red-team, calibrate, or monitor AI systems. It applies whether development is performed internally or by a provider and whether the data is real, public, licensed, customer-provided, employee-provided, scraped, purchased, generated, or synthetic.

Approval to access data for ordinary business operations or inference does not automatically authorize these development and assurance uses.

## 2. Dataset register and manifest

Each material dataset or corpus must have a stable record containing:

- name, identifier, version, owner, steward, and custodian;
- purpose and approved uses: training, fine-tuning, alignment, evaluation, red team, monitoring, or other;
- source systems, providers, collection methods, dates, and geographic scope;
- population, unit of observation, modalities, labels, and sensitive attributes;
- classification, personal/regulated-data flags, confidentiality, and contractual restrictions;
- legal, consent, permission, copyright, license, and usage conditions requiring confirmation;
- inclusion, exclusion, sampling, cleaning, deduplication, labeling, augmentation, and transformation logic;
- quality, coverage, representativeness, known gaps, uncertainty, and bias limitations;
- train/validation/test/red-team split logic and contamination controls;
- storage, region, access, encryption/key boundary, provider, and subprocessor;
- retention, correction, withdrawal, deletion, and model/index impact process;
- related model, adapter, checkpoint, evaluation, release, and monitoring use; and
- integrity reference, evidence location, last review, changes, findings, and exceptions.

Maintain a machine-readable manifest when scale or reproducibility warrants it. The manifest should be version-controlled without placing sensitive data in the code repository.

## 3. Source authorization and rights

Before use:

- confirm that acquisition and intended AI use are authorized separately;
- review terms for training, adaptation, commercial use, redistribution, derivative artifacts, attribution, confidentiality, and deletion;
- identify personal data, sensitive data, minors' data, employee/customer data, privileged material, trade secrets, and regulated records;
- document relevant notices, consent, reasonable expectations, objections, withdrawals, and purpose compatibility as applicable;
- assess whether publicly accessible data remains subject to privacy, copyright, contract, database, confidentiality, or ethical restrictions; and
- require providers to disclose relevant sourcing and governance information at a level sufficient for the use-case risk decision.

If rights or provenance cannot be established, do not quietly recategorize the source as “public.” Exclude, quarantine, obtain authorization, or document a properly approved legal/risk decision.

## 4. Data quality and suitability

Define quality relative to intended use and failure consequences. Assess:

- **accuracy:** values, labels, answers, citations, and annotations are supportable;
- **completeness:** required fields, cases, populations, modalities, languages, and edge conditions are covered;
- **timeliness:** observation periods and concepts reflect the deployment context;
- **consistency:** definitions, units, formats, labels, and transformations are coherent;
- **uniqueness:** duplicates and near-duplicates do not distort learning or evaluation;
- **validity:** records conform to business and technical rules;
- **representativeness:** the dataset reflects relevant users, populations, workflows, environments, and economic or operational conditions;
- **independence:** evaluation results are not inflated by leakage, tuning, or overlap; and
- **integrity:** sources, labels, files, and transformations are protected from unauthorized or malicious change.

Set thresholds and escalation based on materiality. A dataset can be large and statistically balanced yet unsuitable because its labels, period, permissions, or outcome definitions do not match the intended use.

## 5. Representativeness and harmful-bias risk

- Define the target population and relevant subgroups before measuring representation.
- Examine selection, survivorship, historical, measurement, labeling, and missing-data bias.
- Review whether protected or sensitive attributes and plausible proxies are present, absent, inferred, or necessary for fairness testing.
- Compare error and outcome patterns across relevant groups and contexts; do not infer fairness from dataset proportions alone.
- Document population gaps, small samples, uncertainty, mitigation, human oversight, and use limitations.
- Reassess when the deployment population, product, geography, language, channel, or economic environment changes.

Use the [bias and fairness testing guide](../../testing/bias-fairness/testing-guide.md) for test design.

## 6. Preparation, labeling, and synthetic data

### 6.1 Transformations

- Version cleaning, normalization, filtering, redaction, deduplication, sampling, augmentation, tokenization, and feature logic.
- Record exclusions and their effects on population and outcomes.
- Prevent temporary files, notebooks, logs, and annotation exports from becoming uncontrolled copies.
- Independently review transformations that materially define labels, outcomes, sensitive attributes, or evaluation answers.

### 6.2 Labeling and human contributors

- Define label taxonomy, instructions, qualifications, conflicts, adjudication, quality sampling, and acceptance criteria.
- Record whether annotators or feedback providers can see personal, confidential, or harmful content and apply appropriate safeguards.
- Assess inter-rater reliability or other fit-for-purpose agreement measures where labels are subjective.
- Separate production access from annotation access and limit provider/human-review reuse.

### 6.3 Synthetic data

- Label synthetic records and retain generator, prompt/configuration, source basis, version, and validation results.
- Test for source memorization, sensitive-data reproduction, unrealistic distributions, mode collapse, artifacts, and label leakage.
- Do not assume synthetic data is privacy-safe or representative merely because it was generated.
- Prevent synthetic test identities, credentials, or canaries from being mistaken for production records.

## 7. Dataset splits and contamination

- Define train, validation, test, benchmark, red-team, and monitoring datasets with controlled membership and access.
- Detect exact and semantic duplicates, temporal leakage, answer leakage, user/case overlap, source overlap, and benchmark exposure.
- Restrict evaluation answers and adversarial cases from developers, prompts, training pipelines, and provider feedback where independence matters.
- Record all tuning performed against evaluation results; repeated tuning can convert a test set into a development set.
- Maintain a final independent holdout or alternative assurance method for material releases.
- Rebuild or qualify results when contamination is discovered.

## 8. Security and segregation

- Separate production, development, evaluation, and red-team environments according to risk.
- Use managed identities, least privilege, time-bound privileged access, and periodic review.
- Protect datasets, labels, manifests, adapters, checkpoints, outputs, and evaluation answers under classification-appropriate controls.
- Scan datasets and pipelines for secrets, malware, injection content, corrupted files, and unauthorized sources.
- Control bulk export, local download, notebook access, removable media, provider upload, and cross-region transfer.
- Monitor unusual access, enumeration, copying, label changes, and build-manifest changes.
- Treat model artifacts as potentially sensitive when extraction, inversion, or memorization could expose governed data.

## 9. Provider-developed and foundation models

When underlying training data is not available:

- obtain model/system cards, sourcing descriptions, data-governance policies, known limitations, evaluation evidence, security documentation, and contractual commitments proportionate to risk;
- determine whether organizational prompts, files, outputs, feedback, support content, or telemetry are used for training or improvement;
- distinguish default, enterprise, API, opt-in feedback, abuse-monitoring, and human-review settings;
- assess model memorization, extraction, content-rights, privacy, bias, and domain-suitability risk through available evidence and independent testing;
- document residual uncertainty rather than treating non-disclosure as evidence of safety; and
- define change notice, re-evaluation, incident, data deletion, model retirement, and exit requirements.

Use the [vendor assessment questionnaire](../../assessments/vendor-assessment/questionnaire.md) for due diligence.

## 10. Evaluation-data requirements

Evaluation data must be:

- traceable to requirements, risks, users, workflows, and failure consequences;
- representative of normal, boundary, adverse, misuse, and low-frequency/high-impact scenarios;
- separated from training and prompt optimization to the degree required for credible results;
- versioned with cases, expected behavior, scoring logic, evaluator/model version, thresholds, and uncertainty;
- reviewed for privacy, rights, sensitive content, leakage, and evaluator access;
- protected against answer exposure and benchmark gaming; and
- refreshed when system, data, use, population, threat, or regulation changes.

When using an LLM as an evaluator, document evaluator model/version, prompt, reference access, scoring rubric, calibration against qualified human judgment, subgroup behavior, failure modes, and conflicts of interest. Do not use the same opaque model family as the sole judge of its own material performance without additional challenge.

## 11. Correction, withdrawal, deletion, and model impact

Maintain a procedure to:

1. identify affected records, splits, labels, transformations, builds, adapters, checkpoints, indexes, evaluations, releases, and providers;
2. stop new use and preserve necessary investigation evidence;
3. correct, exclude, suppress, or delete data under documented authority;
4. assess whether retraining, unlearning, re-indexing, model replacement, output correction, or use restriction is necessary and feasible;
5. prevent backup or cached restoration from reintroducing removed data;
6. re-run relevant quality, privacy, security, fairness, and performance tests; and
7. communicate material downstream impact and retain a decision record.

Deletion from a source dataset does not necessarily remove learned influence from a model. The accountable decision must distinguish source deletion, artifact deletion, model mitigation, retraining/unlearning feasibility, and residual risk.

## 12. Monitoring and change

Monitor:

- source, license, consent, owner, and provider changes;
- population, schema, concept, quality, and label drift;
- anomalous access, poisoning, unauthorized data, and integrity failures;
- extraction, memorization, sensitive output, and privacy complaints;
- subgroup, language, modality, and edge-case performance;
- contamination, benchmark exposure, evaluator drift, and feedback-loop effects; and
- deletion, withdrawal, retention, and provider-setting failures.

Material changes trigger impact assessment and risk-based revalidation before continued use.

## 13. Minimum evidence package

- dataset register and versioned manifest;
- source authorization, terms/licenses, privacy and IP review;
- data flow, processing record, regions, providers, and access model;
- quality, representativeness, bias, and limitation assessment;
- transformation and labeling documentation;
- split, deduplication, contamination, and independence results;
- security, secret, poisoning, privacy, and memorization/extraction tests;
- reproducible build/evaluation configuration and results;
- retention, withdrawal, correction, deletion, and model-impact procedure;
- monitoring thresholds, issues, exceptions, and approvals; and
- provider evidence and residual-uncertainty decision where source data is opaque.

## 14. Authoritative reference points

- [NIST AI 600-1 Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) addresses data origin, content lineage, privacy, intellectual property, third-party data, representative evaluation, poisoning, and post-adaptation reassessment.
- [NIST SP 800-218A](https://csrc.nist.gov/pubs/sp/800/218/a/final) extends secure software development practices to generative AI and foundation-model development.
- [EDPB Opinion 28/2024](https://www.edpb.europa.eu/documents/opinion-of-the-board-art-64/opinion-282024-on-certain-data-protection-aspects-related-to_en) explains that AI-model anonymity and lawful processing require case-specific analysis.
- [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) includes data-governance requirements for covered high-risk systems; applicability and current dates require legal confirmation.

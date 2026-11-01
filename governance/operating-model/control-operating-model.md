---
schema_version: "1.0"
artifact_id: GOV-OPS-002
title: AI Control Operating Model
artifact_class: governance
artifact_type: operating-model
domains:
  - accountability
  - control-inheritance
  - operating-rhythm
  - programme-metrics
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
  - deployment
  - operation
status: draft
version: "0.1.0"
last_reviewed: 2026-11-01
---

# AI Control Operating Model

## Purpose

The rest of this library states what controls should exist, how to assess them, how to test them, what to verify, and how to record the result. This artifact covers the remaining question: **how the control set is operated across a growing portfolio** without the effort growing with it.

A control framework scales when it runs as a system rather than a document. Four properties make the difference: use cases are tiered so not everything receives the full treatment; controls are built once into the shared platform and inherited; tests run automatically so evidence is produced rather than collected; and every control has exactly one accountable owner.

The most common programme failure is not a missing control. It is a control nobody owns.

## 1. Tier so that not everything gets everything

Depth is allocated at intake by the [risk tiering framework](../risk-tiering/ai-risk-tiering-framework.md) through the [use-case assessment](../../assessments/use-case-assessment/checklist.md) at gate G1. A low-exposure internal drafting tool receives the baseline control set; a system that reaches sensitive data, faces customers, or takes autonomous action receives the full set.

Scale comes from *not* doing everything everywhere. A programme that applies uniform depth will either exhaust itself or quietly stop applying anything.

## 2. Inherited and local controls

This is the largest single lever, and the one most often left implicit.

Controls implemented **once in a shared platform** — authorization evaluated before retrieval, a gateway that scopes every action to the requesting human, correlated logging back to that person, contained execution environments — are **inherited** by every use case built on that platform. Controls specific to one system — which sources it reads, which actions it may take, where a human must approve — are **local**.

> **Two senses of "inherited".** An *inherited control* is implemented in a shared platform and relied upon by the use cases built on it. An *[inherited tier](../risk-tiering/ai-risk-tiering-framework.md#shared-service-tier-inheritance)* is the risk tier a shared service takes from its highest-tier consumer. They are unrelated: a use case can inherit controls from a platform that is not a shared service in the tiering sense.

### Requirements

- **Record the split per use case.** Each use case's control record marks every applicable control as inherited or local, with the platform component or owner that provides it. An unmarked control is a local control by default, because nothing is inherited by assumption.
- **Verify inheritance; do not assert it.** A control recorded as inherited must be evidenced at the platform, once, with the result referenced by each inheriting use case. *"We assumed the platform handles that"* is the predictable failure, and recording the split is what makes it detectable before an incident rather than during one.
- **Name the platform owner as the control's accountable owner.** The use-case owner remains accountable for relying on it correctly — for being in scope of the platform component, and for not bypassing it.
- **Re-evidence inherited controls on platform change.** A platform change is a change to every inheriting use case; see [shared-service change management](../policies/change-management.md#shared-ai-services) (`OPS-05`).
- **Promote reusable local controls.** A local control built twice is a platform control that has not been built yet. Moving it is how the inheritance ratio improves.
- **State the limits of inheritance.** Record which controls the platform does *not* provide, so a use case cannot read silence as coverage.

Inheritance is also what makes the control set difficult to skip: a project team can omit a control it has to build, but not one it receives by construction.

## 3. Use the processes that already exist

Do not operate a parallel AI process. Each control activity attaches to an established enterprise process, with AI-specific requirements added rather than duplicated:

| Activity | Existing process it attaches to | AI-specific addition |
|---|---|---|
| Intake and approval | Governance committee and risk acceptance | Tiering, autonomy and action authority, prohibited-use determination |
| Design and pre-release | Existing development lifecycle gates | Threat model of trust boundaries, authorization model, adversarial testing |
| Change | Change management | A model, prompt, retrieval, tool, or platform change triggers re-test (`OPS-03`) |
| Vendor assessment | Third-party risk | Version and deprecation commitments, telemetry destinations, data-use terms, credential handling |
| Access review | Joiner-mover-leaver and entitlement recertification | Agent, service, and other non-human identities in scope |
| Model risk | Model risk management | Continues to cover performance and conceptual soundness; security controls sit alongside, not inside |
| Incident response | Enterprise incident process | [AI-specific response](../ai-security/incident-response.md) for containment scope, propagation, and attribution |

A parallel structure competes with the real one for attention and loses. Where an existing process genuinely cannot carry a requirement, record why before creating a new one.

## 4. Produce evidence rather than collect it

Evidence that is assembled by hand does not survive portfolio growth.

- Run the scenario libraries as an automated suite on each release and material change, and file the output as the evidence (`QUAL-06`).
- Hold acceptance criteria in the suite, so a release decision is a test result rather than a judgement reconstructed afterwards.
- Let the second line and internal audit review **outputs** rather than request screenshots. Independent review of a generated artifact is both cheaper and stronger than independent reconstruction.
- Carry every closed severe finding into the suite permanently, so a future change cannot silently reintroduce it.
- Record what the evidence supports — design, implementation, operating, or outcome effectiveness. See [eliciting evidence](../control-framework/control-objectives.md#eliciting-evidence).

Evidence that cannot be produced on demand is a control that cannot be relied upon between reviews.

## 5. Operating rhythm

Forum cadence is defined in [roles and decision rights](roles-and-decision-rights.md). This is the activity cut: what happens, when, and who is accountable.

| Cadence | What happens | Accountable |
|---|---|---|
| Every new use case | Intake, tiering, control record with inherited and local marked, owners named for the use case, each data source, and each non-human identity | Use-case owner, with the AI governance function |
| Every release or material change | Automated suite runs against the production-intended configuration; results filed as evidence; owner signs off; re-test on model, prompt, retrieval, tool, or platform change | Use-case owner, with the platform team |
| Monthly | Programme metrics reviewed; open findings and exceptions chased to named owners; new threats added to regression coverage | AI governance function (second line) |
| Quarterly | Inventory certified; higher-risk exceptions and trends reviewed; non-human identities recertified; inherited-control register reconciled against what the platform actually provides | Governance committee, with use-case owners |
| Annually | Control set refreshed against current threats, standards, and obligations; independent assurance performed; the control library itself reviewed for staleness | Second line and internal audit |
| Event-driven | Incident, threshold breach, provider deprecation, or regulatory change routes to the earliest affected gate | Per [escalation triggers](roles-and-decision-rights.md) |

A rhythm nobody is accountable for is a calendar entry. Each row names a role, not a committee.

## 6. Programme metrics

These measure whether the operating model works, as distinct from the [gate-performance measures](../lifecycle/stage-gates.md) and the [effectiveness measures](roles-and-decision-rights.md) that assess decisions.

| Metric | What it tells you |
|---|---|
| Use cases inventoried, tiered, and with a named accountable owner | Whether the portfolio is known. Anything below complete means the other metrics are computed on a partial population |
| Higher-risk use cases with passing tests from the current release | Whether assurance is current rather than historical |
| **Controls inherited from the platform rather than rebuilt per use case** | The maturity trend. This should climb; a flat ratio across a growing portfolio means each project is re-solving solved problems |
| Non-human identities with no human sponsor | Target zero. A non-zero value is unattributable action waiting to happen |
| Open findings and exceptions by age, and the number past expiry | Whether the programme closes what it opens |
| Time to revoke assistant and agent access after a role change or departure | Whether AI access is inside the enterprise identity lifecycle or outside it |
| Controls recorded as inherited but not evidenced at the platform | Assumed coverage, measured directly |

Report the trend, not the point value. A programme improving from a weak position is in better condition than one static at a middling one.

## 7. Standing the model up

Run the whole loop once, on one system, before templating it.

1. **Choose one live, higher-risk system** — ideally one that reaches sensitive data or can take action. A low-risk pilot will not exercise the controls that matter.
2. **Name the owners first.** Use-case owner, a data owner for each source, the platform owner for inherited controls, and a human sponsor for every non-human identity. Most gaps surface at this step alone, before any testing.
3. **Tier it and write the control record**, marking each control inherited or local, with the evidence reference for each inherited one.
4. **Test with tests that can fail.** Run a deliberately broken case first to confirm the suite detects it; a suite that has never failed is unverified. File the results as evidence.
5. **Close, promote, and template.** Remediate the findings, move anything reusable into the platform, and make the intake record, control record, and test suite the standard for the next system.

Expect the first pass to be slower than the controls appear to require. The output is not one assured system; it is the template, and the inventory of what the platform does not yet provide.

## Related artifacts

- [AI Governance Roles and Decision Rights](roles-and-decision-rights.md) — ownership principles and decision rights
- [AI Governance Framework](../ai-governance-framework.md)
- [AI Lifecycle Stage Gates](../lifecycle/stage-gates.md)
- [Enterprise AI Control Objectives](../control-framework/control-objectives.md) — `GOV-04`
- [AI Change Management Policy](../policies/change-management.md) — shared services and `OPS-05`
- [AI Security Overlay](../ai-security/README.md)
- [AI Inventory Minimum Data Standard](../ai-inventory/minimum-data-standard.md)

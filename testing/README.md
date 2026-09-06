# Testing & Assurance

Testing artifacts answer: **How should the AI system be evaluated?**

## Core methodology

- [Enterprise GenAI Testing Framework](testing-framework/enterprise-genai-testing.md)
- [Use-Case-Driven Test Design](test-design/use-case-driven-test-design.md)

## Test dimensions

Each dimension pairs a **method guide** (how to test) with a **scenario library** (what to test, with acceptance criteria and control-objective references).

| Dimension | Method guide | Scenario library |
|---|---|---|
| Functional correctness | [Guide](functional-correctness/testing-guide.md) | [`FCS-01`–`FCS-08`](functional-correctness/scenario-library.md) |
| Hallucination and factuality | [Guide](hallucination-factuality/testing-guide.md) | [`FAS-01`–`FAS-08`](hallucination-factuality/scenario-library.md) |
| Security red teaming | [Guide](security-red-teaming/testing-guide.md) | [`SRS-01`–`SRS-10`](security-red-teaming/scenario-library.md) |
| Safety and alignment | [Guide](safety-alignment/testing-guide.md) | [`SAS-01`–`SAS-08`](safety-alignment/scenario-library.md) |
| Bias and fairness | [Guide](bias-fairness/testing-guide.md) | [`FRS-01`–`FRS-08`](bias-fairness/scenario-library.md) |
| Privacy and data leakage | [Guide](privacy-data-leakage/testing-guide.md) | [`PRS-01`–`PRS-08`](privacy-data-leakage/scenario-library.md) |
| Integration and workflow | [Guide](integration-workflow/testing-guide.md) | [`IWS-01`–`IWS-08`](integration-workflow/scenario-library.md) |
| Agentic AI | [Guide](agentic-ai/testing-guide.md) | [`AGS-01`–`AGS-14`](agentic-ai/scenario-library.md) |
| Regression testing | [Guide](regression-testing/testing-guide.md) | [`RGS-01`–`RGS-08`](regression-testing/scenario-library.md) |

Scenarios reference [control objectives](../governance/control-framework/control-objectives.md); the [control coverage matrix](../governance/control-framework/control-coverage-matrix.md) is the reverse index.

Not every dimension applies equally. Select tests from the use case, failure modes, architecture, data, risk tier, deployment modality, and external obligations.

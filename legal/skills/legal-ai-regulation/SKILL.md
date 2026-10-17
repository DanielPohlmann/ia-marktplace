---
name: legal-ai-regulation
description: Use when identifying AI-specific legal obligations for an AI/ML product. USE FOR: EU AI Act risk classes and obligations, GPAI models, US AI orders and state laws, China AI rules, transparency, audits, compliance timeline. DO NOT USE FOR: prompt injection and AI security (use security-ai-security), routing (use legal).
---

# AI Regulation

> **Disclaimer**: This skill provides general educational information about legal topics relevant to software development. It is **not legal advice**. Laws vary by jurisdiction and change frequently. Always consult a qualified attorney licensed in the relevant jurisdiction before making legal decisions for your organization.

## Overview

AI regulation is the fastest-moving area of technology law. The EU AI Act is the first comprehensive AI law globally, but jurisdictions worldwide are rapidly developing their own frameworks. Any company deploying AI/ML must track these regulations to avoid penalties, reputational damage, and market access restrictions. The regulatory landscape ranges from binding legislation with significant fines to voluntary frameworks and sector-specific guidance.

## Best Practices

- **Recognize that AI regulation is rapidly evolving and requires ongoing legal counsel.** The regulatory landscape is changing on a quarterly basis. Engage legal advisors who specialize in AI law and monitor legislative developments in every jurisdiction where you operate.
- **Classify your AI systems by risk level early in the development process.** Understanding whether your system falls into the high-risk, limited-risk, or minimal-risk category under the EU AI Act (and equivalent frameworks) determines your compliance obligations.
- **Implement a comprehensive AI risk management framework.** Adopt a structured approach such as the NIST AI RMF to govern, map, measure, and manage AI risks across your organization.
- **Design for human oversight from the start.** Build mechanisms that allow humans to understand, monitor, intervene in, and override AI system outputs. This is both a regulatory requirement and an engineering best practice.
- **Maintain thorough documentation of your AI system's lifecycle.** Document training data provenance, model architecture, testing methodology, evaluation results, known limitations, and deployment decisions. This documentation is essential for conformity assessments and audits.
- **Conduct bias and fairness assessments regularly.** Test your AI systems for discriminatory outcomes across protected characteristics. Document the results and remediation steps taken.
- **Implement transparency measures appropriate to your system's risk level.** At minimum, inform users when they are interacting with an AI system. For high-risk systems, provide detailed information about the system's purpose, capabilities, limitations, and the role of human oversight.
- **Monitor your deployed AI systems continuously.** Post-market monitoring is a legal requirement under the EU AI Act and a best practice globally. Track performance metrics, log incidents, and maintain feedback loops to detect model drift and emergent risks.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/eu-ai-act-key-obligations-for-high-risk-ai-syste.md](references/eu-ai-act-key-obligations-for-high-risk-ai-syste.md) | EU AI Act Key Obligations for High-Risk AI Systems |
| [references/details.md](references/details.md) | Global AI Regulation Landscape; EU AI Act Risk Classification; EU AI Act General-Purpose AI (GPAI) Models; US AI Landscape; Compliance Timeline |

## References

- [EU AI Act Official Text (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence)
- [OECD AI Principles](https://oecd.ai/en/ai-principles)

See references/rules.md for the full rule catalog.

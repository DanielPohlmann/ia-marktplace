---
name: security-ai-security
description: Use when addressing security risks specific to LLM and AI applications. USE FOR: OWASP LLM Top 10 (2025), prompt injection, data and model poisoning, excessive agency, insecure output handling, AI red teaming, ML supply chain, responsible AI. DO NOT USE FOR: general web vulns (use security-owasp), AI law (use legal-ai-regulation), API hardening (use security-api-security).
---

# AI Security

## Overview

2025 is the year of LLM agents. As AI systems transition from simple chatbots to autonomous agents capable of executing code, browsing the web, and interacting with APIs, the attack surface expands dramatically. AI introduces novel security challenges that traditional application security frameworks were not designed to address: prompt injection, model poisoning, excessive agency, and supply chain risks unique to machine learning models and training data. Securing AI applications requires specialized security thinking that builds upon — but goes beyond — conventional web application security.

This skill is organized around the **OWASP Top 10 for LLM Applications (2025)**, which provides the authoritative taxonomy of risks specific to large language model applications, supplemented by guidance on AI red teaming methodologies and responsible AI governance frameworks.

## Best Practices

- **Treat all LLM output as untrusted input** — never pass LLM-generated content directly to interpreters, databases, APIs, or downstream systems without validation and encoding.
- **Apply the principle of least privilege to AI agents** — grant only the minimum tools, permissions, and data access required; audit and prune agent capabilities regularly.
- **Implement human-in-the-loop approval** for sensitive actions such as financial transactions, data deletion, external communications, and production system modifications.
- **Do not store secrets, API keys, or sensitive business logic in system prompts** — assume that system prompts are discoverable and treat them accordingly.
- **Conduct regular AI red teaming** using both manual expert testing and automated adversarial frameworks to continuously evaluate your AI system's resilience to attack.
- **Validate and control RAG data sources** — apply access controls to vector stores, verify the integrity of ingested documents, and monitor for poisoned content in your knowledge base.
- **Implement rate limiting, token budgets, and circuit breakers** on all LLM-powered features to prevent unbounded resource consumption and runaway agent loops.
- **Stay current with evolving AI regulations** (EU AI Act, NIST AI RMF, ISO/IEC 42001) and align your AI governance practices with applicable frameworks before enforcement deadlines.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/owasp-top-10-for-llm-applications-2025.md](references/owasp-top-10-for-llm-applications-2025.md) | OWASP Top 10 for LLM Applications (2025) |
| [references/prompt-injection.md](references/prompt-injection.md) | Prompt Injection — Direct Prompt Injection, Indirect Prompt Injection, Mitigation Strategies |
| [references/model-data-poisoning.md](references/model-data-poisoning.md) | Model & Data Poisoning — Attack Types, Attack Vectors, Defenses |
| [references/excessive-agency.md](references/excessive-agency.md) | Excessive Agency — Three Dimensions of Excessive Agency, Mitigation |
| [references/ai-red-teaming.md](references/ai-red-teaming.md) | AI Red Teaming — Manual vs. Automated Approaches, AI Red Teaming Tools, What to Test |
| [references/responsible-ai-frameworks.md](references/responsible-ai-frameworks.md) | Responsible AI Frameworks — Regulatory and Standards Landscape, Core Principles of Responsible AI |

## References

- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence)
- [MITRE ATLAS (Adversarial Threat Landscape for AI Systems)](https://atlas.mitre.org)

See references/rules.md for the full rule catalog.

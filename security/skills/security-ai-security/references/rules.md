# AI Security Rules

Best practices and rules for AI Security.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Treat all LLM output as untrusted input | CRITICAL | [`ai-security-treat-all-llm-output-as-untrusted-input.md`](ai-security-treat-all-llm-output-as-untrusted-input.md) |
| 2 | Apply the principle of least privilege to AI agents | HIGH | [`ai-security-apply-the-principle-of-least-privilege-to-ai-agents.md`](ai-security-apply-the-principle-of-least-privilege-to-ai-agents.md) |
| 3 | Implement human-in-the-loop approval | CRITICAL | [`ai-security-implement-human-in-the-loop-approval.md`](ai-security-implement-human-in-the-loop-approval.md) |
| 4 | Do not store secrets, API keys, or sensitive business logic in system prompts | CRITICAL | [`ai-security-do-not-store-secrets-api-keys-or-sensitive-business-logic.md`](ai-security-do-not-store-secrets-api-keys-or-sensitive-business-logic.md) |
| 5 | Conduct regular AI red teaming | MEDIUM | [`ai-security-conduct-regular-ai-red-teaming.md`](ai-security-conduct-regular-ai-red-teaming.md) |
| 6 | Validate and control RAG data sources | HIGH | [`ai-security-validate-and-control-rag-data-sources.md`](ai-security-validate-and-control-rag-data-sources.md) |
| 7 | Implement rate limiting, token budgets, and circuit breakers | HIGH | [`ai-security-implement-rate-limiting-token-budgets-and-circuit-breakers.md`](ai-security-implement-rate-limiting-token-budgets-and-circuit-breakers.md) |
| 8 | Stay current with evolving AI regulations | HIGH | [`ai-security-stay-current-with-evolving-ai-regulations.md`](ai-security-stay-current-with-evolving-ai-regulations.md) |

---

---
title: "Apply the principle of least privilege to AI agents"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: ai-security, security, llm-security, prompt-injection, model-poisoning
---

## Apply the principle of least privilege to AI agents

Apply the principle of least privilege to AI agents: grant only the minimum tools, permissions, and data access required; audit and prune agent capabilities regularly.

---

---
title: "Conduct regular AI red teaming"
impact: MEDIUM
impactDescription: "general best practice"
tags: ai-security, security, llm-security, prompt-injection, model-poisoning
---

## Conduct regular AI red teaming

Conduct regular AI red teaming: using both manual expert testing and automated adversarial frameworks to continuously evaluate your AI system's resilience to attack.

---

---
title: "Do not store secrets, API keys, or sensitive business logic in system prompts"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: ai-security, security, llm-security, prompt-injection, model-poisoning
---

## Do not store secrets, API keys, or sensitive business logic in system prompts

Do not store secrets, API keys, or sensitive business logic in system prompts: assume that system prompts are discoverable and treat them accordingly.

---

---
title: "Implement human-in-the-loop approval"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: ai-security, security, llm-security, prompt-injection, model-poisoning
---

## Implement human-in-the-loop approval

Implement human-in-the-loop approval: for sensitive actions such as financial transactions, data deletion, external communications, and production system modifications.

---

---
title: "Implement rate limiting, token budgets, and circuit breakers"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: ai-security, security, llm-security, prompt-injection, model-poisoning
---

## Implement rate limiting, token budgets, and circuit breakers

Implement rate limiting, token budgets, and circuit breakers: on all LLM-powered features to prevent unbounded resource consumption and runaway agent loops.

---

---
title: "Stay current with evolving AI regulations"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: ai-security, security, llm-security, prompt-injection, model-poisoning
---

## Stay current with evolving AI regulations

(EU AI Act, NIST AI RMF, ISO/IEC 42001) and align your AI governance practices with applicable frameworks before enforcement deadlines.

---

---
title: "Treat all LLM output as untrusted input"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: ai-security, security, llm-security, prompt-injection, model-poisoning
---

## Treat all LLM output as untrusted input

Treat all LLM output as untrusted input: never pass LLM-generated content directly to interpreters, databases, APIs, or downstream systems without validation and encoding.

---

---
title: "Validate and control RAG data sources"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: ai-security, security, llm-security, prompt-injection, model-poisoning
---

## Validate and control RAG data sources

Validate and control RAG data sources: apply access controls to vector stores, verify the integrity of ingested documents, and monitor for poisoned content in your knowledge base.

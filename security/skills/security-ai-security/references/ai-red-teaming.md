<!-- Part of the security-ai-security skill. Loaded on demand from SKILL.md. -->

# AI Red Teaming

AI red teaming is the practice of systematically probing AI systems for vulnerabilities, biases, and failure modes. Unlike traditional penetration testing, AI red teaming must account for the probabilistic and non-deterministic nature of LLM behavior.

## Manual vs. Automated Approaches

- **Manual red teaming** — Human experts craft adversarial prompts, test edge cases, and explore creative attack vectors. Essential for discovering novel attack techniques and contextual vulnerabilities that automated tools miss.
- **Automated red teaming** — Tools systematically generate and execute large volumes of adversarial test cases, covering a broader range of known attack patterns. Effective for regression testing and continuous security validation.
- **Hybrid approach** — Combine manual creativity with automated scale. Use manual red teaming to discover new attack vectors, then encode them as automated test cases for continuous monitoring.

## AI Red Teaming Tools

| Tool | Type |
|---|---|
| Garak | OWASP project providing modular attack probes, generators, and detectors for LLM vulnerability assessment |
| ARTKIT | Multi-turn conversational testing framework for evaluating AI systems over extended interactions |
| Promptfoo | Prompt testing and evaluation framework with built-in adversarial test suites and LLM-as-judge evaluation |
| DeepTeam | Comprehensive red teaming framework for LLMs with attack modules covering all OWASP LLM Top 10 categories |

## What to Test

- **Prompt injection** — Both direct and indirect injection attempts across multiple encoding and obfuscation strategies.
- **Jailbreaking** — Attempts to bypass safety guardrails using roleplay, hypothetical framing, or multi-step manipulation.
- **Data extraction** — Probing for system prompt leakage, training data memorization, and RAG content exfiltration.
- **Tool misuse** — Testing whether the LLM can be manipulated into misusing its available tools or exceeding its intended authority.
- **Bias and fairness** — Evaluating model outputs for harmful biases across protected categories (race, gender, religion, disability).
- **Hallucination and misinformation** — Assessing the model's tendency to generate false or misleading information, especially in high-stakes domains.

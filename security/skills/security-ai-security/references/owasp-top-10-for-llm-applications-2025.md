<!-- Part of the security-ai-security skill. Loaded on demand from SKILL.md. -->

# OWASP Top 10 for LLM Applications (2025)

| # | Risk | Description | Key Mitigations |
|---|---|---|---|
| LLM01 | Prompt Injection | Attacker manipulates LLM behavior through crafted input (direct) or poisoned external data (indirect) to bypass instructions, exfiltrate data, or trigger unintended actions | Input validation, privilege separation, output filtering, human-in-the-loop for sensitive actions |
| LLM02 | Sensitive Information Disclosure | LLM reveals confidential data from training data, system prompts, RAG context, or conversation history in its responses | Data sanitization, output filtering, access controls on RAG sources, minimize sensitive data in prompts |
| LLM03 | Supply Chain | Compromised models, poisoned training data, vulnerable plugins, or tampered model artifacts introduce hidden risks | Model provenance verification, SBOM for ML pipelines, dependency scanning, model signing |
| LLM04 | Data and Model Poisoning | Attackers corrupt training or fine-tuning data to introduce backdoors, biases, or malicious behaviors into the model | Data validation and provenance, access controls on training pipelines, anomaly detection, model attestation |
| LLM05 | Improper Output Handling | LLM output is trusted and used directly without validation, enabling injection attacks (XSS, SSRF, command injection) in downstream systems | Treat LLM output as untrusted input, apply output encoding, validate before passing to interpreters or APIs |
| LLM06 | Excessive Agency | LLM is granted more functionality, permissions, or autonomy than necessary, enabling it to take harmful actions | Least privilege, limit available tools/plugins, require human approval for sensitive actions, rate limiting |
| LLM07 | System Prompt Leakage | Attackers extract the system prompt, revealing business logic, hidden instructions, API keys, or security controls embedded in the prompt | Do not store secrets in prompts, treat system prompts as discoverable, defense in depth |
| LLM08 | Vector and Embedding Weaknesses | Vulnerabilities in RAG pipelines including poisoned embeddings, retrieval manipulation, and unauthorized access to vector store content | Access controls on vector stores, input validation for RAG sources, embedding integrity checks |
| LLM09 | Misinformation | LLM generates false, misleading, or fabricated information (hallucinations) that users trust and act upon | Grounding with retrieval, fact-checking pipelines, confidence scoring, clear disclaimers, human review |
| LLM10 | Unbounded Consumption | LLM resources are consumed excessively through denial-of-service attacks, recursive agent loops, or resource-intensive queries | Rate limiting, token budgets, timeout controls, circuit breakers, cost monitoring and alerts |

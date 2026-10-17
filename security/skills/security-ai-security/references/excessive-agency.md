<!-- Part of the security-ai-security skill. Loaded on demand from SKILL.md. -->

# Excessive Agency

Excessive agency occurs when an LLM-based system is granted more capability, permission, or autonomy than is necessary for its intended function. As LLM agents become more capable — executing code, calling APIs, managing files, and interacting with external systems — the risk of excessive agency increases dramatically.

## Three Dimensions of Excessive Agency

- **Excessive functionality** — The LLM has access to tools, plugins, or capabilities it does not need. For example, an LLM that only needs to query a database is also given the ability to write to it.
- **Excessive permissions** — The LLM operates with more privileges than necessary. For example, an LLM agent that needs read access to a specific table is given admin access to the entire database.
- **Excessive autonomy** — The LLM is allowed to take high-impact actions without human oversight. For example, an LLM agent can send emails, make purchases, or modify production systems without approval.

## Mitigation

- **Least privilege** — Grant the LLM only the minimum tools, permissions, and data access required for its specific task. Regularly audit and prune available capabilities.
- **Sandboxing** — Execute LLM-triggered actions in sandboxed environments with strict boundaries. Use container isolation, network policies, and resource limits.
- **Approval workflows** — Require human approval for sensitive, irreversible, or high-impact actions (financial transactions, data deletion, external communications, production deployments).
- **Rate limiting** — Implement rate limits and token budgets on LLM actions to prevent runaway agent loops and resource exhaustion. Set maximum iteration counts for autonomous agent workflows.
- **Monitoring** — Log all actions taken by the LLM agent, including tool calls, API requests, and data accesses. Alert on unusual patterns such as unexpected tool usage, high-frequency actions, or access to sensitive resources.

# ADR (Architecture Decision Records) Rules

Best practices and rules for ADR (Architecture Decision Records).

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Write ADRs at decision time | CRITICAL | [`adr-write-adrs-at-decision-time.md`](adr-write-adrs-at-decision-time.md) |
| 2 | Keep ADRs short | LOW | [`adr-keep-adrs-short.md`](adr-keep-adrs-short.md) |
| 3 | Be honest about consequences | MEDIUM | [`adr-be-honest-about-consequences.md`](adr-be-honest-about-consequences.md) |
| 4 | Never delete ADRs | CRITICAL | [`adr-never-delete-adrs.md`](adr-never-delete-adrs.md) |
| 5 | Number sequentially | CRITICAL | [`adr-number-sequentially.md`](adr-number-sequentially.md) |
| 6 | Use active voice in the Decision section | MEDIUM | [`adr-use-active-voice-in-the-decision-section.md`](adr-use-active-voice-in-the-decision-section.md) |
| 7 | Link ADRs to each other | MEDIUM | [`adr-link-adrs-to-each-other.md`](adr-link-adrs-to-each-other.md) |
| 8 | Store ADRs in the repository | MEDIUM | [`adr-store-adrs-in-the-repository.md`](adr-store-adrs-in-the-repository.md) |
| 9 | Review ADRs in pull requests | MEDIUM | [`adr-review-adrs-in-pull-requests.md`](adr-review-adrs-in-pull-requests.md) |
| 10 | Include decision drivers | MEDIUM | [`adr-include-decision-drivers.md`](adr-include-decision-drivers.md) |
| 11 | Revisit ADRs periodically | MEDIUM | [`adr-revisit-adrs-periodically.md`](adr-revisit-adrs-periodically.md) |
| 12 | Use a consistent template | MEDIUM | [`adr-use-a-consistent-template.md`](adr-use-a-consistent-template.md) |

---

---
title: "Be honest about consequences"
impact: MEDIUM
impactDescription: "general best practice"
tags: adr, specs, documentation, recording-architecture-decisions, documenting-technical-trade-offs, decision-rationale-capture
---

## Be honest about consequences

Be honest about consequences: include both positive and negative consequences. Hiding trade-offs undermines trust in the decision log.

---

---
title: "Include decision drivers"
impact: MEDIUM
impactDescription: "general best practice"
tags: adr, specs, documentation, recording-architecture-decisions, documenting-technical-trade-offs, decision-rationale-capture
---

## Include decision drivers

Include decision drivers: explicitly listing what mattered (cost, team skill, performance, time-to-market) makes the rationale transparent.

---

---
title: "Keep ADRs short"
impact: LOW
impactDescription: "recommended but situational"
tags: adr, specs, documentation, recording-architecture-decisions, documenting-technical-trade-offs, decision-rationale-capture
---

## Keep ADRs short

Keep ADRs short: an ADR should be readable in 5 minutes. If it needs more than 2 pages, consider whether it should be an RFC or TRD instead.

---

---
title: "Link ADRs to each other"
impact: MEDIUM
impactDescription: "general best practice"
tags: adr, specs, documentation, recording-architecture-decisions, documenting-technical-trade-offs, decision-rationale-capture
---

## Link ADRs to each other

Link ADRs to each other: decisions often build on or relate to previous decisions. Cross-references create a navigable decision graph.

---

---
title: "Never delete ADRs"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: adr, specs, documentation, recording-architecture-decisions, documenting-technical-trade-offs, decision-rationale-capture
---

## Never delete ADRs

ADRs are immutable records. Supersede or deprecate them, but never delete them. The history matters.

---

---
title: "Number sequentially"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: adr, specs, documentation, recording-architecture-decisions, documenting-technical-trade-offs, decision-rationale-capture
---

## Number sequentially

Number sequentially: do not reuse numbers. Gaps in numbering are fine (they indicate deleted drafts or abandoned proposals).

---

---
title: "Review ADRs in pull requests"
impact: MEDIUM
impactDescription: "general best practice"
tags: adr, specs, documentation, recording-architecture-decisions, documenting-technical-trade-offs, decision-rationale-capture
---

## Review ADRs in pull requests

Review ADRs in pull requests: treat ADRs as code. The team should review and approve decisions before they are accepted.

---

---
title: "Revisit ADRs periodically"
impact: MEDIUM
impactDescription: "general best practice"
tags: adr, specs, documentation, recording-architecture-decisions, documenting-technical-trade-offs, decision-rationale-capture
---

## Revisit ADRs periodically

Revisit ADRs periodically: during architecture reviews, check if accepted ADRs still hold. If the context has changed, write a new ADR.

---

---
title: "Store ADRs in the repository"
impact: MEDIUM
impactDescription: "general best practice"
tags: adr, specs, documentation, recording-architecture-decisions, documenting-technical-trade-offs, decision-rationale-capture
---

## Store ADRs in the repository

ADRs should live alongside the code they describe, versioned in Git, and reviewed in pull requests.

---

---
title: "Use a consistent template"
impact: MEDIUM
impactDescription: "general best practice"
tags: adr, specs, documentation, recording-architecture-decisions, documenting-technical-trade-offs, decision-rationale-capture
---

## Use a consistent template

Use a consistent template: adopt either Nygard or MADR and stick with it across the project for uniformity.

---

---
title: "Use active voice in the Decision section"
impact: MEDIUM
impactDescription: "general best practice"
tags: adr, specs, documentation, recording-architecture-decisions, documenting-technical-trade-offs, decision-rationale-capture
---

## Use active voice in the Decision section

"We will use PostgreSQL" is clearer than "PostgreSQL was selected."

---

---
title: "Write ADRs at decision time"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: adr, specs, documentation, recording-architecture-decisions, documenting-technical-trade-offs, decision-rationale-capture
---

## Write ADRs at decision time

Write ADRs at decision time: do not try to reconstruct decisions retroactively. The context is freshest when the decision is made.

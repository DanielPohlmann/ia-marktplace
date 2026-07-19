# RFC (Request for Comments) Rules

Best practices and rules for RFC (Request for Comments).

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Start with the problem, not the solution | MEDIUM | [`rfc-start-with-the-problem-not-the-solution.md`](rfc-start-with-the-problem-not-the-solution.md) |
| 2 | Always include "Do Nothing" as an alternative | CRITICAL | [`rfc-always-include-do-nothing-as-an-alternative.md`](rfc-always-include-do-nothing-as-an-alternative.md) |
| 3 | Be specific about trade-offs | MEDIUM | [`rfc-be-specific-about-trade-offs.md`](rfc-be-specific-about-trade-offs.md) |
| 4 | Set a review deadline | HIGH | [`rfc-set-a-review-deadline.md`](rfc-set-a-review-deadline.md) |
| 5 | Designate a decision-maker | CRITICAL | [`rfc-designate-a-decision-maker.md`](rfc-designate-a-decision-maker.md) |
| 6 | Address all review comments | MEDIUM | [`rfc-address-all-review-comments.md`](rfc-address-all-review-comments.md) |
| 7 | Convert accepted RFCs into ADRs | CRITICAL | [`rfc-convert-accepted-rfcs-into-adrs.md`](rfc-convert-accepted-rfcs-into-adrs.md) |
| 8 | Keep RFCs scoped | MEDIUM | [`rfc-keep-rfcs-scoped.md`](rfc-keep-rfcs-scoped.md) |
| 9 | Include a migration strategy | MEDIUM | [`rfc-include-a-migration-strategy.md`](rfc-include-a-migration-strategy.md) |
| 10 | Use diagrams liberally | MEDIUM | [`rfc-use-diagrams-liberally.md`](rfc-use-diagrams-liberally.md) |
| 11 | Write for a skeptical reader | MEDIUM | [`rfc-write-for-a-skeptical-reader.md`](rfc-write-for-a-skeptical-reader.md) |
| 12 | Prototype when possible | MEDIUM | [`rfc-prototype-when-possible.md`](rfc-prototype-when-possible.md) |

---

---
title: "Address all review comments"
impact: MEDIUM
impactDescription: "general best practice"
tags: rfc, specs, documentation, design-proposals, technical-change-proposals, architecture-proposals-seeking-feedback
---

## Address all review comments

Address all review comments: even if you disagree, explain your reasoning. Unaddressed comments signal that feedback is not valued.

---

---
title: "Always include \"Do Nothing\" as an alternative"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: rfc, specs, documentation, design-proposals, technical-change-proposals, architecture-proposals-seeking-feedback
---

## Always include "Do Nothing" as an alternative

Always include "Do Nothing" as an alternative: explicitly documenting the cost of inaction gives reviewers a baseline for comparison.

---

---
title: "Be specific about trade-offs"
impact: MEDIUM
impactDescription: "general best practice"
tags: rfc, specs, documentation, design-proposals, technical-change-proposals, architecture-proposals-seeking-feedback
---

## Be specific about trade-offs

Be specific about trade-offs: every design decision has trade-offs. Acknowledging them builds trust and invites constructive feedback.

---

---
title: "Convert accepted RFCs into ADRs"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: rfc, specs, documentation, design-proposals, technical-change-proposals, architecture-proposals-seeking-feedback
---

## Convert accepted RFCs into ADRs

Convert accepted RFCs into ADRs: the RFC captures the discussion; the ADR captures the decision. Do not skip the ADR step.

---

---
title: "Designate a decision-maker"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: rfc, specs, documentation, design-proposals, technical-change-proposals, architecture-proposals-seeking-feedback
---

## Designate a decision-maker

Designate a decision-maker: someone (tech lead, architecture council) must have the authority to make the final call. Consensus is ideal but not always achievable.

---

---
title: "Include a migration strategy"
impact: MEDIUM
impactDescription: "general best practice"
tags: rfc, specs, documentation, design-proposals, technical-change-proposals, architecture-proposals-seeking-feedback
---

## Include a migration strategy

Include a migration strategy: proposals that address how to get from here to there are far more likely to be accepted than those that only describe the end state.

---

---
title: "Keep RFCs scoped"
impact: MEDIUM
impactDescription: "general best practice"
tags: rfc, specs, documentation, design-proposals, technical-change-proposals, architecture-proposals-seeking-feedback
---

## Keep RFCs scoped

Keep RFCs scoped: an RFC that tries to solve everything at once is harder to review and more likely to be rejected. Break large proposals into focused RFCs.

---

---
title: "Prototype when possible"
impact: MEDIUM
impactDescription: "general best practice"
tags: rfc, specs, documentation, design-proposals, technical-change-proposals, architecture-proposals-seeking-feedback
---

## Prototype when possible

Prototype when possible: a working spike alongside the RFC dramatically increases confidence in the proposal.

---

---
title: "Set a review deadline"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: rfc, specs, documentation, design-proposals, technical-change-proposals, architecture-proposals-seeking-feedback
---

## Set a review deadline

Set a review deadline: without a deadline, RFCs linger indefinitely. A clear deadline (e.g., 5-10 business days) ensures timely decisions.

---

---
title: "Start with the problem, not the solution"
impact: MEDIUM
impactDescription: "general best practice"
tags: rfc, specs, documentation, design-proposals, technical-change-proposals, architecture-proposals-seeking-feedback
---

## Start with the problem, not the solution

Start with the problem, not the solution: the Motivation section should clearly explain why the change is needed. If the problem is not compelling, the solution does not matter.

---

---
title: "Use diagrams liberally"
impact: MEDIUM
impactDescription: "general best practice"
tags: rfc, specs, documentation, design-proposals, technical-change-proposals, architecture-proposals-seeking-feedback
---

## Use diagrams liberally

Use diagrams liberally: architecture diagrams, sequence diagrams, and data flow diagrams make proposals easier to understand and review.

---

---
title: "Write for a skeptical reader"
impact: MEDIUM
impactDescription: "general best practice"
tags: rfc, specs, documentation, design-proposals, technical-change-proposals, architecture-proposals-seeking-feedback
---

## Write for a skeptical reader

Write for a skeptical reader: assume the reviewer's first reaction is "why should we change what works?" and address that concern proactively.

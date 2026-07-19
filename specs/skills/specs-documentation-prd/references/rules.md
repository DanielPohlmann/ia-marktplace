# PRD (Product Requirements Document) Rules

Best practices and rules for PRD (Product Requirements Document).

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Start with the problem, not the solution | MEDIUM | [`prd-start-with-the-problem-not-the-solution.md`](prd-start-with-the-problem-not-the-solution.md) |
| 2 | Be specific about non-goals | HIGH | [`prd-be-specific-about-non-goals.md`](prd-be-specific-about-non-goals.md) |
| 3 | Make success metrics measurable | MEDIUM | [`prd-make-success-metrics-measurable.md`](prd-make-success-metrics-measurable.md) |
| 4 | Write user stories from the user's perspective | HIGH | [`prd-write-user-stories-from-the-user-s-perspective.md`](prd-write-user-stories-from-the-user-s-perspective.md) |
| 5 | Include acceptance criteria for every user story | MEDIUM | [`prd-include-acceptance-criteria-for-every-user-story.md`](prd-include-acceptance-criteria-for-every-user-story.md) |
| 6 | Prioritize ruthlessly | CRITICAL | [`prd-prioritize-ruthlessly.md`](prd-prioritize-ruthlessly.md) |
| 7 | Keep the PRD living | HIGH | [`prd-keep-the-prd-living.md`](prd-keep-the-prd-living.md) |
| 8 | Separate functional from non-functional requirements | CRITICAL | [`prd-separate-functional-from-non-functional-requirements.md`](prd-separate-functional-from-non-functional-requirements.md) |
| 9 | Link to related documents | MEDIUM | [`prd-link-to-related-documents.md`](prd-link-to-related-documents.md) |
| 10 | Resolve open questions before development starts | MEDIUM | [`prd-resolve-open-questions-before-development-starts.md`](prd-resolve-open-questions-before-development-starts.md) |
| 11 | Review with all stakeholders | MEDIUM | [`prd-review-with-all-stakeholders.md`](prd-review-with-all-stakeholders.md) |

---

---
title: "Be specific about non-goals"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: prd, specs, documentation, product-requirements, feature-specifications, user-stories
---

## Be specific about non-goals

Be specific about non-goals: explicitly stating what you will *not* build prevents scope creep and misaligned expectations.

---

---
title: "Include acceptance criteria for every user story"
impact: MEDIUM
impactDescription: "general best practice"
tags: prd, specs, documentation, product-requirements, feature-specifications, user-stories
---

## Include acceptance criteria for every user story

Include acceptance criteria for every user story: without testable criteria, it is impossible to know when a story is done.

---

---
title: "Keep the PRD living"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: prd, specs, documentation, product-requirements, feature-specifications, user-stories
---

## Keep the PRD living

Keep the PRD living: update the document as requirements evolve. A stale PRD is worse than no PRD because it actively misleads.

---

---
title: "Link to related documents"
impact: MEDIUM
impactDescription: "general best practice"
tags: prd, specs, documentation, product-requirements, feature-specifications, user-stories
---

## Link to related documents

Link to related documents: reference the BRD for business context, ADRs for architectural decisions, and the TRD for technical design.

---

---
title: "Make success metrics measurable"
impact: MEDIUM
impactDescription: "general best practice"
tags: prd, specs, documentation, product-requirements, feature-specifications, user-stories
---

## Make success metrics measurable

"improve user experience" is not a metric. "Reduce checkout abandonment rate from 68% to 45%" is.

---

---
title: "Prioritize ruthlessly"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: prd, specs, documentation, product-requirements, feature-specifications, user-stories
---

## Prioritize ruthlessly

Prioritize ruthlessly: use MoSCoW or RICE to force trade-off decisions early. Not everything can be "Must Have."

---

---
title: "Resolve open questions before development starts"
impact: MEDIUM
impactDescription: "general best practice"
tags: prd, specs, documentation, product-requirements, feature-specifications, user-stories
---

## Resolve open questions before development starts

Resolve open questions before development starts: open questions that linger into implementation cause rework and delays.

---

---
title: "Review with all stakeholders"
impact: MEDIUM
impactDescription: "general best practice"
tags: prd, specs, documentation, product-requirements, feature-specifications, user-stories
---

## Review with all stakeholders

Review with all stakeholders: engineering, design, QA, and product should all review and approve the PRD before implementation begins.

---

---
title: "Separate functional from non-functional requirements"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: prd, specs, documentation, product-requirements, feature-specifications, user-stories
---

## Separate functional from non-functional requirements

Separate functional from non-functional requirements: performance, security, and scalability constraints deserve explicit attention.

---

---
title: "Start with the problem, not the solution"
impact: MEDIUM
impactDescription: "general best practice"
tags: prd, specs, documentation, product-requirements, feature-specifications, user-stories
---

## Start with the problem, not the solution

Start with the problem, not the solution: clearly articulate the user pain point before proposing any feature.

---

---
title: "Write user stories from the user's perspective"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: prd, specs, documentation, product-requirements, feature-specifications, user-stories
---

## Write user stories from the user's perspective

Write user stories from the user's perspective: avoid implementation language like "the system shall" in favor of "as a user, I want."

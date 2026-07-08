# SOLID Principles Rules

Best practices and rules for SOLID Principles.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Apply SOLID principles as guardrails during code review,... | MEDIUM | [`solid-apply-solid-principles-as-guardrails-during-code-review.md`](solid-apply-solid-principles-as-guardrails-during-code-review.md) |
| 2 | When you feel friction adding a feature, check which SOLID... | MEDIUM | [`solid-when-you-feel-friction-adding-a-feature-check-which-solid.md`](solid-when-you-feel-friction-adding-a-feature-check-which-solid.md) |
| 3 | Use constructor injection as the default mechanism for DIP | CRITICAL | [`solid-use-constructor-injection-as-the-default-mechanism-for-dip.md`](solid-use-constructor-injection-as-the-default-mechanism-for-dip.md) |
| 4 | Write tests first (TDD) | MEDIUM | [`solid-write-tests-first-tdd.md`](solid-write-tests-first-tdd.md) |
| 5 | Balance SOLID with YAGNI | CRITICAL | [`solid-balance-solid-with-yagni.md`](solid-balance-solid-with-yagni.md) |
| 6 | Review class names regularly | MEDIUM | [`solid-review-class-names-regularly.md`](solid-review-class-names-regularly.md) |

---

---
title: "Apply SOLID principles as guardrails during code review,..."
impact: MEDIUM
impactDescription: "general best practice"
tags: solid, dev, craftsmanship, class-design, interface-design, dependency-management
---

## Apply SOLID principles as guardrails during code review,...

Apply SOLID principles as guardrails during code review, not as upfront design mandates.

---

---
title: "Balance SOLID with YAGNI"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: solid, dev, craftsmanship, class-design, interface-design, dependency-management
---

## Balance SOLID with YAGNI

Balance SOLID with YAGNI: do not add abstractions speculatively. Introduce them when the second variation appears.

---

---
title: "Review class names regularly"
impact: MEDIUM
impactDescription: "general best practice"
tags: solid, dev, craftsmanship, class-design, interface-design, dependency-management
---

## Review class names regularly

Review class names regularly — if a class name contains "And" or "Manager" or "Service" doing too many things, SRP is likely violated.

---

---
title: "Use constructor injection as the default mechanism for DIP"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: solid, dev, craftsmanship, class-design, interface-design, dependency-management
---

## Use constructor injection as the default mechanism for DIP

Use constructor injection as the default mechanism for DIP — it makes dependencies explicit and immutable.

---

---
title: "When you feel friction adding a feature, check which SOLID..."
impact: MEDIUM
impactDescription: "general best practice"
tags: solid, dev, craftsmanship, class-design, interface-design, dependency-management
---

## When you feel friction adding a feature, check which SOLID...

When you feel friction adding a feature, check which SOLID principle is being violated.

---

---
title: "Write tests first (TDD)"
impact: MEDIUM
impactDescription: "general best practice"
tags: solid, dev, craftsmanship, class-design, interface-design, dependency-management
---

## Write tests first (TDD)

Write tests first (TDD) — SOLID violations surface quickly when code is hard to test.

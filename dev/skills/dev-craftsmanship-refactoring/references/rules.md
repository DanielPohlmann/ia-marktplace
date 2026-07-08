# Refactoring Rules

Best practices and rules for Refactoring.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Name the refactoring you are applying | MEDIUM | [`refactoring-name-the-refactoring-you-are-applying.md`](refactoring-name-the-refactoring-you-are-applying.md) |
| 2 | Commit after each successful refactoring step | MEDIUM | [`refactoring-commit-after-each-successful-refactoring-step.md`](refactoring-commit-after-each-successful-refactoring-step.md) |
| 3 | Use IDE refactoring tools (rename, extract, inline) | MEDIUM | [`refactoring-use-ide-refactoring-tools-rename-extract-inline.md`](refactoring-use-ide-refactoring-tools-rename-extract-inline.md) |
| 4 | Never refactor and change behavior in the same step | CRITICAL | [`refactoring-never-refactor-and-change-behavior-in-the-same-step.md`](refactoring-never-refactor-and-change-behavior-in-the-same-step.md) |
| 5 | Track technical debt explicitly (TODO comments, issue... | MEDIUM | [`refactoring-track-technical-debt-explicitly-todo-comments-issue.md`](refactoring-track-technical-debt-explicitly-todo-comments-issue.md) |
| 6 | Refactor toward the design you need for the next feature,... | MEDIUM | [`refactoring-refactor-toward-the-design-you-need-for-the-next-feature.md`](refactoring-refactor-toward-the-design-you-need-for-the-next-feature.md) |
| 7 | Pair on refactoring when possible | MEDIUM | [`refactoring-pair-on-refactoring-when-possible.md`](refactoring-pair-on-refactoring-when-possible.md) |
| 8 | If a refactoring takes more than an hour without... | LOW | [`refactoring-if-a-refactoring-takes-more-than-an-hour-without.md`](refactoring-if-a-refactoring-takes-more-than-an-hour-without.md) |

---

---
title: "Commit after each successful refactoring step"
impact: MEDIUM
impactDescription: "general best practice"
tags: refactoring, dev, craftsmanship, code-smell-identification, refactoring-technique-selection, safe-code-transformation
---

## Commit after each successful refactoring step

Commit after each successful refactoring step. Small commits make bisecting safe.

---

---
title: "If a refactoring takes more than an hour without..."
impact: LOW
impactDescription: "recommended but situational"
tags: refactoring, dev, craftsmanship, code-smell-identification, refactoring-technique-selection, safe-code-transformation
---

## If a refactoring takes more than an hour without...

If a refactoring takes more than an hour without completing, break it into smaller steps or reconsider the approach.

---

---
title: "Name the refactoring you are applying"
impact: MEDIUM
impactDescription: "general best practice"
tags: refactoring, dev, craftsmanship, code-smell-identification, refactoring-technique-selection, safe-code-transformation
---

## Name the refactoring you are applying

Name the refactoring you are applying. "I am doing an Extract Method" is clearer than "I am cleaning up this code."

---

---
title: "Never refactor and change behavior in the same step"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: refactoring, dev, craftsmanship, code-smell-identification, refactoring-technique-selection, safe-code-transformation
---

## Never refactor and change behavior in the same step

Never refactor and change behavior in the same step. Separate the two activities with separate commits.

---

---
title: "Pair on refactoring when possible"
impact: MEDIUM
impactDescription: "general best practice"
tags: refactoring, dev, craftsmanship, code-smell-identification, refactoring-technique-selection, safe-code-transformation
---

## Pair on refactoring when possible

Pair on refactoring when possible — two sets of eyes catch more unintended behavior changes.

---

---
title: "Refactor toward the design you need for the next feature,..."
impact: MEDIUM
impactDescription: "general best practice"
tags: refactoring, dev, craftsmanship, code-smell-identification, refactoring-technique-selection, safe-code-transformation
---

## Refactor toward the design you need for the next feature,...

Refactor toward the design you need for the next feature, not toward a theoretically ideal design.

---

---
title: "Track technical debt explicitly (TODO comments, issue..."
impact: MEDIUM
impactDescription: "general best practice"
tags: refactoring, dev, craftsmanship, code-smell-identification, refactoring-technique-selection, safe-code-transformation
---

## Track technical debt explicitly (TODO comments, issue...

Track technical debt explicitly (TODO comments, issue tracker) so refactoring is planned, not ad hoc.

---

---
title: "Use IDE refactoring tools (rename, extract, inline)"
impact: MEDIUM
impactDescription: "general best practice"
tags: refactoring, dev, craftsmanship, code-smell-identification, refactoring-technique-selection, safe-code-transformation
---

## Use IDE refactoring tools (rename, extract, inline)

Use IDE refactoring tools (rename, extract, inline) — they automate the mechanics and reduce errors.

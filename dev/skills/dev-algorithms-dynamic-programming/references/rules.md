# Dynamic Programming Rules

Best practices and rules for Dynamic Programming.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Always verify optimal substructure before applying DP --... | CRITICAL | [`dynamic-programming-always-verify-optimal-substructure-before-applying-dp.md`](dynamic-programming-always-verify-optimal-substructure-before-applying-dp.md) |
| 2 | Define your state precisely and minimally -- extra state... | MEDIUM | [`dynamic-programming-define-your-state-precisely-and-minimally-extra-state.md`](dynamic-programming-define-your-state-precisely-and-minimally-extra-state.md) |
| 3 | Validate your recurrence with small examples before coding | HIGH | [`dynamic-programming-validate-your-recurrence-with-small-examples-before-coding.md`](dynamic-programming-validate-your-recurrence-with-small-examples-before-coding.md) |
| 4 | Consider whether the problem admits a greedy solution... | LOW | [`dynamic-programming-consider-whether-the-problem-admits-a-greedy-solution.md`](dynamic-programming-consider-whether-the-problem-admits-a-greedy-solution.md) |
| 5 | For interview/competition settings, practice identifying... | MEDIUM | [`dynamic-programming-for-interview-competition-settings-practice-identifying.md`](dynamic-programming-for-interview-competition-settings-practice-identifying.md) |
| 6 | Reference Knuth's TAOCP for mathematical rigor on sequence... | MEDIUM | [`dynamic-programming-reference-knuth-s-taocp-for-mathematical-rigor-on-sequence.md`](dynamic-programming-reference-knuth-s-taocp-for-mathematical-rigor-on-sequence.md) |

---

---
title: "Always verify optimal substructure before applying DP --..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: dynamic-programming, dev, algorithms, optimization-problems-with-overlapping-subproblems, memoization-strategies, tabulation-approaches
---

## Always verify optimal substructure before applying DP --...

Always verify optimal substructure before applying DP -- not all optimization problems have it (greedy or exhaustive search may be required instead).

---

---
title: "Consider whether the problem admits a greedy solution..."
impact: LOW
impactDescription: "recommended but situational"
tags: dynamic-programming, dev, algorithms, optimization-problems-with-overlapping-subproblems, memoization-strategies, tabulation-approaches
---

## Consider whether the problem admits a greedy solution...

Consider whether the problem admits a greedy solution (simpler) before committing to DP.

---

---
title: "Define your state precisely and minimally -- extra state..."
impact: MEDIUM
impactDescription: "general best practice"
tags: dynamic-programming, dev, algorithms, optimization-problems-with-overlapping-subproblems, memoization-strategies, tabulation-approaches
---

## Define your state precisely and minimally -- extra state...

Define your state precisely and minimally -- extra state dimensions explode the table size.

---

---
title: "For interview/competition settings, practice identifying..."
impact: MEDIUM
impactDescription: "general best practice"
tags: dynamic-programming, dev, algorithms, optimization-problems-with-overlapping-subproblems, memoization-strategies, tabulation-approaches
---

## For interview/competition settings, practice identifying...

For interview/competition settings, practice identifying the state and recurrence quickly -- the implementation follows mechanically.

---

---
title: "Reference Knuth's TAOCP for mathematical rigor on sequence..."
impact: MEDIUM
impactDescription: "general best practice"
tags: dynamic-programming, dev, algorithms, optimization-problems-with-overlapping-subproblems, memoization-strategies, tabulation-approaches
---

## Reference Knuth's TAOCP for mathematical rigor on sequence...

Reference Knuth's TAOCP for mathematical rigor on sequence problems, optimal search trees, and combinatorial optimization where DP techniques apply.

---

---
title: "Validate your recurrence with small examples before coding"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: dynamic-programming, dev, algorithms, optimization-problems-with-overlapping-subproblems, memoization-strategies, tabulation-approaches
---

## Validate your recurrence with small examples before coding

Validate your recurrence with small examples before coding.

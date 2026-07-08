# Combinatorial Algorithms Rules

Best practices and rules for Combinatorial Algorithms.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Always add pruning to backtracking -- even simple... | CRITICAL | [`combinatorial-always-add-pruning-to-backtracking-even-simple.md`](combinatorial-always-add-pruning-to-backtracking-even-simple.md) |
| 2 | For optimization problems, consider branch and bound before... | LOW | [`combinatorial-for-optimization-problems-consider-branch-and-bound-before.md`](combinatorial-for-optimization-problems-consider-branch-and-bound-before.md) |
| 3 | Use constraint propagation (forward checking, arc... | MEDIUM | [`combinatorial-use-constraint-propagation-forward-checking-arc.md`](combinatorial-use-constraint-propagation-forward-checking-arc.md) |
| 4 | Choose variable and value ordering heuristics carefully --... | MEDIUM | [`combinatorial-choose-variable-and-value-ordering-heuristics-carefully.md`](combinatorial-choose-variable-and-value-ordering-heuristics-carefully.md) |
| 5 | Consider whether the problem has symmetries that can be... | HIGH | [`combinatorial-consider-whether-the-problem-has-symmetries-that-can-be.md`](combinatorial-consider-whether-the-problem-has-symmetries-that-can-be.md) |
| 6 | For problems with overlapping subproblems (e | MEDIUM | [`combinatorial-for-problems-with-overlapping-subproblems-e.md`](combinatorial-for-problems-with-overlapping-subproblems-e.md) |
| 7 | Reference Knuth's TAOCP Vol | MEDIUM | [`combinatorial-reference-knuth-s-taocp-vol.md`](combinatorial-reference-knuth-s-taocp-vol.md) |

---

---
title: "Always add pruning to backtracking -- even simple..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: combinatorial, dev, algorithms, permutation-and-combination-generation, backtracking-algorithm-design, constraint-satisfaction-problems
---

## Always add pruning to backtracking -- even simple...

Always add pruning to backtracking -- even simple feasibility checks can reduce runtime by orders of magnitude.

---

---
title: "Choose variable and value ordering heuristics carefully --..."
impact: MEDIUM
impactDescription: "general best practice"
tags: combinatorial, dev, algorithms, permutation-and-combination-generation, backtracking-algorithm-design, constraint-satisfaction-problems
---

## Choose variable and value ordering heuristics carefully --...

Choose variable and value ordering heuristics carefully -- MRV and LCV are strong general-purpose strategies.

---

---
title: "Consider whether the problem has symmetries that can be..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: combinatorial, dev, algorithms, permutation-and-combination-generation, backtracking-algorithm-design, constraint-satisfaction-problems
---

## Consider whether the problem has symmetries that can be...

Consider whether the problem has symmetries that can be exploited to avoid redundant exploration.

---

---
title: "For optimization problems, consider branch and bound before..."
impact: LOW
impactDescription: "recommended but situational"
tags: combinatorial, dev, algorithms, permutation-and-combination-generation, backtracking-algorithm-design, constraint-satisfaction-problems
---

## For optimization problems, consider branch and bound before...

For optimization problems, consider branch and bound before exhaustive enumeration.

---

---
title: "For problems with overlapping subproblems (e"
impact: MEDIUM
impactDescription: "general best practice"
tags: combinatorial, dev, algorithms, permutation-and-combination-generation, backtracking-algorithm-design, constraint-satisfaction-problems
---

## For problems with overlapping subproblems (e

For problems with overlapping subproblems (e.g., subset sum, TSP), combine backtracking with dynamic programming.

---

---
title: "Reference Knuth's TAOCP Vol"
impact: MEDIUM
impactDescription: "general best practice"
tags: combinatorial, dev, algorithms, permutation-and-combination-generation, backtracking-algorithm-design, constraint-satisfaction-problems
---

## Reference Knuth's TAOCP Vol

Reference Knuth's TAOCP Vol. 4A for the most rigorous and comprehensive treatment of combinatorial generation and backtracking, including Algorithm X and dancing links for exact cover problems.

---

---
title: "Use constraint propagation (forward checking, arc..."
impact: MEDIUM
impactDescription: "general best practice"
tags: combinatorial, dev, algorithms, permutation-and-combination-generation, backtracking-algorithm-design, constraint-satisfaction-problems
---

## Use constraint propagation (forward checking, arc...

Use constraint propagation (forward checking, arc consistency) for CSPs to reduce the effective search space.

---
name: dev-algorithms-combinatorial
description: Use when solving permutation, combination, backtracking, branch-and-bound, or constraint-satisfaction problems. USE FOR: subset enumeration, N-Queens/Sudoku-style search, pruning strategies, generating functions. DO NOT USE FOR: graph traversal (use dev-algorithms-graph-algorithms), overlapping subproblems (use dev-algorithms-dynamic-programming).
---

# Combinatorial Algorithms

## Overview
Combinatorial algorithms deal with counting, generating, and optimizing discrete structures -- permutations, combinations, subsets, partitions, and arrangements subject to constraints. Knuth devoted *The Art of Computer Programming, Volume 4A: Combinatorial Algorithms, Part 1* entirely to this topic, calling combinatorics "the mathematics of choice." This skill covers the core techniques for systematic enumeration, backtracking search, and constraint satisfaction.

## Subset Generation

### Iterative (Bitmask) Approach
Generate all 2^n subsets by iterating from 0 to 2^n - 1, where each bit indicates inclusion/exclusion.

```
GENERATE_SUBSETS(S):
    n = |S|
    for mask = 0 to 2^n - 1:
        subset = {S[i] for each bit i set in mask}
        process(subset)
```

### Recursive Approach
For each element, recursively generate subsets that include it and subsets that exclude it.

```
SUBSETS(S, index, current):
    if index == |S|:
        process(current)
        return
    SUBSETS(S, index + 1, current)              // exclude S[index]
    SUBSETS(S, index + 1, current + {S[index]}) // include S[index]
```

## Best Practices

- Always add pruning to backtracking -- even simple feasibility checks can reduce runtime by orders of magnitude.
- For optimization problems, consider branch and bound before exhaustive enumeration.
- Use constraint propagation (forward checking, arc consistency) for CSPs to reduce the effective search space.
- Choose variable and value ordering heuristics carefully -- MRV and LCV are strong general-purpose strategies.
- Consider whether the problem has symmetries that can be exploited to avoid redundant exploration.
- For problems with overlapping subproblems (e.g., subset sum, TSP), combine backtracking with dynamic programming.
- Reference Knuth's TAOCP Vol. 4A for the most rigorous and comprehensive treatment of combinatorial generation and backtracking, including Algorithm X and dancing links for exact cover problems.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/details.md](references/details.md) | Fundamental Counting; Backtracking; Classic Backtracking Problems; Branch and Bound; Constraint Satisfaction Problems (CSP); Generating Functions (Conceptual); Pruning Strategies; Complexity of Combinatorial Problems; Knuth's TAOCP Vol. 4A: Key Topics |

## References

- [The Art of Computer Programming, Vol. 4A: Combinatorial Algorithms — Donald Knuth](https://www-cs-faculty.stanford.edu/~knuth/taocp.html)
- [Combinatorial Optimization — Wikipedia](https://en.wikipedia.org/wiki/Combinatorial_optimization)

See references/rules.md for the full rule catalog.

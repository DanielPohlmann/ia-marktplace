# Graph Algorithms Rules

Best practices and rules for Graph Algorithms.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Always choose the simplest algorithm that handles your... | CRITICAL | [`graph-algorithms-always-choose-the-simplest-algorithm-that-handles-your.md`](graph-algorithms-always-choose-the-simplest-algorithm-that-handles-your.md) |
| 2 | For sparse graphs, adjacency list representation is almost... | CRITICAL | [`graph-algorithms-for-sparse-graphs-adjacency-list-representation-is-almost.md`](graph-algorithms-for-sparse-graphs-adjacency-list-representation-is-almost.md) |
| 3 | When implementing Kruskal's, always use Union-Find with... | CRITICAL | [`graph-algorithms-when-implementing-kruskal-s-always-use-union-find-with.md`](graph-algorithms-when-implementing-kruskal-s-always-use-union-find-with.md) |
| 4 | For A*, invest time in designing a good heuristic -- the... | MEDIUM | [`graph-algorithms-for-a-invest-time-in-designing-a-good-heuristic-the.md`](graph-algorithms-for-a-invest-time-in-designing-a-good-heuristic-the.md) |
| 5 | Consider whether the graph is a DAG -- many problems... | LOW | [`graph-algorithms-consider-whether-the-graph-is-a-dag-many-problems.md`](graph-algorithms-consider-whether-the-graph-is-a-dag-many-problems.md) |
| 6 | Reference Knuth's TAOCP for rigorous mathematical analysis... | MEDIUM | [`graph-algorithms-reference-knuth-s-taocp-for-rigorous-mathematical-analysis.md`](graph-algorithms-reference-knuth-s-taocp-for-rigorous-mathematical-analysis.md) |

---

---
title: "Always choose the simplest algorithm that handles your..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: graph-algorithms, dev, algorithms, graph-traversal, shortest-path-computation, minimum-spanning-tree-construction
---

## Always choose the simplest algorithm that handles your...

Always choose the simplest algorithm that handles your constraints: BFS for unweighted shortest paths, Dijkstra for non-negative weights, Bellman-Ford only when negative weights are present.

---

---
title: "Consider whether the graph is a DAG -- many problems..."
impact: LOW
impactDescription: "recommended but situational"
tags: graph-algorithms, dev, algorithms, graph-traversal, shortest-path-computation, minimum-spanning-tree-construction
---

## Consider whether the graph is a DAG -- many problems...

Consider whether the graph is a DAG -- many problems simplify dramatically on acyclic graphs (shortest paths become linear time via topological order relaxation).

---

---
title: "For A*, invest time in designing a good heuristic -- the..."
impact: MEDIUM
impactDescription: "general best practice"
tags: graph-algorithms, dev, algorithms, graph-traversal, shortest-path-computation, minimum-spanning-tree-construction
---

## For A*, invest time in designing a good heuristic -- the...

For A*, invest time in designing a good heuristic -- the quality of the heuristic determines practical performance.

---

---
title: "For sparse graphs, adjacency list representation is almost..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: graph-algorithms, dev, algorithms, graph-traversal, shortest-path-computation, minimum-spanning-tree-construction
---

## For sparse graphs, adjacency list representation is almost...

For sparse graphs, adjacency list representation is almost always preferred. Use adjacency matrices only for dense graphs or when edge-existence queries dominate.

---

---
title: "Reference Knuth's TAOCP for rigorous mathematical analysis..."
impact: MEDIUM
impactDescription: "general best practice"
tags: graph-algorithms, dev, algorithms, graph-traversal, shortest-path-computation, minimum-spanning-tree-construction
---

## Reference Knuth's TAOCP for rigorous mathematical analysis...

Reference Knuth's TAOCP for rigorous mathematical analysis of graph traversal, network flows, and combinatorial graph structures.

---

---
title: "When implementing Kruskal's, always use Union-Find with..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: graph-algorithms, dev, algorithms, graph-traversal, shortest-path-computation, minimum-spanning-tree-construction
---

## When implementing Kruskal's, always use Union-Find with...

When implementing Kruskal's, always use Union-Find with path compression and union by rank for near-constant-time operations.

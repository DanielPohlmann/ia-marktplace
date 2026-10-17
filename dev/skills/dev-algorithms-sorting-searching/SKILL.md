---
name: dev-algorithms-sorting-searching
description: Use when selecting or implementing sorting or searching algorithms. USE FOR: quicksort/mergesort/heapsort/timsort, counting/radix/bucket sort, stability, binary search variants, two pointers, sliding window. DO NOT USE FOR: graph search (use dev-algorithms-graph-algorithms), data structure selection (use dev-algorithms-data-structures).
---

# Sorting & Searching Algorithms

## Overview
Sorting and searching are among the most fundamental operations in computer science. Knuth dedicated the entirety of *The Art of Computer Programming, Volume 3: Sorting and Searching* to these topics, reflecting their importance and depth. This skill covers the major algorithms in both categories, their complexities, and guidance on when to use each.

## Stability in Sorting

A sort is **stable** if elements with equal keys retain their original relative order after sorting. Stability matters when:
- Sorting by multiple keys (sort by secondary key first, then by primary key with a stable sort).
- Preserving meaningful insertion order.
- Composing sorts for multi-level ordering.

## Best Practices

- Use your language's built-in sort (typically Timsort or Introsort) unless you have a specific reason not to -- they are highly optimized.
- For searching in a sorted collection, always prefer binary search over linear search.
- Consider the two pointers technique before reaching for nested loops on sorted data.
- The sliding window technique converts many O(n^2) brute-force subarray problems into O(n).
- When data has bounded integer keys, consider counting or radix sort for linear-time performance.
- Reference Knuth's TAOCP Vol. 3 for rigorous analysis of any sorting or searching method.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/sorting-algorithms.md](references/sorting-algorithms.md) | Sorting Algorithms — Comparison Sorts, Linear Sorts, Sorting Complexity Comparison, When to Use Which Sort |
| [references/searching-algorithms.md](references/searching-algorithms.md) | Searching Algorithms — Binary Search, Interpolation Search, Two Pointers Technique, Sliding Window Technique, Searching Complexity Comparison |

## References

- [The Art of Computer Programming, Vol. 3: Sorting and Searching — Donald Knuth](https://www-cs-faculty.stanford.edu/~knuth/taocp.html)
- [Sorting Algorithm — Wikipedia](https://en.wikipedia.org/wiki/Sorting_algorithm)

See references/rules.md for the full rule catalog.

# Sorting & Searching Algorithms Rules

Best practices and rules for Sorting & Searching Algorithms.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Use your language's built-in sort (typically Timsort or... | MEDIUM | [`sorting-searching-use-your-language-s-built-in-sort-typically-timsort-or.md`](sorting-searching-use-your-language-s-built-in-sort-typically-timsort-or.md) |
| 2 | For searching in a sorted collection, always prefer binary... | CRITICAL | [`sorting-searching-for-searching-in-a-sorted-collection-always-prefer-binary.md`](sorting-searching-for-searching-in-a-sorted-collection-always-prefer-binary.md) |
| 3 | Consider the two pointers technique before reaching for... | LOW | [`sorting-searching-consider-the-two-pointers-technique-before-reaching-for.md`](sorting-searching-consider-the-two-pointers-technique-before-reaching-for.md) |
| 4 | The sliding window technique converts many O(n^2)... | MEDIUM | [`sorting-searching-the-sliding-window-technique-converts-many-o-n-2.md`](sorting-searching-the-sliding-window-technique-converts-many-o-n-2.md) |
| 5 | When data has bounded integer keys, consider counting or... | LOW | [`sorting-searching-when-data-has-bounded-integer-keys-consider-counting-or.md`](sorting-searching-when-data-has-bounded-integer-keys-consider-counting-or.md) |
| 6 | Reference Knuth's TAOCP Vol | MEDIUM | [`sorting-searching-reference-knuth-s-taocp-vol.md`](sorting-searching-reference-knuth-s-taocp-vol.md) |

---

---
title: "Consider the two pointers technique before reaching for..."
impact: LOW
impactDescription: "recommended but situational"
tags: sorting-searching, dev, algorithms, sorting-algorithm-selection, searching-algorithm-selection, understanding-sort-stability
---

## Consider the two pointers technique before reaching for...

Consider the two pointers technique before reaching for nested loops on sorted data.

---

---
title: "For searching in a sorted collection, always prefer binary..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: sorting-searching, dev, algorithms, sorting-algorithm-selection, searching-algorithm-selection, understanding-sort-stability
---

## For searching in a sorted collection, always prefer binary...

For searching in a sorted collection, always prefer binary search over linear search.

---

---
title: "Reference Knuth's TAOCP Vol"
impact: MEDIUM
impactDescription: "general best practice"
tags: sorting-searching, dev, algorithms, sorting-algorithm-selection, searching-algorithm-selection, understanding-sort-stability
---

## Reference Knuth's TAOCP Vol

Reference Knuth's TAOCP Vol. 3 for rigorous analysis of any sorting or searching method.

---

---
title: "The sliding window technique converts many O(n^2)..."
impact: MEDIUM
impactDescription: "general best practice"
tags: sorting-searching, dev, algorithms, sorting-algorithm-selection, searching-algorithm-selection, understanding-sort-stability
---

## The sliding window technique converts many O(n^2)...

The sliding window technique converts many O(n^2) brute-force subarray problems into O(n).

---

---
title: "Use your language's built-in sort (typically Timsort or..."
impact: MEDIUM
impactDescription: "general best practice"
tags: sorting-searching, dev, algorithms, sorting-algorithm-selection, searching-algorithm-selection, understanding-sort-stability
---

## Use your language's built-in sort (typically Timsort or...

Use your language's built-in sort (typically Timsort or Introsort) unless you have a specific reason not to -- they are highly optimized.

---

---
title: "When data has bounded integer keys, consider counting or..."
impact: LOW
impactDescription: "recommended but situational"
tags: sorting-searching, dev, algorithms, sorting-algorithm-selection, searching-algorithm-selection, understanding-sort-stability
---

## When data has bounded integer keys, consider counting or...

When data has bounded integer keys, consider counting or radix sort for linear-time performance.

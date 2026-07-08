# Data Structures Rules

Best practices and rules for Data Structures.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Choose the data structure based on the dominant operation... | MEDIUM | [`data-structures-choose-the-data-structure-based-on-the-dominant-operation.md`](data-structures-choose-the-data-structure-based-on-the-dominant-operation.md) |
| 2 | Prefer standard library implementations -- they are... | LOW | [`data-structures-prefer-standard-library-implementations-they-are.md`](data-structures-prefer-standard-library-implementations-they-are.md) |
| 3 | Consider cache locality | LOW | [`data-structures-consider-cache-locality.md`](data-structures-consider-cache-locality.md) |
| 4 | For concurrent access, consider concurrent variants... | LOW | [`data-structures-for-concurrent-access-consider-concurrent-variants.md`](data-structures-for-concurrent-access-consider-concurrent-variants.md) |
| 5 | Remember that theoretical complexity is not the full story... | MEDIUM | [`data-structures-remember-that-theoretical-complexity-is-not-the-full-story.md`](data-structures-remember-that-theoretical-complexity-is-not-the-full-story.md) |
| 6 | Reference Knuth's TAOCP Vol | MEDIUM | [`data-structures-reference-knuth-s-taocp-vol.md`](data-structures-reference-knuth-s-taocp-vol.md) |

---

---
title: "Choose the data structure based on the dominant operation..."
impact: MEDIUM
impactDescription: "general best practice"
tags: data-structures, dev, algorithms, choosing-data-structures-by-access-pattern, understanding-operation-complexities, implementing-fundamental-data-structures
---

## Choose the data structure based on the dominant operation...

Choose the data structure based on the dominant operation pattern: read-heavy, write-heavy, or balanced.

---

---
title: "Consider cache locality"
impact: LOW
impactDescription: "recommended but situational"
tags: data-structures, dev, algorithms, choosing-data-structures-by-access-pattern, understanding-operation-complexities, implementing-fundamental-data-structures
---

## Consider cache locality

Consider cache locality: arrays and array-backed structures (heaps, hash tables with open addressing) are more cache-friendly than pointer-based structures.

---

---
title: "For concurrent access, consider concurrent variants..."
impact: LOW
impactDescription: "recommended but situational"
tags: data-structures, dev, algorithms, choosing-data-structures-by-access-pattern, understanding-operation-complexities, implementing-fundamental-data-structures
---

## For concurrent access, consider concurrent variants...

For concurrent access, consider concurrent variants (ConcurrentHashMap, lock-free queues).

---

---
title: "Prefer standard library implementations -- they are..."
impact: LOW
impactDescription: "recommended but situational"
tags: data-structures, dev, algorithms, choosing-data-structures-by-access-pattern, understanding-operation-complexities, implementing-fundamental-data-structures
---

## Prefer standard library implementations -- they are...

Prefer standard library implementations -- they are well-tested and optimized for real-world usage.

---

---
title: "Reference Knuth's TAOCP Vol"
impact: MEDIUM
impactDescription: "general best practice"
tags: data-structures, dev, algorithms, choosing-data-structures-by-access-pattern, understanding-operation-complexities, implementing-fundamental-data-structures
---

## Reference Knuth's TAOCP Vol

Reference Knuth's TAOCP Vol. 1, Chapter 2 (Information Structures) for rigorous treatment of linked structures, trees, and multilinked representations.

---

---
title: "Remember that theoretical complexity is not the full story..."
impact: MEDIUM
impactDescription: "general best practice"
tags: data-structures, dev, algorithms, choosing-data-structures-by-access-pattern, understanding-operation-complexities, implementing-fundamental-data-structures
---

## Remember that theoretical complexity is not the full story...

Remember that theoretical complexity is not the full story -- constant factors, memory allocation patterns, and cache behavior matter in practice.

---
name: dev-algorithms-data-structures
description: Use when choosing, implementing, or comparing data structures by access pattern. USE FOR: arrays, linked lists, stacks, queues, hash tables, BST/AVL/Red-Black/B-Tree/Trie, heaps, graph representations, operation complexities. DO NOT USE FOR: algorithms on graphs (use dev-algorithms-graph-algorithms), sort/search selection (use dev-algorithms-sorting-searching).
---

# Data Structures

## Overview
Data structures are the foundation of efficient software. The choice of data structure determines the complexity of every operation your program performs. Knuth's *The Art of Computer Programming, Volume 1: Fundamental Algorithms* provides the definitive treatment of information structures -- from linear lists through trees and multilinked structures. This skill covers the major data structures, their operation complexities, and guidance on when to use each.

## Arrays

A contiguous block of memory storing elements of the same type, accessed by index.

| Operation | Time |
|-----------|------|
| Access by index | O(1) |
| Search (unsorted) | O(n) |
| Search (sorted) | O(log n) |
| Insert at end | O(1) amortized (dynamic array) |
| Insert at position | O(n) |
| Delete at position | O(n) |

**Use when**: Random access is frequent, data size is known or grows by appending, cache locality matters.

## Stacks

Last-In, First-Out (LIFO) structure.

| Operation | Time |
|-----------|------|
| Push | O(1) |
| Pop | O(1) |
| Peek/Top | O(1) |
| Search | O(n) |

**Implementations**: Array-based (dynamic array) or linked-list-based.

**Use when**: Undo operations, expression evaluation/parsing, DFS traversal, call stack simulation, balanced parentheses checking.

## Choosing the Right Data Structure

| Need | Data Structure | Why |
|------|---------------|-----|
| Fast index-based access | Array | O(1) random access |
| Fast insertions/deletions anywhere | Linked List | O(1) with pointer |
| LIFO behavior | Stack | Push/pop O(1) |
| FIFO behavior | Queue | Enqueue/dequeue O(1) |
| Fast key-value lookup | Hash Table | O(1) average |
| Ordered key-value storage | BST / Red-Black Tree | O(log n) with ordering |
| Fast lookup with frequent reads | AVL Tree | Strict balance |
| Fast lookup with frequent writes | Red-Black Tree | Fewer rotations |
| Disk-based storage / databases | B-Tree | Minimizes I/O |
| String prefix operations | Trie | O(m) prefix search |
| Priority-based processing | Heap / Priority Queue | O(log n) extract-min/max |
| Modeling relationships | Graph (adjacency list) | Flexible structure |

## Best Practices

- Choose the data structure based on the dominant operation pattern: read-heavy, write-heavy, or balanced.
- Prefer standard library implementations -- they are well-tested and optimized for real-world usage.
- Consider cache locality: arrays and array-backed structures (heaps, hash tables with open addressing) are more cache-friendly than pointer-based structures.
- For concurrent access, consider concurrent variants (ConcurrentHashMap, lock-free queues).
- Remember that theoretical complexity is not the full story -- constant factors, memory allocation patterns, and cache behavior matter in practice.
- Reference Knuth's TAOCP Vol. 1, Chapter 2 (Information Structures) for rigorous treatment of linked structures, trees, and multilinked representations.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/trees.md](references/trees.md) | Trees — Binary Search Tree (BST), AVL Tree, Red-Black Tree, B-Tree, Trie (Prefix Tree) |
| [references/details.md](references/details.md) | Linked Lists; Queues; Hash Tables; Heaps; Graphs |

## References

- [The Art of Computer Programming, Vol. 1: Fundamental Algorithms — Donald Knuth](https://www-cs-faculty.stanford.edu/~knuth/taocp.html)
- [Data Structure — Wikipedia](https://en.wikipedia.org/wiki/Data_structure)

See references/rules.md for the full rule catalog.

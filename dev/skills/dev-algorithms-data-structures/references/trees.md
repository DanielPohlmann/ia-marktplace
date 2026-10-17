<!-- Part of the dev-algorithms-data-structures skill. Loaded on demand from SKILL.md. -->

# Trees

## Binary Search Tree (BST)
Each node has at most two children; left child < parent < right child.

| Operation | Average | Worst (degenerate) |
|-----------|---------|---------------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

## AVL Tree
Self-balancing BST where the height difference between left and right subtrees of any node is at most 1.

| Operation | Time |
|-----------|------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |

**Tradeoff**: Strictly balanced, so faster lookups than Red-Black trees, but more rotations on insert/delete.

## Red-Black Tree
Self-balancing BST with color properties guaranteeing that the longest path is at most twice the shortest.

| Operation | Time |
|-----------|------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |

**Tradeoff**: Less strictly balanced than AVL, so fewer rotations on insert/delete but slightly slower lookups. Used in most standard library map/set implementations (C++ std::map, Java TreeMap).

## B-Tree
Generalized self-balancing tree where each node can have many children. Designed for systems that read/write large blocks of data.

| Operation | Time |
|-----------|------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |

**Use when**: Databases and file systems -- minimizes disk I/O by maximizing keys per node.

## Trie (Prefix Tree)
Tree where each node represents a character; paths from root to leaves represent strings.

| Operation | Time |
|-----------|------|
| Search | O(m) where m = key length |
| Insert | O(m) |
| Delete | O(m) |
| Prefix search | O(m) |

**Use when**: Autocomplete, spell checking, IP routing tables, prefix-based searching.

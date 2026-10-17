<!-- Part of the dev-algorithms-data-structures skill. Loaded on demand from SKILL.md. -->

# Data Structures — details

## Linked Lists

Elements (nodes) are stored non-contiguously; each node contains data and a pointer to the next (and optionally previous) node.

### Variants
- **Singly linked**: Each node points to the next. Traversal is forward only.
- **Doubly linked**: Each node points to both next and previous. Traversal in both directions.
- **Circular**: The last node points back to the first, forming a cycle.

| Operation | Singly | Doubly |
|-----------|--------|--------|
| Access by index | O(n) | O(n) |
| Search | O(n) | O(n) |
| Insert at head | O(1) | O(1) |
| Insert at tail (with tail pointer) | O(1) | O(1) |
| Insert at position (given pointer) | O(1) | O(1) |
| Delete at head | O(1) | O(1) |
| Delete at position (given pointer) | O(n) for singly, O(1) for doubly | O(1) |

**Use when**: Frequent insertions/deletions at arbitrary positions, no need for random access, implementing stacks/queues.

## Queues

### Standard Queue (FIFO)
First-In, First-Out structure.

| Operation | Time |
|-----------|------|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Peek/Front | O(1) |
| Search | O(n) |

### Deque (Double-Ended Queue)
Insert and remove from both ends.

| Operation | Time |
|-----------|------|
| Insert front/back | O(1) |
| Remove front/back | O(1) |
| Peek front/back | O(1) |

### Priority Queue
Elements are dequeued by priority, not insertion order. Typically implemented with a heap.

| Operation | Time (binary heap) |
|-----------|--------------------|
| Insert | O(log n) |
| Extract-min/max | O(log n) |
| Peek min/max | O(1) |
| Decrease key | O(log n) |

**Use when**: BFS traversal (standard queue), scheduling (priority queue), sliding window problems (deque).

## Hash Tables

Store key-value pairs with near-constant-time access by hashing keys to array indices.

### Collision Handling

- **Chaining**: Each bucket holds a linked list (or other collection) of entries that hash to the same index.
  - Simple to implement. Performance degrades to O(n/k) with poor hash distribution.
- **Open Addressing**: All entries stored in the array itself. On collision, probe for the next open slot.
  - **Linear probing**: Check the next slot sequentially. Simple but suffers from clustering.
  - **Quadratic probing**: Check slots at quadratic intervals. Reduces clustering.
  - **Double hashing**: Use a second hash function to determine probe step. Best distribution.

| Operation | Average | Worst |
|-----------|---------|-------|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Delete | O(1) | O(n) |

**Load factor**: Ratio of stored elements to table size. Keep below 0.7-0.75 for good performance; resize (rehash) when exceeded.

**Use when**: Fast key-based lookup is critical, keys are hashable, order does not matter.

## Heaps

A complete binary tree satisfying the heap property.

### Min-Heap
Parent <= children. Root is the minimum element.

### Max-Heap
Parent >= children. Root is the maximum element.

| Operation | Time |
|-----------|------|
| Insert | O(log n) |
| Extract min/max | O(log n) |
| Peek min/max | O(1) |
| Build heap | O(n) |
| Decrease/increase key | O(log n) |

**Implementations**: Typically a binary heap backed by an array. For better amortized performance, consider Fibonacci heaps (O(1) amortized insert and decrease-key).

**Use when**: Priority queues, heap sort, finding k-th largest/smallest, median maintenance.

## Graphs

A graph G = (V, E) consists of vertices V and edges E connecting pairs of vertices.

### Representations

#### Adjacency List
Each vertex stores a list of its neighbors.

| Operation | Time |
|-----------|------|
| Add vertex | O(1) |
| Add edge | O(1) |
| Remove edge | O(degree) |
| Check edge exists | O(degree) |
| Space | O(V + E) |

**Best for**: Sparse graphs (E << V^2). Most graph algorithms prefer this representation.

#### Adjacency Matrix
A V x V matrix where entry (i, j) indicates whether an edge exists between vertices i and j.

| Operation | Time |
|-----------|------|
| Add vertex | O(V^2) -- resize |
| Add edge | O(1) |
| Remove edge | O(1) |
| Check edge exists | O(1) |
| Space | O(V^2) |

**Best for**: Dense graphs (E close to V^2), when fast edge existence checks are needed, small graphs.

<!-- Part of the dev-design-patterns-behavioral skill. Loaded on demand from SKILL.md. -->

# 3. Iterator

## Intent
Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

## Structure

```
┌──────────────────┐        ┌──────────────────┐
│   Aggregate       │───────▶│    Iterator       │
│   (interface)     │creates │    (interface)    │
├──────────────────┤        ├──────────────────┤
│ + createIterator()│        │ + hasNext(): bool │
└──────────────────┘        │ + next(): T       │
                             └──────────────────┘
```

## Participants
- **Iterator** — defines an interface for accessing and traversing elements
- **ConcreteIterator** — implements the Iterator interface; tracks the current position
- **Aggregate** — defines an interface for creating an Iterator object
- **ConcreteAggregate** — returns an instance of the ConcreteIterator

## When to Use
- You want to access a collection's elements without exposing its internal structure
- You want to support multiple traversals of the same collection
- You want a uniform interface for traversing different types of collections

## TypeScript Example

```typescript
// Iterator interface
interface Iterator<T> {
  hasNext(): boolean;
  next(): T;
  reset(): void;
}

// Concrete collection with custom iterator
class TreeNode<T> {
  children: TreeNode<T>[] = [];
  constructor(public value: T) {}

  add(...nodes: TreeNode<T>[]): this {
    this.children.push(...nodes);
    return this;
  }
}

// Depth-first iterator
class DepthFirstIterator<T> implements Iterator<T> {
  private stack: TreeNode<T>[];

  constructor(private root: TreeNode<T>) {
    this.stack = [root];
  }

  hasNext(): boolean {
    return this.stack.length > 0;
  }

  next(): T {
    if (!this.hasNext()) throw new Error("No more elements");
    const node = this.stack.pop()!;
    // Push children in reverse so left child is processed first
    for (let i = node.children.length - 1; i >= 0; i--) {
      this.stack.push(node.children[i]);
    }
    return node.value;
  }

  reset(): void {
    this.stack = [this.root];
  }
}

// Breadth-first iterator
class BreadthFirstIterator<T> implements Iterator<T> {
  private queue: TreeNode<T>[];

  constructor(private root: TreeNode<T>) {
    this.queue = [root];
  }

  hasNext(): boolean {
    return this.queue.length > 0;
  }

  next(): T {
    if (!this.hasNext()) throw new Error("No more elements");
    const node = this.queue.shift()!;
    this.queue.push(...node.children);
    return node.value;
  }

  reset(): void {
    this.queue = [this.root];
  }
}

// Usage
const tree = new TreeNode("A")
  .add(
    new TreeNode("B").add(new TreeNode("D"), new TreeNode("E")),
    new TreeNode("C").add(new TreeNode("F"))
  );

const dfs = new DepthFirstIterator(tree);
const dfsResult: string[] = [];
while (dfs.hasNext()) dfsResult.push(dfs.next());
console.log("DFS:", dfsResult.join(" -> ")); // A -> B -> D -> E -> C -> F

const bfs = new BreadthFirstIterator(tree);
const bfsResult: string[] = [];
while (bfs.hasNext()) bfsResult.push(bfs.next());
console.log("BFS:", bfsResult.join(" -> ")); // A -> B -> C -> D -> E -> F
```

---

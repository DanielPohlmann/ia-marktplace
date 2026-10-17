<!-- Part of the dev-design-patterns-structural skill. Loaded on demand from SKILL.md. -->

# 3. Composite

## Intent
Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.

## Structure

```
┌──────────────────┐
│   Component       │◀─────────────────────┐
│   (interface)     │                      │
├──────────────────┤                      │
│ + operation()     │                      │
└──────┬───────────┘                      │ children
       │ implements                        │
       ├──────────────────┐               │
       ▼                  ▼               │
┌──────────────┐   ┌──────────────┐       │
│    Leaf       │   │  Composite    │──────┘
├──────────────┤   ├──────────────┤
│ + operation() │   │ + operation() │
└──────────────┘   │ + add()       │
                    │ + remove()    │
                    │ + getChild()  │
                    └──────────────┘
```

## Participants
- **Component** — declares the interface for objects in the composition
- **Leaf** — represents leaf objects in the composition (no children)
- **Composite** — defines behavior for components with children; stores child components

## When to Use
- You want to represent part-whole hierarchies of objects
- You want clients to treat individual objects and compositions uniformly
- File systems, org charts, UI component trees, menu structures

## TypeScript Example

```typescript
// Component
interface FileSystemNode {
  name: string;
  getSize(): number;
  print(indent?: string): string;
}

// Leaf
class File implements FileSystemNode {
  constructor(public name: string, private size: number) {}

  getSize(): number { return this.size; }

  print(indent = ""): string {
    return `${indent}📄 ${this.name} (${this.size} bytes)`;
  }
}

// Composite
class Directory implements FileSystemNode {
  private children: FileSystemNode[] = [];

  constructor(public name: string) {}

  add(node: FileSystemNode): this {
    this.children.push(node);
    return this;
  }

  remove(node: FileSystemNode): void {
    this.children = this.children.filter(c => c !== node);
  }

  getSize(): number {
    return this.children.reduce((sum, child) => sum + child.getSize(), 0);
  }

  print(indent = ""): string {
    const lines = [`${indent}📁 ${this.name}/ (${this.getSize()} bytes)`];
    for (const child of this.children) {
      lines.push(child.print(indent + "  "));
    }
    return lines.join("\n");
  }
}

// Usage — uniform treatment of files and directories
const root = new Directory("src")
  .add(new File("index.ts", 1200))
  .add(new Directory("utils")
    .add(new File("helpers.ts", 800))
    .add(new File("constants.ts", 300)))
  .add(new File("app.ts", 2500));

console.log(root.print());
console.log(`Total size: ${root.getSize()} bytes`); // 4800
```

---

<!-- Part of the dev-design-patterns-structural skill. Loaded on demand from SKILL.md. -->

# 6. Flyweight

## Intent
Use sharing to support large numbers of fine-grained objects efficiently.

## Structure

```
┌─────────────────┐       ┌────────────────────┐
│ FlyweightFactory │──────▶│   Flyweight         │
├─────────────────┤pool   │   (interface)       │
│ + getFlyweight() │       ├────────────────────┤
└─────────────────┘       │ + operation(extSt)  │
                           └──────┬─────────────┘
                                  │ implements
                           ┌──────┴─────────────┐
                           ▼                     ▼
                    ┌──────────────┐     ┌──────────────────┐
                    │ ConcreteFW    │     │ UnsharedConcreteFW│
                    │ (shared)      │     │ (not shared)      │
                    ├──────────────┤     ├──────────────────┤
                    │ intrinsicState│     │ allState          │
                    └──────────────┘     └──────────────────┘
```

## Participants
- **Flyweight** — declares an interface through which flyweights can receive and act on extrinsic state
- **ConcreteFlyweight** — stores intrinsic (shared) state; must be shareable
- **FlyweightFactory** — creates and manages flyweight objects; ensures sharing
- **Client** — maintains extrinsic state; passes it to flyweight operations

## When to Use
- An application uses a large number of objects
- Storage costs are high because of the sheer quantity of objects
- Most object state can be made extrinsic (passed in at operation time)
- Many groups of objects may be replaced by relatively few shared objects once extrinsic state is removed

## TypeScript Example

```typescript
// Flyweight — stores intrinsic (shared) state
class TreeType {
  constructor(
    public readonly name: string,
    public readonly color: string,
    public readonly texture: string
  ) {}

  render(x: number, y: number): string {
    return `[${this.name}] color=${this.color} at (${x},${y})`;
  }
}

// Flyweight factory
class TreeTypeFactory {
  private static types = new Map<string, TreeType>();

  static getType(name: string, color: string, texture: string): TreeType {
    const key = `${name}-${color}-${texture}`;
    if (!this.types.has(key)) {
      this.types.set(key, new TreeType(name, color, texture));
      console.log(`  Created new TreeType: ${key}`);
    }
    return this.types.get(key)!;
  }

  static get count(): number {
    return this.types.size;
  }
}

// Context — stores extrinsic (unique) state
class Tree {
  private type: TreeType;

  constructor(
    public x: number,
    public y: number,
    name: string,
    color: string,
    texture: string
  ) {
    this.type = TreeTypeFactory.getType(name, color, texture);
  }

  render(): string {
    return this.type.render(this.x, this.y);
  }
}

// Usage — 1 million trees but only a few TreeType objects
const forest: Tree[] = [];
for (let i = 0; i < 100000; i++) {
  forest.push(new Tree(
    Math.random() * 1000,
    Math.random() * 1000,
    i % 3 === 0 ? "Oak" : i % 3 === 1 ? "Pine" : "Birch",
    i % 2 === 0 ? "green" : "dark-green",
    "standard"
  ));
}
console.log(`Trees: ${forest.length}, Unique types: ${TreeTypeFactory.count}`);
// Trees: 100000, Unique types: 6  (instead of 100000 type objects)
```

---

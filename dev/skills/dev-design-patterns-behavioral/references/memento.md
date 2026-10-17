<!-- Part of the dev-design-patterns-behavioral skill. Loaded on demand from SKILL.md. -->

# 5. Memento

## Intent
Without violating encapsulation, capture and externalize an object's internal state so that the object can be restored to this state later.

## Structure

```
┌──────────────┐     ┌──────────────────┐     ┌──────────────┐
│  Caretaker    │────▶│    Memento        │◀────│  Originator   │
├──────────────┤keeps│    (opaque)       │saves├──────────────┤
│ - mementos[]  │     ├──────────────────┤     │ - state       │
└──────────────┘     │ + getState()      │     │ + save()      │
                      └──────────────────┘     │ + restore(m)  │
                                                └──────────────┘
```

## Participants
- **Memento** — stores internal state of the Originator; protects against access by objects other than the Originator
- **Originator** — creates a Memento containing a snapshot of its current state; uses a Memento to restore
- **Caretaker** — responsible for keeping the Memento; never operates on or examines its contents

## When to Use
- A snapshot of an object's state must be saved so it can be restored later
- A direct interface to obtaining the state would expose implementation details and break encapsulation

## TypeScript Example

```typescript
// Memento
class EditorMemento {
  constructor(
    private readonly content: string,
    private readonly cursorPos: number,
    private readonly timestamp: Date
  ) {}

  getContent(): string { return this.content; }
  getCursorPos(): number { return this.cursorPos; }
  getTimestamp(): Date { return this.timestamp; }
}

// Originator
class DocumentEditor {
  private content = "";
  private cursorPos = 0;

  type(text: string): void {
    this.content =
      this.content.slice(0, this.cursorPos) +
      text +
      this.content.slice(this.cursorPos);
    this.cursorPos += text.length;
  }

  moveCursor(pos: number): void {
    this.cursorPos = Math.max(0, Math.min(pos, this.content.length));
  }

  save(): EditorMemento {
    return new EditorMemento(this.content, this.cursorPos, new Date());
  }

  restore(memento: EditorMemento): void {
    this.content = memento.getContent();
    this.cursorPos = memento.getCursorPos();
  }

  toString(): string {
    return `"${this.content}" (cursor@${this.cursorPos})`;
  }
}

// Caretaker
class EditorHistory {
  private snapshots: EditorMemento[] = [];

  push(memento: EditorMemento): void {
    this.snapshots.push(memento);
  }

  pop(): EditorMemento | undefined {
    return this.snapshots.pop();
  }
}

// Usage
const doc = new DocumentEditor();
const history = new EditorHistory();

doc.type("Hello");
history.push(doc.save());

doc.type(" World");
history.push(doc.save());

doc.type("!!!");
console.log(doc.toString()); // "Hello World!!!" (cursor@14)

doc.restore(history.pop()!);
console.log(doc.toString()); // "Hello World" (cursor@11)

doc.restore(history.pop()!);
console.log(doc.toString()); // "Hello" (cursor@5)
```

---

<!-- Part of the dev-design-patterns-behavioral skill. Loaded on demand from SKILL.md. -->

# 6. Observer

## Intent
Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

## Structure

```
┌──────────────────┐         ┌──────────────────┐
│    Subject        │────────▶│    Observer       │
├──────────────────┤ notifies│    (interface)    │
│ - observers[]     │         ├──────────────────┤
│ + attach(obs)     │         │ + update(data)    │
│ + detach(obs)     │         └──────┬───────────┘
│ + notify()        │                │ implements
└──────────────────┘                ▼
                              ┌──────────────────┐
                              │ ConcreteObserver   │
                              ├──────────────────┤
                              │ + update(data)    │
                              └──────────────────┘
```

## Participants
- **Subject** — knows its observers; provides an interface for attaching and detaching Observer objects
- **Observer** — defines an updating interface for objects that should be notified of changes
- **ConcreteSubject** — stores state of interest; sends a notification when state changes
- **ConcreteObserver** — maintains a reference to a ConcreteSubject; implements the update interface

## When to Use
- When a change to one object requires changing others, and you do not know how many objects need to change
- When an object should notify other objects without making assumptions about who those objects are

## TypeScript Example

```typescript
// Observer interface
interface EventListener<T> {
  update(event: string, data: T): void;
}

// Subject — generic event emitter
class EventEmitter<T> {
  private listeners = new Map<string, Set<EventListener<T>>>();

  subscribe(event: string, listener: EventListener<T>): () => void {
    if (!this.listeners.has(event)) {
      this.listeners.set(event, new Set());
    }
    this.listeners.get(event)!.add(listener);

    // Return unsubscribe function
    return () => this.listeners.get(event)?.delete(listener);
  }

  protected notify(event: string, data: T): void {
    this.listeners.get(event)?.forEach(listener => listener.update(event, data));
  }
}

// Concrete subject
class Store extends EventEmitter<{ key: string; value: unknown }> {
  private state = new Map<string, unknown>();

  set(key: string, value: unknown): void {
    const old = this.state.get(key);
    this.state.set(key, value);
    this.notify("change", { key, value });
    if (old === undefined) {
      this.notify("add", { key, value });
    }
  }

  get(key: string): unknown {
    return this.state.get(key);
  }
}

// Concrete observers
class LoggingObserver implements EventListener<{ key: string; value: unknown }> {
  update(event: string, data: { key: string; value: unknown }): void {
    console.log(`[LOG] ${event}: ${data.key} = ${JSON.stringify(data.value)}`);
  }
}

class ValidationObserver implements EventListener<{ key: string; value: unknown }> {
  update(event: string, data: { key: string; value: unknown }): void {
    if (data.key === "email" && typeof data.value === "string") {
      if (!data.value.includes("@")) {
        console.log(`[WARN] Invalid email: ${data.value}`);
      }
    }
  }
}

// Usage
const store = new Store();
const unsubLog = store.subscribe("change", new LoggingObserver());
store.subscribe("change", new ValidationObserver());

store.set("name", "Alice");    // [LOG] change: name = "Alice"
store.set("email", "invalid"); // [LOG] change: email = "invalid"
                                // [WARN] Invalid email: invalid

unsubLog(); // unsubscribe logger
store.set("name", "Bob");      // (no log output, validation still active)
```

---

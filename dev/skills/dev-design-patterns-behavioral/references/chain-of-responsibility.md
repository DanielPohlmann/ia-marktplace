<!-- Part of the dev-design-patterns-behavioral skill. Loaded on demand from SKILL.md. -->

# 1. Chain of Responsibility

## Intent
Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.

## Structure

```
┌──────────────────┐
│    Handler        │◀────────────┐
│    (interface)    │             │ next
├──────────────────┤             │
│ + handle(req)     │─────────────┘
│ + setNext(h)      │
└──────┬───────────┘
       │ implements
       ├──────────────┬──────────────┐
       ▼              ▼              ▼
┌────────────┐ ┌────────────┐ ┌────────────┐
│ HandlerA    │ │ HandlerB    │ │ HandlerC    │
└────────────┘ └────────────┘ └────────────┘
```

## Participants
- **Handler** — defines an interface for handling requests; optionally links to a successor
- **ConcreteHandler** — handles requests it is responsible for; forwards unhandled requests to the next handler
- **Client** — initiates the request to a handler in the chain

## When to Use
- More than one object may handle a request, and the handler is not known a priori
- You want to issue a request to one of several objects without specifying the receiver explicitly
- The set of handlers should be configurable dynamically (e.g., middleware pipelines)

## TypeScript Example

```typescript
// Handler interface
interface SupportHandler {
  setNext(handler: SupportHandler): SupportHandler;
  handle(issue: { level: string; message: string }): string;
}

// Base handler
abstract class BaseSupportHandler implements SupportHandler {
  private next: SupportHandler | null = null;

  setNext(handler: SupportHandler): SupportHandler {
    this.next = handler;
    return handler;
  }

  handle(issue: { level: string; message: string }): string {
    if (this.next) {
      return this.next.handle(issue);
    }
    return `No handler found for: ${issue.message}`;
  }
}

// Concrete handlers
class TierOneSupport extends BaseSupportHandler {
  handle(issue: { level: string; message: string }): string {
    if (issue.level === "basic") {
      return `[Tier 1] Resolved: ${issue.message}`;
    }
    return super.handle(issue);
  }
}

class TierTwoSupport extends BaseSupportHandler {
  handle(issue: { level: string; message: string }): string {
    if (issue.level === "intermediate") {
      return `[Tier 2] Resolved: ${issue.message}`;
    }
    return super.handle(issue);
  }
}

class EngineeringSupport extends BaseSupportHandler {
  handle(issue: { level: string; message: string }): string {
    if (issue.level === "critical") {
      return `[Engineering] Resolved: ${issue.message}`;
    }
    return super.handle(issue);
  }
}

// Usage — build the chain
const tier1 = new TierOneSupport();
const tier2 = new TierTwoSupport();
const engineering = new EngineeringSupport();

tier1.setNext(tier2).setNext(engineering);

console.log(tier1.handle({ level: "basic", message: "Password reset" }));
// [Tier 1] Resolved: Password reset
console.log(tier1.handle({ level: "critical", message: "Data corruption" }));
// [Engineering] Resolved: Data corruption
```

---

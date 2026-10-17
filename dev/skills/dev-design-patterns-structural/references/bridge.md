<!-- Part of the dev-design-patterns-structural skill. Loaded on demand from SKILL.md. -->

# 2. Bridge

## Intent
Decouple an abstraction from its implementation so that the two can vary independently.

## Structure

```
┌────────────────────┐         ┌─────────────────────┐
│   Abstraction       │────────▶│   Implementor        │
├────────────────────┤  has-a  │   (interface)        │
│ + operation()       │         ├─────────────────────┤
└──────┬─────────────┘         │ + operationImpl()    │
       │ extends                └──────┬──────────────┘
       ▼                               │ implements
┌────────────────────┐         ┌───────┴──────────────┐
│ RefinedAbstraction  │         │                      │
├────────────────────┤   ┌─────────────┐  ┌─────────────┐
│ + operation()       │   │ ConcreteImplA│  │ ConcreteImplB│
└────────────────────┘   └─────────────┘  └─────────────┘
```

## Participants
- **Abstraction** — defines the abstraction's interface; maintains a reference to Implementor
- **RefinedAbstraction** — extends the interface defined by Abstraction
- **Implementor** — defines the interface for implementation classes
- **ConcreteImplementor** — implements the Implementor interface

## When to Use
- You want to avoid a permanent binding between an abstraction and its implementation
- Both the abstraction and its implementation should be extensible via subclassing
- You have a class explosion from combining two independent dimensions of variation (e.g., Shape x Renderer, Notification x Channel)

## TypeScript Example

```typescript
// Implementor
interface NotificationChannel {
  send(title: string, body: string): void;
}

// Concrete implementors
class EmailChannel implements NotificationChannel {
  send(title: string, body: string): void {
    console.log(`[Email] Subject: ${title} | Body: ${body}`);
  }
}

class SlackChannel implements NotificationChannel {
  send(title: string, body: string): void {
    console.log(`[Slack] *${title}*: ${body}`);
  }
}

class SMSChannel implements NotificationChannel {
  send(title: string, body: string): void {
    console.log(`[SMS] ${title}: ${body.substring(0, 160)}`);
  }
}

// Abstraction
abstract class Notification {
  constructor(protected channel: NotificationChannel) {}
  abstract notify(message: string): void;
}

// Refined abstractions
class AlertNotification extends Notification {
  notify(message: string): void {
    this.channel.send("ALERT", `URGENT: ${message}`);
  }
}

class InfoNotification extends Notification {
  notify(message: string): void {
    this.channel.send("Info", message);
  }
}

// Usage — any notification type x any channel
const urgentEmail = new AlertNotification(new EmailChannel());
urgentEmail.notify("Server CPU at 98%");
// [Email] Subject: ALERT | Body: URGENT: Server CPU at 98%

const infoSlack = new InfoNotification(new SlackChannel());
infoSlack.notify("Deployment complete");
// [Slack] *Info*: Deployment complete
```

---

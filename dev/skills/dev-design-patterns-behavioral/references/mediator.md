<!-- Part of the dev-design-patterns-behavioral skill. Loaded on demand from SKILL.md. -->

# 4. Mediator

## Intent
Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently.

## Structure

```
┌──────────────────┐        ┌──────────────────┐
│    Mediator       │◀───────│   Colleague       │
│    (interface)    │        │   (interface)     │
├──────────────────┤        ├──────────────────┤
│ + notify(sender,  │        │ - mediator        │
│         event)    │        └──────┬───────────┘
└──────┬───────────┘               │ implements
       │ implements                 ├──────────┐
       ▼                           ▼          ▼
┌──────────────────┐       ┌──────────┐┌──────────┐
│ ConcreteMediator  │       │ColleagueA││ColleagueB│
│                   │       └──────────┘└──────────┘
│ - colleagueA      │
│ - colleagueB      │
└──────────────────┘
```

## Participants
- **Mediator** — defines an interface for communicating with Colleague objects
- **ConcreteMediator** — implements cooperative behavior by coordinating Colleague objects
- **Colleague** — each Colleague knows its Mediator and communicates with it instead of other Colleagues

## When to Use
- A set of objects communicate in well-defined but complex ways
- Reusing an object is difficult because it refers to and communicates with many other objects
- A behavior distributed between several classes should be customizable without subclassing

## TypeScript Example

```typescript
// Mediator interface
interface ChatMediator {
  sendMessage(message: string, sender: ChatUser): void;
  addUser(user: ChatUser): void;
}

// Colleague
class ChatUser {
  private messages: string[] = [];

  constructor(
    public name: string,
    private mediator: ChatMediator
  ) {
    mediator.addUser(this);
  }

  send(message: string): void {
    console.log(`${this.name} sends: ${message}`);
    this.mediator.sendMessage(message, this);
  }

  receive(message: string, from: string): void {
    const formatted = `${from}: ${message}`;
    this.messages.push(formatted);
    console.log(`  ${this.name} received <- ${formatted}`);
  }

  getHistory(): string[] {
    return [...this.messages];
  }
}

// Concrete mediator
class ChatRoom implements ChatMediator {
  private users: ChatUser[] = [];

  addUser(user: ChatUser): void {
    this.users.push(user);
  }

  sendMessage(message: string, sender: ChatUser): void {
    for (const user of this.users) {
      if (user !== sender) {
        user.receive(message, sender.name);
      }
    }
  }
}

// Usage — users never reference each other directly
const room = new ChatRoom();
const alice = new ChatUser("Alice", room);
const bob = new ChatUser("Bob", room);
const charlie = new ChatUser("Charlie", room);

alice.send("Hello everyone!");
// Alice sends: Hello everyone!
//   Bob received <- Alice: Hello everyone!
//   Charlie received <- Alice: Hello everyone!

bob.send("Hey Alice!");
// Bob sends: Hey Alice!
//   Alice received <- Bob: Hey Alice!
//   Charlie received <- Bob: Hey Alice!
```

---

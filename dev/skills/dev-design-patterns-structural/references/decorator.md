<!-- Part of the dev-design-patterns-structural skill. Loaded on demand from SKILL.md. -->

# 4. Decorator

## Intent
Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

## Structure

```
┌──────────────────┐
│   Component       │◀──────────────────────┐
│   (interface)     │                       │
├──────────────────┤                       │
│ + operation()     │                       │ wraps
└──────┬───────────┘                       │
       │ implements                         │
       ├──────────────────┐                │
       ▼                  ▼                │
┌────────────────┐ ┌─────────────────┐     │
│ ConcreteComp.   │ │   Decorator      │────┘
├────────────────┤ ├─────────────────┤
│ + operation()   │ │ + operation()    │
└────────────────┘ └──────┬──────────┘
                          │ extends
                   ┌──────┴──────────┐
                   ▼                 ▼
            ┌────────────┐   ┌────────────┐
            │ DecoratorA  │   │ DecoratorB  │
            ├────────────┤   ├────────────┤
            │ + operation()│  │ + operation()│
            └────────────┘   └────────────┘
```

## Participants
- **Component** — defines the interface for objects that can have responsibilities added
- **ConcreteComponent** — the object to which additional responsibilities are attached
- **Decorator** — maintains a reference to a Component and conforms to Component's interface
- **ConcreteDecorator** — adds responsibilities to the component

## When to Use
- You want to add responsibilities to individual objects dynamically, without affecting other objects
- You want to add responsibilities that can be withdrawn
- Extension by subclassing is impractical (e.g., the number of combinations explodes)

## TypeScript Example

```typescript
// Component interface
interface DataSource {
  write(data: string): string;
  read(): string;
}

// Concrete component
class FileDataSource implements DataSource {
  private content = "";

  write(data: string): string {
    this.content = data;
    return `Written: ${data}`;
  }

  read(): string {
    return this.content;
  }
}

// Base decorator
abstract class DataSourceDecorator implements DataSource {
  constructor(protected wrappee: DataSource) {}

  write(data: string): string {
    return this.wrappee.write(data);
  }

  read(): string {
    return this.wrappee.read();
  }
}

// Concrete decorators
class EncryptionDecorator extends DataSourceDecorator {
  write(data: string): string {
    const encrypted = Buffer.from(data).toString("base64");
    return super.write(encrypted);
  }

  read(): string {
    const data = super.read();
    return Buffer.from(data, "base64").toString("utf-8");
  }
}

class CompressionDecorator extends DataSourceDecorator {
  write(data: string): string {
    const compressed = `[compressed:${data.length}]${data}`;
    return super.write(compressed);
  }

  read(): string {
    const data = super.read();
    return data.replace(/^\[compressed:\d+\]/, "");
  }
}

class LoggingDecorator extends DataSourceDecorator {
  write(data: string): string {
    console.log(`[LOG] Writing ${data.length} chars`);
    return super.write(data);
  }

  read(): string {
    console.log("[LOG] Reading data");
    return super.read();
  }
}

// Usage — stack decorators in any combination
let source: DataSource = new FileDataSource();
source = new CompressionDecorator(source);
source = new EncryptionDecorator(source);
source = new LoggingDecorator(source);

source.write("Hello, World!");
console.log(source.read()); // Hello, World!
```

---

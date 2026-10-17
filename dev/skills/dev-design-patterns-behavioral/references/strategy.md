<!-- Part of the dev-design-patterns-behavioral skill. Loaded on demand from SKILL.md. -->

# 8. Strategy

## Intent
Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

## Structure

```
┌──────────────────┐        ┌──────────────────┐
│    Context        │───────▶│    Strategy       │
├──────────────────┤ has-a  │    (interface)    │
│ - strategy        │        ├──────────────────┤
│ + execute()       │        │ + execute(data)   │
└──────────────────┘        └──────┬───────────┘
                                   │ implements
                            ┌──────┼──────────┐
                            ▼      ▼          ▼
                     ┌────────┐┌────────┐┌────────┐
                     │ StratA  ││ StratB  ││ StratC  │
                     └────────┘└────────┘└────────┘
```

## Participants
- **Strategy** — declares an interface common to all supported algorithms
- **ConcreteStrategy** — implements the algorithm using the Strategy interface
- **Context** — is configured with a ConcreteStrategy; delegates to its Strategy

## When to Use
- Many related classes differ only in their behavior
- You need different variants of an algorithm
- An algorithm uses data that clients should not know about
- A class defines many behaviors, and these appear as multiple conditional statements

## TypeScript Example

```typescript
// Strategy interface
interface CompressionStrategy {
  compress(data: string): string;
  name: string;
}

// Concrete strategies
class GzipStrategy implements CompressionStrategy {
  name = "gzip";
  compress(data: string): string {
    return `[gzip:${data.length}]${data.substring(0, 10)}...`;
  }
}

class BrotliStrategy implements CompressionStrategy {
  name = "brotli";
  compress(data: string): string {
    return `[br:${data.length}]${data.substring(0, 8)}...`;
  }
}

class NoCompressionStrategy implements CompressionStrategy {
  name = "none";
  compress(data: string): string {
    return data;
  }
}

// Context
class FileCompressor {
  constructor(private strategy: CompressionStrategy) {}

  setStrategy(strategy: CompressionStrategy): void {
    this.strategy = strategy;
  }

  compressFile(filename: string, content: string): string {
    const result = this.strategy.compress(content);
    return `${filename} compressed with ${this.strategy.name}: ${result}`;
  }
}

// Usage — swap algorithms at runtime
const compressor = new FileCompressor(new GzipStrategy());
console.log(compressor.compressFile("data.json", "a]".repeat(1000)));

compressor.setStrategy(new BrotliStrategy());
console.log(compressor.compressFile("data.json", "a".repeat(1000)));

// Strategy selection based on file size
function selectStrategy(size: number): CompressionStrategy {
  if (size > 10000) return new BrotliStrategy();
  if (size > 1000) return new GzipStrategy();
  return new NoCompressionStrategy();
}
```

---

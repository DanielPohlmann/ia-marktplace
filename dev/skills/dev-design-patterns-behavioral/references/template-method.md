<!-- Part of the dev-design-patterns-behavioral skill. Loaded on demand from SKILL.md. -->

# 9. Template Method

## Intent
Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.

## Structure

```
┌──────────────────────┐
│   AbstractClass       │
├──────────────────────┤
│ + templateMethod()    │  ← calls step1, step2, step3 in order
│ + step1()            │  ← may have default implementation
│ + step2()            │  ← abstract — subclass MUST implement
│ + step3()            │  ← hook — subclass CAN override
└──────┬───────────────┘
       │ extends
       ▼
┌──────────────────────┐
│   ConcreteClass       │
├──────────────────────┤
│ + step2()            │  ← implements required step
│ + step3()            │  ← optionally overrides hook
└──────────────────────┘
```

## Participants
- **AbstractClass** — defines the template method (the skeleton); declares abstract steps and optional hooks
- **ConcreteClass** — implements the abstract steps; optionally overrides hooks

## When to Use
- You want to implement the invariant parts of an algorithm once and let subclasses fill in the varying parts
- You want to control which parts of an algorithm subclasses can override (hooks vs. required steps)
- Common behavior among subclasses should be factored and localized in a common class to avoid duplication

## TypeScript Example

```typescript
// Abstract class with template method
abstract class DataPipeline {
  // Template method — defines the skeleton
  run(source: string): string {
    const raw = this.extract(source);
    const validated = this.validate(raw);
    const transformed = this.transform(validated);
    this.beforeLoad(transformed); // hook
    const result = this.load(transformed);
    this.afterLoad(result); // hook
    return result;
  }

  // Abstract steps — subclasses MUST implement
  protected abstract extract(source: string): string[];
  protected abstract transform(data: string[]): string[];
  protected abstract load(data: string[]): string;

  // Default step — can be overridden
  protected validate(data: string[]): string[] {
    return data.filter(item => item.trim().length > 0);
  }

  // Hooks — do nothing by default, subclasses CAN override
  protected beforeLoad(_data: string[]): void {}
  protected afterLoad(_result: string): void {}
}

// Concrete implementation
class CsvToJsonPipeline extends DataPipeline {
  protected extract(source: string): string[] {
    return source.split("\n");
  }

  protected transform(data: string[]): string[] {
    const headers = data[0].split(",");
    return data.slice(1).map(row => {
      const values = row.split(",");
      const obj: Record<string, string> = {};
      headers.forEach((h, i) => obj[h.trim()] = values[i]?.trim() ?? "");
      return JSON.stringify(obj);
    });
  }

  protected load(data: string[]): string {
    return `[${data.join(",")}]`;
  }

  protected afterLoad(result: string): void {
    console.log(`Loaded ${JSON.parse(result).length} records`);
  }
}

// Usage
const pipeline = new CsvToJsonPipeline();
const csv = "name,age\nAlice,30\nBob,25\n";
const json = pipeline.run(csv);
console.log(json); // [{"name":"Alice","age":"30"},{"name":"Bob","age":"25"}]
// Loaded 2 records
```

---

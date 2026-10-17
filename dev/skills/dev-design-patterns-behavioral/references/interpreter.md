<!-- Part of the dev-design-patterns-behavioral skill. Loaded on demand from SKILL.md. -->

# 11. Interpreter

## Intent
Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.

## Note on Usage
The Interpreter pattern is the **least commonly used** GoF pattern in modern practice. Most real-world expression evaluation is handled by parser generators, embedded scripting engines (Lua, JS), or expression libraries. Use Interpreter only for simple, well-defined grammars (e.g., query filters, configuration rules).

## Structure

```
┌───────────────────────┐
│  AbstractExpression    │
│  (interface)           │
├───────────────────────┤
│ + interpret(context)   │
└──────┬────────────────┘
       │ implements
       ├──────────────────┐
       ▼                  ▼
┌──────────────────┐ ┌──────────────────┐
│TerminalExpression │ │NonterminalExpr.  │
│(literal values)   │ │(rules/operators) │
└──────────────────┘ └──────────────────┘
```

## When to Use
- The grammar is simple and efficiency is not a critical concern
- You want to evaluate simple rule expressions, search filters, or configuration DSLs

## TypeScript Example

```typescript
// Context
interface InterpretContext {
  variables: Record<string, boolean>;
}

// Abstract expression
interface BoolExpression {
  interpret(ctx: InterpretContext): boolean;
  toString(): string;
}

// Terminal expression
class Variable implements BoolExpression {
  constructor(private name: string) {}
  interpret(ctx: InterpretContext): boolean {
    return ctx.variables[this.name] ?? false;
  }
  toString(): string { return this.name; }
}

// Nonterminal expressions
class AndExpression implements BoolExpression {
  constructor(private left: BoolExpression, private right: BoolExpression) {}
  interpret(ctx: InterpretContext): boolean {
    return this.left.interpret(ctx) && this.right.interpret(ctx);
  }
  toString(): string { return `(${this.left} AND ${this.right})`; }
}

class OrExpression implements BoolExpression {
  constructor(private left: BoolExpression, private right: BoolExpression) {}
  interpret(ctx: InterpretContext): boolean {
    return this.left.interpret(ctx) || this.right.interpret(ctx);
  }
  toString(): string { return `(${this.left} OR ${this.right})`; }
}

class NotExpression implements BoolExpression {
  constructor(private expr: BoolExpression) {}
  interpret(ctx: InterpretContext): boolean {
    return !this.expr.interpret(ctx);
  }
  toString(): string { return `NOT(${this.expr})`; }
}

// Usage — evaluate: (isAdmin OR (isActive AND NOT(isBanned)))
const expr = new OrExpression(
  new Variable("isAdmin"),
  new AndExpression(
    new Variable("isActive"),
    new NotExpression(new Variable("isBanned"))
  )
);

console.log(`Rule: ${expr}`);
console.log(expr.interpret({ variables: { isAdmin: false, isActive: true, isBanned: false } })); // true
console.log(expr.interpret({ variables: { isAdmin: false, isActive: true, isBanned: true } }));  // false
console.log(expr.interpret({ variables: { isAdmin: true, isActive: false, isBanned: true } }));  // true
```

---

<!-- Part of the dev-design-patterns-behavioral skill. Loaded on demand from SKILL.md. -->

# 10. Visitor

## Intent
Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.

## Structure

```
┌──────────────────┐       ┌──────────────────────┐
│    Visitor        │       │     Element           │
│    (interface)    │       │     (interface)       │
├──────────────────┤       ├──────────────────────┤
│ + visitA(elemA)   │       │ + accept(visitor)     │
│ + visitB(elemB)   │       └──────┬───────────────┘
└──────┬───────────┘              │ implements
       │ implements                ├──────────┐
       ▼                          ▼          ▼
┌────────────────┐         ┌──────────┐┌──────────┐
│ConcreteVisitor  │         │ ElementA  ││ ElementB  │
├────────────────┤         ├──────────┤├──────────┤
│ + visitA(elemA) │         │ accept(v) ││ accept(v) │
│ + visitB(elemB) │         │{v.visitA} ││{v.visitB} │
└────────────────┘         └──────────┘└──────────┘
```

## Participants
- **Visitor** — declares a visit operation for each class of ConcreteElement
- **ConcreteVisitor** — implements each visit operation
- **Element** — defines an accept(visitor) method
- **ConcreteElement** — implements accept by calling the appropriate visitor method

## When to Use
- An object structure contains many classes with differing interfaces, and you want to perform operations that depend on their concrete classes
- Many distinct and unrelated operations need to be performed on objects in a structure, and you want to avoid "polluting" their classes
- The classes in the structure rarely change, but you often define new operations over the structure

## TypeScript Example

```typescript
// Visitor interface
interface ASTVisitor<R> {
  visitNumber(node: NumberNode): R;
  visitBinaryOp(node: BinaryOpNode): R;
  visitUnaryOp(node: UnaryOpNode): R;
}

// Element interface
interface ASTNode {
  accept<R>(visitor: ASTVisitor<R>): R;
}

// Concrete elements
class NumberNode implements ASTNode {
  constructor(public value: number) {}

  accept<R>(visitor: ASTVisitor<R>): R {
    return visitor.visitNumber(this);
  }
}

class BinaryOpNode implements ASTNode {
  constructor(
    public operator: "+" | "-" | "*" | "/",
    public left: ASTNode,
    public right: ASTNode
  ) {}

  accept<R>(visitor: ASTVisitor<R>): R {
    return visitor.visitBinaryOp(this);
  }
}

class UnaryOpNode implements ASTNode {
  constructor(public operator: "-", public operand: ASTNode) {}

  accept<R>(visitor: ASTVisitor<R>): R {
    return visitor.visitUnaryOp(this);
  }
}

// Concrete visitor — evaluator
class EvaluatorVisitor implements ASTVisitor<number> {
  visitNumber(node: NumberNode): number { return node.value; }

  visitBinaryOp(node: BinaryOpNode): number {
    const l = node.left.accept(this);
    const r = node.right.accept(this);
    switch (node.operator) {
      case "+": return l + r;
      case "-": return l - r;
      case "*": return l * r;
      case "/": return l / r;
    }
  }

  visitUnaryOp(node: UnaryOpNode): number {
    return -node.operand.accept(this);
  }
}

// Concrete visitor — printer
class PrinterVisitor implements ASTVisitor<string> {
  visitNumber(node: NumberNode): string { return String(node.value); }

  visitBinaryOp(node: BinaryOpNode): string {
    return `(${node.left.accept(this)} ${node.operator} ${node.right.accept(this)})`;
  }

  visitUnaryOp(node: UnaryOpNode): string {
    return `(-${node.operand.accept(this)})`;
  }
}

// Usage — same AST, different operations without modifying nodes
// Represents: (3 + 4) * (-2)
const ast = new BinaryOpNode("*",
  new BinaryOpNode("+", new NumberNode(3), new NumberNode(4)),
  new UnaryOpNode("-", new NumberNode(2))
);

console.log(ast.accept(new PrinterVisitor()));    // ((3 + 4) * (-2))
console.log(ast.accept(new EvaluatorVisitor()));  // -14
```

---

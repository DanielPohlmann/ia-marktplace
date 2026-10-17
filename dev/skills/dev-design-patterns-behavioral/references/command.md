<!-- Part of the dev-design-patterns-behavioral skill. Loaded on demand from SKILL.md. -->

# 2. Command

## Intent
Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

## Structure

```
┌──────────┐       ┌──────────────────┐       ┌──────────────┐
│  Invoker  │──────▶│    Command        │       │   Receiver    │
│           │       │    (interface)    │       ├──────────────┤
└──────────┘       ├──────────────────┤       │ + action()    │
                    │ + execute()       │       └──────┬───────┘
                    │ + undo()          │              │
                    └──────┬───────────┘              │
                           │ implements                │
                           ▼                           │
                    ┌──────────────────┐              │
                    │ ConcreteCommand   │──────────────┘
                    ├──────────────────┤   calls
                    │ - receiver        │
                    │ - state           │
                    │ + execute()       │
                    │ + undo()          │
                    └──────────────────┘
```

## Participants
- **Command** — declares an interface for executing an operation
- **ConcreteCommand** — binds a Receiver to an action; implements execute/undo
- **Invoker** — asks the command to carry out the request
- **Receiver** — knows how to perform the operations associated with the request

## When to Use
- You need to parameterize objects with an action to perform
- You need to specify, queue, and execute requests at different times
- You need to support undo/redo
- You need to support logging changes so they can be reapplied after a crash

## TypeScript Example

```typescript
// Receiver
class TextEditor {
  content = "";

  insert(text: string, position: number): void {
    this.content = this.content.slice(0, position) + text + this.content.slice(position);
  }

  delete(position: number, length: number): string {
    const deleted = this.content.slice(position, position + length);
    this.content = this.content.slice(0, position) + this.content.slice(position + length);
    return deleted;
  }
}

// Command interface
interface EditorCommand {
  execute(): void;
  undo(): void;
}

// Concrete commands
class InsertCommand implements EditorCommand {
  constructor(
    private editor: TextEditor,
    private text: string,
    private position: number
  ) {}

  execute(): void {
    this.editor.insert(this.text, this.position);
  }

  undo(): void {
    this.editor.delete(this.position, this.text.length);
  }
}

class DeleteCommand implements EditorCommand {
  private deletedText = "";

  constructor(
    private editor: TextEditor,
    private position: number,
    private length: number
  ) {}

  execute(): void {
    this.deletedText = this.editor.delete(this.position, this.length);
  }

  undo(): void {
    this.editor.insert(this.deletedText, this.position);
  }
}

// Invoker with undo/redo
class CommandHistory {
  private undoStack: EditorCommand[] = [];
  private redoStack: EditorCommand[] = [];

  execute(command: EditorCommand): void {
    command.execute();
    this.undoStack.push(command);
    this.redoStack = []; // clear redo on new action
  }

  undo(): void {
    const cmd = this.undoStack.pop();
    if (cmd) {
      cmd.undo();
      this.redoStack.push(cmd);
    }
  }

  redo(): void {
    const cmd = this.redoStack.pop();
    if (cmd) {
      cmd.execute();
      this.undoStack.push(cmd);
    }
  }
}

// Usage
const editor = new TextEditor();
const history = new CommandHistory();

history.execute(new InsertCommand(editor, "Hello", 0));
history.execute(new InsertCommand(editor, " World", 5));
console.log(editor.content); // "Hello World"

history.undo();
console.log(editor.content); // "Hello"

history.redo();
console.log(editor.content); // "Hello World"
```

---

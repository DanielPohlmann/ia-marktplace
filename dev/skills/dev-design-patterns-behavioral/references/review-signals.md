<!-- Part of the dev-design-patterns-behavioral skill. Loaded on demand from SKILL.md. -->

# Review Signals — Behavioral Patterns

Use this file during code review. **Signals in code** are what a reviewer sees that suggests the pattern is missing; **When NOT to use** lists anti-signals and overuse.

## Quick table

| Pattern | Signals in code (pattern is needed) | When NOT to use (anti-signals / overuse) |
|---------|-------------------------------------|------------------------------------------|
| **Chain of Responsibility** | A long method of sequential `if (canHandle) … return` blocks; validation or middleware steps hard-coded in one place and reordered by editing it | Exactly one handler always applies; the order of handlers matters but is implicit and untested; a request can silently fall off the end of the chain |
| **Command** | Undo/redo, retry, queueing or auditing of operations implemented ad hoc; the same action triggered from menu, shortcut and API with duplicated code | A plain method call with no need to defer, log, queue or undo — wrapping it in a command class is ceremony |
| **Interpreter** | Hand-written string parsing of a small rule language repeated in several places | The grammar is non-trivial or growing — use a parser library or an existing expression engine |
| **Iterator** | Callers index into internal arrays or know the storage layout to traverse a collection | The language already provides iteration (`IEnumerable<T>`, generators, `for…of`) — expose that instead of a custom iterator class |
| **Mediator** | Many components reference each other directly; one UI change ripples through several sibling classes | Two or three collaborators with simple calls; the mediator keeps absorbing business logic and turns into a god object |
| **Memento** | Undo or rollback implemented by exposing private fields through getters/setters | State is large and changes often (snapshots cost memory) — consider Command-based undo or event sourcing |
| **Observer** | One change must trigger several independent reactions; the subject imports and calls every dependent directly | A single reaction — a direct call is clearer and easier to trace. See pitfalls below |
| **State** | A status string/enum with a public setter; transition checks scattered across services | Two states with a single trivial transition; a status that is only displayed, never drives behavior. See below |
| **Strategy** | A `switch` on a type/mode inside an algorithm, repeated in several methods | Only one algorithm exists, or variants never change at runtime or per configuration. See below |
| **Template Method** | Two or more classes repeat the same sequence of steps and differ only in some of them | Duplication does not exist yet; steps vary independently. See below |
| **Visitor** | Type switches (`is`/`instanceof`) over a stable hierarchy, repeated for each new operation | The element hierarchy changes often — every new element type forces edits to every visitor; a language with pattern matching over closed types may be simpler |

## Observer — pitfalls

- **Subscriptions never removed.** The subject holds references to its observers, so a forgotten unsubscribe keeps them alive — a memory leak. In C#, an `event` handler keeps the subscriber reachable for as long as the publisher lives; a long-lived publisher (singleton, static event) with short-lived subscribers is the classic leak. Unsubscribe (`-=`, dispose the subscription token) in `Dispose`/teardown.
- **Notification order assumptions.** Observers must not rely on being called before or after another observer. If order matters, it is a pipeline — make it explicit (Chain of Responsibility or an orchestrating method).
- **One failing observer breaks the others.** An exception in one handler aborts the loop and the remaining observers never run. Isolate each call (catch, log, continue) or deliver through a mechanism that retries per subscriber.
- **Synchronous fan-out of slow work.** Every observer runs on the caller's thread and adds to its latency; a slow handler (email, HTTP, heavy I/O) stalls the subject. When volume or latency matters, publish to a queue or message broker and let consumers process asynchronously.
- **Re-entrancy.** An observer that modifies the subject during notification can trigger nested notifications or mutate the subscriber list mid-iteration — iterate over a copy and avoid cascading updates.

## State — signals and correction

**Signal:** an entity exposes `Status` as a string or enum with a public setter, and transition rules (`if (order.Status == "Paid") …`) are spread across services, controllers and jobs. Nothing stops an illegal jump such as `Cancelled → Shipped`, and adding a state means finding every check.

**Correction:**
- Make the status private to the entity; change it only through intention-revealing methods (`Pay()`, `Ship()`, `Cancel()`).
- Model each state as a type that decides which transitions it allows and what the next state is.
- An invalid transition **fails loudly** — throw a domain exception or return an explicit failure result — never a silent no-op or a log line.
- For a small, stable lifecycle a transition table (current state + trigger → next state) inside the entity is an acceptable lighter alternative; the key property is that transitions are checked in one place.

## Strategy — selection does not disappear

Strategy removes the conditional from the algorithm, but the decision "which strategy for this case?" still has to be made somewhere. Done well, that selection **moves to one place** — a factory, a registry keyed by mode/type, or DI configuration (keyed services, named registrations) — instead of being scattered. In review, check that:
- the selection logic exists exactly once and is covered by tests;
- an unknown key fails explicitly rather than silently falling back to a default;
- the context class receives a strategy and does not re-introduce the `switch` itself.

## Template Method — apply after duplication exists

- Extract a template method only when **two or more classes already repeat the same sequence of steps**; designing the base class up-front usually guesses the wrong extension points.
- Cost: inheritance coupling. Subclasses depend on the base class's internal call order and protected members; changing the skeleton can break every subclass, and a class can inherit only one skeleton.
- Anti-signals: many hooks that most subclasses leave empty; subclasses overriding steps to undo base behavior; a deep hierarchy of templates.
- **Alternative — composition with Strategy:** keep the fixed sequence in a concrete class and inject the varying steps as strategy objects (or delegates). Steps can then vary independently, be tested in isolation and be combined without new subclasses.

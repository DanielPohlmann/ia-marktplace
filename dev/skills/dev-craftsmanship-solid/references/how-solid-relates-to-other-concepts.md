<!-- Part of the dev-craftsmanship-solid skill. Loaded on demand from SKILL.md. -->

# How SOLID Relates to Other Concepts

## SOLID and Clean Architecture
Clean Architecture is the architectural expression of SOLID at the system level:

| SOLID Principle | Clean Architecture Manifestation |
|----------------|----------------------------------|
| SRP | Each layer has a single reason to change (UI, business rules, data). |
| OCP | New features are added by creating new Use Cases, not modifying existing ones. |
| LSP | Interface Adapters can be swapped (PostgreSQL for MySQL) without breaking Use Cases. |
| ISP | Ports (interfaces) are defined per use case, not as monolithic repository interfaces. |
| DIP | The Dependency Rule — inner layers define interfaces, outer layers implement them. |

## SOLID and Design Patterns
Many GoF design patterns exist specifically to satisfy SOLID:

| Pattern | Primary SOLID Principle |
|---------|------------------------|
| Strategy | OCP, DIP |
| Observer | OCP, DIP |
| Decorator | OCP, SRP |
| Factory Method / Abstract Factory | DIP |
| Adapter | ISP, DIP |
| Command | SRP, OCP |
| Template Method | OCP, LSP |

## SOLID and Testability
Each SOLID principle directly improves testability:

| Principle | Testing Benefit |
|-----------|----------------|
| SRP | Smaller classes with fewer dependencies = simpler test setup. |
| OCP | New behavior tested in isolation via new classes, existing tests remain green. |
| LSP | Test doubles (mocks, stubs) can replace real implementations safely. |
| ISP | Narrow interfaces require fewer mock methods. |
| DIP | Dependencies are injected, making them trivially replaceable with test doubles. |

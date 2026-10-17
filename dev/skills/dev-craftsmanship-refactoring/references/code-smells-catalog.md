<!-- Part of the dev-craftsmanship-refactoring skill. Loaded on demand from SKILL.md. -->

# Code Smells Catalog

Code smells are surface indicators that usually correspond to a deeper problem in the system. Smells are not bugs — the code works — but they signal that the design could be improved.

## Bloaters
Smells where code grows excessively large.

| Smell | Description | Typical Refactoring |
|-------|-------------|---------------------|
| **Long Method** | A method that has grown too long. The longer a method is, the harder it is to understand. | Extract Method, Replace Temp with Query, Introduce Parameter Object, Decompose Conditional |
| **Large Class** | A class that does too much and has too many fields or methods. | Extract Class, Extract Subclass, Extract Interface |
| **Primitive Obsession** | Using primitives (strings, numbers) instead of small objects for simple tasks (money, phone numbers, ranges). | Replace Data Value with Object, Introduce Parameter Object, Replace Type Code with Class |
| **Long Parameter List** | A method takes too many parameters, making it hard to call and understand. | Introduce Parameter Object, Replace Parameter with Method Call, Preserve Whole Object |
| **Data Clumps** | Groups of data that appear together repeatedly (e.g., `startDate`/`endDate`, `x`/`y`/`z`). | Extract Class, Introduce Parameter Object |

## Object-Orientation Abusers
Smells that indicate incomplete or incorrect application of OO principles.

| Smell | Description | Typical Refactoring |
|-------|-------------|---------------------|
| **Switch Statements** | Complex switch/case or if/else chains that dispatch on a type code. | Replace Conditional with Polymorphism, Replace Type Code with Subclasses |
| **Parallel Inheritance Hierarchies** | Every time you add a subclass to one hierarchy, you have to add one to another. | Move Method, Move Field to eliminate the parallel hierarchy |
| **Temporary Field** | A field that is only set in certain circumstances, leading to confusion about when it is valid. | Extract Class, Introduce Null Object |
| **Refused Bequest** | A subclass uses only some of the methods and properties of its parent. | Replace Inheritance with Delegation, Extract Subclass |

## Change Preventers
Smells that make changes disproportionately expensive.

| Smell | Description | Typical Refactoring |
|-------|-------------|---------------------|
| **Divergent Change** | One class is commonly changed in different ways for different reasons — it has multiple responsibilities. | Extract Class (split along axes of change) |
| **Shotgun Surgery** | A single change requires editing many classes in many places. | Move Method, Move Field, Inline Class (consolidate scattered responsibility) |

## Dispensables
Smells where something is unnecessary and should be removed.

| Smell | Description | Typical Refactoring |
|-------|-------------|---------------------|
| **Lazy Class** | A class that does too little to justify its existence. | Inline Class, Collapse Hierarchy |
| **Speculative Generality** | Abstract classes, interfaces, or parameters that exist "just in case" but have only one user. | Collapse Hierarchy, Inline Class, Remove Parameter |
| **Dead Code** | Code that is never executed. | Delete it. Version control remembers. |
| **Duplicate Code** | The same code structure appears in more than one place. | Extract Method, Extract Class, Pull Up Method |

## Couplers
Smells that indicate excessive coupling between classes.

| Smell | Description | Typical Refactoring |
|-------|-------------|---------------------|
| **Feature Envy** | A method that uses more features of another class than its own. | Move Method, Extract Method |
| **Inappropriate Intimacy** | Two classes are too tightly coupled, accessing each other's private details. | Move Method, Move Field, Extract Class, Replace Inheritance with Delegation |
| **Message Chains** | `a.getB().getC().getD().doSomething()` — the client is coupled to the navigation structure. | Hide Delegate, Extract Method, Move Method |
| **Middle Man** | A class that does nothing but delegate to another. | Remove Middle Man, Inline Method |

---

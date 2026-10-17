<!-- Part of the dev-craftsmanship-clean-code skill. Loaded on demand from SKILL.md. -->

# Clean Code — details

## Comments

### Good Comments
- **Legal comments:** Copyright and license headers.
- **Informative comments:** Explain a regex pattern or complex algorithm.
- **Explanation of intent:** Why a decision was made, not what the code does.
- **Warning comments:** Alert others to consequences (e.g., "This test takes 10 minutes to run").
- **TODO comments:** Mark incomplete work with a consistent `TODO(author):` convention.
- **Amplification:** Emphasize importance of something that might seem trivial.

### Bad Comments
- **Redundant comments:** Restating what the code already says.
- **Mandated comments:** Javadoc for every function regardless of clarity.
- **Journal comments:** Change logs in the file (use version control instead).
- **Noise comments:** `/** Default constructor */` on a default constructor.
- **Commented-out code:** Delete it. Version control remembers.
- **Position markers:** `// ---- ACTIONS ----` banners (if you need them, the class is too large).

```typescript
// Bad — redundant comment
// Check if the user is active
if (user.isActive) { /* ... */ }

// Good — explains intent
// Users flagged during the 2024 migration may have stale tokens;
// force re-authentication to prevent silent data loss.
if (user.requiresReauthentication) { /* ... */ }
```

## Formatting

### Vertical Formatting
- **Newspaper metaphor:** The name should tell you if you are in the right module. The top should give the high-level concepts. Detail increases as you move down.
- **Vertical openness:** Separate concepts with blank lines.
- **Vertical density:** Lines that are tightly related should appear close together.
- **Vertical distance:** Concepts that are closely related should be kept vertically close to each other. Variables should be declared as close to their usage as possible.

### Horizontal Formatting
- **Horizontal openness and density:** Use spaces to associate strongly related things and separate weakly related things.
- **Indentation:** Never ignore the indentation. Even for short `if` bodies, use braces and indent.
- Keep lines under 100-120 characters where practical.

### Team Rules
A team of developers should agree upon a single formatting style. Consistency within a project is more important than any individual's preferred style. Use automated formatters (Prettier, ESLint, editorconfig) to enforce the rules without debate.

## Error Handling

### Use Exceptions Rather Than Return Codes
Return codes force the caller to check immediately and clutter the happy path.

```typescript
// Bad — error code
function deletePage(page: Page): number {
    if (page === null) return -1;
    if (!page.canDelete()) return -2;
    page.delete();
    return 0;
}

// Good — exception
function deletePage(page: Page): void {
    if (!page) throw new ArgumentError("Page must not be null");
    if (!page.canDelete()) throw new PermissionError("Page cannot be deleted");
    page.delete();
}
```

### Write Your Try-Catch-Finally First
Start with the try-catch-finally when writing code that could throw. This helps define scope and invariants.

### Don't Return Null
Returning null forces every caller to add a null check. Instead, throw an exception or return a special-case object (Null Object pattern).

```typescript
// Bad
function getEmployee(id: string): Employee | null {
    const record = db.find(id);
    return record ? new Employee(record) : null;
}

// Good — throw if not found
function getEmployee(id: string): Employee {
    const record = db.find(id);
    if (!record) throw new EmployeeNotFoundError(id);
    return new Employee(record);
}

// Good — return a Null Object when absence is normal
function getEmployees(): Employee[] {
    return db.findAll() ?? [];  // never null, may be empty
}
```

### Don't Pass Null
Passing null as an argument is even worse than returning it. It forces every function to start with null-checking boilerplate.

## Objects and Data Structures

### Data/Object Anti-Symmetry
- **Objects** hide their data behind abstractions and expose functions that operate on it.
- **Data structures** expose their data and have no meaningful functions.

These two approaches are complementary opposites:
- Procedural code (using data structures) makes it easy to add new functions without changing existing data structures.
- OO code (using objects) makes it easy to add new classes without changing existing functions.

```typescript
// Data structure approach — easy to add new functions
interface Point {
    x: number;
    y: number;
}

function area(shape: Square): number { return shape.side * shape.side; }
function perimeter(shape: Square): number { return 4 * shape.side; }

// Object approach — easy to add new shapes
interface Shape {
    area(): number;
    perimeter(): number;
}
```

### Law of Demeter
A method `f` of class `C` should only call methods on:
- `C` itself
- Objects created by `f`
- Objects passed as arguments to `f`
- Objects held in instance variables of `C`

```typescript
// Bad — train wreck
const outputDir = ctxt.getOptions().getScratchDir().getAbsolutePath();

// Good — tell, don't ask
const outputDir = ctxt.getOutputDirectoryPath();
```

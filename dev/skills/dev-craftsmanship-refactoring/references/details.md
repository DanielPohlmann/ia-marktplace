<!-- Part of the dev-craftsmanship-refactoring skill. Loaded on demand from SKILL.md. -->

# Refactoring — details

## The Refactoring Workflow

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Write Tests │ ──> │  Small Change│ ──> │  Run Tests   │ ──> │   Commit     │
│  (if missing)│     │  (one smell) │     │  (all green?)│     │   (repeat)   │
└──────────────┘     └──────────────┘     └──────┬───────┘     └──────────────┘
                           ^                     │
                           │     Red? Revert.    │
                           └─────────────────────┘
```

1. **Ensure tests exist.** If they do not, write characterization tests that lock in current behavior before you change anything.
2. **Make one small change.** Apply a single, named refactoring technique.
3. **Run all tests.** If they pass, commit. If they fail, revert and try a smaller step.
4. **Repeat.** Each commit is a safe checkpoint. Accumulate small improvements into significant structural change.

**Never refactor and add features in the same commit.** Separate "hat switching" — wear the refactoring hat or the feature hat, never both.

---

## Refactoring and Testing

Refactoring requires a safety net of tests:

- **Before refactoring:** Ensure tests cover the code you are about to change. If they do not, write **characterization tests** — tests that assert what the code currently does, whether or not that is "correct."
- **During refactoring:** Run tests after every small change. Green means you preserved behavior. Red means you broke something — revert and try a smaller step.
- **After refactoring:** The tests should pass without modification. If you had to change tests, you changed behavior — that is not a refactoring.

```
Confidence = Test Coverage * Test Quality
```

If you have high coverage but the tests are fragile (testing implementation rather than behavior), refactoring becomes painful because tests break on every change. Write tests against the public interface, not internal details.

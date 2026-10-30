<!-- Part of the dev-craftsmanship-clean-code skill. Loaded on demand from SKILL.md. -->

# Meaningful Names

## Intention-Revealing Names
Names should answer: why it exists, what it does, and how it is used.

```typescript
// Bad
const d: number = 0; // elapsed time in days

// Good
const elapsedTimeInDays: number = 0;
```

## Avoid Disinformation
Do not use names that imply a meaning different from the actual purpose.

```typescript
// Bad — it is not actually a List
const accountList: Map<string, Account> = new Map();

// Good
const accountsByName: Map<string, Account> = new Map();
```

## Pronounceable Names
If you cannot pronounce a name, you cannot discuss it without sounding awkward.

```typescript
// Bad
const genymdhms: Date = new Date();

// Good
const generationTimestamp: Date = new Date();
```

## Searchable Names
Single-letter names and numeric constants are hard to search for.

```typescript
// Bad
for (let i = 0; i < 34; i++) {
    s += t[i] * 4 / 5;
}

// Good
const WORK_DAYS_PER_WEEK = 5;
const NUMBER_OF_TASKS = 34;
for (let taskIndex = 0; taskIndex < NUMBER_OF_TASKS; taskIndex++) {
    realDaysPerIdealDay += taskEstimate[taskIndex] * DAYS_PER_IDEAL_DAY / WORK_DAYS_PER_WEEK;
}
```

## Naming Conventions Summary

| Rule | Example (Bad) | Example (Good) |
|------|---------------|----------------|
| Use intention-revealing names | `d` | `elapsedTimeInDays` |
| Avoid disinformation | `accountList` (for a Map) | `accountsByName` |
| Make meaningful distinctions | `a1`, `a2` | `source`, `destination` |
| Use pronounceable names | `genymdhms` | `generationTimestamp` |
| Use searchable names | `7` | `MAX_CLASSES_PER_STUDENT` |
| Avoid encodings / prefixes | `m_name`, `strName`, `iCount` | `name`, `count` |
| Use nouns for classes | `Manager`, `Processor`, `Data` (vague) | `Account`, `WikiPage`, `AddressParser` |
| Use verbs for methods | `data()` | `fetchData()`, `save()`, `deletePage()` |

> **Language conventions override this table.** "Avoid encodings" targets type and scope warts (Hungarian notation, `m_` prefixes). It does not override idioms the ecosystem expects: in C#/.NET the `I` prefix on interfaces (`IShapeFactory`) is the standard convention and should be kept.

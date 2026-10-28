---
name: dev-craftsmanship-clean-code
description: Use when writing or reviewing code for readability (Robert C. Martin's Clean Code). USE FOR: naming, small single-purpose functions, comments, formatting, error handling, objects vs data structures. DO NOT USE FOR: layer rules (use dev-craftsmanship-clean-architecture), smell-driven refactoring (use dev-craftsmanship-refactoring), SOLID (use dev-craftsmanship-solid).
---

# Clean Code

## Overview
*Clean Code: A Handbook of Agile Software Craftsmanship* by Robert C. Martin establishes that code is read far more often than it is written. Clean code is code that is easy to understand, easy to change, and does what the reader expects. It reads like well-written prose.

> "Clean code always looks like it was written by someone who cares." — Michael Feathers

> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." — Martin Fowler

## Clean Code Checklist

| Area | Question |
|------|----------|
| Names | Does every name reveal intent? Could a new team member understand this without context? |
| Functions | Does each function do one thing at one level of abstraction? Length is a signal, not a verdict — a long function deserves a look, not an automatic finding. |
| Arguments | Does any function take more than 3 arguments? |
| Comments | Does every comment explain *why*, not *what*? Are there commented-out blocks? |
| Formatting | Does the file read top-to-bottom like a newspaper article? |
| Error Handling | Are exceptions used instead of error codes? Is null returned where absence is not an expected outcome, or passed as an argument? |
| Duplication | Is there any copy-pasted logic? (Apply DRY) |
| Dead Code | Is there any code that is never executed? |

## Best Practices
- Read code aloud. If it sounds awkward, the names or structure need work.
- Apply the Boy Scout Rule: clean up one thing every time you visit a file.
- Use automated linters and formatters to handle formatting debates mechanically.
- Treat tests as first-class citizens of clean code — apply all the same naming, function, and formatting rules.
- Prefer polymorphism over switch/if-else chains when you find the same condition repeated.
- When you write a comment, first ask: "Can I make this code so clear that the comment is unnecessary?"
- The language's own conventions win over generic rules: keep the `I` prefix on C#/.NET interfaces, `snake_case` in Python, and so on.
- Treat numeric limits (lines per function, arguments per call) as review prompts. Report the underlying problem — mixed abstraction levels, hidden responsibilities — never the count alone.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/meaningful-names.md](references/meaningful-names.md) | Meaningful Names — Intention-Revealing Names, Avoid Disinformation, Pronounceable Names, Searchable Names, Naming Conventions Summary |
| [references/functions.md](references/functions.md) | Functions — Small Functions, One Level of Abstraction, Command-Query Separation, Function Arguments, Avoid Side Effects |
| [references/details.md](references/details.md) | Comments; Formatting; Error Handling; Objects and Data Structures |

## References

- [Clean Code — Robert C. Martin (Book)](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
- [Robert C. Martin (Uncle Bob) — Clean Coder](https://blog.cleancoder.com/)

See references/rules.md for the full rule catalog.

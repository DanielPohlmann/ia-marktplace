---
name: specs-documentation-gauge
description: Use when writing Gauge (ThoughtWorks) markdown test specifications. USE FOR: spec files, scenarios, steps, concepts, data tables, tags, step implementations, data-driven specs, Gauge CLI. DO NOT USE FOR: Given/When/Then specs (use specs-documentation-gherkin), requirements (use specs-documentation-prd), diagrams (use specs-diagramming).
---

# Gauge

## Overview
Gauge is an open-source test automation framework created by ThoughtWorks that uses Markdown as its specification language. Unlike Gherkin's rigid `Given/When/Then` structure, Gauge allows free-form, natural-language specifications written as plain Markdown files (`.spec`). This makes specifications more readable for non-technical stakeholders while remaining fully executable.

Gauge separates the *specification layer* (Markdown) from the *implementation layer* (code in any supported language), enabling teams to write test specs that read like documentation.

## Reporting

Gauge generates reports automatically after each run.

| Format | Command Flag | Output |
|--------|-------------|--------|
| HTML | `--env default` (default) | `reports/html-report/index.html` |
| XML (JUnit) | Plugin: `gauge-xml-report` | `reports/xml-report/` |
| JSON | Plugin: `gauge-json-report` | `reports/json-report/result.json` |
| Spectacle | Plugin: `spectacle` | Interactive HTML dashboard |

Generate HTML report: `gauge run specs/`
Generate XML for CI: `gauge install xml-report && gauge run specs/`

## Gauge vs Gherkin

| Aspect | Gauge | Gherkin |
|--------|-------|---------|
| **Syntax** | Free-form Markdown | Structured Given/When/Then keywords |
| **File format** | `.spec` (Markdown) | `.feature` |
| **Readability** | Reads like documentation | Reads like structured test cases |
| **Flexibility** | Any natural language phrasing | Must follow keyword grammar |
| **Abstraction** | Concepts (`.cpt` files) | No built-in macro system |
| **Data tables** | Markdown tables + external CSV | Inline Examples tables |
| **Context steps** | Steps before first scenario | `Background` keyword |
| **Teardown** | `___` separator section | Hooks in code |
| **Runners** | Java, C#, JS, Python, Ruby, Go | Cucumber (Java), Behave (Python), SpecFlow/Reqnroll (C#), etc. |
| **Best for** | Teams wanting documentation-first specs | Teams wanting structured BDD with strict grammar |

## Project Structure

```
project-root/
  env/
    default/
      default.properties
  specs/
    concepts/
      login.cpt
      navigation.cpt
    authentication/
      login.spec
      registration.spec
    checkout/
      checkout.spec
      payment.spec
    data/
      products.csv
      users.csv
  tests/           # Step implementations
    authentication_steps.js
    checkout_steps.js
    hooks.js
  manifest.json
```

## Best Practices

- **Write specs as documentation first** -- the specification should be readable and valuable even without the automation layer.
- **Use concepts to build a domain vocabulary** -- concepts create a high-level language specific to your application that makes specs concise and expressive.
- **Keep steps atomic** -- each step should do one thing. Compose complex behaviors using concepts.
- **Use context steps for shared setup** -- avoid duplicating login or navigation steps across every scenario.
- **Use teardown steps for cleanup** -- ensure each scenario leaves the system in a clean state.
- **Externalize large data sets** -- use CSV files for data-driven testing rather than embedding large tables in spec files.
- **Tag consistently** -- adopt a tagging convention (`smoke`, `regression`, `wip`, feature area tags) and document it for the team.
- **Run specs in parallel** -- Gauge supports parallel execution natively; structure specs to be independent so they run reliably in parallel.
- **Integrate with CI/CD** -- use XML or JSON reports for CI integration and HTML reports for human review.
- **Validate specs regularly** -- run `gauge validate` in CI to catch unimplemented steps early.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/core-concepts.md](references/core-concepts.md) | Core Concepts — Specification Files (.spec), Steps, Concepts, Tags, Data Tables, Data-Driven Testing with External Sources, … |
| [references/step-implementations.md](references/step-implementations.md) | Step Implementations — JavaScript / TypeScript, C# (.NET), Python, Java |
| [references/complete-specification-example.md](references/complete-specification-example.md) | Complete Specification Example |
| [references/details.md](references/details.md) | CLI Reference |

## References

- [Gauge Official Documentation](https://docs.gauge.org/)
- [Gauge — GitHub Repository](https://github.com/getgauge/gauge)

See references/rules.md for the full rule catalog.

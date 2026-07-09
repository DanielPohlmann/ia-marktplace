# Gauge Rules

Best practices and rules for Gauge.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Write specs as documentation first | MEDIUM | [`gauge-write-specs-as-documentation-first.md`](gauge-write-specs-as-documentation-first.md) |
| 2 | Use concepts to build a domain vocabulary | MEDIUM | [`gauge-use-concepts-to-build-a-domain-vocabulary.md`](gauge-use-concepts-to-build-a-domain-vocabulary.md) |
| 3 | Keep steps atomic | MEDIUM | [`gauge-keep-steps-atomic.md`](gauge-keep-steps-atomic.md) |
| 4 | Use context steps for shared setup | HIGH | [`gauge-use-context-steps-for-shared-setup.md`](gauge-use-context-steps-for-shared-setup.md) |
| 5 | Use teardown steps for cleanup | HIGH | [`gauge-use-teardown-steps-for-cleanup.md`](gauge-use-teardown-steps-for-cleanup.md) |
| 6 | Externalize large data sets | MEDIUM | [`gauge-externalize-large-data-sets.md`](gauge-externalize-large-data-sets.md) |
| 7 | Tag consistently | MEDIUM | [`gauge-tag-consistently.md`](gauge-tag-consistently.md) |
| 8 | Run specs in parallel | MEDIUM | [`gauge-run-specs-in-parallel.md`](gauge-run-specs-in-parallel.md) |
| 9 | Integrate with CI/CD | MEDIUM | [`gauge-integrate-with-ci-cd.md`](gauge-integrate-with-ci-cd.md) |
| 10 | Validate specs regularly | HIGH | [`gauge-validate-specs-regularly.md`](gauge-validate-specs-regularly.md) |

---

---
title: "Externalize large data sets"
impact: MEDIUM
impactDescription: "general best practice"
tags: gauge, specs, documentation, markdown-test-specifications, free-form-acceptance-tests, gauge-spec-files
---

## Externalize large data sets

Externalize large data sets: use CSV files for data-driven testing rather than embedding large tables in spec files.

---

---
title: "Integrate with CI/CD"
impact: MEDIUM
impactDescription: "general best practice"
tags: gauge, specs, documentation, markdown-test-specifications, free-form-acceptance-tests, gauge-spec-files
---

## Integrate with CI/CD

Integrate with CI/CD: use XML or JSON reports for CI integration and HTML reports for human review.

---

---
title: "Keep steps atomic"
impact: MEDIUM
impactDescription: "general best practice"
tags: gauge, specs, documentation, markdown-test-specifications, free-form-acceptance-tests, gauge-spec-files
---

## Keep steps atomic

Keep steps atomic: each step should do one thing. Compose complex behaviors using concepts.

---

---
title: "Run specs in parallel"
impact: MEDIUM
impactDescription: "general best practice"
tags: gauge, specs, documentation, markdown-test-specifications, free-form-acceptance-tests, gauge-spec-files
---

## Run specs in parallel

Gauge supports parallel execution natively; structure specs to be independent so they run reliably in parallel.

---

---
title: "Tag consistently"
impact: MEDIUM
impactDescription: "general best practice"
tags: gauge, specs, documentation, markdown-test-specifications, free-form-acceptance-tests, gauge-spec-files
---

## Tag consistently

Tag consistently: adopt a tagging convention (`smoke`, `regression`, `wip`, feature area tags) and document it for the team.

---

---
title: "Use concepts to build a domain vocabulary"
impact: MEDIUM
impactDescription: "general best practice"
tags: gauge, specs, documentation, markdown-test-specifications, free-form-acceptance-tests, gauge-spec-files
---

## Use concepts to build a domain vocabulary

Use concepts to build a domain vocabulary: concepts create a high-level language specific to your application that makes specs concise and expressive.

---

---
title: "Use context steps for shared setup"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: gauge, specs, documentation, markdown-test-specifications, free-form-acceptance-tests, gauge-spec-files
---

## Use context steps for shared setup

Use context steps for shared setup: avoid duplicating login or navigation steps across every scenario.

---

---
title: "Use teardown steps for cleanup"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: gauge, specs, documentation, markdown-test-specifications, free-form-acceptance-tests, gauge-spec-files
---

## Use teardown steps for cleanup

Use teardown steps for cleanup: ensure each scenario leaves the system in a clean state.

---

---
title: "Validate specs regularly"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: gauge, specs, documentation, markdown-test-specifications, free-form-acceptance-tests, gauge-spec-files
---

## Validate specs regularly

Validate specs regularly: run `gauge validate` in CI to catch unimplemented steps early.

---

---
title: "Write specs as documentation first"
impact: MEDIUM
impactDescription: "general best practice"
tags: gauge, specs, documentation, markdown-test-specifications, free-form-acceptance-tests, gauge-spec-files
---

## Write specs as documentation first

Write specs as documentation first: the specification should be readable and valuable even without the automation layer.

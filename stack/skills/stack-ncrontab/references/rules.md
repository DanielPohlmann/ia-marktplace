# NCrontab Rules

Best practices and rules for NCrontab.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Use UTC times consistently | HIGH | [`ncrontab-use-utc-times-consistently.md`](ncrontab-use-utc-times-consistently.md) |
| 2 | Parse cron expressions once and reuse the `CrontabSchedule` instance | MEDIUM | [`ncrontab-parse-cron-expressions-once-and-reuse-the-crontabschedule.md`](ncrontab-parse-cron-expressions-once-and-reuse-the-crontabschedule.md) |
| 3 | Validate cron expressions at application startup or configuration save time | HIGH | [`ncrontab-validate-cron-expressions-at-application-startup-or.md`](ncrontab-validate-cron-expressions-at-application-startup-or.md) |
| 4 | Use the six-field format with `IncludingSeconds = true` | MEDIUM | [`ncrontab-use-the-six-field-format-with-includingseconds-true.md`](ncrontab-use-the-six-field-format-with-includingseconds-true.md) |
| 5 | Document cron patterns in configuration | MEDIUM | [`ncrontab-document-cron-patterns-in-configuration.md`](ncrontab-document-cron-patterns-in-configuration.md) |
| 6 | Account for task execution time | MEDIUM | [`ncrontab-account-for-task-execution-time.md`](ncrontab-account-for-task-execution-time.md) |
| 7 | Handle the gap between calculated delay and actual wake time | MEDIUM | [`ncrontab-handle-the-gap-between-calculated-delay-and-actual-wake-time.md`](ncrontab-handle-the-gap-between-calculated-delay-and-actual-wake-time.md) |
| 8 | Use `GetNextOccurrences` to display upcoming schedules | MEDIUM | [`ncrontab-use-getnextoccurrences-to-display-upcoming-schedules.md`](ncrontab-use-getnextoccurrences-to-display-upcoming-schedules.md) |
| 9 | Combine NCrontab with `BackgroundService` | LOW | [`ncrontab-combine-ncrontab-with-backgroundservice.md`](ncrontab-combine-ncrontab-with-backgroundservice.md) |
| 10 | Test cron schedules across time boundaries | MEDIUM | [`ncrontab-test-cron-schedules-across-time-boundaries.md`](ncrontab-test-cron-schedules-across-time-boundaries.md) |

---

---
title: "Account for task execution time"
impact: MEDIUM
impactDescription: "general best practice"
tags: ncrontab, dotnet, general, parsing-cron-expressions, calculating-nextprevious-occurrences, validating-cron-syntax
---

## Account for task execution time

Account for task execution time: when calculating the next occurrence -- if a task takes 5 minutes and runs every 5 minutes, use the task's end time as the base for `GetNextOccurrence`.

---

---
title: "Combine NCrontab with `BackgroundService`"
impact: LOW
impactDescription: "recommended but situational"
tags: ncrontab, dotnet, general, parsing-cron-expressions, calculating-nextprevious-occurrences, validating-cron-syntax
---

## Combine NCrontab with `BackgroundService`

Combine NCrontab with `BackgroundService`: for simple cron-scheduled tasks, but prefer Quartz.NET or Hangfire when you need persistence, retries, or distributed coordination.

---

---
title: "Consider daylight saving time"
impact: LOW
impactDescription: "recommended but situational"
tags: ncrontab, dotnet, general
---

## Consider daylight saving time

Consider daylight saving time

---

---
title: "Document cron patterns in configuration"
impact: MEDIUM
impactDescription: "general best practice"
tags: ncrontab, dotnet, general, parsing-cron-expressions, calculating-nextprevious-occurrences, validating-cron-syntax
---

## Document cron patterns in configuration

Document cron patterns in configuration: with comments explaining the schedule in plain English, since cron syntax is not self-documenting.

---

---
title: "Document cron patterns"
impact: MEDIUM
impactDescription: "general best practice"
tags: ncrontab, dotnet, general
---

## Document cron patterns

Document cron patterns

---

---
title: "Handle the gap between calculated delay and actual wake time"
impact: MEDIUM
impactDescription: "general best practice"
tags: ncrontab, dotnet, general, parsing-cron-expressions, calculating-nextprevious-occurrences, validating-cron-syntax
---

## Handle the gap between calculated delay and actual wake time

Handle the gap between calculated delay and actual wake time: by re-checking the current time after `Task.Delay` returns, since the OS may wake the task slightly early or late.

---

---
title: "Parse cron expressions once and reuse the `CrontabSchedule` instance"
impact: MEDIUM
impactDescription: "general best practice"
tags: ncrontab, dotnet, general, parsing-cron-expressions, calculating-nextprevious-occurrences, validating-cron-syntax
---

## Parse cron expressions once and reuse the `CrontabSchedule` instance

Parse cron expressions once and reuse the `CrontabSchedule` instance: since parsing involves string splitting and validation that should not repeat per tick.

---

---
title: "Test cron schedules across time boundaries"
impact: MEDIUM
impactDescription: "general best practice"
tags: ncrontab, dotnet, general, parsing-cron-expressions, calculating-nextprevious-occurrences, validating-cron-syntax
---

## Test cron schedules across time boundaries

Test cron schedules across time boundaries: including month-end, year-end, leap years, and DST transitions to verify occurrence calculation correctness.

---

---
title: "Test edge cases"
impact: MEDIUM
impactDescription: "general best practice"
tags: ncrontab, dotnet, general
---

## Test edge cases

Test edge cases

---

---
title: "Use appropriate time zones"
impact: MEDIUM
impactDescription: "general best practice"
tags: ncrontab, dotnet, general
---

## Use appropriate time zones

Use appropriate time zones

---

---
title: "Use `GetNextOccurrences` to display upcoming schedules"
impact: MEDIUM
impactDescription: "general best practice"
tags: ncrontab, dotnet, general, parsing-cron-expressions, calculating-nextprevious-occurrences, validating-cron-syntax
---

## Use `GetNextOccurrences` to display upcoming schedules

Use `GetNextOccurrences` to display upcoming schedules: in admin UIs so operators can verify that a cron expression produces the expected pattern.

---

---
title: "Use the six-field format with `IncludingSeconds = true`"
impact: MEDIUM
impactDescription: "general best practice"
tags: ncrontab, dotnet, general, parsing-cron-expressions, calculating-nextprevious-occurrences, validating-cron-syntax
---

## Use the six-field format with `IncludingSeconds = true`

Use the six-field format with `IncludingSeconds = true`: only when sub-minute precision is genuinely needed -- five-field expressions are more portable and widely understood.

---

---
title: "Use UTC times consistently"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: ncrontab, dotnet, general, parsing-cron-expressions, calculating-nextprevious-occurrences, validating-cron-syntax
---

## Use UTC times consistently

Use UTC times consistently: with `DateTime.UtcNow` for cron calculations to avoid daylight saving time issues that cause skipped or doubled executions.

---

---
title: "Validate cron expressions at application startup or configuration save time"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: ncrontab, dotnet, general, parsing-cron-expressions, calculating-nextprevious-occurrences, validating-cron-syntax
---

## Validate cron expressions at application startup or configuration save time

Validate cron expressions at application startup or configuration save time: rather than at execution time to fail fast on invalid patterns.

---

---
title: "Validate expressions"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: ncrontab, dotnet, general
---

## Validate expressions

Validate expressions

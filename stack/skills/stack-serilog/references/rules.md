# Serilog Rules

Best practices and rules for Serilog.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Use message templates instead of string interpolation | MEDIUM | [`serilog-use-message-templates-instead-of-string-interpolation.md`](serilog-use-message-templates-instead-of-string-interpolation.md) |
| 2 | Use the `@` destructuring operator | MEDIUM | [`serilog-use-the-destructuring-operator.md`](serilog-use-the-destructuring-operator.md) |
| 3 | Call `Log.CloseAndFlush()` | HIGH | [`serilog-call-log-closeandflush.md`](serilog-call-log-closeandflush.md) |
| 4 | Override framework log levels | CRITICAL | [`serilog-override-framework-log-levels.md`](serilog-override-framework-log-levels.md) |
| 5 | Use `Serilog.AspNetCore`'s `UseSerilogRequestLogging()` | MEDIUM | [`serilog-use-serilog-aspnetcore-s-useserilogrequestlogging.md`](serilog-use-serilog-aspnetcore-s-useserilogrequestlogging.md) |
| 6 | Enrich globally with `FromLogContext` | MEDIUM | [`serilog-enrich-globally-with-fromlogcontext.md`](serilog-enrich-globally-with-fromlogcontext.md) |
| 7 | Configure sinks in `appsettings.json` | MEDIUM | [`serilog-configure-sinks-in-appsettings-json.md`](serilog-configure-sinks-in-appsettings-json.md) |
| 8 | Wrap high-latency sinks | HIGH | [`serilog-wrap-high-latency-sinks.md`](serilog-wrap-high-latency-sinks.md) |
| 9 | Avoid logging sensitive data | HIGH | [`serilog-avoid-logging-sensitive-data.md`](serilog-avoid-logging-sensitive-data.md) |
| 10 | Use the two-stage initialization pattern | MEDIUM | [`serilog-use-the-two-stage-initialization-pattern.md`](serilog-use-the-two-stage-initialization-pattern.md) |

---

---
title: "Avoid logging sensitive data"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: serilog, dotnet, logging, serilog-sink-configuration, structured-event-logging, log-enrichment
---

## Avoid logging sensitive data

Avoid logging sensitive data: by using Serilog's `Destructure.ByTransforming<T>()` to mask or omit sensitive fields before they reach any sink.

---

---
title: "Avoid string interpolation in log messages"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: serilog, dotnet, logging
---

## Avoid string interpolation in log messages

Avoid string interpolation in log messages

---

---
title: "Call `Log.CloseAndFlush()`"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: serilog, dotnet, logging, serilog-sink-configuration, structured-event-logging, log-enrichment
---

## Call `Log.CloseAndFlush()`

Call `Log.CloseAndFlush()`: in a `finally` block to ensure all buffered events are written before the process exits; without this, async sinks may lose the final batch.

---

---
title: "Configure different sinks for different log levels"
impact: MEDIUM
impactDescription: "general best practice"
tags: serilog, dotnet, logging
---

## Configure different sinks for different log levels

Configure different sinks for different log levels

---

---
title: "Configure sinks in `appsettings.json`"
impact: MEDIUM
impactDescription: "general best practice"
tags: serilog, dotnet, logging, serilog-sink-configuration, structured-event-logging, log-enrichment
---

## Configure sinks in `appsettings.json`

Configure sinks in `appsettings.json`: via `Serilog.Settings.Configuration` so operations can add or remove sinks and adjust levels without code changes or redeployment.

---

---
title: "Enrich globally with `FromLogContext`"
impact: MEDIUM
impactDescription: "general best practice"
tags: serilog, dotnet, logging, serilog-sink-configuration, structured-event-logging, log-enrichment
---

## Enrich globally with `FromLogContext`

Enrich globally with `FromLogContext`: and push scoped properties (correlation ID, tenant ID) via `LogContext.PushProperty` so all downstream log events carry contextual data.

---

---
title: "Enrich with context (correlation IDs, user info)"
impact: MEDIUM
impactDescription: "general best practice"
tags: serilog, dotnet, logging
---

## Enrich with context (correlation IDs, user info)

Enrich with context (correlation IDs, user info)

---

---
title: "Override framework log levels"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: serilog, dotnet, logging, serilog-sink-configuration, structured-event-logging, log-enrichment
---

## Override framework log levels

(`Microsoft.AspNetCore`, `Microsoft.EntityFrameworkCore`) to `Warning` in production to reduce high-volume noise from internal framework logging.

---

---
title: "Use message templates instead of string interpolation"
impact: MEDIUM
impactDescription: "general best practice"
tags: serilog, dotnet, logging, serilog-sink-configuration, structured-event-logging, log-enrichment
---

## Use message templates instead of string interpolation

(`"Order {OrderId}"` not `$"Order {orderId}"`) so structured properties are preserved in sinks like Seq and Elasticsearch.

---

---
title: "Use `Serilog.AspNetCore`'s `UseSerilogRequestLogging()`"
impact: MEDIUM
impactDescription: "general best practice"
tags: serilog, dotnet, logging, serilog-sink-configuration, structured-event-logging, log-enrichment
---

## Use `Serilog.AspNetCore`'s `UseSerilogRequestLogging()`

Use `Serilog.AspNetCore`'s `UseSerilogRequestLogging()`: instead of the default ASP.NET Core request logging to get a single structured event per request with timing, status code, and custom properties.

---

---
title: "Use Serilog"
impact: MEDIUM
impactDescription: "general best practice"
tags: serilog, dotnet, logging
---

## Use Serilog

Use Serilog.AspNetCore for web apps

---

---
title: "Use structured logging with message templates"
impact: MEDIUM
impactDescription: "general best practice"
tags: serilog, dotnet, logging
---

## Use structured logging with message templates

Use structured logging with message templates

---

---
title: "Use the `@` destructuring operator"
impact: MEDIUM
impactDescription: "general best practice"
tags: serilog, dotnet, logging, serilog-sink-configuration, structured-event-logging, log-enrichment
---

## Use the `@` destructuring operator

Use the `@` destructuring operator: for complex objects (`{@Order}`) to capture their full structure, and the `$` stringify operator for enums and types where only the string representation matters.

---

---
title: "Use the two-stage initialization pattern"
impact: MEDIUM
impactDescription: "general best practice"
tags: serilog, dotnet, logging, serilog-sink-configuration, structured-event-logging, log-enrichment
---

## Use the two-stage initialization pattern

(bootstrap logger then full logger) so exceptions during host startup are captured and logged rather than lost to the void.

---

---
title: "Wrap high-latency sinks"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: serilog, dotnet, logging, serilog-sink-configuration, structured-event-logging, log-enrichment
---

## Wrap high-latency sinks

(file, database, network) with `Serilog.Sinks.Async` to prevent I/O from blocking the application's hot path.

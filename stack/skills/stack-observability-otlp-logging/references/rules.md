# OTLP Logging and Observability Rules

Best practices and rules for OTLP Logging and Observability.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Configure all three signals (traces, metrics, logs) together | MEDIUM | [`otlp-logging-configure-all-three-signals-traces-metrics-logs-together.md`](otlp-logging-configure-all-three-signals-traces-metrics-logs-together.md) |
| 2 | Use semantic conventions | MEDIUM | [`otlp-logging-use-semantic-conventions.md`](otlp-logging-use-semantic-conventions.md) |
| 3 | Set an appropriate sampling rate | CRITICAL | [`otlp-logging-set-an-appropriate-sampling-rate.md`](otlp-logging-set-an-appropriate-sampling-rate.md) |
| 4 | Add `ActivitySource.StartActivity` for business-critical operations | CRITICAL | [`otlp-logging-add-activitysource-startactivity-for-business-critical.md`](otlp-logging-add-activitysource-startactivity-for-business-critical.md) |
| 5 | Use the `OTEL_*` environment variables | MEDIUM | [`otlp-logging-use-the-otel-environment-variables.md`](otlp-logging-use-the-otel-environment-variables.md) |
| 6 | Include `IncludeFormattedMessage = true` | MEDIUM | [`otlp-logging-include-includeformattedmessage-true.md`](otlp-logging-include-includeformattedmessage-true.md) |
| 7 | Register custom `Meter` names | MEDIUM | [`otlp-logging-register-custom-meter-names.md`](otlp-logging-register-custom-meter-names.md) |
| 8 | Export to an OpenTelemetry Collector | MEDIUM | [`otlp-logging-export-to-an-opentelemetry-collector.md`](otlp-logging-export-to-an-opentelemetry-collector.md) |
| 9 | Check `activity is not null` | MEDIUM | [`otlp-logging-check-activity-is-not-null.md`](otlp-logging-check-activity-is-not-null.md) |
| 10 | Record error details on spans | MEDIUM | [`otlp-logging-record-error-details-on-spans.md`](otlp-logging-record-error-details-on-spans.md) |

---

---
title: "Add `ActivitySource.StartActivity` for business-critical operations"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: otlp-logging, dotnet, observability, otlp-log-export, opentelemetry-traces-and-metrics, distributed-tracing-with-activity-api
---

## Add `ActivitySource.StartActivity` for business-critical operations

(order processing, payment charging, inventory updates) to create custom spans that appear in the trace timeline alongside framework spans.

---

---
title: "Check `activity is not null`"
impact: MEDIUM
impactDescription: "general best practice"
tags: otlp-logging, dotnet, observability, otlp-log-export, opentelemetry-traces-and-metrics, distributed-tracing-with-activity-api
---

## Check `activity is not null`

Check `activity is not null`: before calling `SetTag` or `AddEvent` because `StartActivity` returns null when no listener (sampler) is active for the source, which is expected behavior.

---

---
title: "Configure all three signals (traces, metrics, logs) together"
impact: MEDIUM
impactDescription: "general best practice"
tags: otlp-logging, dotnet, observability, otlp-log-export, opentelemetry-traces-and-metrics, distributed-tracing-with-activity-api
---

## Configure all three signals (traces, metrics, logs) together

Configure all three signals (traces, metrics, logs) together: with a shared `Resource` so the observability backend can correlate data from the same service instance.

---

---
title: "Configure appropriate sampling"
impact: MEDIUM
impactDescription: "general best practice"
tags: otlp-logging, dotnet, observability
---

## Configure appropriate sampling

Configure appropriate sampling

---

---
title: "Correlate logs with traces"
impact: MEDIUM
impactDescription: "general best practice"
tags: otlp-logging, dotnet, observability
---

## Correlate logs with traces

Correlate logs with traces

---

---
title: "Export to an OpenTelemetry Collector"
impact: MEDIUM
impactDescription: "general best practice"
tags: otlp-logging, dotnet, observability, otlp-log-export, opentelemetry-traces-and-metrics, distributed-tracing-with-activity-api
---

## Export to an OpenTelemetry Collector

Export to an OpenTelemetry Collector: rather than directly to backends, so you can fan out to multiple destinations, apply transformations, and change backends without redeploying the application.

---

---
title: "Export to OTLP collector"
impact: MEDIUM
impactDescription: "general best practice"
tags: otlp-logging, dotnet, observability
---

## Export to OTLP collector

Export to OTLP collector

---

---
title: "Include `IncludeFormattedMessage = true`"
impact: MEDIUM
impactDescription: "general best practice"
tags: otlp-logging, dotnet, observability, otlp-log-export, opentelemetry-traces-and-metrics, distributed-tracing-with-activity-api
---

## Include `IncludeFormattedMessage = true`

Include `IncludeFormattedMessage = true`: and `IncludeScopes = true` in the logging exporter configuration so log messages in the backend are human-readable and include scope properties.

---

---
title: "Include trace context"
impact: MEDIUM
impactDescription: "general best practice"
tags: otlp-logging, dotnet, observability
---

## Include trace context

Include trace context

---

---
title: "Record error details on spans"
impact: MEDIUM
impactDescription: "general best practice"
tags: otlp-logging, dotnet, observability, otlp-log-export, opentelemetry-traces-and-metrics, distributed-tracing-with-activity-api
---

## Record error details on spans

Record error details on spans: using `activity?.SetStatus(ActivityStatusCode.Error, exception.Message)` and `activity?.RecordException(exception)` so error rates and stack traces are visible in the tracing backend.

---

---
title: "Register custom `Meter` names"
impact: MEDIUM
impactDescription: "general best practice"
tags: otlp-logging, dotnet, observability, otlp-log-export, opentelemetry-traces-and-metrics, distributed-tracing-with-activity-api
---

## Register custom `Meter` names

Register custom `Meter` names: in `AddMeter("MyApp.Orders")` on the metrics builder; meters not registered are silently ignored, which is a common configuration mistake.

---

---
title: "Set an appropriate sampling rate"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: otlp-logging, dotnet, observability, otlp-log-export, opentelemetry-traces-and-metrics, distributed-tracing-with-activity-api
---

## Set an appropriate sampling rate

Set an appropriate sampling rate: in production using `parentbased_traceidratio` (e.g., 10% via `OTEL_TRACES_SAMPLER_ARG=0.1`) to reduce storage costs while maintaining statistical significance.

---

---
title: "Use semantic conventions"
impact: MEDIUM
impactDescription: "general best practice"
tags: otlp-logging, dotnet, observability, otlp-log-export, opentelemetry-traces-and-metrics, distributed-tracing-with-activity-api
---

## Use semantic conventions

Use semantic conventions: for span names and attributes (e.g., `http.request.method`, `db.system`, `order.id`) so observability tools can provide automatic dashboards and alerts.

---

---
title: "Use structured logging"
impact: MEDIUM
impactDescription: "general best practice"
tags: otlp-logging, dotnet, observability
---

## Use structured logging

Use structured logging

---

---
title: "Use the `OTEL_*` environment variables"
impact: MEDIUM
impactDescription: "general best practice"
tags: otlp-logging, dotnet, observability, otlp-log-export, opentelemetry-traces-and-metrics, distributed-tracing-with-activity-api
---

## Use the `OTEL_*` environment variables

Use the `OTEL_*` environment variables: for configuration in containerized deployments, as the OpenTelemetry SDK reads them automatically without code changes.

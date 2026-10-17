---
name: stack-observability
description: Use when deciding how OTLP and Serilog fit together for .NET observability before wiring anything. USE FOR: approach selection, shared Resource config, log-trace correlation strategy, routing to the right sub-skill. DO NOT USE FOR: OTel exporter, spans, meters (use stack-observability-otlp-logging), Serilog config (use stack-serilog), dashboards and alert rules.
---

# Observability

## Overview

Observability in this .NET stack is built on two complementary layers: **OpenTelemetry (OTLP)** for distributed traces and metrics, and **Serilog** for structured log output. Together they provide the three pillars of observability — logs, traces, and metrics — with correlation between them via trace and span IDs injected into log entries.

## Sub-Skills

| Sub-Skill | Covers |
|-----------|--------|
| `otlp-logging` | OpenTelemetry setup, OTLP export, distributed tracing with `Activity` API, custom metrics with `System.Diagnostics.Metrics`, log-trace correlation |

## Choosing the Right Sub-Skill

| Need | Sub-Skill |
|------|-----------|
| Configure OTLP export, Activity spans, custom Meters | `otlp-logging` |
| Serilog sinks, enrichers, output templates | `stack-serilog` |

## Best Practices

- Configure all three signals (logs, traces, metrics) together with a shared `Resource` so the observability backend can correlate data from the same service instance.
- Prefer `OTEL_*` environment variables for endpoint and sampler configuration in containerized deployments so settings can change without code rebuilds.
- Add custom `ActivitySource` spans only for business-critical operations (payment processing, order creation, external API calls) — don't instrument every method or you'll create noise.
- Always export to an OpenTelemetry Collector rather than directly to backends so you can fan out to multiple destinations without redeploying services.

## References

- [OpenTelemetry .NET Documentation](https://opentelemetry.io/docs/languages/dotnet/)
- [Serilog Documentation](https://serilog.net)

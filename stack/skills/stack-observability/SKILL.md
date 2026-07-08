---
name: stack-observability
description: Observability entry point for LinkDaily services — routes to the right sub-skill for OpenTelemetry/OTLP tracing, metrics, and structured logging across LinkDaily.Api and LinkDaily.Worker. USE FOR: deciding which observability approach to use, understanding how OTLP and Serilog fit together in the LinkDaily stack, shared Resource configuration, log-trace correlation strategy. DO NOT USE FOR: OTLP exporter wiring, Activity API spans, custom Meters, or OTel collector config (use stack-observability-otlp-logging); Serilog sinks, enrichers, and output templates (use stack-serilog); infrastructure-level monitoring dashboards or alerting rule management.
---

# Observability

## Overview

Observability in the LinkDaily stack is built on two complementary layers: **OpenTelemetry (OTLP)** for distributed traces and metrics, and **Serilog** for structured log output. Together they provide the three pillars of observability — logs, traces, and metrics — with correlation between them via trace and span IDs injected into log entries.

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

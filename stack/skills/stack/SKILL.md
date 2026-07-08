---
name: stack
description: Router skill — use when you need to select the right .NET library for a task in LinkDaily and are unsure which specific stack-* skill to invoke. USE FOR: library selection guidance, choosing between NuGet packages, routing to the correct sub-skill (stack-masstransit, stack-mediatr, stack-dapper, stack-redis, stack-polly, stack-serilog, stack-automapper, stack-aspnet-identity, stack-openapi, stack-observability, stack-i18n, stack-docker, stack-hygiene, stack-validot, stack-ncrontab, stack-topshelf, stack-plunk-email). DO NOT USE FOR: general architecture decisions (use dev-architecture), security patterns (use security), cross-cutting backend design (use dev-backend) — once the right library is identified, use the specific stack-* child skill instead of this parent.
---

# Stack & Libraries

## Overview

This skill tree covers the specific third-party libraries and packages used in the LinkDaily .NET stack. Each sub-skill provides opinionated guidance on how to use the library correctly within this codebase, including configuration, patterns, and common pitfalls.

## Library Map

```
┌─────────────────────────────────────────────────────────────┐
│                    Messaging & CQRS                         │
│         MassTransit (messaging)  │  MediatR (CQRS)         │
├─────────────────────────────────────────────────────────────┤
│          Data Access             │      Caching             │
│      Dapper (micro-ORM)          │   Redis (distributed)    │
├─────────────────────────────────────────────────────────────┤
│         Resilience               │    Scheduling            │
│    Polly (retry, circuit break)  │  NCrontab (cron syntax)  │
│                                  │  Topshelf (host service) │
├─────────────────────────────────────────────────────────────┤
│        Object Mapping            │    Validation            │
│     AutoMapper (DTO mapping)     │  Validot (rules-based)   │
├─────────────────────────────────────────────────────────────┤
│       Observability              │      Email               │
│  OTLP / Serilog (logs, traces)   │  Plunk (transactional)   │
├─────────────────────────────────────────────────────────────┤
│          API                     │    Identity & Auth       │
│   OpenAPI (Scalar / Swashbuckle) │  ASP.NET Core Identity   │
├─────────────────────────────────────────────────────────────┤
│         i18n / l10n              │     Code Hygiene         │
│  Localization patterns & helpers │  Null safety, guards     │
│           Docker                 │                          │
│  Containerization for .NET apps  │                          │
└─────────────────────────────────────────────────────────────┘
```

## Choosing the Right Sub-Skill

| Need | Sub-Skill |
|------|-----------|
| Publish/consume messages, sagas, outbox pattern | `masstransit` |
| CQRS commands, queries, and pipeline behaviors | `mediatr` |
| Raw SQL queries, stored procedures, typed mapping | `dapper` |
| Distributed caching, pub/sub, distributed locks | `redis` |
| Retry policies, circuit breakers, timeouts, bulkhead | `polly` |
| Cron schedule parsing and next-occurrence calculation | `ncrontab` |
| Windows service hosting, start/stop lifecycle | `topshelf` |
| Flat DTO ↔ domain object mapping | `automapper` |
| Declarative validation rules and error messages | `validot` |
| OTLP traces, metrics, and structured logging | `observability` |
| Structured log sinks, enrichers, and output templates | `serilog` |
| Transactional and marketing emails via Plunk | `plunk-email` |
| OpenAPI spec generation and Scalar/Swagger UI | `openapi` |
| User registration, login, roles, and claims | `aspnet-identity` |
| Localization resources and culture-aware formatting | `i18n` |
| Containerize .NET services with Dockerfile and Compose | `docker` |
| Guard clauses, null checks, and defensive patterns | `hygiene` |

## Best Practices

- Match the library to the problem scope — don't use MassTransit for in-process events that MediatR handles better, and don't use MediatR notifications as a substitute for durable messaging that MassTransit provides.
- Keep library-specific configuration centralized (e.g., one `AddMassTransit()` call in `Program.cs`) and avoid scattering registration across multiple files.
- Treat the library version pinned in `Directory.Build.props` as the project standard — avoid upgrading a single project in isolation.
- Read the sub-skill before adding a new dependency to verify the library is already in the stack before proposing an alternative.

## References

- [NuGet Gallery](https://www.nuget.org)
- [.NET Documentation](https://learn.microsoft.com/en-us/dotnet/)

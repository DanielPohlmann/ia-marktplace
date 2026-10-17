---
name: dev-craftsmanship-twelve-factor
description: Use when designing or auditing a cloud-native service against the Twelve-Factor App. USE FOR: env-based config, backing services as attached resources, stateless processes, build/release/run, graceful shutdown, dev/prod parity, logs as streams. DO NOT USE FOR: container config (use tools-docker), service decomposition (use dev-architecture-microservices), logging library setup (use stack-serilog).
---

# The Twelve-Factor App

## Overview
The Twelve-Factor App is a methodology for building software-as-a-service applications, originally published by Adam Wiggins at Heroku in 2012. It provides a set of best practices for building applications that are portable, scalable, and suitable for deployment on modern cloud platforms.

These factors are technology-agnostic and apply equally to applications written in any language, deployed on any cloud provider or container orchestrator.

## Quick Reference

| # | Factor | One-Line Summary |
|---|--------|------------------|
| 1 | Codebase | One codebase tracked in revision control, many deploys. |
| 2 | Dependencies | Explicitly declare and isolate dependencies. |
| 3 | Config | Store config in the environment. |
| 4 | Backing Services | Treat backing services as attached resources. |
| 5 | Build, Release, Run | Strictly separate build and run stages. |
| 6 | Processes | Execute the app as one or more stateless processes. |
| 7 | Port Binding | Export services via port binding. |
| 8 | Concurrency | Scale out via the process model. |
| 9 | Disposability | Maximize robustness with fast startup and graceful shutdown. |
| 10 | Dev/Prod Parity | Keep development, staging, and production as similar as possible. |
| 11 | Logs | Treat logs as event streams. |
| 12 | Admin Processes | Run admin/management tasks as one-off processes. |

---

## Beyond the Twelve Factors

Kevin Hoffman's *Beyond the Twelve-Factor App* (2016) adds several factors relevant to modern cloud-native development:

| Factor | Description |
|--------|-------------|
| **API First** | Design the API contract before implementation. Use OpenAPI/Swagger, gRPC proto definitions, or AsyncAPI specs. |
| **Telemetry** | Go beyond logs: include metrics (Prometheus, StatsD), distributed tracing (OpenTelemetry, Jaeger), and health checks. |
| **Authentication & Authorization** | Security is not optional. Implement identity (OAuth2, OIDC), token validation, and least-privilege access at the app level. |

## Twelve-Factor Checklist

| # | Factor | Question to Ask |
|---|--------|-----------------|
| 1 | Codebase | Is there exactly one repo for this app? Can it be deployed independently? |
| 2 | Dependencies | Can a new developer clone and run with only the declared manifest? No global installs? |
| 3 | Config | Is every environment-specific value in env vars or a secrets manager? Zero secrets in code? |
| 4 | Backing Services | Can you swap the database provider by changing one config variable? |
| 5 | Build/Release/Run | Is the build artifact immutable? Is every release versioned? |
| 6 | Processes | If the process restarts, is all state preserved in a backing service? |
| 7 | Port Binding | Is the app self-contained with its own HTTP listener? No external webserver dependency? |
| 8 | Concurrency | Can you scale by running more instances, not bigger instances? |
| 9 | Disposability | Does the app start in under 10 seconds? Handle SIGTERM gracefully? |
| 10 | Dev/Prod Parity | Are the same backing services used in dev, staging, and production? |
| 11 | Logs | Does the app write to stdout only? No file-based logging? |
| 12 | Admin Processes | Are migrations and scripts run in the same environment as the app? |

## Best Practices
- Treat the twelve factors as a checklist during architecture reviews and pull requests.
- Adopt factors incrementally — you do not need to satisfy all twelve on day one.
- Use containers (Docker) as the natural packaging for twelve-factor apps: they enforce dependency isolation, port binding, and process disposability.
- Combine twelve-factor with cloud-native patterns: circuit breakers, retries with backoff, health checks, and graceful degradation.
- Automate compliance: use CI checks to verify no secrets in code (Factor III), lock files present (Factor II), and health endpoints exist (Factor IX).
- When twelve-factor conflicts with pragmatism (e.g., local file caching for performance), document the deviation and contain the blast radius.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/details.md](references/details.md) | I. Codebase; II. Dependencies; III. Config; IV. Backing Services; V. Build, Release, Run; VI. Processes; VII. Port Binding; VIII. Concurrency; IX. Disposability; X. Dev/Prod Parity; XI. Logs; XII. Admin Processes |

## References

- [The Twelve-Factor App](https://12factor.net/)
- [Twelve-Factor App Methodology — Wikipedia](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology)

See references/rules.md for the full rule catalog.

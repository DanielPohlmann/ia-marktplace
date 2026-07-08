# Polly Rules

Best practices and rules for Polly.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Use Polly v8's `ResiliencePipelineBuilder` API exclusively | CRITICAL | [`polly-use-polly-v8-s-resiliencepipelinebuilder-api-exclusively.md`](polly-use-polly-v8-s-resiliencepipelinebuilder-api-exclusively.md) |
| 2 | Always enable `UseJitter = true` on retry strategies | CRITICAL | [`polly-always-enable-usejitter-true-on-retry-strategies.md`](polly-always-enable-usejitter-true-on-retry-strategies.md) |
| 3 | Add strategies in order from outermost to innermost: total timeout, retry, circuit breaker, attempt timeout | MEDIUM | [`polly-add-strategies-in-order-from-outermost-to-innermost-total.md`](polly-add-strategies-in-order-from-outermost-to-innermost-total.md) |
| 4 | Use `PredicateBuilder` with `Handle<TException>()` and `HandleResult()` to explicitly define which failures trigger resilience strategies | MEDIUM | [`polly-use-predicatebuilder-with-handle-texception-and.md`](polly-use-predicatebuilder-with-handle-texception-and.md) |
| 5 | Set `MinimumThroughput` on circuit breakers to at least 10 | HIGH | [`polly-set-minimumthroughput-on-circuit-breakers-to-at-least-10.md`](polly-set-minimumthroughput-on-circuit-breakers-to-at-least-10.md) |
| 6 | Build pipelines once and reuse them | MEDIUM | [`polly-build-pipelines-once-and-reuse-them.md`](polly-build-pipelines-once-and-reuse-them.md) |
| 7 | Use the `OnRetry`, `OnOpened`, `OnClosed` lifecycle callbacks for logging and metrics | MEDIUM | [`polly-use-the-onretry-onopened-onclosed-lifecycle-callbacks-for.md`](polly-use-the-onretry-onopened-onclosed-lifecycle-callbacks-for.md) |
| 8 | Handle `BrokenCircuitException` and `TimeoutRejectedException` at the caller level | MEDIUM | [`polly-handle-brokencircuitexception-and-timeoutrejectedexception.md`](polly-handle-brokencircuitexception-and-timeoutrejectedexception.md) |
| 9 | Prefer `Microsoft.Extensions.Http.Resilience` with `AddStandardResilienceHandler` for HttpClient resilience | LOW | [`polly-prefer-microsoft-extensions-http-resilience-with.md`](polly-prefer-microsoft-extensions-http-resilience-with.md) |
| 10 | Test resilience pipelines by injecting controlled failures | MEDIUM | [`polly-test-resilience-pipelines-by-injecting-controlled-failures.md`](polly-test-resilience-pipelines-by-injecting-controlled-failures.md) |

---

---
title: "Add strategies in order from outermost to innermost: total timeout, retry, circuit breaker, attempt timeout"
impact: MEDIUM
impactDescription: "general best practice"
tags: polly, dotnet, resilience, implementing-resilience-patterns-retry, circuit-breaker, timeout
---

## Add strategies in order from outermost to innermost: total timeout, retry, circuit breaker, attempt timeout

Add strategies in order from outermost to innermost: total timeout, retry, circuit breaker, attempt timeout: so that the total timeout caps the entire operation, retries wrap the circuit breaker, and the attempt timeout applies to each individual call.

---

---
title: "Always enable `UseJitter = true` on retry strategies"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: polly, dotnet, resilience, implementing-resilience-patterns-retry, circuit-breaker, timeout
---

## Always enable `UseJitter = true` on retry strategies

Always enable `UseJitter = true` on retry strategies: to add randomized spread to retry delays, preventing synchronized retry storms when many clients recover from the same outage simultaneously.

---

---
title: "Build pipelines once and reuse them"
impact: MEDIUM
impactDescription: "general best practice"
tags: polly, dotnet, resilience, implementing-resilience-patterns-retry, circuit-breaker, timeout
---

## Build pipelines once and reuse them

Build pipelines once and reuse them: because `ResiliencePipeline` instances are thread-safe and immutable after `Build()` is called; creating a new pipeline per request wastes resources and bypasses circuit breaker state.

---

---
title: "Combine policies with PolicyWrap"
impact: MEDIUM
impactDescription: "general best practice"
tags: polly, dotnet, resilience
---

## Combine policies with PolicyWrap

Combine policies with PolicyWrap

---

---
title: "Configure appropriate timeouts"
impact: MEDIUM
impactDescription: "general best practice"
tags: polly, dotnet, resilience
---

## Configure appropriate timeouts

Configure appropriate timeouts

---

---
title: "Handle `BrokenCircuitException` and `TimeoutRejectedException` at the caller level"
impact: MEDIUM
impactDescription: "general best practice"
tags: polly, dotnet, resilience, implementing-resilience-patterns-retry, circuit-breaker, timeout
---

## Handle `BrokenCircuitException` and `TimeoutRejectedException` at the caller level

Handle `BrokenCircuitException` and `TimeoutRejectedException` at the caller level: to provide meaningful error messages or fallback responses when the circuit is open or the operation times out, rather than letting these propagate as unhandled exceptions.

---

---
title: "Log policy events"
impact: MEDIUM
impactDescription: "general best practice"
tags: polly, dotnet, resilience
---

## Log policy events

Log policy events

---

---
title: "Prefer `Microsoft.Extensions.Http.Resilience` with `AddStandardResilienceHandler` for HttpClient resilience"
impact: LOW
impactDescription: "recommended but situational"
tags: polly, dotnet, resilience, implementing-resilience-patterns-retry, circuit-breaker, timeout
---

## Prefer `Microsoft.Extensions.Http.Resilience` with `AddStandardResilienceHandler` for HttpClient resilience

Prefer `Microsoft.Extensions.Http.Resilience` with `AddStandardResilienceHandler` for HttpClient resilience: over manually constructing Polly pipelines, because the standard handler provides Microsoft-tested defaults and integrates with `IHttpClientFactory` lifecycle management.

---

---
title: "Set `MinimumThroughput` on circuit breakers to at least 10"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: polly, dotnet, resilience, implementing-resilience-patterns-retry, circuit-breaker, timeout
---

## Set `MinimumThroughput` on circuit breakers to at least 10

Set `MinimumThroughput` on circuit breakers to at least 10: to prevent the circuit from tripping during low-traffic periods where a single failure could exceed the failure ratio; this ensures statistical significance.

---

---
title: "Test resilience pipelines by injecting controlled failures"
impact: MEDIUM
impactDescription: "general best practice"
tags: polly, dotnet, resilience, implementing-resilience-patterns-retry, circuit-breaker, timeout
---

## Test resilience pipelines by injecting controlled failures

Test resilience pipelines by injecting controlled failures: using a test `DelegatingHandler` that returns HTTP 503 or throws `HttpRequestException` on specific calls to verify that retry counts, circuit breaker transitions, and timeout behavior work as configured.

---

---
title: "Use circuit breakers for remote calls"
impact: MEDIUM
impactDescription: "general best practice"
tags: polly, dotnet, resilience
---

## Use circuit breakers for remote calls

Use circuit breakers for remote calls

---

---
title: "Use Polly.Extensions"
impact: MEDIUM
impactDescription: "general best practice"
tags: polly, dotnet, resilience
---

## Use Polly.Extensions

Use Polly.Extensions.Http for HttpClient

---

---
title: "Use Polly v8's `ResiliencePipelineBuilder` API exclusively"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: polly, dotnet, resilience, implementing-resilience-patterns-retry, circuit-breaker, timeout
---

## Use Polly v8's `ResiliencePipelineBuilder` API exclusively

Use Polly v8's `ResiliencePipelineBuilder` API exclusively: and do not mix it with the legacy v7 `Policy` API; v8 pipelines are allocation-free on the hot path and provide built-in telemetry that v7 policies do not.

---

---
title: "Use `PredicateBuilder` with `Handle<TException>()` and `HandleResult()` to explicitly define which failures trigger resilience strategies"
impact: MEDIUM
impactDescription: "general best practice"
tags: polly, dotnet, resilience, implementing-resilience-patterns-retry, circuit-breaker, timeout
---

## Use `PredicateBuilder` with `Handle<TException>()` and `HandleResult()` to explicitly define which failures trigger resilience strategies

Use `PredicateBuilder` with `Handle<TException>()` and `HandleResult()` to explicitly define which failures trigger resilience strategies: rather than catching all exceptions, which would retry permanent failures like `ArgumentException` or `AuthenticationException`.

---

---
title: "Use the `OnRetry`, `OnOpened`, `OnClosed` lifecycle callbacks for logging and metrics"
impact: MEDIUM
impactDescription: "general best practice"
tags: polly, dotnet, resilience, implementing-resilience-patterns-retry, circuit-breaker, timeout
---

## Use the `OnRetry`, `OnOpened`, `OnClosed` lifecycle callbacks for logging and metrics

Use the `OnRetry`, `OnOpened`, `OnClosed` lifecycle callbacks for logging and metrics: rather than wrapping pipeline execution in try/catch blocks, because the callbacks receive structured context (`AttemptNumber`, `RetryDelay`, `BreakDuration`) that is not available in catch blocks.

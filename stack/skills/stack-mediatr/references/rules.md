# MediatR Rules

Best practices and rules for MediatR.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Keep handlers focused on a single responsibility | MEDIUM | [`mediatr-keep-handlers-focused-on-a-single-responsibility.md`](mediatr-keep-handlers-focused-on-a-single-responsibility.md) |
| 2 | Use `IPipelineBehavior<,>` for cross-cutting concerns... | MEDIUM | [`mediatr-use-ipipelinebehavior-for-cross-cutting-concerns.md`](mediatr-use-ipipelinebehavior-for-cross-cutting-concerns.md) |
| 3 | Separate commands (`IRequest<TResponse>`) from queries... | MEDIUM | [`mediatr-separate-commands-irequest-tresponse-from-queries.md`](mediatr-separate-commands-irequest-tresponse-from-queries.md) |
| 4 | Use `INotification` and `INotificationHandler<>` for... | MEDIUM | [`mediatr-use-inotification-and-inotificationhandler-for.md`](mediatr-use-inotification-and-inotificationhandler-for.md) |
| 5 | Register pipeline behaviors in the correct order (e | MEDIUM | [`mediatr-register-pipeline-behaviors-in-the-correct-order-e.md`](mediatr-register-pipeline-behaviors-in-the-correct-order-e.md) |
| 6 | Inject `IMediator` or `ISender` into controllers/endpoints,... | MEDIUM | [`mediatr-inject-imediator-or-isender-into-controllers-endpoints.md`](mediatr-inject-imediator-or-isender-into-controllers-endpoints.md) |
| 7 | Use `CancellationToken` consistently by passing it through... | MEDIUM | [`mediatr-use-cancellationtoken-consistently-by-passing-it-through.md`](mediatr-use-cancellationtoken-consistently-by-passing-it-through.md) |
| 8 | Prefer `ISender` (for `Send`) or `IPublisher` (for... | LOW | [`mediatr-prefer-isender-for-send-or-ipublisher-for.md`](mediatr-prefer-isender-for-send-or-ipublisher-for.md) |
| 9 | Validate command inputs in a `ValidationBehavior` pipeline... | HIGH | [`mediatr-validate-command-inputs-in-a-validationbehavior-pipeline.md`](mediatr-validate-command-inputs-in-a-validationbehavior-pipeline.md) |
| 10 | Avoid using MediatR for inter-service communication; it is... | HIGH | [`mediatr-avoid-using-mediatr-for-inter-service-communication-it-is.md`](mediatr-avoid-using-mediatr-for-inter-service-communication-it-is.md) |

---

---
title: "Avoid using MediatR for inter-service communication; it is..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: mediatr, dotnet, eventing, in-process-commandquery-dispatch, cqrs-with-pipeline-behaviors, notification-fan-out
---

## Avoid using MediatR for inter-service communication; it is...

Avoid using MediatR for inter-service communication; it is strictly in-process -- use MassTransit, NServiceBus, or Rebus for distributed messaging.

---

---
title: "Inject `IMediator` or `ISender` into controllers/endpoints,..."
impact: MEDIUM
impactDescription: "general best practice"
tags: mediatr, dotnet, eventing, in-process-commandquery-dispatch, cqrs-with-pipeline-behaviors, notification-fan-out
---

## Inject `IMediator` or `ISender` into controllers/endpoints,...

Inject `IMediator` or `ISender` into controllers/endpoints, not into domain services; MediatR is a composition root concern, not a domain concern.

---

---
title: "Keep handlers focused on a single responsibility"
impact: MEDIUM
impactDescription: "general best practice"
tags: mediatr, dotnet, eventing, in-process-commandquery-dispatch, cqrs-with-pipeline-behaviors, notification-fan-out
---

## Keep handlers focused on a single responsibility

Keep handlers focused on a single responsibility: one handler per command or query, with no shared mutable state between handlers.

---

---
title: "Prefer `ISender` (for `Send`) or `IPublisher` (for..."
impact: LOW
impactDescription: "recommended but situational"
tags: mediatr, dotnet, eventing, in-process-commandquery-dispatch, cqrs-with-pipeline-behaviors, notification-fan-out
---

## Prefer `ISender` (for `Send`) or `IPublisher` (for...

Prefer `ISender` (for `Send`) or `IPublisher` (for `Publish`) over the full `IMediator` interface to express minimal dependency.

---

---
title: "Register pipeline behaviors in the correct order (e"
impact: MEDIUM
impactDescription: "general best practice"
tags: mediatr, dotnet, eventing, in-process-commandquery-dispatch, cqrs-with-pipeline-behaviors, notification-fan-out
---

## Register pipeline behaviors in the correct order (e

Register pipeline behaviors in the correct order (e.g., logging first, then validation, then caching) since they execute as a nested middleware chain.

---

---
title: "Separate commands (`IRequest<TResponse>`) from queries..."
impact: MEDIUM
impactDescription: "general best practice"
tags: mediatr, dotnet, eventing, in-process-commandquery-dispatch, cqrs-with-pipeline-behaviors, notification-fan-out
---

## Separate commands (`IRequest<TResponse>`) from queries...

Separate commands (`IRequest<TResponse>`) from queries conceptually even though they use the same interface; commands should mutate state and queries should read without side effects.

---

---
title: "Use `CancellationToken` consistently by passing it through..."
impact: MEDIUM
impactDescription: "general best practice"
tags: mediatr, dotnet, eventing, in-process-commandquery-dispatch, cqrs-with-pipeline-behaviors, notification-fan-out
---

## Use `CancellationToken` consistently by passing it through...

Use `CancellationToken` consistently by passing it through from the request to the handler and to all async calls within the handler.

---

---
title: "Use `INotification` and `INotificationHandler<>` for..."
impact: MEDIUM
impactDescription: "general best practice"
tags: mediatr, dotnet, eventing, in-process-commandquery-dispatch, cqrs-with-pipeline-behaviors, notification-fan-out
---

## Use `INotification` and `INotificationHandler<>` for...

Use `INotification` and `INotificationHandler<>` for in-process fan-out events; for cross-service events, publish to a message broker instead.

---

---
title: "Use `IPipelineBehavior<,>` for cross-cutting concerns..."
impact: MEDIUM
impactDescription: "general best practice"
tags: mediatr, dotnet, eventing, in-process-commandquery-dispatch, cqrs-with-pipeline-behaviors, notification-fan-out
---

## Use `IPipelineBehavior<,>` for cross-cutting concerns...

Use `IPipelineBehavior<,>` for cross-cutting concerns (validation, logging, caching, authorization) rather than duplicating logic in every handler.

---

---
title: "Validate command inputs in a `ValidationBehavior` pipeline..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: mediatr, dotnet, eventing, in-process-commandquery-dispatch, cqrs-with-pipeline-behaviors, notification-fan-out
---

## Validate command inputs in a `ValidationBehavior` pipeline...

Validate command inputs in a `ValidationBehavior` pipeline step using FluentValidation so handlers can assume valid input.

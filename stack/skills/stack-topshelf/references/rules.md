# Topshelf Rules

Best practices and rules for Topshelf.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Use Topshelf only for .NET Framework services or legacy maintenance | LOW | [`topshelf-use-topshelf-only-for-net-framework-services-or-legacy.md`](topshelf-use-topshelf-only-for-net-framework-services-or-legacy.md) |
| 2 | Always return `true` from `Start` and `Stop` | CRITICAL | [`topshelf-always-return-true-from-start-and-stop.md`](topshelf-always-return-true-from-start-and-stop.md) |
| 3 | Configure service recovery | MEDIUM | [`topshelf-configure-service-recovery.md`](topshelf-configure-service-recovery.md) |
| 4 | Test as a console application first | MEDIUM | [`topshelf-test-as-a-console-application-first.md`](topshelf-test-as-a-console-application-first.md) |
| 5 | Use `RunAsLocalSystem()` for services that do not need network access | CRITICAL | [`topshelf-use-runaslocalsystem-for-services-that-do-not-need-network.md`](topshelf-use-runaslocalsystem-for-services-that-do-not-need-network.md) |
| 6 | Set `StartAutomatically()` | CRITICAL | [`topshelf-set-startautomatically.md`](topshelf-set-startautomatically.md) |
| 7 | Enable `EnableShutdown()` | MEDIUM | [`topshelf-enable-enableshutdown.md`](topshelf-enable-enableshutdown.md) |
| 8 | Use the `HostControl` parameter in `Start`/`Stop` | MEDIUM | [`topshelf-use-the-hostcontrol-parameter-in-start-stop.md`](topshelf-use-the-hostcontrol-parameter-in-start-stop.md) |
| 9 | Integrate a DI container | MEDIUM | [`topshelf-integrate-a-di-container.md`](topshelf-integrate-a-di-container.md) |
| 10 | Plan migration to BackgroundService | MEDIUM | [`topshelf-plan-migration-to-backgroundservice.md`](topshelf-plan-migration-to-backgroundservice.md) |

---

---
title: "Always return `true` from `Start` and `Stop`"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: topshelf, dotnet, general, creating-windows-services-with-fluent-api, service-installuninstall-from-command-line, service-recovery-configuration
---

## Always return `true` from `Start` and `Stop`

Always return `true` from `Start` and `Stop`: unless there is a genuine startup failure that should prevent the service from running.

---

---
title: "Configure appropriate recovery options"
impact: MEDIUM
impactDescription: "general best practice"
tags: topshelf, dotnet, general
---

## Configure appropriate recovery options

Configure appropriate recovery options

---

---
title: "Configure service recovery"
impact: MEDIUM
impactDescription: "general best practice"
tags: topshelf, dotnet, general, creating-windows-services-with-fluent-api, service-installuninstall-from-command-line, service-recovery-configuration
---

## Configure service recovery

Configure service recovery: with `EnableServiceRecovery` so the service restarts automatically after crashes without manual intervention.

---

---
title: "Consider modern alternatives (BackgroundService)"
impact: LOW
impactDescription: "recommended but situational"
tags: topshelf, dotnet, general
---

## Consider modern alternatives (BackgroundService)

Consider modern alternatives (BackgroundService)

---

---
title: "Enable `EnableShutdown()`"
impact: MEDIUM
impactDescription: "general best practice"
tags: topshelf, dotnet, general, creating-windows-services-with-fluent-api, service-installuninstall-from-command-line, service-recovery-configuration
---

## Enable `EnableShutdown()`

Enable `EnableShutdown()`: so the service responds properly to system shutdown events and has time to clean up resources.

---

---
title: "Handle start/stop gracefully"
impact: MEDIUM
impactDescription: "general best practice"
tags: topshelf, dotnet, general
---

## Handle start/stop gracefully

Handle start/stop gracefully

---

---
title: "Implement proper logging"
impact: MEDIUM
impactDescription: "general best practice"
tags: topshelf, dotnet, general
---

## Implement proper logging

Implement proper logging

---

---
title: "Integrate a DI container"
impact: MEDIUM
impactDescription: "general best practice"
tags: topshelf, dotnet, general, creating-windows-services-with-fluent-api, service-installuninstall-from-command-line, service-recovery-configuration
---

## Integrate a DI container

Integrate a DI container: by building the service provider before `HostFactory.Run` and resolving the service inside `ConstructUsing`.

---

---
title: "Plan migration to BackgroundService"
impact: MEDIUM
impactDescription: "general best practice"
tags: topshelf, dotnet, general, creating-windows-services-with-fluent-api, service-installuninstall-from-command-line, service-recovery-configuration
---

## Plan migration to BackgroundService

Plan migration to BackgroundService: for any Topshelf service that will be upgraded to .NET 6+, since Topshelf is in maintenance mode and the modern hosting model is more capable and actively maintained.

---

---
title: "Set `StartAutomatically()`"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: topshelf, dotnet, general, creating-windows-services-with-fluent-api, service-installuninstall-from-command-line, service-recovery-configuration
---

## Set `StartAutomatically()`

Set `StartAutomatically()`: for production services so they start on system boot without manual intervention.

---

---
title: "Test as a console application first"
impact: MEDIUM
impactDescription: "general best practice"
tags: topshelf, dotnet, general, creating-windows-services-with-fluent-api, service-installuninstall-from-command-line, service-recovery-configuration
---

## Test as a console application first

Test as a console application first: by running the executable directly -- Topshelf automatically detects console mode vs. service mode.

---

---
title: "Test as console app first"
impact: MEDIUM
impactDescription: "general best practice"
tags: topshelf, dotnet, general
---

## Test as console app first

Test as console app first

---

---
title: "Use `RunAsLocalSystem()` for services that do not need network access"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: topshelf, dotnet, general, creating-windows-services-with-fluent-api, service-installuninstall-from-command-line, service-recovery-configuration
---

## Use `RunAsLocalSystem()` for services that do not need network access

Use `RunAsLocalSystem()` for services that do not need network access: and `RunAsNetworkService()` for services that need to authenticate on the network.

---

---
title: "Use the `HostControl` parameter in `Start`/`Stop`"
impact: MEDIUM
impactDescription: "general best practice"
tags: topshelf, dotnet, general, creating-windows-services-with-fluent-api, service-installuninstall-from-command-line, service-recovery-configuration
---

## Use the `HostControl` parameter in `Start`/`Stop`

Use the `HostControl` parameter in `Start`/`Stop`: to request service stop from within the service itself (e.g., `hostControl.Stop()` on unrecoverable error).

---

---
title: "Use Topshelf only for .NET Framework services or legacy maintenance"
impact: LOW
impactDescription: "recommended but situational"
tags: topshelf, dotnet, general, creating-windows-services-with-fluent-api, service-installuninstall-from-command-line, service-recovery-configuration
---

## Use Topshelf only for .NET Framework services or legacy maintenance

Use Topshelf only for .NET Framework services or legacy maintenance: for new .NET 6+ services, prefer `BackgroundService` with `AddWindowsService()`.

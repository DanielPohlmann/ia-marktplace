# AutoMapper Rules

Best practices and rules for AutoMapper.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Organize mappings into `Profile` classes | MEDIUM | [`automapper-organize-mappings-into-profile-classes.md`](automapper-organize-mappings-into-profile-classes.md) |
| 2 | Call `AssertConfigurationIsValid()` | MEDIUM | [`automapper-call-assertconfigurationisvalid.md`](automapper-call-assertconfigurationisvalid.md) |
| 3 | Use `ProjectTo<T>()` instead of `Map<T>()` | HIGH | [`automapper-use-projectto-t-instead-of-map-t.md`](automapper-use-projectto-t-instead-of-map-t.md) |
| 4 | Avoid placing business logic inside mapping profiles | HIGH | [`automapper-avoid-placing-business-logic-inside-mapping-profiles.md`](automapper-avoid-placing-business-logic-inside-mapping-profiles.md) |
| 5 | Use `ForMember(..., opt => opt.Ignore())` | HIGH | [`automapper-use-formember-opt-opt-ignore.md`](automapper-use-formember-opt-opt-ignore.md) |
| 6 | Prefer `IMapper` injection | CRITICAL | [`automapper-prefer-imapper-injection.md`](automapper-prefer-imapper-injection.md) |
| 7 | Flatten nested objects by convention | MEDIUM | [`automapper-flatten-nested-objects-by-convention.md`](automapper-flatten-nested-objects-by-convention.md) |
| 8 | Register value resolvers and type converters in DI | MEDIUM | [`automapper-register-value-resolvers-and-type-converters-in-di.md`](automapper-register-value-resolvers-and-type-converters-in-di.md) |
| 9 | Keep DTOs simple and flat | MEDIUM | [`automapper-keep-dtos-simple-and-flat.md`](automapper-keep-dtos-simple-and-flat.md) |
| 10 | Consider migrating to Mapperly | LOW | [`automapper-consider-migrating-to-mapperly.md`](automapper-consider-migrating-to-mapperly.md) |

---

---
title: "Avoid mapping business logic"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: automapper, dotnet, mapping
---

## Avoid mapping business logic

Avoid mapping business logic

---

---
title: "Avoid placing business logic inside mapping profiles"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: automapper, dotnet, mapping, convention-based-object-to-object-mapping, profile-based-mapping-configuration, flatteningunflattening
---

## Avoid placing business logic inside mapping profiles

; mappings should be pure data transformations. Complex logic belongs in service classes that call the mapper.

---

---
title: "Call `AssertConfigurationIsValid()`"
impact: MEDIUM
impactDescription: "general best practice"
tags: automapper, dotnet, mapping, convention-based-object-to-object-mapping, profile-based-mapping-configuration, flatteningunflattening
---

## Call `AssertConfigurationIsValid()`

Call `AssertConfigurationIsValid()`: during application startup or in an integration test to catch missing member mappings, typos, and configuration errors before they cause runtime exceptions.

---

---
title: "Consider Mapperly for source generation alternative"
impact: LOW
impactDescription: "recommended but situational"
tags: automapper, dotnet, mapping
---

## Consider Mapperly for source generation alternative

Consider Mapperly for source generation alternative

---

---
title: "Consider migrating to Mapperly"
impact: LOW
impactDescription: "recommended but situational"
tags: automapper, dotnet, mapping, convention-based-object-to-object-mapping, profile-based-mapping-configuration, flatteningunflattening
---

## Consider migrating to Mapperly

Consider migrating to Mapperly: for new projects or hot-path mappings where the compile-time safety and zero-reflection performance of source generation outweigh AutoMapper's runtime flexibility.

---

---
title: "Flatten nested objects by convention"
impact: MEDIUM
impactDescription: "general best practice"
tags: automapper, dotnet, mapping, convention-based-object-to-object-mapping, profile-based-mapping-configuration, flatteningunflattening
---

## Flatten nested objects by convention

(AutoMapper automatically maps `src.Customer.Name` to `dest.CustomerName`) and only use `ForMember` when the convention does not apply.

---

---
title: "Keep DTOs simple and flat"
impact: MEDIUM
impactDescription: "general best practice"
tags: automapper, dotnet, mapping, convention-based-object-to-object-mapping, profile-based-mapping-configuration, flatteningunflattening
---

## Keep DTOs simple and flat

Keep DTOs simple and flat: to take advantage of AutoMapper's convention-based mapping; deeply nested DTOs negate the benefit of the library.

---

---
title: "Organize mappings into `Profile` classes"
impact: MEDIUM
impactDescription: "general best practice"
tags: automapper, dotnet, mapping, convention-based-object-to-object-mapping, profile-based-mapping-configuration, flatteningunflattening
---

## Organize mappings into `Profile` classes

Organize mappings into `Profile` classes: by feature area or bounded context (e.g., `OrderMappingProfile`, `CustomerMappingProfile`) rather than putting all mappings in a single profile.

---

---
title: "Prefer `IMapper` injection"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: automapper, dotnet, mapping, convention-based-object-to-object-mapping, profile-based-mapping-configuration, flatteningunflattening
---

## Prefer `IMapper` injection

Prefer `IMapper` injection: over `Mapper.Map` static calls so mappings are testable with mock/stub implementations and do not rely on global state.

---

---
title: "Register value resolvers and type converters in DI"
impact: MEDIUM
impactDescription: "general best practice"
tags: automapper, dotnet, mapping, convention-based-object-to-object-mapping, profile-based-mapping-configuration, flatteningunflattening
---

## Register value resolvers and type converters in DI

Register value resolvers and type converters in DI: so they can access services like `IHttpContextAccessor` or `ICurrentUser` for context-dependent mapping.

---

---
title: "Use `ForMember(..., opt => opt.Ignore())`"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: automapper, dotnet, mapping, convention-based-object-to-object-mapping, profile-based-mapping-configuration, flatteningunflattening
---

## Use `ForMember(..., opt => opt.Ignore())`

Use `ForMember(..., opt => opt.Ignore())`: explicitly for destination properties that should not be mapped (e.g., `Id` on creation DTOs) to prevent `AssertConfigurationIsValid` from flagging them as unmapped.

---

---
title: "Use profiles to organize mappings"
impact: MEDIUM
impactDescription: "general best practice"
tags: automapper, dotnet, mapping
---

## Use profiles to organize mappings

Use profiles to organize mappings

---

---
title: "Use ProjectTo for IQueryable"
impact: MEDIUM
impactDescription: "general best practice"
tags: automapper, dotnet, mapping
---

## Use ProjectTo for IQueryable

Use ProjectTo for IQueryable

---

---
title: "Use `ProjectTo<T>()` instead of `Map<T>()`"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: automapper, dotnet, mapping, convention-based-object-to-object-mapping, profile-based-mapping-configuration, flatteningunflattening
---

## Use `ProjectTo<T>()` instead of `Map<T>()`

Use `ProjectTo<T>()` instead of `Map<T>()`: when querying with EF Core to generate efficient SQL that selects only the mapped columns, avoiding N+1 queries and unnecessary data loading.

---

---
title: "Validate configuration on startup"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: automapper, dotnet, mapping
---

## Validate configuration on startup

Validate configuration on startup

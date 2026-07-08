# Dapper Rules

Best practices and rules for Dapper.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Always use parameterized queries with anonymous objects (e | CRITICAL | [`dapper-always-use-parameterized-queries-with-anonymous-objects-e.md`](dapper-always-use-parameterized-queries-with-anonymous-objects-e.md) |
| 2 | Create and dispose `IDbConnection` per operation or per... | CRITICAL | [`dapper-create-and-dispose-idbconnection-per-operation-or-per.md`](dapper-create-and-dispose-idbconnection-per-operation-or-per.md) |
| 3 | Use `QuerySingleOrDefaultAsync` when you expect zero or one... | MEDIUM | [`dapper-use-querysingleordefaultasync-when-you-expect-zero-or-one.md`](dapper-use-querysingleordefaultasync-when-you-expect-zero-or-one.md) |
| 4 | Specify `splitOn` explicitly in multi-mapping queries to... | HIGH | [`dapper-specify-spliton-explicitly-in-multi-mapping-queries-to.md`](dapper-specify-spliton-explicitly-in-multi-mapping-queries-to.md) |
| 5 | Use `DynamicParameters` with `ParameterDirection | MEDIUM | [`dapper-use-dynamicparameters-with-parameterdirection.md`](dapper-use-dynamicparameters-with-parameterdirection.md) |
| 6 | Wrap multiple related write operations in an explicit... | MEDIUM | [`dapper-wrap-multiple-related-write-operations-in-an-explicit.md`](dapper-wrap-multiple-related-write-operations-in-an-explicit.md) |
| 7 | Use `QueryMultipleAsync` to batch multiple SELECT... | MEDIUM | [`dapper-use-querymultipleasync-to-batch-multiple-select.md`](dapper-use-querymultipleasync-to-batch-multiple-select.md) |
| 8 | Keep Dapper queries in dedicated repository or query... | MEDIUM | [`dapper-keep-dapper-queries-in-dedicated-repository-or-query.md`](dapper-keep-dapper-queries-in-dedicated-repository-or-query.md) |
| 9 | Use `buffered | HIGH | [`dapper-use-buffered.md`](dapper-use-buffered.md) |
| 10 | Add a thin abstraction (e | MEDIUM | [`dapper-add-a-thin-abstraction-e.md`](dapper-add-a-thin-abstraction-e.md) |

---

---
title: "Add a thin abstraction (e"
impact: MEDIUM
impactDescription: "general best practice"
tags: dapper, dotnet, data, high-performance-sql-queries-mapped-to-pocos, read-heavy-and-latency-critical-data-access, stored-procedure-invocation
---

## Add a thin abstraction (e

Add a thin abstraction (e.g., `IDbConnectionFactory`) over connection creation to simplify testing with in-memory databases like SQLite.

---

---
title: "Always use parameterized queries with anonymous objects (e"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: dapper, dotnet, data, high-performance-sql-queries-mapped-to-pocos, read-heavy-and-latency-critical-data-access, stored-procedure-invocation
---

## Always use parameterized queries with anonymous objects (e

Always use parameterized queries with anonymous objects (e.g., `new { Id = id }`) instead of string interpolation to prevent SQL injection and enable query plan caching.

---

---
title: "Create and dispose `IDbConnection` per operation or per..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: dapper, dotnet, data, high-performance-sql-queries-mapped-to-pocos, read-heavy-and-latency-critical-data-access, stored-procedure-invocation
---

## Create and dispose `IDbConnection` per operation or per...

Create and dispose `IDbConnection` per operation or per request; do not share a single connection across concurrent operations or store it in a singleton.

---

---
title: "Keep Dapper queries in dedicated repository or query..."
impact: MEDIUM
impactDescription: "general best practice"
tags: dapper, dotnet, data, high-performance-sql-queries-mapped-to-pocos, read-heavy-and-latency-critical-data-access, stored-procedure-invocation
---

## Keep Dapper queries in dedicated repository or query...

Keep Dapper queries in dedicated repository or query classes with single-responsibility boundaries rather than scattering SQL throughout controllers or services.

---

---
title: "Specify `splitOn` explicitly in multi-mapping queries to..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: dapper, dotnet, data, high-performance-sql-queries-mapped-to-pocos, read-heavy-and-latency-critical-data-access, stored-procedure-invocation
---

## Specify `splitOn` explicitly in multi-mapping queries to...

Specify `splitOn` explicitly in multi-mapping queries to avoid ambiguity when join columns share the same name across tables.

---

---
title: "Use `buffered"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: dapper, dotnet, data, high-performance-sql-queries-mapped-to-pocos, read-heavy-and-latency-critical-data-access, stored-procedure-invocation
---

## Use `buffered

Use `buffered: false` in `QueryAsync` for very large result sets that should be streamed row-by-row to avoid loading the entire result into memory at once.

---

---
title: "Use `DynamicParameters` with `ParameterDirection"
impact: MEDIUM
impactDescription: "general best practice"
tags: dapper, dotnet, data, high-performance-sql-queries-mapped-to-pocos, read-heavy-and-latency-critical-data-access, stored-procedure-invocation
---

## Use `DynamicParameters` with `ParameterDirection

Use `DynamicParameters` with `ParameterDirection.Output` for stored procedures that return values through output parameters rather than result sets.

---

---
title: "Use `QueryMultipleAsync` to batch multiple SELECT..."
impact: MEDIUM
impactDescription: "general best practice"
tags: dapper, dotnet, data, high-performance-sql-queries-mapped-to-pocos, read-heavy-and-latency-critical-data-access, stored-procedure-invocation
---

## Use `QueryMultipleAsync` to batch multiple SELECT...

Use `QueryMultipleAsync` to batch multiple SELECT statements into a single round trip when a single method needs data from several tables.

---

---
title: "Use `QuerySingleOrDefaultAsync` when you expect zero or one..."
impact: MEDIUM
impactDescription: "general best practice"
tags: dapper, dotnet, data, high-performance-sql-queries-mapped-to-pocos, read-heavy-and-latency-critical-data-access, stored-procedure-invocation
---

## Use `QuerySingleOrDefaultAsync` when you expect zero or one...

Use `QuerySingleOrDefaultAsync` when you expect zero or one row and `QueryFirstOrDefaultAsync` when you want the first of potentially many rows, to clearly express intent.

---

---
title: "Wrap multiple related write operations in an explicit..."
impact: MEDIUM
impactDescription: "general best practice"
tags: dapper, dotnet, data, high-performance-sql-queries-mapped-to-pocos, read-heavy-and-latency-critical-data-access, stored-procedure-invocation
---

## Wrap multiple related write operations in an explicit...

Wrap multiple related write operations in an explicit `IDbTransaction` and call `Commit` only after all operations succeed to maintain data consistency.

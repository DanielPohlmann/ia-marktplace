<!-- Part of the specs-diagramming-erd skill. Loaded on demand from SKILL.md. -->

# Normalization

Normalization is the process of organizing data to reduce redundancy and improve integrity. Each normal form builds on the previous one.

## First Normal Form (1NF)
**Rule:** Every column contains only atomic (indivisible) values. No repeating groups or arrays.

**Violation:**
```
| OrderID | Products              |
|---------|----------------------|
| 1       | Widget, Gadget, Bolt |
```

**1NF Corrected:**
```
| OrderID | Product |
|---------|---------|
| 1       | Widget  |
| 1       | Gadget  |
| 1       | Bolt    |
```

## Second Normal Form (2NF)
**Rule:** Must be in 1NF, and every non-key attribute must depend on the entire primary key (no partial dependencies).

**Violation (composite key: OrderID + ProductID):**
```
| OrderID | ProductID | ProductName | Quantity |
|---------|-----------|-------------|----------|
| 1       | 101       | Widget      | 5        |
```
`ProductName` depends only on `ProductID`, not on the full key.

**2NF Corrected:**
```
ORDER_ITEM:  | OrderID | ProductID | Quantity |
PRODUCT:     | ProductID | ProductName |
```

## Third Normal Form (3NF)
**Rule:** Must be in 2NF, and no non-key attribute depends on another non-key attribute (no transitive dependencies).

**Violation:**
```
| EmployeeID | DepartmentID | DepartmentName |
|------------|-------------|----------------|
| 1          | 10          | Engineering    |
```
`DepartmentName` depends on `DepartmentID`, not on `EmployeeID`.

**3NF Corrected:**
```
EMPLOYEE:    | EmployeeID | DepartmentID |
DEPARTMENT:  | DepartmentID | DepartmentName |
```

## Summary of Normal Forms

| Normal Form | Eliminates | Rule |
|------------|------------|------|
| **1NF** | Repeating groups, multi-valued columns | All values are atomic |
| **2NF** | Partial dependencies | Non-key attributes depend on the whole key |
| **3NF** | Transitive dependencies | Non-key attributes depend only on the key |
| **BCNF** | Remaining anomalies from candidate keys | Every determinant is a candidate key |

## When to Denormalize

Denormalization intentionally reintroduces redundancy for performance or simplicity:

| Scenario | Justification |
|----------|--------------|
| **Read-heavy workloads** | Joins are expensive; pre-computed columns or materialized views reduce query time |
| **Reporting tables** | Star/snowflake schemas for data warehouses are intentionally denormalized |
| **Caching hot data** | Storing a copy of frequently accessed data in a denormalized form |
| **Reducing join complexity** | When a query always needs data from 5+ tables, strategic denormalization simplifies access |
| **Document databases** | NoSQL stores like MongoDB embed related data in a single document by design |

**Denormalization trade-offs:**
- Faster reads, slower writes
- Increased storage, reduced query complexity
- Risk of data inconsistency without proper update discipline

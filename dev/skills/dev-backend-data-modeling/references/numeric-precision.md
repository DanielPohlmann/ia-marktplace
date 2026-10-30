# Numeric Precision — Money, Counters and Exact Values

Choosing a numeric type is a data-modeling decision. The wrong choice does not fail loudly: it produces totals that are off by a cent, comparisons that are never equal, or a counter that silently becomes negative. This reference covers the type choice end to end — application, database, driver and wire format.

## 1. Why binary floating point is wrong for exact values

`float`/`double` (IEEE 754) store a number as a binary fraction times a power of two. Only fractions whose denominator is a power of two are exact. Most decimal fractions — 0.1, 0.2, 0.01 — have no finite binary representation, so the stored value is the nearest representable neighbor.

Consequences:
- `0.1 + 0.2 == 0.3` is false in most languages; the sum is `0.30000000000000004`.
- Errors **accumulate**: summing many small amounts drifts further from the true total, and the result depends on summation order.
- Equality comparisons become unreliable; code starts sprouting epsilon tolerances, which are wrong for money (an auditor does not accept "close enough").
- Converting back to text can show unexpected digits, or hide them, depending on formatting.

Binary floating point is the right tool for measurements and scientific computation, where inputs are already approximate and relative error matters more than exact digits.

## 2. What to use instead

| Need | Application type |
|---|---|
| Money, prices, tax, balances, anything summed, compared for equality or audited | C# `decimal`, Java `BigDecimal`, Python `decimal.Decimal`, JavaScript a decimal library or integer minor units |
| Simplest exact option, fixed currency precision | Integer **minor units** (cents) in a 64-bit integer |
| Measurements, sensor values, statistics, geometry | `double` is fine; document the expected precision |

Notes:
- **C# `decimal`** is a 128-bit scaled integer: a 96-bit integer plus a power-of-ten scale (0–28). It is not text and not a binary fraction, so 0.1 is exact. Range is about ±7.9 × 10^28 with 28–29 significant digits.
- **Java `BigDecimal`**: construct from a string or `BigDecimal.valueOf(double)`, never `new BigDecimal(0.1)` (that captures the binary error). `equals` compares scale too (`2.0` ≠ `2.00`); use `compareTo` for numeric equality.
- **Python `Decimal`**: construct from strings; set the context precision and rounding explicitly.
- **Minor units**: fast and exact, but every currency has its own number of decimals (0, 2 or 3 are common) — store the exponent per currency, not a hard-coded 100. Division and percentages still need an explicit rounding step.

## 3. Database side

- Use exact numeric types with **explicit precision and scale**: `NUMERIC(p,s)` / `DECIMAL(p,s)`, or the vendor equivalent (`NUMBER(p,s)`).
- Avoid binary floating column types (`FLOAT`, `REAL`, `DOUBLE PRECISION`, `BINARY_DOUBLE`) for money and other exact values. Some vendors' "money" types have fixed scale and odd rounding rules — prefer plain `DECIMAL`.
- Choose scale from the business rule, not from the display: unit prices may need more decimals (4–6) than invoice totals (currency precision).
- Choose precision with headroom for aggregates: a `SUM` over millions of rows needs more integer digits than a single row.
- Store the **currency code** (ISO 4217) in a column next to every amount. An amount without its currency is ambiguous once a second currency appears, and the second currency always appears.

## 4. Driver and mapping pitfalls

- A column declared without precision (for example an unbounded `NUMBER` or `NUMERIC`) can hold values with more digits than the client type supports. Reading such values into C# `decimal` can throw an overflow or cast exception at runtime, typically only for some rows. Fix it in SQL: `ROUND(col, s)` or `CAST(col AS DECIMAL(p,s))` in the query, or declare the column with explicit precision.
- Computed expressions (division, averages) can produce long fractional parts even from well-typed columns — round them in SQL before they reach the driver.
- Mappers may silently map a numeric column to `double` when the target property is untyped or `object`. Declare the property type explicitly.
- Check how the driver handles scale on write: some truncate, some round, some reject.

## 5. Rounding policy

Rounding is a business rule; write it down.

- **Mode:** half-even (banker's rounding, the default for C# `Math.Round` and `decimal`) reduces bias over many operations; half-away-from-zero is what most people expect from school and what many invoices and tax rules specify. Java `BigDecimal` requires you to choose; Python `Decimal` defaults to half-even.
- **Step:** decide *where* rounding happens — per line item, per tax line, or only on the total. Rounding per line and then summing gives a different total than summing then rounding. Pick one, apply it everywhere, and test it.
- **Allocation:** when splitting an amount (installments, cost sharing), the rounded parts must add back to the total. Assign the remainder explicitly (for example to the last or largest part).
- Never let the formatting layer be the only place rounding happens — what is displayed must equal what is stored.

## 6. Narrowing conversions and overflow

- Converting a wider type to a narrower one (64-bit → 32- or 16-bit integer, `double` → `int`, `decimal` → `int`) can lose the high bits or the fraction silently in many languages. Overflow from unchecked narrowing has caused real production failures, including in safety-critical software.
- Guard every narrowing: range-check before converting, or use checked conversions (C# `checked` blocks/`Convert.ToInt32`, Java `Math.toIntExact`, Rust `try_from`). Decide what happens on failure — reject, clamp, or escalate — instead of letting the runtime decide.
- Integer arithmetic can overflow too: multiplying quantities by minor-unit prices in 32-bit integers overflows sooner than expected. Use 64-bit for amounts.

## 7. Counters that can wrap

- Sequence numbers, packet counters, meter registers and hardware counters may roll over to zero (or to a negative value in signed types) after reaching their maximum.
- When computing a delta between two readings, detect the wrap (`current < previous`) and handle it according to the counter's width, rather than storing a negative or huge delta.
- Pick column and application types wide enough for the counter's real lifetime; 32-bit counters incremented frequently can exhaust within months or years.

## 8. Serialization

- Many JSON parsers (JavaScript `JSON.parse` and clients built on it) read every number as a `double`. A decimal amount or a 64-bit id beyond 2^53 loses precision in transit, without an error.
- Send exact decimals and large integer ids as **strings** in JSON (`"amount": "1234.50", "currency": "BRL"`), and document the format in the API contract. Parse them directly into the decimal type on the other side.
- Keep currency and amount together in the payload, the same as in storage.
- CSV/Excel exports: spreadsheet tools may reinterpret numbers (scientific notation, dropped leading zeros, locale decimal separators). Specify locale-independent formatting.

## Review checklist

- [ ] No `float`/`double` (or binary floating DB columns) for money or other values that are summed, compared for equality or audited.
- [ ] Decimal values are constructed from strings or integers, never from binary floating literals.
- [ ] Every DB numeric column for exact values declares precision and scale, with headroom for aggregates.
- [ ] Queries reading unbounded or computed numerics round or cast in SQL before mapping to the client decimal type.
- [ ] Rounding mode and rounding step are explicit, documented and consistent across services; allocations add back to the total.
- [ ] Every narrowing conversion is range-checked or uses checked arithmetic, with a defined failure behavior.
- [ ] Monetary amounts use 64-bit integers or decimals, never 32-bit integers.
- [ ] Wrapping counters are handled when computing deltas.
- [ ] Currency code is stored and transmitted alongside every amount.
- [ ] JSON contracts send decimals and large ids as strings.

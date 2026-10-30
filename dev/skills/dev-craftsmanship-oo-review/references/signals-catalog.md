# Signals Catalog — Before/After Sketches

Each entry: the signal, a minimal before/after, when to skip it, and a severity hint. Sketches are deliberately short; they show the shape of the correction, not production code. Examples alternate between TypeScript and C#.

## Contents
1. Type-code conditional → Strategy
2. Client type checks / refused overrides → LSP
3. Not-supported interface members → ISP
4. Infrastructure `new` in domain → DIP
5. Static mutable singleton → DI lifetime
6. Public status setter → encapsulated transitions
7. Anemic entity → tell, don't ask
8. Primitive obsession → value object
9. Train-wreck navigation → Law of Demeter
10. Else cascade → guard clauses
11. Duplicated creation logic → simple factory
12. Parallel step sequences → template method / composition
13. Flag-toggled behavior → decorator
14. Cross-cutting code in business methods → proxy/decorator
15. Long parameter list → parameter object

---

## 1. Type-code conditional → Strategy (OCP)

```ts
// before
function shippingCost(order: Order): number {
  switch (order.carrier) {
    case "ground": return order.weight * 1.2;
    case "air":    return order.weight * 4 + 10;
    case "pickup": return 0;
  }
}

// after
interface ShippingRate { cost(order: Order): number; }
const rates: Record<Carrier, ShippingRate> = {
  ground: { cost: o => o.weight * 1.2 },
  air:    { cost: o => o.weight * 4 + 10 },
  pickup: { cost: () => 0 },
};
const shippingCost = (o: Order) => rates[o.carrier].cost(o);
```

The selection still exists — in exactly one place (the map). **Skip** when branches are one-line mappings with no rules and the set is stable. **Severity:** suggestion; blocking only if the same switch is duplicated and already drifting.

## 2. Client type checks / refused overrides (LSP)

```csharp
// before
foreach (var account in accounts)
{
    if (account is FixedTermDeposit) continue;   // withdrawing throws there
    account.Withdraw(amount);
}

// after: withdrawal is a capability, not a promise of the base type
public interface IWithdrawable { void Withdraw(decimal amount); }

// the caller receives what it can actually use — no runtime filtering
public void WithdrawFromAll(IEnumerable<IWithdrawable> accounts, decimal amount)
{
    foreach (var account in accounts)
        account.Withdraw(amount);
}
```

**Skip** for type checks in serialization, mapping or pattern-matching over closed discriminated unions where that is the intended design. **Severity:** blocking when an existing caller can now fail.

## 3. Not-supported interface members (ISP)

```ts
// before
interface Printer { print(d: Doc): void; scan(): Image; fax(n: string): void; }
class BasicPrinter implements Printer {
  print(d: Doc) { /* ... */ }
  scan(): Image { throw new Error("not supported"); }
  fax(n: string) { throw new Error("not supported"); }
}

// after
interface Printer { print(d: Doc): void; }
interface Scanner { scan(): Image; }
class BasicPrinter implements Printer { print(d: Doc) { /* ... */ } }
```

**Skip** splitting into one-method interfaces when clients always use the methods together. **Severity:** suggestion; blocking if callers hit the throwing members.

## 4. Infrastructure `new` in domain (DIP)

```csharp
// before
public class InvoiceService
{
    public void Close(Invoice invoice)
    {
        invoice.ClosedAt = DateTime.Now;
        new SmtpClient("mail.internal").Send(/* ... */);
    }
}

// after — step 1: own and inject; step 2: interface only where tests need a fake
public class InvoiceService(TimeProvider clock, IInvoiceMailer mailer)
{
    public void Close(Invoice invoice)
    {
        invoice.Close(clock.GetUtcNow());
        mailer.SendClosed(invoice);
    }
}
```

**Skip** the interface for stable, pure dependencies (standard library utilities). **Severity:** blocking when it prevents required tests; otherwise suggestion.

## 5. Static mutable singleton → DI lifetime

```csharp
// before
public sealed class RateCache
{
    public static readonly RateCache Instance = new();
    public Dictionary<string, decimal> Rates = new();   // shared, unsynchronized
}

// after: one container-managed instance, state encapsulated and synchronized
public sealed class RateCache
{
    private readonly ConcurrentDictionary<string, decimal> _rates = new();
    public decimal? Get(string currency) => _rates.TryGetValue(currency, out var r) ? r : null;
    public void Set(string currency, decimal rate) => _rates[currency] = rate;
}

services.AddSingleton<RateCache>();   // injected where needed
```

`Lazy<T>` is fine for an expensive **immutable** value. **Skip** for static pure functions and constants. **Severity:** blocking if the state is mutated from concurrent requests.

## 6. Public status setter → encapsulated transitions

```ts
// before — rules live in every caller
if (order.status === "Paid") order.status = "Shipped";

// after
class Order {
  private _status: Status = "Draft";
  get status() { return this._status; }
  ship(): void {
    if (this._status !== "Paid") throw new InvalidTransition(this._status, "Shipped");
    this._status = "Shipped";
  }
}
```

Promote to a full State pattern only when each state carries distinct behavior, not just allowed transitions. **Severity:** suggestion; blocking if illegal transitions already reached production data.

## 7. Anemic entity → tell, don't ask

```csharp
// before (in a service)
if (cart.Items.Sum(i => i.Price * i.Qty) > customer.CreditLimit) throw ...;
cart.Items.Add(item);

// after
cart.Add(item, customer.CreditLimit);   // Cart owns the total and the rule
```

**Skip** for DTOs, view models, messages and query projections. **Severity:** suggestion.

## 8. Primitive obsession → value object

```csharp
// before: validated in three controllers and one importer
public void Register(string email) { if (!email.Contains('@')) throw ...; }

// after
public sealed record Email
{
    public string Value { get; }
    public Email(string value)
    {
        if (string.IsNullOrWhiteSpace(value) || !value.Contains('@'))
            throw new ArgumentException("Invalid email", nameof(value));
        Value = value.Trim().ToLowerInvariant();
    }
}
public void Register(Email email) { /* already valid */ }
```

Older C# without `record`: implement `Equals`, `GetHashCode` and `==` by hand. Typed ids (`CustomerId` vs `OrderId`) prevent swapped-argument bugs. **Skip** when the primitive is used in one place with no rules. **Severity:** suggestion.

## 9. Train-wreck navigation → Law of Demeter

```ts
// before: the caller digs out data and decides
if (order.getCustomer().getAddress().getCountry() === "BR") order.applyTax(BR_TAX);

// after: tell the owner what to do
order.applyTaxes(taxPolicy);

// not a fix: order.customerCountry() still hands data out for the caller to decide
```

**Not a violation:** fluent builders, LINQ/stream pipelines, navigating plain DTO trees in a mapping layer. **Severity:** suggestion.

## 10. Else cascade → guard clauses

```csharp
// before
if (user != null) { if (user.IsActive) { if (amount > 0) { Pay(user, amount); } else { throw ...; } } }

// after — same behavior: null or inactive users are still ignored
if (user is null || !user.IsActive) return;
if (amount <= 0) throw new ArgumentOutOfRangeException(nameof(amount));
Pay(user, amount);
```

**Severity:** suggestion.

## 11. Duplicated creation logic → simple factory

```ts
// before: copied in the API handler, the CLI and the import job
const parser = format === "csv" ? new CsvParser(sep) : format === "json" ? new JsonParser() : new XmlParser();

// after: one injectable factory (or registry) owns the choice
class ParserFactory {
    create(format: Format, options: ParserOptions): Parser { /* the single switch lives here */ }
}
const parser = this.parserFactory.create(format, options);   // injected, replaceable in tests
```

**Skip** when the creation appears once. **Severity:** suggestion; higher when copies already differ.

## 12. Parallel step sequences → template method or composition

```csharp
// before: MonthlyReport and AnnualReport each do Load → Filter → Format → Save, differing only in Filter

// after (composition, usually preferred)
public class ReportPipeline(IReportFilter filter, IReportStore store)
{
    public void Run(Period p) => store.Save(Format(filter.Apply(Load(p))));
}
```

Template method (abstract base with one overridable step) is acceptable when the hierarchy is shallow and stable. **Severity:** suggestion.

## 13. Flag-toggled behavior → decorator

```ts
// before
class Notifier { constructor(private retry: boolean, private audit: boolean) {} send(m: Msg) { /* ifs */ } }

// after
let notifier: Notifier = new EmailNotifier();
if (config.retry) notifier = new RetryingNotifier(notifier);
if (config.audit) notifier = new AuditedNotifier(notifier, auditLog);
```

**Skip** for a single flag that never grows. **Severity:** suggestion.

## 14. Cross-cutting code in business methods → proxy/decorator

```csharp
// before
public Quote Price(Request r)
{
    _log.Info("start"); var sw = Stopwatch.StartNew();
    if (_cache.TryGet(r.Key, out var q)) return q;
    q = Compute(r);                                  // the only business line
    _cache.Set(r.Key, q); _log.Info($"done {sw.ElapsedMilliseconds}");
    return q;
}

// after: PricingService.Price only computes; CachingPricing and a logging middleware wrap it
```

**Severity:** suggestion.

## 15. Long parameter list → parameter object

```ts
// before
search(from: Date, to: Date, region: string, minAmount: number, maxAmount: number, page: number)

// after
search(period: Period, filter: SearchFilter, page: number)
```

Group by what travels together; a group with invariants (from ≤ to) becomes a value object. Never report the count alone. **Severity:** suggestion.

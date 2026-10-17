<!-- Part of the dev-integration-patterns-transactional-outbox skill. Loaded on demand from SKILL.md. -->

# .NET examples (EF Core)

Use a framework outbox when you already have the framework: MassTransit
(`AddEntityFrameworkOutbox` + `UseBusOutbox`, see stack-masstransit), NServiceBus,
or Wolverine. Hand-roll only when you have no such bus or need a custom relay.

## Entity and mapping

```csharp
public sealed class OutboxMessage
{
    public Guid Id { get; init; } = Guid.NewGuid();
    public long Seq { get; init; }                     // identity column
    public required string AggregateType { get; init; }
    public required string AggregateId { get; init; }
    public required string Type { get; init; }
    public required string Payload { get; init; }      // JSON, serialized at write time
    public DateTimeOffset OccurredAt { get; init; } = DateTimeOffset.UtcNow;
    public DateTimeOffset? SentAt { get; set; }
    public int Attempts { get; set; }
    public string? LastError { get; set; }
}

// OnModelCreating
b.Entity<OutboxMessage>(e =>
{
    e.ToTable("outbox");
    e.HasKey(x => x.Id);
    e.Property(x => x.Seq).UseIdentityAlwaysColumn();
    e.Property(x => x.Payload).HasColumnType("jsonb");
    e.HasIndex(x => x.Seq).HasFilter("sent_at IS NULL");
});
```

## Turn domain events into outbox rows on SaveChanges

Aggregates collect integration events; an interceptor converts them inside the
same `SaveChanges` call, so they commit atomically with the state change.

```csharp
public sealed class OutboxInterceptor : SaveChangesInterceptor
{
    public override ValueTask<InterceptionResult<int>> SavingChangesAsync(
        DbContextEventData data, InterceptionResult<int> result, CancellationToken ct = default)
    {
        var db = data.Context!;
        var aggregates = db.ChangeTracker.Entries<IHasIntegrationEvents>()
            .Select(e => e.Entity)
            .Where(a => a.IntegrationEvents.Count > 0)
            .ToList();

        foreach (var aggregate in aggregates)
        {
            foreach (var evt in aggregate.IntegrationEvents)
            {
                db.Set<OutboxMessage>().Add(new OutboxMessage
                {
                    AggregateType = aggregate.GetType().Name,
                    AggregateId = aggregate.Id.ToString(),
                    Type = evt.GetType().Name,
                    Payload = JsonSerializer.Serialize(evt, evt.GetType()),
                });
            }
            aggregate.ClearIntegrationEvents();
        }
        return base.SavingChangesAsync(data, result, ct);
    }
}
```

The handler just calls `await db.SaveChangesAsync(ct)` — no broker call in the
request path.

## Relay as a BackgroundService

```csharp
public sealed class OutboxRelay(IServiceScopeFactory scopes, IMessagePublisher publisher,
    ILogger<OutboxRelay> log) : BackgroundService
{
    protected override async Task ExecuteAsync(CancellationToken ct)
    {
        var delay = TimeSpan.FromMilliseconds(100);
        while (!ct.IsCancellationRequested)
        {
            var published = await RelayBatchAsync(ct);
            delay = published > 0 ? TimeSpan.FromMilliseconds(100)
                                  : TimeSpan.FromMilliseconds(Math.Min(delay.TotalMilliseconds * 2, 5000));
            if (published == 0) await Task.Delay(delay, ct);
        }
    }

    private async Task<int> RelayBatchAsync(CancellationToken ct)
    {
        await using var scope = scopes.CreateAsyncScope();
        var db = scope.ServiceProvider.GetRequiredService<AppDbContext>();
        await using var tx = await db.Database.BeginTransactionAsync(ct);

        var batch = await db.Set<OutboxMessage>()
            .FromSqlRaw("""
                SELECT * FROM outbox
                WHERE sent_at IS NULL AND attempts < 10
                ORDER BY seq LIMIT 100
                FOR UPDATE SKIP LOCKED
                """)
            .ToListAsync(ct);

        foreach (var msg in batch)
        {
            try
            {
                // message id = outbox id, partition/routing key = aggregate id
                await publisher.PublishAsync(msg.Type, msg.Payload, msg.Id, msg.AggregateId, ct);
                msg.SentAt = DateTimeOffset.UtcNow;
            }
            catch (Exception ex)
            {
                msg.Attempts++;
                msg.LastError = ex.Message;
                log.LogWarning(ex, "Outbox publish failed for {MessageId}", msg.Id);
                break; // keep per-aggregate order: stop the batch on first failure
            }
        }

        await db.SaveChangesAsync(ct);
        await tx.CommitAsync(ct);
        return batch.Count(m => m.SentAt is not null);
    }
}
```

`IMessagePublisher` must wait for broker confirms before returning. Register the
relay with `services.AddHostedService<OutboxRelay>()` in the process that owns
the database (API or worker), and run **one** active instance or shard by key if
strict per-aggregate ordering is required.

## Switching to the MassTransit outbox

Move to the built-in outbox when MassTransit is already the bus: it covers the
outbox table, delivery service, inbox (consumer dedupe), and cleanup. Configure
it with stack-masstransit; keep the decision rules from SKILL.md (one transaction,
idempotent consumers, alert on outbox age).

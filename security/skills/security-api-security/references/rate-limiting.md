<!-- Part of the security-api-security skill. Loaded on demand from SKILL.md. -->

# Rate Limiting

Rate limiting protects APIs from abuse, brute-force attacks, and denial-of-service attempts by restricting the number of requests a client can make within a given time window.

**Algorithms**

| Algorithm | How It Works | Pros | Cons |
|---|---|---|---|
| Token Bucket | Tokens are added at a fixed rate; each request consumes a token; requests are rejected when the bucket is empty | Allows bursts up to bucket size; smooth average rate | Requires per-client state; bucket size tuning needed |
| Sliding Window | Counts requests in a rolling time window by combining current and previous window counts | More accurate than fixed window; smooth rate enforcement | Higher memory usage; slightly more complex |
| Fixed Window | Counts requests in discrete time intervals (e.g., per minute) | Simple to implement; low overhead | Vulnerable to burst at window boundaries (2x burst) |
| Leaky Bucket | Requests enter a queue (bucket) and are processed at a fixed rate; overflow is rejected | Very smooth output rate; prevents bursts entirely | Can add latency for queued requests; rigid |

**Response Headers**

Include rate limit information in every response so clients can self-regulate:

| Header | Purpose |
|---|---|
| `X-RateLimit-Limit` | Maximum number of requests allowed in the current window |
| `X-RateLimit-Remaining` | Number of requests remaining in the current window |
| `X-RateLimit-Reset` | Unix timestamp when the current window resets |
| `Retry-After` | Seconds to wait before retrying (sent with `429 Too Many Requests`) |

**Tiered Limits by Authentication Level**

| Tier | Authentication | Rate Limit | Use Case |
|---|---|---|---|
| Anonymous | None | 60 requests/hour | Public read-only endpoints |
| Authenticated | API key or Bearer token | 1,000 requests/hour | Standard application usage |
| Premium | API key with premium plan | 10,000 requests/hour | High-volume integrations |
| Internal | mTLS or service mesh identity | 100,000 requests/hour | Service-to-service communication |

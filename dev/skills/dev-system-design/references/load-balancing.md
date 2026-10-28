# Load Balancing

A load balancer spreads requests across interchangeable backends, removes unhealthy ones, and gives clients one stable address.

## L4 vs L7

| Aspect | Layer 4 (transport) | Layer 7 (application) |
|---|---|---|
| Sees | IP, port, TCP/UDP connection | HTTP method, path, headers, cookies, host |
| Routing | Per connection | Per request (path, header, host based) |
| TLS | Usually passed through | Usually terminated (can re-encrypt) |
| Overhead | Very low | Higher (parses requests) |
| Features | Simple, fast, protocol-agnostic | Path routing, header rewriting, retries, rate limits, auth offload, canary splits |
| Fits | Raw TCP/UDP protocols, databases, very high connection counts, non-HTTP traffic | Most web APIs and websites, microservice routing |

Default to **L7** for HTTP services. Choose **L4** when the protocol is not HTTP, when you need minimal overhead at extreme connection counts, or when TLS must pass through untouched.

WebSockets work through L7 balancers that support the HTTP Upgrade handshake (most modern ones do). After the upgrade, the connection stays pinned to one backend for its lifetime; tune idle timeouts so long-lived connections are not cut.

## Algorithms

| Algorithm | How it works | Use when | Watch out for |
|---|---|---|---|
| Round robin | Next backend in turn | Identical backends, uniform request cost | Uneven request durations pile up on some nodes |
| Weighted round robin | Turns proportional to weight | Mixed instance sizes, gradual canary | Weights need maintenance |
| Least connections | Backend with fewest active connections | Requests vary widely in duration; long-lived connections | Needs connection tracking; new nodes get flooded briefly |
| Least response time | Combines latency and active load | Latency-sensitive services | Can oscillate |
| IP / header hash | Hash of a client attribute picks the backend | Need affinity without cookies | Uneven if a few clients dominate |
| Consistent hashing | Keys mapped onto a ring; few keys move when nodes change | Routing to stateful backends (cache shards, partitioned services) | Use virtual nodes to even out distribution |

## Sticky sessions are a smell
Session affinity keeps a user on the same backend so in-memory session state works. It causes:
- Uneven load (a few heavy users pinned to one node).
- Lost sessions when that node restarts or scales in.
- Harder deploys and autoscaling.

Move session state to a shared store (key-value store, database) or into a signed token, and keep the app tier stateless. Use affinity only where it is intrinsic (an open WebSocket) or as a short-term mitigation.

## Health checks
- **Liveness**: is the process alive? Failing it means restart.
- **Readiness**: can it serve traffic now (dependencies reachable, warm-up done)? Failing it means take out of rotation.
- Keep checks cheap and avoid deep dependency checks that would remove every node when one shared dependency blips (cascading removal).
- Use connection draining on removal so in-flight requests finish.

## Other concerns
- The load balancer itself must be redundant (managed service, or active-passive pair with a floating IP).
- DNS-based balancing across regions is coarse because of client caching; combine with health-checked global load balancing.
- Put rate limiting and request-size limits at the edge to protect backends.

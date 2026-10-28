# Real-Time Updates

How to get new data to clients quickly: live scores, chat, notifications, dashboards, collaborative editing.

## Options

| Technique | How it works | Latency | Direction | Fits | Costs |
|---|---|---|---|---|---|
| Short polling | Client requests every N seconds | Up to N seconds | Client pulls | Infrequent changes, simple dashboards, small user counts | Many empty responses; load scales with clients ÷ interval |
| Long polling | Server holds the request until data arrives or a timeout, client re-requests | Low | Client pulls | Fallback when streaming is blocked; moderate update rates | Reconnect per message; held connections |
| Server-Sent Events (SSE) | One long-lived HTTP response streaming events | Low | Server → client | Feeds, notifications, live scores, progress updates | One open connection per client; text only; client-to-server goes over normal requests |
| WebSockets | Upgraded full-duplex TCP connection | Lowest | Both ways | Chat, multiplayer, collaborative editing, trading | Stateful connections, custom protocol, harder load balancing and scaling |

**Rule of thumb:** if the server only pushes, use SSE — it runs over plain HTTP, reconnects automatically, and supports resuming with `Last-Event-ID`. Use WebSockets when the client also sends frequent low-latency messages. Use polling when updates are rare or the scale is small and simplicity wins.

## Architecture for fan-out
```
clients ⇄ connection servers (SSE/WebSocket) ← pub/sub ← producers / domain services
```
- Connection servers hold client connections and nothing else of importance; they are horizontally scalable.
- Producers publish an event once to a pub/sub channel (per room, per topic, per user).
- Each connection server subscribes to the channels its connected clients need and forwards events locally.
- A registry (which user is on which server) is only needed for targeted delivery; topic subscription often removes the need.

## Pitfalls
- **Closing the stream after each event.** An SSE endpoint that sends one event and ends the response is just polling with extra steps. Keep the response open and flush events as they occur.
- **Ignoring client disconnects.** Detect closed connections (cancellation token, write errors, heartbeat timeouts) and release subscriptions, timers and memory; otherwise servers leak until they fall over.
- **One broker connection or subscription per client.** Opening a separate pub/sub connection for every browser multiplies broker load. Share one connection per server and multiplex subscriptions in-process.
- **Auth tokens in query strings.** Browsers cannot set headers on `EventSource` or the WebSocket constructor, so tokens end up in URLs — and URLs get written to access logs, proxies and browser history. Prefer cookies (with CSRF/origin checks), a short-lived single-use ticket exchanged just before connecting, or an auth message sent as the first frame.
- **No heartbeat.** Proxies and load balancers close idle connections. Send periodic comments/pings and tune idle timeouts.
- **No backpressure.** A slow client must not make the server buffer unboundedly; drop, coalesce or disconnect.
- **Thundering reconnect.** After a deploy, every client reconnects at once. Add jittered backoff on the client and drain servers gradually.
- **Assuming delivery.** Real-time channels are best-effort. Persist important events and let clients catch up from a cursor after reconnecting.

## Sizing notes
- Each open connection costs memory (buffers, TLS state). Estimate connections per server from measured memory per connection.
- Fan-out volume (events × subscribers) is usually the real bottleneck, not the number of producers.
- Coalesce rapid updates (e.g. send the latest score once per second) when clients only need the current state.

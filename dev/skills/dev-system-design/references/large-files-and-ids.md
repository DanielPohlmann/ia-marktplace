# Large Files and Unique IDs

## Large files

### Keep bytes off the application servers
Routing gigabytes through the API ties up threads, memory and bandwidth on the most expensive tier. Instead:
1. Client asks the API for permission to upload; the API checks auth, quota and file type, creates a metadata record (`status = pending`) and returns a **pre-signed URL** (time-limited, scoped to one object key and method).
2. Client uploads directly to object storage.
3. Storage emits an event (or the client calls "complete"); the API marks the record `uploaded` and triggers processing (virus scan, thumbnails, transcoding).
4. Downloads use a pre-signed GET URL or, for public/popular content, a **CDN** in front of the bucket.

### Multipart and resumable uploads
- Split large files into chunks (e.g. 5–100 MB), upload them in parallel, then commit the assembled object.
- On failure, retry only the failed chunks; persist the upload ID and completed parts so the client can resume after a crash or network change.
- Verify integrity with per-part checksums and a final checksum.
- Clean up abandoned multipart uploads with a lifecycle rule.

### Do not base64 files inside JSON
Base64 inflates size by about 33%, forces the whole payload into memory for parsing, and prevents streaming. Use binary bodies, multipart form uploads for small files, or pre-signed URLs for large ones.

### Delivery decisions

| Need | Approach |
|---|---|
| Private file, occasional access | Short-lived pre-signed GET |
| Public or widely shared content | CDN in front of object storage, long cache TTL with versioned keys |
| Video | Transcode to segments and stream adaptively via CDN |
| Access control on CDN content | Signed CDN URLs or cookies |

## Unique ID generation

| Strategy | Ordered? | Coordination | Pros | Cons |
|---|---|---|---|---|
| Database sequence / auto-increment | Yes | The database | Simple, compact | Single writer bottleneck; exposes volume; hard across shards |
| Centralised counter service, handing out ranges | Roughly | Counter service | Compact, scalable with batched ranges | Another critical service; gaps when nodes restart |
| Snowflake-style (timestamp + worker ID + sequence) | Time-ordered | Worker ID assignment only | 64-bit, sortable, no runtime coordination | Clock skew/backwards clocks must be handled; worker IDs must be unique |
| UUIDv4 (random) | No | None | Trivial, globally unique | 128-bit; random inserts fragment B-tree indexes |
| UUIDv7 (time-ordered) | Time-ordered | None | Standard, index-friendly, no coordination | 128-bit; reveals creation time |
| Random or hash-derived short code | No | Collision check | Short, unguessable | Collision risk grows with volume; needs check-and-retry |

### Collision math
For random codes from a space of size S, the probability of at least one collision becomes significant (around 50%) after roughly 1.18·√S codes (√(2·ln2·S)) — the birthday paradox. With 62^7 ≈ 3.5 × 10^12, that is about 2 million codes. Either:
- check uniqueness on insert (unique constraint) and regenerate on conflict,
- lengthen the code, or
- derive the code from a counter so collisions are impossible.

### Base62 encoding
Encoding a numeric ID in `[0-9a-zA-Z]` gives short, URL-safe strings: 62^6 ≈ 57 billion, 62^7 ≈ 3.5 trillion values. A 64-bit integer fits in at most 11 base62 characters.

### Enumeration and obfuscation
Sequential IDs in URLs let anyone guess the next record and estimate your volume. Options:
- Use random or UUID identifiers for public references.
- Apply a reversible permutation (e.g. a keyed bijective shuffle or block cipher over the integer) before base62 encoding, so counter-based codes look random but stay collision-free.
- Never rely on obscurity for authorization — always check access on the server.

## Short-link redirects: 301 vs 302

| | 301 Moved Permanently | 302 Found / 307 Temporary |
|---|---|---|
| Browser/CDN caching | Cached, often indefinitely | Not cached by default |
| Load on your service | Lower after first hit | Every click reaches you |
| Analytics per click | Lost after caching | Complete |
| Changing the target later | Unreliable (clients keep the old one) | Easy |

Choose 302 (or 307) when click analytics or editable targets matter; choose 301 when offloading traffic matters more than per-click visibility. A middle path is 302 with short `Cache-Control` max-age.

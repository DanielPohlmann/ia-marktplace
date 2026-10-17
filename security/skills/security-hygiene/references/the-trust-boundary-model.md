<!-- Part of the security-hygiene skill. Loaded on demand from SKILL.md. -->

# The Trust Boundary Model

Every component has boundaries where data enters and exits. Each boundary is a point where hygiene must be enforced.

```
                    ┌─────────────────────┐
  User Input ──────►│                     │──────► Database
                    │    Your Component   │
  Database ────────►│                     │──────► API Response
                    │   SANITIZE HERE     │
  Message Queue ───►│   ON EVERY EDGE     │──────► Message Queue
                    │                     │
  Cache ───────────►│                     │──────► Logs
                    │                     │
  Partner API ─────►│                     │──────► Downstream Service
                    └─────────────────────┘
```

## Why Internal Sources Are Untrusted

| Source | Why It Can't Be Trusted | Example Threat |
|--------|------------------------|----------------|
| **Database** | Rows may have been inserted by a compromised service, SQL injection, or legacy code without validation | Stored XSS: HTML in a database field rendered without encoding |
| **Cache (Redis, Memcached)** | Cache poisoning, stale data, no authentication by default | Attacker writes malicious payload to shared cache key |
| **Message Queue** | Any producer can publish; messages may be replayed or tampered | Deserialization attack via crafted message payload |
| **Internal API / Microservice** | Service may be compromised, misconfigured, or returning unexpected data | Downstream service returns user-controlled data without sanitization |
| **Configuration Store** | Config values may be modified by operators or injected via environment | Command injection through a config value used in a shell call |
| **File System** | Files may be written by other processes, users, or symlink attacks | Path traversal via a filename read from a temp directory |
| **Logs (when read back)** | Log entries may contain injected content | Log injection leading to SIEM manipulation or log4shell-style attacks |

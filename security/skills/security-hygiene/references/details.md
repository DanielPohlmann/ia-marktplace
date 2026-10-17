<!-- Part of the security-hygiene skill. Loaded on demand from SKILL.md. -->

# Hygiene — Trust No Data — details

## Sanitization

Sanitization removes or neutralizes dangerous content from data. It should happen **on input to your component**, before the data is processed or stored.

### Strategies

| Strategy | What It Does | When to Use |
|----------|-------------|-------------|
| **Stripping** | Removes disallowed characters or tags entirely | HTML tags from plain-text fields, control characters from strings |
| **Escaping** | Replaces special characters with safe equivalents | HTML entities, SQL parameterization, shell escaping |
| **Allowlisting** | Accepts only values matching a known-good pattern | Enum fields, expected formats (UUID, ISO date, email) |
| **Type coercion** | Converts data to the expected type | Parse string to integer, parse to date object |

### Sanitize Both Directions

- **Inbound**: Validate and sanitize data entering your component from any source.
- **Outbound**: Encode data leaving your component for the target context (HTML, SQL, shell, URL, JSON, XML).

```
  Inbound                           Outbound
  ────────                          ────────
  Validate type/format              Encode for HTML context
  Enforce allowlist                 Encode for SQL (parameterize)
  Strip/escape dangerous chars      Encode for shell (avoid shell if possible)
  Normalize/canonicalize            Encode for URL
  Reject if invalid                 Encode for JSON/XML
```

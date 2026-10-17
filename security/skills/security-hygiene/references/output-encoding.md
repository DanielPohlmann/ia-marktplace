<!-- Part of the security-hygiene skill. Loaded on demand from SKILL.md. -->

# Output Encoding

Output encoding ensures data is safe for the **specific context** it is being rendered or transmitted into. This applies to ALL outputs, not just HTTP responses.

## Context-Specific Encoding

| Output Context | Encoding Required | Why |
|---------------|-------------------|-----|
| **HTML body** | HTML entity encoding (`<` → `&lt;`) | Prevents XSS |
| **HTML attributes** | Attribute encoding (quote special chars) | Prevents attribute injection |
| **JavaScript** | JS string encoding or `JSON.stringify()` | Prevents script injection |
| **SQL** | Parameterized queries (never string concat) | Prevents SQL injection |
| **Shell commands** | Avoid shell entirely; if unavoidable, use library escaping | Prevents command injection |
| **URLs** | URL-encode query parameters and path segments | Prevents parameter injection |
| **XML** | XML entity encoding | Prevents XXE and injection |
| **JSON** | Proper serialization (not string concatenation) | Prevents JSON injection |
| **Log entries** | Strip newlines and control characters | Prevents log injection |
| **Email headers** | Strip newlines from header values | Prevents header injection |

## Encoding Data From Internal Sources

```
Database row → render in HTML?    → HTML-encode the value
Cache value  → insert into SQL?   → use parameterized query
Queue msg    → pass to shell?     → use subprocess array (no shell)
Config value → embed in template? → encode for template context
API response → return to client?  → serialize properly, set Content-Type
```

The encoding must match the **destination context**, regardless of where the data came from.

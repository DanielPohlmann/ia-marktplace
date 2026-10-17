<!-- Part of the security-hygiene skill. Loaded on demand from SKILL.md. -->

# Canonicalization

Canonicalization (C14N) converts data to its simplest, standard form **before** validation. Without canonicalization, attackers bypass validation by using alternate representations of the same value.

## Common Bypass Techniques Prevented by Canonicalization

| Technique | Example | What Canonicalization Does |
|-----------|---------|--------------------------|
| **Unicode normalization** | `\uFF41` (fullwidth 'a') vs `a` | Normalize to NFC/NFD before comparing |
| **URL encoding** | `%2e%2e%2f` = `../` | Decode URL encoding before path validation |
| **Double encoding** | `%252e` → `%2e` → `.` | Decode iteratively until stable |
| **Case variation** | `SELECT` vs `SeLeCt` | Lowercase before matching keywords |
| **Path normalization** | `/app/../etc/passwd` | Resolve to canonical absolute path (`/etc/passwd`) |
| **Null bytes** | `file.php%00.jpg` | Strip null bytes before extension check |
| **Homoglyph substitution** | `pаypal.com` (Cyrillic 'а') | Normalize to ASCII or punycode |
| **Whitespace injection** | `admin\t` vs `admin` | Trim and normalize whitespace |

## Canonicalization Order

Always canonicalize **before** validation:

```
Raw Input → Decode → Normalize → Canonicalize → Validate → Process
```

If you validate before canonicalizing, an attacker can encode their payload to pass validation and then have it decoded into a malicious form later.

## Language Examples

**Path Canonicalization**
```csharp
// C# — Resolve to absolute path and verify it's within the allowed directory
string basePath = Path.GetFullPath("/app/uploads");
string requested = Path.GetFullPath(Path.Combine(basePath, userInput));
if (!requested.StartsWith(basePath + Path.DirectorySeparatorChar))
    throw new SecurityException("Path traversal detected");
```

```python
# Python — Resolve symlinks and relative segments
import os
base = os.path.realpath("/app/uploads")
requested = os.path.realpath(os.path.join(base, user_input))
if not requested.startswith(base + os.sep):
    raise ValueError("Path traversal detected")
```

**Unicode Normalization**
```python
import unicodedata

# Normalize to NFC before comparing or validating
clean = unicodedata.normalize("NFC", user_input)
```

```csharp
// C# — Normalize to FormC (NFC)
string clean = userInput.Normalize(NormalizationForm.FormC);
```

**URL Canonicalization**
```python
from urllib.parse import unquote

def canonicalize_url(url: str) -> str:
    prev = None
    while prev != url:
        prev = url
        url = unquote(url)
    return url
```

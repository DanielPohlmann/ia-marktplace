<!-- Part of the security-owasp skill. Loaded on demand from SKILL.md. -->

# CWE/SANS Top 25 (Selected Critical Entries)

| CWE ID | Name | Description | Key Mitigations |
|--------|------|-------------|-----------------|
| CWE-79 | Cross-Site Scripting (XSS) | Improper neutralization of input during web page generation allows attackers to inject malicious scripts. | Context-aware output encoding; Content Security Policy (CSP); use frameworks that auto-escape by default; validate and sanitize all user input. |
| CWE-89 | SQL Injection | Improper neutralization of special elements in SQL commands allows attackers to execute arbitrary queries. | Parameterized queries (prepared statements); stored procedures; input validation; least-privilege database accounts. |
| CWE-22 | Path Traversal | Improper limitation of a pathname allows attackers to access files outside the intended directory. | Validate and canonicalize file paths; use chroot jails or sandboxes; deny-list `../` sequences; restrict file system permissions. |
| CWE-78 | OS Command Injection | Improper neutralization of special elements in OS commands allows attackers to execute arbitrary system commands. | Avoid OS commands from user input; use language APIs instead of shell commands; input validation with strict allow-lists; least-privilege execution. |
| CWE-352 | Cross-Site Request Forgery (CSRF) | Attacker tricks an authenticated user's browser into sending a forged request to a vulnerable application. | Anti-CSRF tokens (synchronizer pattern); SameSite cookie attribute; verify Origin/Referer headers; require re-authentication for sensitive operations. |
| CWE-434 | Unrestricted Upload of File with Dangerous Type | Application allows uploading of files without validating type, size, or content, enabling code execution. | Validate file type by content (magic bytes), not extension alone; store uploads outside webroot; rename files; enforce size limits; scan for malware. |
| CWE-416 | Use After Free | Referencing memory after it has been freed can lead to program crashes, arbitrary code execution, or data corruption. | Use memory-safe languages (Rust, Go, C#); enable compiler protections (ASLR, stack canaries); use smart pointers; static analysis tools. |
| CWE-400 | Uncontrolled Resource Consumption | Application does not properly restrict resource usage, enabling denial of service. | Implement rate limiting; set timeouts and resource quotas; validate input sizes; use circuit breakers; monitor resource consumption. |
| CWE-200 | Exposure of Sensitive Information to an Unauthorized Actor | Application unintentionally reveals sensitive data through error messages, logs, or API responses. | Suppress detailed error messages in production; filter sensitive data from logs; use generic error pages; review API responses for data leakage. |
| CWE-269 | Improper Privilege Management | Application does not properly manage privileges, allowing users to gain elevated access. | Enforce least privilege; validate authorization on every request; use role-based or attribute-based access control; audit privilege escalation paths. |

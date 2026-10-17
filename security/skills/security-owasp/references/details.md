<!-- Part of the security-owasp skill. Loaded on demand from SKILL.md. -->

# OWASP Standards — details

## Mapping Between Lists

The OWASP Top 10 categories map to specific CWE entries, creating a bridge between the high-level risk taxonomy and granular vulnerability types:

- **A01 Broken Access Control** maps to CWE-200 (Information Disclosure), CWE-269 (Improper Privilege Management), CWE-352 (CSRF), and CWE-22 (Path Traversal).
- **A02 Cryptographic Failures** maps to CWE-259 (Hard-coded Password), CWE-327 (Broken Crypto Algorithm), and CWE-331 (Insufficient Entropy).
- **A03 Injection** maps to CWE-79 (XSS), CWE-89 (SQL Injection), and CWE-78 (OS Command Injection).
- **A04 Insecure Design** maps to CWE-209 (Error Information Leak), CWE-256 (Plaintext Storage of Password), and CWE-501 (Trust Boundary Violation).
- **A05 Security Misconfiguration** maps to CWE-16 (Configuration), CWE-611 (XXE), and CWE-1004 (Sensitive Cookie Without HttpOnly).
- **A06 Vulnerable and Outdated Components** maps to CWE-1104 (Use of Unmaintained Third-Party Components).
- **A07 Identification and Authentication Failures** maps to CWE-287 (Improper Authentication), CWE-384 (Session Fixation), and CWE-798 (Hard-coded Credentials).
- **A08 Software and Data Integrity Failures** maps to CWE-502 (Deserialization of Untrusted Data) and CWE-829 (Inclusion of Untrusted Functionality).
- **A09 Security Logging and Monitoring Failures** maps to CWE-778 (Insufficient Logging) and CWE-223 (Omission of Security-Relevant Information).
- **A10 Server-Side Request Forgery** maps to CWE-918 (SSRF).

This mapping helps teams trace a high-level OWASP finding down to specific CWE entries for detailed remediation guidance, and vice versa.

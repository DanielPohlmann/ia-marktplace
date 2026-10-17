---
name: security-cryptography
description: Use when selecting or implementing cryptographic controls. USE FOR: TLS versions and ciphers, Argon2/bcrypt/scrypt, AES/RSA/ECDSA, key and secrets management (Vault, KMS), certificates, homomorphic encryption. DO NOT USE FOR: auth protocols (use security-authentication), masking and anonymization (use security-data-protection), headers and CORS (use security-api-security). Never roll your own crypto.
---

# Cryptography

## Overview

Cryptography is the foundation of trust in modern software systems. It underpins confidentiality, integrity, authentication, and non-repudiation for data in transit and at rest. Every secure communication channel, every stored password, and every signed artifact relies on well-implemented cryptographic primitives.

The cardinal rule of applied cryptography is **never roll your own crypto**. Use established, peer-reviewed libraries and standards. Custom cryptographic algorithms or ad-hoc constructions are almost guaranteed to contain exploitable weaknesses. Rely on proven implementations such as OpenSSL, libsodium, Bouncy Castle, or the native cryptography modules provided by your platform.

## Best Practices

- **Use established cryptographic libraries** (libsodium, OpenSSL, Bouncy Castle, platform-native crypto APIs) rather than implementing primitives yourself.
- **Enforce TLS 1.2 as the minimum** for all communications, and prefer TLS 1.3 where supported.
- **Hash passwords with Argon2id** as the default; fall back to bcrypt (cost 12+) if Argon2 is unavailable.
- **Use authenticated encryption** (AES-GCM or ChaCha20-Poly1305) for all symmetric encryption; never use unauthenticated modes like ECB or plain CBC.
- **Rotate cryptographic keys on a defined schedule** and immediately upon suspected compromise.
- **Store all secrets in a dedicated secrets management tool** with audit logging and access controls — never in code, configuration files, or version control.
- **Use Hardware Security Modules (HSMs)** or cloud KMS for high-value key storage and cryptographic operations.
- **Keep cryptographic dependencies up to date** and monitor for vulnerability disclosures affecting the algorithms and libraries you use.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/homomorphic-encryption.md](references/homomorphic-encryption.md) | Homomorphic Encryption — Schemes, Libraries and Frameworks, Practical Considerations |
| [references/details.md](references/details.md) | TLS Configuration; Password Hashing; Symmetric Encryption; Asymmetric Encryption; Key Management; Secrets Management |

## References

- [NIST SP 800-57 Recommendation for Key Management](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
- [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
- [NIST SP 800-175B Guide to Secure Web Services](https://csrc.nist.gov/publications/detail/sp/800-175b/rev-1/final)

See references/rules.md for the full rule catalog.

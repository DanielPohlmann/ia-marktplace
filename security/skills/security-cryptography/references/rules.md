# Cryptography Rules

Best practices and rules for Cryptography.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Use established cryptographic libraries | MEDIUM | [`cryptography-use-established-cryptographic-libraries.md`](cryptography-use-established-cryptographic-libraries.md) |
| 2 | Enforce TLS 1.2 as the minimum | HIGH | [`cryptography-enforce-tls-1-2-as-the-minimum.md`](cryptography-enforce-tls-1-2-as-the-minimum.md) |
| 3 | Hash passwords with Argon2id | MEDIUM | [`cryptography-hash-passwords-with-argon2id.md`](cryptography-hash-passwords-with-argon2id.md) |
| 4 | Use authenticated encryption | CRITICAL | [`cryptography-use-authenticated-encryption.md`](cryptography-use-authenticated-encryption.md) |
| 5 | Rotate cryptographic keys on a defined schedule | MEDIUM | [`cryptography-rotate-cryptographic-keys-on-a-defined-schedule.md`](cryptography-rotate-cryptographic-keys-on-a-defined-schedule.md) |
| 6 | Store all secrets in a dedicated secrets management tool | CRITICAL | [`cryptography-store-all-secrets-in-a-dedicated-secrets-management-tool.md`](cryptography-store-all-secrets-in-a-dedicated-secrets-management-tool.md) |
| 7 | Use Hardware Security Modules (HSMs) | CRITICAL | [`cryptography-use-hardware-security-modules-hsms.md`](cryptography-use-hardware-security-modules-hsms.md) |
| 8 | Keep cryptographic dependencies up to date | CRITICAL | [`cryptography-keep-cryptographic-dependencies-up-to-date.md`](cryptography-keep-cryptographic-dependencies-up-to-date.md) |

---

---
title: "Enforce TLS 1.2 as the minimum"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: cryptography, security, tls, encryption, hashing
---

## Enforce TLS 1.2 as the minimum

Enforce TLS 1.2 as the minimum: for all communications, and prefer TLS 1.3 where supported.

---

---
title: "Hash passwords with Argon2id"
impact: MEDIUM
impactDescription: "general best practice"
tags: cryptography, security, tls, encryption, hashing
---

## Hash passwords with Argon2id

Hash passwords with Argon2id: as the default; fall back to bcrypt (cost 12+) if Argon2 is unavailable.

---

---
title: "Keep cryptographic dependencies up to date"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: cryptography, security, tls, encryption, hashing
---

## Keep cryptographic dependencies up to date

Keep cryptographic dependencies up to date: and monitor for vulnerability disclosures affecting the algorithms and libraries you use.

---

---
title: "Rotate cryptographic keys on a defined schedule"
impact: MEDIUM
impactDescription: "general best practice"
tags: cryptography, security, tls, encryption, hashing
---

## Rotate cryptographic keys on a defined schedule

Rotate cryptographic keys on a defined schedule: and immediately upon suspected compromise.

---

---
title: "Store all secrets in a dedicated secrets management tool"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: cryptography, security, tls, encryption, hashing
---

## Store all secrets in a dedicated secrets management tool

Store all secrets in a dedicated secrets management tool: with audit logging and access controls — never in code, configuration files, or version control.

---

---
title: "Use authenticated encryption"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: cryptography, security, tls, encryption, hashing
---

## Use authenticated encryption

(AES-GCM or ChaCha20-Poly1305) for all symmetric encryption; never use unauthenticated modes like ECB or plain CBC.

---

---
title: "Use established cryptographic libraries"
impact: MEDIUM
impactDescription: "general best practice"
tags: cryptography, security, tls, encryption, hashing
---

## Use established cryptographic libraries

(libsodium, OpenSSL, Bouncy Castle, platform-native crypto APIs) rather than implementing primitives yourself.

---

---
title: "Use Hardware Security Modules (HSMs)"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: cryptography, security, tls, encryption, hashing
---

## Use Hardware Security Modules (HSMs)

Use Hardware Security Modules (HSMs): or cloud KMS for high-value key storage and cryptographic operations.

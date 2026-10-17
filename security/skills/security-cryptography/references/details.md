<!-- Part of the security-cryptography skill. Loaded on demand from SKILL.md. -->

# Cryptography — details

## TLS Configuration

Transport Layer Security protects data in transit. All services must enforce a minimum of **TLS 1.2**, and should prefer **TLS 1.3** wherever supported.

### Disabled Protocols

| Protocol  | Status     | Reason                                      |
|-----------|------------|---------------------------------------------|
| SSL 3.0   | **Disabled** | Vulnerable to POODLE attack                |
| TLS 1.0   | **Disabled** | Deprecated by RFC 8996; known weaknesses   |
| TLS 1.1   | **Disabled** | Deprecated by RFC 8996; no modern benefits |

### Recommended Cipher Suites

| Cipher Suite              | Protocol | Notes                              |
|---------------------------|----------|------------------------------------|
| AES-128-GCM / AES-256-GCM | TLS 1.2+ | Authenticated encryption, hardware-accelerated on modern CPUs |
| ChaCha20-Poly1305         | TLS 1.2+ | Excellent performance on devices without AES-NI |

- In TLS 1.3, cipher suite negotiation is simplified and only secure options are available by default.
- Disable CBC-mode ciphers when possible to avoid padding oracle attacks.
- Always enable **HSTS** (HTTP Strict Transport Security) to prevent protocol downgrade attacks:

```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

## Password Hashing

Passwords must be hashed with a slow, memory-hard function designed specifically for password storage. General-purpose hash functions are not suitable.

### Algorithm Comparison

| Algorithm | Status         | Memory-Hard | GPU Resistant | Recommended Parameters          |
|-----------|----------------|-------------|---------------|---------------------------------|
| Argon2id  | Gold standard  | Yes         | Yes           | m=64MB, t=3, p=4               |
| bcrypt    | Secure         | 4KB fixed   | Partial       | cost=12+                        |
| scrypt    | Secure         | Yes         | Yes           | N=16384, r=8, p=1              |
| PBKDF2    | Legacy         | No          | No            | 600,000+ iterations (SHA-256)  |

**Argon2id** is the recommended default. It won the Password Hashing Competition and combines resistance to both side-channel and GPU-based attacks.

> **Never use MD5 or SHA-family functions (SHA-1, SHA-256, SHA-512) for password hashing.** These are general-purpose hash functions optimized for speed, which makes them trivially brute-forceable for password cracking. They lack salting by design and have no work-factor parameter.

## Symmetric Encryption

Symmetric encryption uses a single shared key for both encryption and decryption.

- **AES-256-GCM** is the standard for data at rest. GCM mode provides both confidentiality and integrity (authenticated encryption with associated data, or AEAD).
- **ChaCha20-Poly1305** is an excellent alternative, especially on platforms without hardware AES acceleration. It is the default in TLS 1.3 for non-AES-NI environments.
- **Never use ECB mode.** ECB encrypts identical plaintext blocks to identical ciphertext blocks, leaking patterns in the data. Always use an authenticated mode such as GCM or an encrypt-then-MAC construction.

When using AES-GCM:
- Use a unique nonce (IV) for every encryption operation under the same key.
- Limit the amount of data encrypted under a single key to avoid nonce reuse (approximately 2^32 encryptions with random 96-bit nonces).
- Rotate keys before reaching these limits.

## Asymmetric Encryption

Asymmetric (public-key) cryptography uses a key pair: a public key for encryption or verification and a private key for decryption or signing.

### Key Sizes and Algorithms

| Algorithm | Use Case             | Minimum Key Size | Recommended           | Notes                                  |
|-----------|----------------------|------------------|-----------------------|----------------------------------------|
| RSA       | Encryption, signing  | 2048 bits        | 3072+ bits            | Widely supported; use OAEP for encryption, PSS for signing |
| ECDSA     | Signing              | P-256 (256 bits) | P-256 or P-384        | Smaller keys, faster operations than RSA |
| Ed25519   | Signing              | 256 bits (fixed) | 256 bits (fixed)      | Modern, fast, resistant to side-channel attacks; preferred for new systems |
| X25519    | Key exchange         | 256 bits (fixed) | 256 bits (fixed)      | Used in TLS 1.3 and modern protocols  |

- **Ed25519** is the recommended choice for digital signatures in new systems due to its simplicity, performance, and security properties.
- RSA keys below 2048 bits are considered insecure and must not be used.
- For encryption use cases, prefer hybrid encryption: use asymmetric crypto to exchange a symmetric key, then encrypt the payload with AES-GCM.

## Key Management

Cryptographic keys have a defined lifecycle that must be managed rigorously:

```
Generation --> Storage --> Distribution --> Usage --> Rotation --> Revocation --> Destruction
```

### Lifecycle Principles

1. **Generation** — Use cryptographically secure random number generators (CSPRNG). Never use `Math.random()` or similar non-cryptographic sources.
2. **Storage** — Keys must never be stored in plaintext. Use Hardware Security Modules (HSMs) for high-value keys. HSMs provide tamper-resistant storage and perform cryptographic operations without exposing key material.
3. **Distribution** — Use secure channels (TLS, out-of-band exchange). Never transmit keys alongside the data they protect.
4. **Usage** — Limit key usage to a single purpose (encryption OR signing, not both). Enforce access controls.
5. **Rotation** — Rotate keys on a regular schedule and immediately after any suspected compromise.
6. **Revocation** — Maintain revocation lists (CRL) or use OCSP for certificates. Ensure revoked keys are no longer accepted.
7. **Destruction** — Securely erase keys when they are no longer needed. Overwrite key material in memory.

### Cloud KMS Services

| Service             | Provider   | HSM-Backed | Auto-Rotation | Key Types                     |
|---------------------|------------|------------|---------------|-------------------------------|
| AWS KMS             | AWS        | Yes        | Yes (annual)  | Symmetric, RSA, ECC          |
| Azure Key Vault     | Microsoft  | Yes        | Yes           | Symmetric, RSA, EC           |
| GCP Cloud KMS       | Google     | Yes        | Yes           | Symmetric, RSA, EC, Ed25519  |
| HashiCorp Vault     | HashiCorp  | Optional   | Yes           | All types; transit secrets engine |

## Secrets Management

Secrets include API keys, database credentials, tokens, certificates, and encryption keys. Mismanaged secrets are one of the most common causes of security breaches.

### Rules

- **Never store secrets in source code or version control.** Even if a repository is private, secrets in VCS persist in history and are easily leaked.
- **Use dedicated secrets management tools.** These provide encryption, access control, audit logging, and automatic rotation.
- **Inject secrets at runtime** via environment variables, mounted files, or API calls — never bake them into container images or build artifacts.

### Secrets Management Tools

| Tool                          | Provider   | Dynamic Secrets | Auto-Rotation | Audit Log | Notes                            |
|-------------------------------|------------|-----------------|---------------|-----------|----------------------------------|
| HashiCorp Vault               | HashiCorp  | Yes             | Yes           | Yes       | Industry standard; self-hosted or cloud |
| AWS Secrets Manager           | AWS        | Yes             | Yes           | Yes       | Native AWS integration           |
| Azure Key Vault               | Microsoft  | No              | Yes           | Yes       | Integrated with Azure AD         |
| GCP Secret Manager            | Google     | No              | Yes           | Yes       | IAM-based access control         |
| Doppler                       | Doppler    | No              | Yes           | Yes       | Developer-friendly; multi-cloud  |
| 1Password Secrets Automation  | 1Password  | No              | No            | Yes       | Good for smaller teams; CLI and SDK support |

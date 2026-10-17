<!-- Part of the security-cryptography skill. Loaded on demand from SKILL.md. -->

# Homomorphic Encryption

Homomorphic encryption (HE) allows computation on encrypted data without decrypting it first. The result, when decrypted, matches the result of performing the same operations on the plaintext. This enables data processing by untrusted parties (cloud providers, third-party analytics) while preserving confidentiality.

## Schemes

| Scheme | Operations Supported | Performance | Use Case |
|--------|---------------------|-------------|----------|
| **Partially Homomorphic (PHE)** | Addition OR multiplication (not both) | Fast | Simple aggregations, voting |
| **Somewhat Homomorphic (SHE)** | Limited additions and multiplications | Moderate | Bounded computations |
| **Fully Homomorphic (FHE)** | Arbitrary additions and multiplications | Slow (improving) | General-purpose encrypted computation |

## Libraries and Frameworks

| Library | Language | Scheme | Maintainer |
|---------|----------|--------|------------|
| **Microsoft SEAL** | C++ (with .NET, Python wrappers) | BFV, CKKS | Microsoft Research |
| **OpenFHE** | C++ (with Python bindings) | BGV, BFV, CKKS, TFHE, FHEW | DARPA-funded consortium |
| **TFHE-rs** | Rust | TFHE | Zama |
| **Concrete** | Python / Rust | TFHE | Zama |
| **HElib** | C++ | BGV, CKKS | IBM |

## Practical Considerations

- **Performance**: FHE is orders of magnitude slower than plaintext computation. Use it only when the confidentiality requirement justifies the overhead.
- **CKKS vs BFV/BGV**: CKKS supports approximate arithmetic on real numbers (good for ML inference). BFV/BGV support exact integer arithmetic (good for counting, voting, database queries).
- **Bootstrapping**: FHE schemes accumulate noise with each operation. Bootstrapping refreshes ciphertexts but is expensive. Leveled HE avoids bootstrapping by pre-setting the maximum circuit depth.
- **Key sizes**: HE keys and ciphertexts are much larger than traditional encryption (megabytes vs bytes). Plan for storage and bandwidth overhead.
- **Use cases**: Privacy-preserving ML inference, encrypted database queries, secure multi-party computation, confidential cloud analytics, healthcare data analysis without exposure.

> **When to use HE**: When you need a third party to compute on your data but cannot afford to reveal the plaintext — and you can tolerate the performance overhead. For most applications, traditional encryption with access controls is simpler and sufficient.

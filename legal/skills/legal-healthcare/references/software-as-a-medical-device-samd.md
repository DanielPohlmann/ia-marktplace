<!-- Part of the legal-healthcare skill. Loaded on demand from SKILL.md. -->

# Software as a Medical Device (SaMD)

The FDA regulates software that meets the definition of a **medical device** — specifically, software intended for one or more medical purposes that performs these purposes without being part of a hardware medical device. This is known as **Software as a Medical Device (SaMD)**.

## FDA Classification

| Classification | Risk Level | FDA Pathway | Examples |
|---|---|---|---|
| **Class I** | Low risk | Exempt or 510(k) | General wellness apps that do not diagnose or treat, simple data display |
| **Class II** | Moderate risk | 510(k) + Special Controls | Clinical decision support with review by clinician, remote patient monitoring |
| **Class III** | High risk | Premarket Approval (PMA) | AI-driven diagnosis without human review, life-critical treatment decisions |

## Clinical Decision Support (CDS) Exclusion

The **21st Century Cures Act** exempts certain clinical decision support software from FDA regulation if it meets **all five criteria**:

1. Not intended to acquire, process, or analyze a medical image or signal from an in vitro diagnostic device or a pattern or signal from a signal acquisition system
2. Intended for the purpose of displaying, analyzing, or printing medical information
3. Intended for the purpose of supporting or providing recommendations to a healthcare professional
4. Intended for the purpose of enabling the healthcare professional to independently review the basis for the recommendation
5. The healthcare professional does not primarily rely on the software to make a clinical decision without independently reviewing the basis for the recommendation

If your CDS software fails **any one** of these criteria, it may be regulated as a medical device.

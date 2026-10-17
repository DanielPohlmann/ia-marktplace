<!-- Part of the specs-documentation-prd skill. Loaded on demand from SKILL.md. -->

# Prioritization Frameworks

## MoSCoW Method

| Priority | Meaning | Guideline |
|----------|---------|-----------|
| **Must Have** | Non-negotiable for launch | ~60% of effort |
| **Should Have** | Important but not critical | ~20% of effort |
| **Could Have** | Nice to have, low impact if omitted | ~20% of effort |
| **Won't Have** | Explicitly out of scope for this release | Documented for future |

Example:
```markdown
## Requirements by Priority

## Must Have
- FR-1: User registration and login
- FR-2: Product search with basic filters
- FR-3: Shopping cart and checkout
- NFR-1: Page load time < 3 seconds

## Should Have
- FR-4: Wishlist functionality
- FR-5: Order tracking dashboard
- NFR-2: Support for 3 languages

## Could Have
- FR-6: Product recommendation engine
- FR-7: Social sharing buttons

## Won't Have (this release)
- FR-8: Marketplace for third-party sellers
- FR-9: Mobile native app
```

## RICE Scoring

| Factor | Description | Scale |
|--------|-------------|-------|
| **R**each | How many users will this impact per quarter? | Number of users |
| **I**mpact | How much will this impact each user? | 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal |
| **C**onfidence | How confident are we in estimates? | 100% = high, 80% = medium, 50% = low |
| **E**ffort | How many person-months to complete? | Person-months |

**Formula:** `RICE Score = (Reach x Impact x Confidence) / Effort`

| Feature | Reach | Impact | Confidence | Effort | Score |
|---------|-------|--------|------------|--------|-------|
| Search filters | 5000 | 2 | 80% | 2 | 4000 |
| Wishlist | 2000 | 1 | 80% | 1 | 1600 |
| Recommendations | 5000 | 2 | 50% | 4 | 1250 |
| Social sharing | 1000 | 0.5 | 80% | 0.5 | 800 |

Higher RICE score = higher priority.

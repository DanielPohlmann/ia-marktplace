<!-- Part of the specs-documentation-prd skill. Loaded on demand from SKILL.md. -->

# Writing Good User Stories

## The Standard Format
```
As a [persona/role],
I want [action or capability],
So that [business value or benefit].
```

## INVEST Criteria for User Stories
| Criterion | Meaning |
|-----------|---------|
| **I**ndependent | Can be developed and delivered independently of other stories |
| **N**egotiable | Details can be discussed and refined collaboratively |
| **V**aluable | Delivers clear value to the user or business |
| **E**stimable | Team can estimate the effort required |
| **S**mall | Can be completed within a single sprint |
| **T**estable | Has clear acceptance criteria that can be verified |

## Good vs Poor User Stories

**Poor (too vague):**
```
As a user, I want a better search so that I can find things.
```

**Good (specific and valuable):**
```
As a product catalog browser,
I want to filter search results by price range, category, and rating,
So that I can quickly find products that match my budget and preferences.

Acceptance Criteria:
- [ ] Filter panel displays on the search results page
- [ ] Price range filter supports min/max with a slider
- [ ] Category filter shows top-level categories with item counts
- [ ] Rating filter allows selecting minimum star rating (1-5)
- [ ] Filters can be combined (AND logic)
- [ ] Clearing all filters restores the full result set
- [ ] Filter selections persist across pagination
```

## Acceptance Criteria Formats

**Checklist format:**
```
Acceptance Criteria:
- [ ] User can upload files up to 50MB
- [ ] Supported formats: PDF, DOCX, XLSX, PNG, JPG
- [ ] Upload progress bar is displayed during upload
- [ ] Error message shown for unsupported file types
```

**Given/When/Then format (for complex scenarios):**
```
Acceptance Criteria:
- Given I am on the search results page
  When I set the price filter to $10-$50
  Then only products priced between $10 and $50 are displayed
```

<!-- Part of the bdd-gherkin skill. Loaded on demand from SKILL.md. -->

# BDD with Gherkin — details

## Data tables and doc strings

Use a data table when a step carries 2+ fields or would otherwise run long.

**Multiple records — horizontal headers:**
```gherkin
Given the following services are in the professional's catalog:
  | Service        | Duration | Price |
  | Haircut        | 45       | 80    |
  | Beard trim     | 20       | 40    |
  | Full grooming  | 75       | 150   |
```

**One entity, many fields — vertical key/value:**
```gherkin
Given a client books an appointment with the following details:
  | Service   | Haircut            |
  | Date      | 2026-07-15         |
  | Time      | 14:30              |
  | Address   | 120 Oak Street     |
```

**Don't** cram it inline:
```gherkin
Given a client books a Haircut on 2026-07-15 at 14:30 at 120 Oak Street with notes "please be on time"
```

Use a doc string for larger free text:
```gherkin
Given a client leaves this review for a completed appointment:
  """
  Arrived right on time and did a fantastic job.
  Booking through the profile link was effortless.
  """
When the review is submitted
Then the review is published on the professional's public profile
```

## Worked example (Scheduling)

```gherkin
Feature: Appointment booking within plan limits
  As a client
  I want to book an appointment with a professional
  So that I reserve a confirmed time slot

  Background:
    Given the professional accepts online bookings

  Scenario: Client books an available slot
    Given the professional has a free slot on 2026-07-15 at 14:30
    When a client books that slot
    Then the appointment is confirmed
    And the professional is notified of the booking

  Scenario: Booking is rejected when the monthly plan limit is reached
    Given the professional is on the Free plan
    And 5 appointments are already booked this month
    When a client books another appointment
    Then the booking is rejected
    And the client is told the professional is fully booked this month

  Scenario: Overlapping slot cannot be double-booked
    Given the professional has a confirmed appointment on 2026-07-15 at 14:30
    When another client books the 14:30 slot on 2026-07-15
    Then the booking is rejected
    And the slot is shown as unavailable
```

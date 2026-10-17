<!-- Part of the specs-documentation-gherkin skill. Loaded on demand from SKILL.md. -->

# Core Keywords

## Feature
The top-level keyword that describes a single capability or business rule. Each `.feature` file contains exactly one `Feature`.

```gherkin
Feature: User Authentication
  As a registered user
  I want to log in with my credentials
  So that I can access my personalized dashboard
```

The free-text description below the `Feature` keyword is not parsed by the runner but serves as living documentation.

## Scenario
A concrete example of the feature's expected behavior. Each scenario is an independent, self-contained test case.

```gherkin
Scenario: Successful login with valid credentials
  Given a registered user with email "alice@example.com" and password "Str0ng!Pass"
  When the user submits the login form
  Then the user should be redirected to the dashboard
  And the welcome message should display "Hello, Alice"
```

## Steps: Given / When / Then / And / But

| Keyword | Purpose | Example |
|---------|---------|---------|
| **Given** | Establish preconditions (arrange) | `Given the user has items in the cart` |
| **When** | Perform the action under test (act) | `When the user clicks "Checkout"` |
| **Then** | Assert the expected outcome (assert) | `Then the order confirmation page is displayed` |
| **And** | Continue the previous step type | `And the order total is "$42.00"` |
| **But** | Negative continuation of the previous step type | `But the coupon field should not be visible` |

`And` and `But` inherit the keyword type of the step they follow. They exist purely for readability.

## Background
Steps that run before every scenario in the feature file. Use for shared preconditions to reduce duplication.

```gherkin
Feature: Shopping Cart

  Background:
    Given the user is logged in
    And the product catalog is loaded

  Scenario: Add item to empty cart
    Given the cart is empty
    When the user adds "Wireless Mouse" to the cart
    Then the cart should contain 1 item

  Scenario: Add item to non-empty cart
    Given the cart contains "Keyboard"
    When the user adds "Wireless Mouse" to the cart
    Then the cart should contain 2 items
```

## Scenario Outline (Scenario Template)
A parameterized scenario that runs once for each row in the `Examples` table. Use when the same behavior applies to multiple input/output combinations.

```gherkin
Scenario Outline: Login validation
  Given the user enters email "<email>" and password "<password>"
  When the user submits the login form
  Then the system should respond with "<result>"

  Examples:
    | email              | password    | result          |
    | alice@example.com  | Str0ng!Pass | success         |
    | alice@example.com  | wrong       | invalid_password|
    | unknown@test.com   | any         | user_not_found  |
    |                    | Str0ng!Pass | email_required  |
```

## Data Tables
Tabular data passed to a single step for structured input.

```gherkin
Scenario: Create multiple users
  Given the following users exist:
    | name    | email              | role    |
    | Alice   | alice@example.com  | admin   |
    | Bob     | bob@example.com    | editor  |
    | Charlie | charlie@example.com| viewer  |
  When the admin views the user list
  Then all 3 users should be displayed
```

## Doc Strings
Multi-line text blocks passed to a step, delimited by triple quotes.

```gherkin
Scenario: Submit a support request
  Given the user is on the support page
  When the user submits a request with the following message:
    """
    Hello Support Team,

    I am experiencing an issue with my account settings.
    The timezone selector does not save my preference.

    Thank you,
    Alice
    """
  Then the support ticket should be created
  And the ticket body should contain "timezone selector"
```

Doc strings can also specify a content type:

```gherkin
When the API receives the following JSON payload:
  """json
  {
    "name": "Widget",
    "price": 9.99,
    "inStock": true
  }
  """
```

## Tags
Annotations prefixed with `@` that categorize and filter features, scenarios, or examples.

```gherkin
@authentication @smoke
Feature: User Authentication

  @happy-path
  Scenario: Successful login
    Given a registered user
    When the user logs in with valid credentials
    Then the login should succeed

  @negative @security
  Scenario: Account lockout after failed attempts
    Given a registered user
    When the user fails login 5 times consecutively
    Then the account should be locked for 30 minutes
```

Common tag uses:
- `@smoke`, `@regression`, `@wip` -- test suite categorization
- `@slow`, `@fast` -- execution time hints
- `@ignore`, `@skip` -- temporarily exclude scenarios
- `@api`, `@ui`, `@integration` -- test layer classification

Run filtered tests: `cucumber --tags "@smoke and not @wip"`

## Rules (Gherkin 6+)
Group related scenarios under a business rule within a feature.

```gherkin
Feature: Account Withdrawal

  Rule: Withdrawals must not exceed account balance
    Scenario: Withdrawal within balance
      Given an account balance of $500
      When the user withdraws $200
      Then the new balance should be $300

    Scenario: Withdrawal exceeding balance
      Given an account balance of $500
      When the user withdraws $600
      Then the withdrawal should be declined
      And the balance should remain $500

  Rule: Daily withdrawal limit is $1000
    Scenario: Withdrawal at the daily limit
      Given an account balance of $5000
      And the user has withdrawn $800 today
      When the user withdraws $200
      Then the withdrawal should succeed

    Scenario: Withdrawal exceeding daily limit
      Given an account balance of $5000
      And the user has withdrawn $800 today
      When the user withdraws $300
      Then the withdrawal should be declined
```

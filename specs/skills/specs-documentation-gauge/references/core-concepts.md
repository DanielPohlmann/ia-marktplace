<!-- Part of the specs-documentation-gauge skill. Loaded on demand from SKILL.md. -->

# Core Concepts

## Specification Files (.spec)
A specification is a Markdown file containing a heading (the spec name) and one or more scenarios.

```markdown
# User Authentication

This specification covers the login and logout flows
for registered users of the application.

## Successful Login

* Navigate to the login page
* Enter username "alice@example.com"
* Enter password "Str0ng!Pass"
* Click the login button
* Verify the dashboard is displayed
* Verify the welcome message shows "Hello, Alice"

## Failed Login with Wrong Password

* Navigate to the login page
* Enter username "alice@example.com"
* Enter password "wrong-password"
* Click the login button
* Verify the error message "Invalid credentials" is displayed
```

- The `#` heading is the **specification name**.
- The `##` headings are **scenario names**.
- Lines beginning with `*` are **steps**.
- Free-form text between headings is documentation (not executed).

## Steps
Steps are the executable units in Gauge. Each step in the spec maps to a step implementation in code.

Steps can contain **parameters** in quotes or angle brackets:
- Static parameters: `* Enter username "alice@example.com"`
- Dynamic parameters: `* Enter username <username>`
- Table parameters (passed as data tables)
- File parameters: `* Upload file <file:data/sample.csv>`

## Concepts
Concepts are reusable groups of steps -- like macros or subroutines for specifications. They are defined in `.cpt` files.

**File: `specs/concepts/login.cpt`**
```markdown
# Login as user <username> with password <password>

* Navigate to the login page
* Enter username <username>
* Enter password <password>
* Click the login button
```

**Using the concept in a spec:**
```markdown
## Successful Login

* Login as user "alice@example.com" with password "Str0ng!Pass"
* Verify the dashboard is displayed
```

Concepts reduce duplication and create a higher-level vocabulary for specs.

## Tags
Tags categorize specifications and scenarios for filtered execution.

```markdown
# User Authentication

Tags: authentication, smoke

## Successful Login

Tags: happy-path, critical

* Login as user "alice@example.com" with password "Str0ng!Pass"
* Verify the dashboard is displayed
```

Run filtered: `gauge run --tags "smoke & !wip" specs/`

## Data Tables
Tabular data can be embedded directly in specifications for data-driven scenarios.

```markdown
## Create users with different roles

   | username | role   | permissions        |
   |----------|--------|--------------------|
   | alice    | admin  | read,write,delete  |
   | bob      | editor | read,write         |
   | charlie  | viewer | read               |

* Create user <username> with role <role>
* Verify user <username> has permissions <permissions>
```

The scenario runs once per row with the column values substituted into the dynamic parameters.

## Data-Driven Testing with External Sources
Gauge supports CSV and other external data sources for large data sets.

**Using a CSV data source:**
```markdown
## Validate product pricing

Tags: data-driven

table: data/products.csv

* Search for product <name>
* Verify the displayed price is <expected_price>
* Verify the stock status is <stock_status>
```

**`data/products.csv`:**
```csv
name,expected_price,stock_status
Wireless Mouse,$29.99,In Stock
Mechanical KB,$89.99,In Stock
USB-C Hub,$49.99,Out of Stock
```

## Teardown Steps
Steps that run after every scenario in a specification, used for cleanup.

```markdown
# Shopping Cart

## Add item to cart

* Login as user "shopper@example.com" with password "Pass123"
* Add product "Wireless Mouse" to cart
* Verify cart contains 1 item

## Remove item from cart

* Login as user "shopper@example.com" with password "Pass123"
* Add product "Wireless Mouse" to cart
* Remove product "Wireless Mouse" from cart
* Verify cart is empty

___
* Clear the shopping cart
* Logout the current user
```

The `___` (three or more underscores) marks the beginning of teardown steps.

## Context Steps
Steps that run before every scenario in a specification, similar to Gherkin's `Background`.

```markdown
# Shopping Cart

* Login as user "shopper@example.com" with password "Pass123"
* Navigate to the product catalog

## Add item to cart

* Add product "Wireless Mouse" to cart
* Verify cart contains 1 item

## View empty cart

* Navigate to the cart page
* Verify the cart is empty
```

Steps placed between the specification heading and the first scenario heading are context steps.

<!-- Part of the specs-documentation-gherkin skill. Loaded on demand from SKILL.md. -->

# Complete Feature File Example

```gherkin
@e-commerce @cart
Feature: Shopping Cart Management
  As an online shopper
  I want to manage items in my shopping cart
  So that I can review and purchase the products I want

  Background:
    Given the user is logged in as "shopper@example.com"
    And the product catalog contains:
      | sku   | name           | price  | stock |
      | WM001 | Wireless Mouse | 29.99  | 50    |
      | KB002 | Mechanical KB  | 89.99  | 25    |
      | HD003 | USB-C Hub      | 49.99  | 0     |

  @happy-path
  Scenario: Add an in-stock item to the cart
    Given the shopping cart is empty
    When the user adds product "WM001" to the cart
    Then the cart should contain 1 item
    And the cart total should be "$29.99"

  @happy-path
  Scenario: Update item quantity in the cart
    Given the cart contains 1 unit of "WM001"
    When the user changes the quantity of "WM001" to 3
    Then the cart should contain 3 items
    And the cart total should be "$89.97"

  @negative
  Scenario: Cannot add out-of-stock item
    Given the shopping cart is empty
    When the user adds product "HD003" to the cart
    Then the user should see an error "This item is currently out of stock"
    And the cart should remain empty

  @negative
  Scenario: Cannot exceed available stock
    Given the cart contains 1 unit of "WM001"
    When the user changes the quantity of "WM001" to 100
    Then the user should see an error "Only 50 units available"
    And the quantity of "WM001" should remain 1

  Scenario: Remove item from cart
    Given the cart contains 1 unit of "WM001"
    And the cart contains 1 unit of "KB002"
    When the user removes "WM001" from the cart
    Then the cart should contain 1 item
    And the cart total should be "$89.99"

  @data-driven
  Scenario Outline: Apply discount codes
    Given the cart total is "$100.00"
    When the user applies discount code "<code>"
    Then the discount should be "<discount>"
    And the new total should be "<total>"

    Examples:
      | code       | discount | total  |
      | SAVE10     | 10%      | $90.00 |
      | FLAT20     | $20.00   | $80.00 |
      | EXPIRED01  | 0%       | $100.00|

    @vip
    Examples: VIP codes
      | code       | discount | total  |
      | VIP25      | 25%      | $75.00 |
      | VIPFLAT50  | $50.00   | $50.00 |
```

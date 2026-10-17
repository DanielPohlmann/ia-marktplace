<!-- Part of the specs-documentation-gauge skill. Loaded on demand from SKILL.md. -->

# Complete Specification Example

```markdown
# E-Commerce Checkout

Tags: checkout, e2e

This specification covers the end-to-end checkout process
including cart review, shipping, payment, and order confirmation.

* Login as user "shopper@example.com" with password "Shop!Pass1"
* Navigate to the product catalog

## Purchase a single item

Tags: happy-path, smoke

* Add product "Wireless Mouse" to the cart
* Navigate to the cart page
* Verify the cart total is "$29.99"
* Proceed to checkout
* Enter shipping address:

   | field       | value              |
   |-------------|--------------------|
   | name        | Alice Smith        |
   | street      | 123 Main St        |
   | city        | Springfield        |
   | state       | IL                 |
   | zip         | 62701              |

* Select shipping method "Standard (5-7 days)"
* Enter payment card "4111111111111111" expiry "12/27" cvv "123"
* Place the order
* Verify order confirmation is displayed
* Verify confirmation email is sent to "shopper@example.com"

## Apply discount code during checkout

Tags: discounts

* Add product "Mechanical KB" to the cart
* Navigate to the cart page
* Apply discount code "SAVE10"
* Verify the discount of "10%" is applied
* Verify the cart total is "$80.99"
* Proceed to checkout
* Place the order with saved shipping and payment
* Verify order confirmation is displayed

## Checkout with empty cart

Tags: negative

* Navigate to the cart page
* Verify the cart is empty
* Verify the checkout button is disabled
* Verify the message "Add items to your cart to proceed" is displayed

___
* Clear the shopping cart
* Logout the current user
```

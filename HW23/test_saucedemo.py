""" Homework 23: Selectors map for saucedemo.com

LOGIN PAGE:
1. Open the website: https://saucedemo.com
2. Enter username
   - CSS: input[data-test="username"]
3. Enter password
   - CSS: input[data-test="password"]
4. Click 'Login' button
   - CSS: input[data-test="login-button"]


INVENTORY PAGE:
5. Click "Add to cart" button for Sauce Labs Backpack
   - CSS: button[data-test="add-to-cart-sauce-labs-backpack"]
6. Click shopping cart icon
   - CSS: a[data-test="shopping-cart-link"]


CART PAGE:
7. Click "Checkout" button
   - CSS: button[data-test="checkout"]


CHECKOUT: YOUR INFORMATION PAGE:
8. Enter First Name
   - CSS: input[data-test="firstName"]
9. Enter Last Name
   - CSS: input[data-test="lastName"]
10. Enter Zip/Postal Code
    - CSS: input[data-test="postalCode"]
11. Click "Continue" button
    - CSS: input[data-test="continue"]


CHECKOUT: OVERVIEW PAGE:
12. Click "Finish" button to complete the purchase
    - CSS: button[data-test="finish"]


CHECKOUT: COMPLETE PAGE:
13. Assert successful order header text ("Thank you for your order!")
    - CSS: h2[data-test="complete-header"]
14. Click "Back Home" button to return to the inventory page
    - CSS: button[data-test="back-to-products"]


LOGOUT FLOW:
15. Click the burger menu button to open the sidebar
    - CSS: button[id="react-burger-menu-btn"]
16. Click "Logout" link to sign out
    - CSS: a[data-test="logout-sidebar-link"] """

"""UI automation tests for saucedemo.com shopping cart and checkout flows."""

from playwright.sync_api import Page, expect
from logger_config import get_logger

logger = get_logger(__name__)

base_url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"

first_name = "Mike"
last_name = "Ness"
zip_code = "12345"


def login(page: Page):
    logger.info("Opening the main page: %s", base_url)
    page.goto(base_url)
    logger.info("Entering username: %s", username)
    page.locator('input[data-test="username"]').fill(username)
    logger.info("Entering password")
    page.locator('input[data-test="password"]').fill(password)
    logger.info("Clicking the Login button")
    page.locator('input[data-test="login-button"]').click()


def test_login(page: Page):
    logger.info("--- Starting test: Login ---")
    login(page)
    logger.info("Asserting redirection to the inventory page")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    logger.info("--- Test successfully passed ---")


def test_add_to_cart(page: Page):
    logger.info("--- Starting test: Add to Cart ---")
    login(page)

    logger.info("Adding 'Sauce Labs Backpack' to the cart")
    page.locator('button[data-test="add-to-cart-sauce-labs-backpack"]').click()

    logger.info("Clicking the shopping cart icon")
    page.locator('a[data-test="shopping-cart-link"]').click()

    logger.info("Asserting navigation to the cart page")
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    logger.info("--- Test successfully passed ---")


def test_complete_order_and_logout(page: Page):
    logger.info("--- Starting test: Checkout and Logout ---")
    login(page)

    logger.info("Adding item to cart and navigating to cart page")
    page.locator('button[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('a[data-test="shopping-cart-link"]').click()

    logger.info("Clicking the Checkout button")
    page.locator('button[data-test="checkout"]').click()

    logger.info("Filling in the customer information form")
    page.locator('input[data-test="firstName"]').fill(first_name)
    page.locator('input[data-test="lastName"]').fill(last_name)
    page.locator('input[data-test="postalCode"]').fill(zip_code)

    logger.info("Clicking the Continue button")
    page.locator('input[data-test="continue"]').click()

    logger.info("Clicking the Finish button to complete the purchase")
    page.locator('button[data-test="finish"]').click()

    logger.info("Asserting successful order header text")
    success_header = page.locator('h2[data-test="complete-header"]')
    expect(success_header).to_have_text("Thank you for your order!")

    logger.info("Returning to the inventory page")
    page.locator('button[data-test="back-to-products"]').click()

    logger.info("Logging out via the sidebar burger menu")
    page.locator('button[id="react-burger-menu-btn"]').click()
    page.locator('a[data-test="logout-sidebar-link"]').click()

    logger.info("Asserting return to the login page")
    expect(page).to_have_url(base_url)
    logger.info("--- Test successfully passed ---")

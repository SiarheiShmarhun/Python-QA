"""UI automation tests for saucedemo.com shopping cart and checkout flows."""

from playwright.sync_api import Page, expect

from HW25.pages.cart_pages import (CartPage, CheckoutCompletePage,
                                   CheckoutInformationPage)
from HW25.pages.inventory_page import InventoryPage
from HW25.test_data.users import TestData
from logger_config import get_logger

logger = get_logger(__name__)


def test_login(page: Page, login_page):
    logger.info("--- Starting test: Login (POM) ---")
    login_page.navigate()
    login_page.login(TestData.username, TestData.password)

    logger.info("Asserting redirection to the inventory page")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    logger.info("--- Test successfully passed ---")


def test_add_to_cart(page: Page, login_page, inventory_page):
    logger.info("--- Starting test: Add to Cart (POM) ---")
    login_page.navigate()
    login_page.login(TestData.username, TestData.password)

    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    logger.info("Asserting navigation to the cart page")
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    logger.info("--- Test successfully passed ---")


def test_complete_order_and_logout(page: Page, login_page):
    logger.info("--- Starting test: Checkout and Logout (POM) ---")
    login_page.navigate()
    login_page.login(TestData.username, TestData.password)

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    checkout_info_page = CheckoutInformationPage(page)
    checkout_info_page.fill_customer_info(TestData.first_name, TestData.last_name, TestData.zip_code)

    checkout_complete_page = CheckoutCompletePage(page)
    checkout_complete_page.finish_order()

    logger.info("Asserting successful order header text")
    expect(checkout_complete_page.success_header).to_have_text("Thank you for your order!")

    logger.info("Returning to the inventory page")
    checkout_complete_page.return_to_products()

    logger.info("Logging out via the sidebar burger menu")
    inventory_page.logout()

    logger.info("Asserting return to the login page")
    expect(page).to_have_url(TestData.base_url)
    logger.info("--- Test successfully passed ---")

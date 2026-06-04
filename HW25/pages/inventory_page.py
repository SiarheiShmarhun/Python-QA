"""Inventory page module managing the main product catalog."""

from playwright.sync_api import Page

from HW25.pages.base_page import BasePage
from logger_config import get_logger

logger = get_logger(__name__)


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.backpack_add_to_cart_btn = page.locator('button[data-test="add-to-cart-sauce-labs-backpack"]')
        self.cart_link = page.locator('a[data-test="shopping-cart-link"]')
        self.burger_menu_btn = page.locator('button[id="react-burger-menu-btn"]')
        self.logout_link = page.locator('a[data-test="logout-sidebar-link"]')

    def add_backpack_to_cart(self):
        logger.info("Adding 'Sauce Labs Backpack' to the cart")
        self.backpack_add_to_cart_btn.click()

    def go_to_cart(self):
        logger.info("Clicking the shopping cart icon")
        self.cart_link.click()

    def logout(self):
        logger.info("Logging out via sidebar menu")
        self.burger_menu_btn.click()
        self.logout_link.click()

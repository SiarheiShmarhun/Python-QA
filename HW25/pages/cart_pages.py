"""Cart and checkout workflow pages module."""

from playwright.sync_api import Page

from HW25.pages.base_page import BasePage
from logger_config import get_logger

logger = get_logger(__name__)


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.checkout_button = page.locator('button[data-test="checkout"]')

    def proceed_to_checkout(self):
        logger.info("Clicking the Checkout button")
        self.checkout_button.click()


class CheckoutInformationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name_input = page.locator('input[data-test="firstName"]')
        self.last_name_input = page.locator('input[data-test="lastName"]')
        self.zip_code_input = page.locator('input[data-test="postalCode"]')
        self.continue_button = page.locator('input[data-test="continue"]')

    def fill_customer_info(self, first_name, last_name, zip_code):
        logger.info("Filling in customer info: %s %s, %s", first_name, last_name, zip_code)
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.zip_code_input.fill(zip_code)
        self.continue_button.click()


class CheckoutCompletePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.finish_button = page.locator('button[data-test="finish"]')
        self.success_header = page.locator('h2[data-test="complete-header"]')
        self.back_to_products_button = page.locator('button[data-test="back-to-products"]')

    def finish_order(self):
        logger.info("Clicking the Finish button")
        self.finish_button.click()

    def return_to_products(self):
        logger.info("Clicking Back to Products button")
        self.back_to_products_button.click()

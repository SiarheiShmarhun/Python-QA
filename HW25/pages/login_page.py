"""Login page module for authentication actions and locators."""

from playwright.sync_api import Page

from HW25.pages.base_page import BasePage
from HW25.test_data.users import TestData
from logger_config import get_logger

logger = get_logger(__name__)


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator('input[data-test="username"]')
        self.password_input = page.locator('input[data-test="password"]')
        self.login_button = page.locator('input[data-test="login-button"]')

    def navigate(self):
        logger.info("Opening the login page: %s", TestData.base_url)
        self.page.goto(TestData.base_url)

    def login(self, username, password):
        logger.info("Performing login for user: %s", username)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

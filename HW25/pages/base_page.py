"""Base page module providing core functionality for all Page Objects."""

from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

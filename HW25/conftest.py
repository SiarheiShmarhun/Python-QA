"""PyTest local fixtures and automation reporting hooks configuration."""

import pytest
from playwright.sync_api import Page

from HW25.pages.cart_pages import (CartPage, CheckoutCompletePage,
                                   CheckoutInformationPage)
from HW25.pages.inventory_page import InventoryPage
from HW25.pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    return InventoryPage(page)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def checkout_info_page(page: Page) -> CheckoutInformationPage:
    return CheckoutInformationPage(page)


@pytest.fixture
def checkout_complete_page(page: Page) -> CheckoutCompletePage:
    return CheckoutCompletePage(page)

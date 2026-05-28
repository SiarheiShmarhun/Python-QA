"""Unit tests for the Bank and CurrencyConverter classes using PyTest."""

import pytest
from HW12.bank_deposit import Bank, CurrencyConverter
from logger_config import get_logger

logger = get_logger(__name__)


@pytest.fixture
def bank():
    return Bank()


@pytest.fixture
def client_id(bank):
    c_id = "001"
    bank.register_client(c_id, "Siarhei")
    return c_id


# Positive Tests


def test_calc_deposit_success(bank, client_id):
    logger.info("Testing successful interest calculation for 1 year")
    bank.open_deposit_account(client_id, 1000, 1)
    assert bank.calc_deposit_interest_rate(client_id) == 1104.71
    logger.info("Test passed successfully")


def test_close_deposit_success(bank, client_id):
    logger.info("Testing successful deposit closure and client removal")
    bank.open_deposit_account(client_id, 1000, 1)
    bank.close_deposit(client_id)
    assert client_id not in bank.clients
    logger.info("Test passed successfully")


def test_exchange_usd_to_byn_success():
    logger.info("Testing successful exchange USD to BYN")
    converter = CurrencyConverter()
    result, curr = converter.exchange_currency("USD", 10, "BYN")
    assert result == 32.69
    assert curr == "BYN"
    logger.info("Test passed successfully")


# Negative Tests


def test_calc_deposit_non_existent_client(bank):
    logger.info("Testing interest calculation for non-existent client")
    assert bank.calc_deposit_interest_rate("999") == 0.0
    logger.info("Test passed successfully")


def test_calc_deposit_zero_balance(bank, client_id):
    logger.info("Testing calculation with zero balance")
    bank.open_deposit_account(client_id, 0, 1)
    assert bank.calc_deposit_interest_rate(client_id) == 0.0
    logger.info("Test passed successfully")


def test_close_non_existent_deposit(bank, client_id):
    logger.info("Testing closure of a deposit that does not exist")
    bank.close_deposit(client_id)
    assert client_id in bank.clients
    logger.info("Test passed successfully")


def test_exchange_invalid_amount_type():
    logger.info("Testing exchange with invalid amount type (string)")
    converter = CurrencyConverter()
    assert converter.exchange_currency("USD", "invalid_amount") is None
    logger.info("Test passed successfully")


def test_exchange_unsupported_currency():
    logger.info("Testing exchange with unsupported currency code")
    converter = CurrencyConverter()
    assert converter.exchange_currency("GBP", 100) is None
    logger.info("Test passed successfully")

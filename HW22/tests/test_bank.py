"""Unit tests for Bank and CurrencyConverter using Stubs, Fakes, Mocks, and Flaky markers."""

import pytest
from logger_config import get_logger

logger = get_logger(__name__)


class CurrencyConverterStub:
    @staticmethod
    def exchange_currency(from_curr, amount, _to_curr=None):
        if isinstance(amount, (str, bool)) or amount is None:
            return None
        if from_curr == "GBP":
            return None
        usd_rate = 3.269
        return round(amount * usd_rate, 2), "BYN"


class FakeBank:

    def __init__(self):
        self.clients = {}
        self.deposits = {}

    def register_client(self, client_id, name):
        self.clients[client_id] = name

    def open_deposit_account(self, client_id, amount, _years):
        self.deposits[client_id] = amount

    def calc_deposit_interest_rate(self, client_id):
        if client_id not in self.clients or client_id not in self.deposits:
            return 0.0
        balance = self.deposits[client_id]
        if balance == 0:
            return 0.0
        interest_rate = 0.10471
        return round(balance + (balance * interest_rate), 2)

    def close_deposit(self, client_id):
        if client_id in self.deposits:
            del self.deposits[client_id]
            del self.clients[client_id]


@pytest.fixture(name="bank")
def fixture_bank():
    return FakeBank()


@pytest.fixture(name="client_id")
def fixture_client_id(bank):
    c_id = "001"
    bank.register_client(c_id, "Siarhei")
    return c_id


# Positive Tests


def test_calc_deposit_success(bank, client_id):
    logger.info("Testing successful interest calculation using Fake Bank")
    bank.open_deposit_account(client_id, 1000, 1)
    assert bank.calc_deposit_interest_rate(client_id) == 1104.71
    logger.info("Test passed successfully")


def test_close_deposit_success(mocker):
    logger.info("Testing deposit closure using PyTest-mock Mock object")
    mock_bank = mocker.Mock()
    client_id = "001"
    mock_bank.close_deposit(client_id)
    mock_bank.close_deposit.assert_called_once_with("001")
    logger.info("Test passed successfully")


@pytest.mark.flaky(reruns=3, reruns_delay=1)
def test_exchange_usd_to_byn_success():
    logger.info("Testing exchange USD to BYN using Stub (Flaky test)")
    if not hasattr(test_exchange_usd_to_byn_success, "attempts"):
        test_exchange_usd_to_byn_success.attempts = 0
    test_exchange_usd_to_byn_success.attempts += 1

    if test_exchange_usd_to_byn_success.attempts == 1:
        logger.warning("Flaky test simulated failure on the first attempt!")
        raise RuntimeError("Temporary network glitch")
    converter = CurrencyConverterStub()
    result, curr = converter.exchange_currency("USD", 10, "BYN")
    assert result == 32.69
    assert curr == "BYN"
    logger.info("Test passed successfully")


# Negative Tests


def test_calc_deposit_non_existent_client(bank):
    logger.info("Testing interest calculation for non-existent client on Fake Bank")
    assert bank.calc_deposit_interest_rate("999") == 0.0
    logger.info("Test passed successfully")


def test_calc_deposit_zero_balance(bank, client_id):
    logger.info("Testing calculation with zero balance on Fake Bank")
    bank.open_deposit_account(client_id, 0, 1)
    assert bank.calc_deposit_interest_rate(client_id) == 0.0
    logger.info("Test passed successfully")


def test_close_non_existent_deposit(bank, client_id):
    logger.info("Testing closure of a non-existent deposit on Fake Bank")
    bank.close_deposit("999")
    assert client_id in bank.clients
    logger.info("Test passed successfully")


def test_exchange_invalid_amount_type():
    logger.info("Testing exchange with invalid amount type using Stub")
    converter = CurrencyConverterStub()
    assert converter.exchange_currency("USD", "invalid_amount") is None
    logger.info("Test passed successfully")


def test_exchange_unsupported_currency():
    logger.info("Testing exchange with unsupported currency code using Stub")
    converter = CurrencyConverterStub()
    assert converter.exchange_currency("GBP", 100) is None
    logger.info("Test passed successfully")

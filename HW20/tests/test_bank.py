"""Unit tests for the Bank and CurrencyConverter classes."""

import unittest

from HW12.bank_deposit import Bank, CurrencyConverter
from logger_config import get_logger

logger = get_logger(__name__)
logger.info("Bank module started")


class TestBank(unittest.TestCase):

    def setUp(self):
        logger.info("Setting up Bank test environment")
        self.bank = Bank()
        self.client_id = "001"
        self.bank.register_client(self.client_id, "Siarhei")
        logger.info("Bank test environment set up successfully")

    def tearDown(self):
        logger.info("Tearing down Bank test environment")
        del self.bank
        logger.info("Bank test environment torn down successfully")

    # Positive Tests

    def test_calc_deposit_success(self):
        logger.info("Testing successful interest calculation for 1 year")
        self.bank.open_deposit_account(self.client_id, 1000, 1)
        result = self.bank.calc_deposit_interest_rate(self.client_id)
        self.assertEqual(result, 1104.71)
        logger.info("Test passed successfully")

    def test_close_deposit_success(self):
        logger.info("Testing successful deposit closure and client removal")
        self.bank.open_deposit_account(self.client_id, 1000, 1)
        self.bank.close_deposit(self.client_id)
        self.assertNotIn(self.client_id, self.bank.clients)
        logger.info("Test passed successfully")

    # Negative Tests

    def test_calc_deposit_non_existent_client(self):
        logger.info("Testing interest calculation for non-existent client")
        result = self.bank.calc_deposit_interest_rate("999")
        self.assertEqual(result, 0.0)
        logger.info("Test passed successfully")

    def test_calc_deposit_zero_balance(self):
        logger.info("Testing calculation with zero balance")
        self.bank.open_deposit_account(self.client_id, 0, 1)
        result = self.bank.calc_deposit_interest_rate(self.client_id)
        self.assertEqual(result, 0.0)
        logger.info("Test passed successfully")

    def test_close_non_existent_deposit(self):
        logger.info("Testing closure of a deposit that does not exist")
        self.bank.close_deposit(self.client_id)
        self.assertIn(self.client_id, self.bank.clients)
        logger.info("Test passed successfully")


class TestConverter(unittest.TestCase):

    def test_exchange_usd_to_byn_success(self):
        logger.info("Testing successful exchange USD to BYN")
        converter = CurrencyConverter()
        result, curr = converter.exchange_currency("USD", 10, "BYN")
        self.assertEqual(result, 32.69)
        self.assertEqual(curr, "BYN")
        logger.info("Test passed successfully")

    def test_exchange_invalid_amount_type(self):
        logger.info("Testing exchange with invalid amount type (string)")
        converter = CurrencyConverter()
        result = converter.exchange_currency("USD", "invalid_amount")
        self.assertIsNone(result)
        logger.info("Test passed successfully")

    def test_exchange_unsupported_currency(self):
        logger.info("Testing exchange with unsupported currency code")
        converter = CurrencyConverter()
        result = converter.exchange_currency("GBP", 100)
        self.assertIsNone(result)
        logger.info("Test passed successfully")


if __name__ == '__main__':
    unittest.main()

"""A class for managing bank deposits with monthly capitalization."""

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Bank:

    def __init__(self):
        self.clients = {}

    def register_client(self, client_id, name):
        self.clients[client_id] = {"name": name, "deposit": 0, "years": 0}
        logger.info("Client registered: %s (ID: %s)", name, client_id)

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id not in self.clients:
            logger.error("Client %s is not registered!", client_id)
            return
        self.clients[client_id]["deposit"] = start_balance
        self.clients[client_id]["years"] = years

    def calc_deposit_interest_rate(self, client_id):
        if client_id not in self.clients or self.clients[client_id]["deposit"] <= 0:
            logger.warning("No active deposit for client %s!", client_id)
            return 0.0
        amount = self.clients[client_id]["deposit"]
        years = self.clients[client_id]["years"]
        months = years * 12
        for _ in range(months):
            amount += amount * (0.10 / 12)
        return round(amount, 2)

    def close_deposit(self, client_id):
        if client_id in self.clients and self.clients[client_id]["deposit"] > 0:
            del self.clients[client_id]
        else:
            logger.error("Cannot close deposit for client %s. Deposit not found.", client_id)


class Person:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount


class CurrencyConverter:
    def __init__(self):
        self.rates = {"USD": 3.269, "EUR": 3.52, "BYN": 1.0}

    def exchange_currency(self, from_curr, amount, to_curr="BYN"):
        if from_curr not in self.rates or to_curr not in self.rates:
            return None
        if not isinstance(amount, (int, float)) or amount < 0:
            logger.error("Incorrect amount to convert!")
            return None
        from_rate = self.rates[from_curr]
        to_rate = self.rates[to_curr]
        result = amount * from_rate / to_rate
        return round(result, 2), to_curr


if __name__ == "__main__":
    test_client_id = "00000001"
    bank = Bank()
    bank.register_client(client_id=test_client_id, name="Siarhei")
    bank.open_deposit_account(client_id=test_client_id, start_balance=1000, years=1)

    assert bank.calc_deposit_interest_rate(client_id=test_client_id) == 1104.71
    bank.close_deposit(client_id=test_client_id)
    logger.info("Bank manual test passed!")

    converter = CurrencyConverter()
    vasya = Person('USD', 10)
    assert converter.exchange_currency(vasya.currency, vasya.amount) == (32.69, "BYN")
    logger.info("Converter manual test passed!")

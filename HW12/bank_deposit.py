"""A class for managing bank deposits with monthly capitalization."""


class Bank:

    def __init__(self):
        self.clients = {}

    def register_client(self, client_id, name):
        self.clients[client_id] = {"name": name, "deposit": 0, "years": 0}

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id not in self.clients:
            print(f"Error: Client {client_id} is not registered!")
            return
        self.clients[client_id]["deposit"] = start_balance
        self.clients[client_id]["years"] = years

    def calc_deposit_interest_rate(self, client_id):
        if client_id not in self.clients or self.clients[client_id]["deposit"] <= 0:
            print(f"Error: No active deposit for client {client_id}!")
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
            print(f"Error: Cannot close deposit for client {client_id}. Deposit not found.")


test_client_id = "00000001"
bank = Bank()
bank.register_client(client_id=test_client_id, name="Siarhei")
bank.open_deposit_account(client_id=test_client_id, start_balance=1000, years=1)

assert bank.calc_deposit_interest_rate(client_id=test_client_id) == 1104.71, "Error in percentage calculation!"

bank.close_deposit(client_id=test_client_id)


print("Test passed!")

bank.open_deposit_account(client_id="666", start_balance=300, years=2)
bank.register_client(client_id="666", name="Edward")
bank.calc_deposit_interest_rate(client_id="666")
bank.close_deposit(client_id="00000001")


print("Test passed!")


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
            print("Error: Incorrect amount to convert!")
            return None
        from_rate = self.rates[from_curr]
        to_rate = self.rates[to_curr]
        result = amount * from_rate / to_rate
        return round(result, 2), to_curr


converter = CurrencyConverter()
vasya = Person('USD', 10)
petya = Person('EUR', 5)

assert converter.exchange_currency(vasya.currency, vasya.amount) == (32.69, "BYN"), "The USD to BYN exchange rate is not correct!"
assert converter.exchange_currency(petya.currency, petya.amount) == (17.60, "BYN"), "The EUR to BYN exchange rate is incorrect!"
assert converter.exchange_currency(vasya.currency, vasya.amount, 'EUR') == (9.29, "EUR"), "Conversion USD -> EUR is invalid!"
assert converter.exchange_currency(petya.currency, petya.amount, 'USD') == (5.38, "USD"), "The conversion EUR -> USD is incorrect!"

print("Test passed!")

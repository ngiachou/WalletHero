from transaction import Transaction
from cost_types.base_type import Product
from datetime import date
import re


class Account:

    """
    Takes the users balance and his history of transactions.
    Account's methods create and add a transaction into the dictionary of
    transactions (new_transaction).
    """

    def __init__(self, user, balance=0.0, monthly_target=0.0):
        """
        Sets some initial values.

        @param user -- string which represents the user
        @param balance (default 0.0) -- floating point number representing the
        total balance
        @param monthly_target (default 0.0) -- floating point number
        representing the target total cost of the current month
        """
        self.user = user
        self._balance = float(balance)
        self._monthly_target = float(monthly_target)
        self.transactions_per_date = {}

    def new_transaction(self, transaction_str, date_str):
        """Adding a new transaction into transactions_per_date attribute"""
        date_obj = date.fromisoformat(date_str)
        self.transactions_per_date.setdefault(date_obj, [])

        transaction = self.parse_transaction(transaction_str, date_obj)

        self.transactions_per_date[date_str].append(transaction)
        self.update_balance(transaction)

    def parse_transaction(self, transaction_str, date_obj):
        """
        Parsing the transaction string.

        @param: transaction_str -- string representing a transaction
        for example 'food:5.5,drink:2.5'
        """
        matches = re.match(r"(\w+):(\d+\.\d+),*")

        # instantiate products
        products = []
        for match in matches:
            product = Product(match.group(1), float(match.group(2)))
            products.append(product)

        return Transaction(products, "", "", date_obj)

    def change_balance(self, amount):
        """Changing balance according to amount's value with some checks"""
        if amount < 0 and self._balance < -amount:
            raise ValueError("cannot substract " + amount + " from "
                             + self._balance)

        self._balance += amount

    def update_balance(self, transaction):
        """Updating balance according to a transaction"""
        for product in transaction.product_list:
            self.change_balance(-product.price)


if __name__ == "__main__":
    account = Account("Nikos", 200, 200)

from transaction import Transaction
from cost_types.base_type import Product
import datetime


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
        self.balance = balance
        self.transactions_per_date = {}

    def new_transaction(self):
        # TODO implement
        raise NotImplementedError()


if __name__ == "__main__":
    beer = Product("Beer", 3.5)                 # Creating a transaction
    pizza = Product("Pizza", 7)
    a_date = datetime.date(2018, 10, 2)
    a_product_list = [beer, pizza]
    a_transaction = Transaction(a_product_list, "friends", "in", a_date)

    coffee = Product("Coffee", 3)               # Creating a second transaction
    b_date = datetime.date(2018, 10, 1)
    b_product_list = coffee
    b_transaction = Transaction(b_product_list, "significant other", "out", b_date)

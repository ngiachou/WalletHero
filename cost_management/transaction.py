from .cost_types.base_type import Product
import datetime


class Transaction:
    """
    Takes the various costs(products) you had in a single day,
    as well as where, what time, and the environment -- friends, coleagues,
    etc.
    """
    def __init__(self, product_list, environment_characteristic, place, date):

        self.product_list = product_list
        self.environment_characteristic = environment_characteristic
        self.place = place
        self.date = date

    def __repr__(self):
        return "({}, {}, {}, {})".format(
            self.date,
            self.environment_characteristic,
            self.place,
            self.product_list
        )


if __name__ == "__main__":

    a_date = datetime.date(2018, 10, 2)  # creating a date

    beer = Product("Beer", 4.50)
    pizza = Product("Pizza", 7.00)

    a_product_list = [beer, pizza]  # inserting two products, created above

    # initializing a Transaction instance
    a_transaction = Transaction(a_product_list, "friends", "in", a_date)

    assert(a_transaction.environment_characteristic == "friends")
    assert(a_transaction.place == "in")
    assert(str(a_transaction.date) == "2018-10-02")
    assert(repr(a_transaction.product_list) == "[(Beer, 4.5), (Pizza, 7.0)]")
    print(a_transaction)

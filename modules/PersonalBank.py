from Transaction import Transaction
from Product import Product
import datetime

class PersonalBank:
    
    def __init__(self, balance, history_of_transactions):

        self.balance = balance
        self.history_of_transactions = history_of_transactions

    def add_transaction(transaction):

        return transaction

    def show_transaction_history(history_of_transactions):
        sorted_list = sorted(history_of_transactions, 
                key = lambda Transaction: Transaction.date)
        for i in sorted_list:
            print(i)

    def __repr__(self):
        
        return "({}, {})".format(self.balance, self.history_of_transactions)

if __name__ == "__main__":

    beer = Product("Beer", 3.5)
    pizza = Product("Pizza", 7)
    a_date = datetime.date(2018, 10, 2)
    a_product_list = [beer, pizza]
    a_transaction = Transaction(a_product_list, "friends", "in", a_date)

    coffee = Product("Coffee", 3)
    b_date = datetime.date(2018, 10, 1)
    b_product_list = coffee
    b_transaction = Transaction(b_product_list, "girlfriend", "out", b_date)

        
    my_transactions = [PersonalBank.add_transaction(b_transaction),
                        PersonalBank.add_transaction(a_transaction)]
    
    my_personal_bank = PersonalBank(350, my_transactions)

    PersonalBank.show_transaction_history(my_transactions)

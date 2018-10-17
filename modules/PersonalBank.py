from Transaction import Transaction
from Product import Product
import datetime


class PersonalBank:


    """
    Takes the users balance and his history of transactions.
    PersonalBank's methonds create and add a transaction into the list of 
    transactions (add_transaction) and return a list of transactions until
    now in chronological order (show_transaction_history).
    """

    
    def __init__(self, balance = 350):
        
        self.balance = balance
        self.history_of_transactions = []

    def add_transaction(self, transaction):

        self.history_of_transactions.append(transaction)  

    def get_transaction_history(self):
    
        sorted_list = sorted(self.history_of_transactions, 
                key = lambda Transaction: Transaction.date)
        return sorted_list

    def __repr__(self):
        
        return "{}".format(self.balance)
        
        
        
if __name__ == "__main__":

    beer = Product("Beer", 3.5)                 #Creating a transaction
    pizza = Product("Pizza", 7)
    a_date = datetime.date(2018, 10, 2)
    a_product_list = [beer, pizza]
    a_transaction = Transaction(a_product_list, "friends", "in", a_date)

    coffee = Product("Coffee", 3)               #Creating a second transaction
    b_date = datetime.date(2018, 10, 1)
    b_product_list = coffee
    b_transaction = Transaction(b_product_list, "significant other", "out", b_date)
    
    p1 = PersonalBank()
    p2 = PersonalBank(400)
    
    p1.add_transaction(a_transaction)
    p1.add_transaction(b_transaction) 
   
    print(p1.get_transaction_history())
    
    print(p1)                      #testing repr function

    assert(p2.balance == 400)      #testing if balance can take a value manually
    
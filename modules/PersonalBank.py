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

    
    def __init__(self, balance = None):      
        
        if balance == None:
            self.balance = 350
        else:
            self.balance = balance

    def add_transaction(history_of_transactions, transaction):

        history_of_transactions.append(transaction)

    def show_transaction_history(history_of_transactions):
    
        sorted_list = sorted(history_of_transactions, 
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
    
    a_history_of_transactions = []
    
    PersonalBank.add_transaction(a_history_of_transactions, a_transaction)
    PersonalBank.add_transaction(a_history_of_transactions, b_transaction) 
    
    a_personal_bank = PersonalBank()
    b_personal_bank = PersonalBank(400)
    
    print(PersonalBank.show_transaction_history(a_history_of_transactions))
    
    print(a_personal_bank)                      #testing repr function

    assert(b_personal_bank.balance == 400)      #testing if balance can take a value manually
    
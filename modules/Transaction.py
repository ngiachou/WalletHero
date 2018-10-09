from Product import Product
import datetime

"""Takes the various costs(products) you had in a single day,
	as well as where, what time, and the enviroment -- friends, coleagues, etc."""
class Transaction:
	def __init__(self, product_list, enviroment_characteristic, place, date):

		self.product_list = product_list
		self.enviroment_characteristic = enviroment_characteristic
		self.place = place
		self.date = date

	def __repr__(self):
		return "({}, {}, {}, {})".format(self.date, self.enviroment_characteristic, 
			self.place, self.product_list)


if __name__ == "__main__":

	a_date = datetime.date(2018, 10, 2) #creating a date

	beer = Product("Beer", 4.50)
	pizza = Product("Pizza", 7.00)

	a_product_list = [beer, pizza] #inserting two products, created above

	a_transaction = Transaction(a_product_list, "friends", "in", a_date) #initializing a Transaction instance


	assert(a_transaction.enviroment_characteristic == "friends")
	assert(a_transaction.place == "in")
	assert(str(a_transaction.date) == "2018-10-02")
	assert(repr(a_transaction.product_list) == "[(Beer, 4.5), (Pizza, 7.0)]")
	print(a_transaction)
from Product import Product
import datetime

"""Takes the various costs(products) you had in a single day,
	as well as where, what time, and the enviroment -- friends, coleagues, etc."""
class Transaction:
	def __init__(self, product_list, enviroment_characteristic, place, date):

		self.product_list = [Product(object)] #a list which takes products in type of Product
		self.enviroment_characteristic = enviroment_characteristic
		self.place = place
		self.date = date(a_date)

	print("\n---constructor begins---\n") #testing purposes

if __name__ == "__main__": #testing purposes
	print("------hello, main-------\n") #testing purposes

	beer = Product("Beer", 4.50)
	pizza = Product("Pizza", 7.00)

	a_product_list = [beer, pizza]

	a_transaction = Transaction(a_product_list, "friends", "in", "2018/10/02")
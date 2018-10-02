class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)


if __name__ == "__main__":

    beer = Product("Beer", 5.5)
    print(beer.name, " ", beer.price)
    print(type(beer.price))

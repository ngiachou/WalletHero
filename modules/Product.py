class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = float(price)

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price


if __name__ == "__main__":

    beer = Product("Beer", 5.5)
    assert(beer.name == "Beer")
    assert(beer.price == 5.5)
    print(beer)

class Product:
    def __init__(self, name, price:float):
        self.name = name
        self.price = float(price)
    
if __name__ == "__main__":
    
    beer = Product("Beer", 2)
    print(beer.name, " ", beer.price)
    print(type(beer.price))

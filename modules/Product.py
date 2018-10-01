class Product:
    def __init__(self, name, price:float):
        self.name = name
        self.price = float(price)
    
def main():     #Testing a signle Product
    
    beer = Product("Beer", 2)
    print(beer.name, " ", beer.price)
    print(type(beer.price))

if __name__ == "__main__":
    main()

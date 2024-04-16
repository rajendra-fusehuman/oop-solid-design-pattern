from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, product_name):
        self.product_name = product_name

    @abstractmethod
    def calculate_price(self):
        pass


class Laptop(Product):
    def __init__(self, price, discount):
        super(Laptop, self).__init__("Laptop")
        self.price = price
        self.discount = discount

    def calculate_price(self):
        return self.price - self.discount


class TV(Product):
    def __init__(self, price, discount):
        super(TV, self).__init__("TV")
        self.price = price
        self.discount = discount

    def calculate_price(self):
        return self.price - self.discount


class Monitor(Product):
    def __init__(self, price, discount):
        super(Monitor, self).__init__("Monitor")
        self.price = price
        self.discount = discount

    def calculate_price(self):
        return self.price - self.discount


def calculate_total_price(products):
    total_price = 0
    for product in products:
        total_price += product.calculate_price()
    return total_price

def main():
    products = [Laptop(100000, 5000), TV(50000, 3000), Monitor(22000, 0)]
    print("Total Price:", calculate_total_price(products))

if __name__ == '__main__':
    main()

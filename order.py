from customer import Customer
from coffee import Coffee


class Order:
    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        self._price = price

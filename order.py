from customer import Customer
from coffee import Coffee


class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError('must be a Customer instance!')
        self._customer = customer
        self._coffee = coffee
        self._price = price

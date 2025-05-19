from customer import Customer
from coffee import Coffee


class Order:

    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError('must be a Customer instance!')
        self._customer = customer
        if not isinstance(coffee, Coffee):
            raise TypeError('must be a Coffee instance!')
        self._coffee = coffee
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Must be a float between 1.0 and 10.0")
        self._price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

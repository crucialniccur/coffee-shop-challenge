from order import Order


class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # add validation with isinstance later
        self._name = value

    def orders(self):
        return [order for order in Order.all() if order.customer == self]

from order import Order


class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError(
                'name should be a string and greater than or equal to 3 chars ')

    @property
    def name(self):
        return self._name

    def orders(self):
        return [order for order in Order.all() if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

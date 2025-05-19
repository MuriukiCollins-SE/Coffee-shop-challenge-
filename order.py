class Order:
    _all_orders = []

    def __init__(self, customer, coffee, price):
        if not (hasattr(customer, "__class__") and customer.__class__.__name__ == "Customer"):
            raise TypeError("customer must be a Customer instance.")
        if not (hasattr(coffee, "__class__") and coffee.__class__.__name__ == "Coffee"):
            raise TypeError("coffee must be a Coffee instance.")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        if not (1.0 <= float(price) <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._customer = customer
        self._coffee = coffee
        self._price = float(price)
        Order._all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @classmethod
    def all(cls):
        return cls._all_orders
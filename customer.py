class Customer:
    def __init__(self, name):
        self.name = name 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be 1–15 characters long.")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order.all() if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        orders = [order for order in Order.all() if order.coffee == coffee]
        if not orders:
            return None
        spending = {}
        max_single_order = {}  # Track the highest single order price per customer
        for order in orders:
            customer = order.customer
            spending[customer] = spending.get(customer, 0) + order.price
            max_single_order[customer] = max(max_single_order.get(customer, 0), order.price)
        
        # Find the maximum total spending
        max_spending = max(spending.values())
        # Get all customers with the maximum total spending
        top_customers = [c for c, s in spending.items() if s == max_spending]
        
        # If there's a tie, select the customer with the highest single order price
        if len(top_customers) > 1:
            return max(top_customers, key=lambda c: (max_single_order[c], c.name))
        
        return top_customers[0]
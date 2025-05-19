# Coffee Shop Challenge

A simple Python OOP project to model a coffee shop with Customers, Coffees, and Orders.

## Features

- **Customer**: Name validation, order creation, and coffee tracking.
- **Coffee**: Name validation, order and customer tracking, order statistics.
- **Order**: Links a customer and a coffee with a price, enforces type and range.
- **Relationships**: Query all orders for a customer or coffee, unique coffees/customers, and most aficionado customer for a coffee.

## Requirements

- Python 3.7+
- [pytest](https://pytest.org/) for running tests

## Project Structure

```
Coffee-Shop/
├── customer.py
├── coffee.py
├── order.py
├── tests/
│   ├── customer_test.py
│   ├── coffee_test.py
│   └── order_test.py
├── README.md
└── Pipfile
```

## Running Tests

From the project root or `Coffee-Shop` directory, run:

```sh
pytest tests

```

## Usage Example

```python
from customer import Customer
from coffee import Coffee
from order import Order

alice = Customer("Alice")
latte = Coffee("Latte")
order = alice.create_order(latte, 4.5)
print(order.customer.name)  
print(order.coffee.name)    
```

## License

MIT License
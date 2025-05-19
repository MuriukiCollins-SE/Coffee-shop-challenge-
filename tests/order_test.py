import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

@pytest.fixture(autouse=True)
def clear_orders()
    Order._all_orders.clear()

def test_customer_name_validation():
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("a" * 16)
    c = Customer("Alice")
    assert c.name == "Alice"

def test_coffee_name_validation():
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("ab")
    c = Coffee("Latte")
    assert c.name == "Latte"

def test_order_creation_and_properties():
    cust = Customer("Bob")
    cof = Coffee("Mocha")
    order = Order(cust, cof, 5.0)
    assert order.customer is cust
    assert order.coffee is cof
    assert order.price == 5.0

def test_order_price_validation():
    cust = Customer("Bob")
    cof = Coffee("Mocha")
    with pytest.raises(TypeError):
        Order(cust, cof, "expensive")
    with pytest.raises(ValueError):
        Order(cust, cof, 0.5)
    with pytest.raises(ValueError):
        Order(cust, cof, 20.0)

def test_customer_orders_and_coffees():
    alice = Customer("Alice")
    bob = Customer("Bob")
    latte = Coffee("Latte")
    mocha = Coffee("Mocha")
    o1 = alice.create_order(latte, 3.0)
    o2 = alice.create_order(mocha, 4.0)
    o3 = bob.create_order(latte, 5.0)
    assert set(alice.orders()) == {o1, o2}
    assert set(alice.coffees()) == {latte, mocha}
    assert set(latte.customers()) == {alice, bob}
    assert set(latte.orders()) == {o1, o3}

def test_coffee_num_orders_and_average_price():
    alice = Customer("Alice")
    bob = Customer("Bob")
    latte = Coffee("Latte")
    assert latte.num_orders() == 0
    assert latte.average_price() == 0
    alice.create_order(latte, 4.0)
    bob.create_order(latte, 6.0)
    assert latte.num_orders() == 2
    assert latte.average_price() == 5.0

def test_most_aficionado():
    alice = Customer("Alice")
    bob = Customer("Bob")
    latte = Coffee("Latte")
    mocha = Coffee("Mocha")
    assert Customer.most_aficionado(latte) is None
    alice.create_order(latte, 4.0)
    bob.create_order(latte, 6.0)
    alice.create_order(latte, 2.0)
    assert Customer.most_aficionado(latte) == bob
    alice.create_order(latte, 10.0)
    assert Customer.most_aficionado(latte) == alice
    assert Customer.most_aficionado(mocha) is None

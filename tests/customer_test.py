import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

@pytest.fixture(autouse=True)
def clear_orders():
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

def test_create_order_links_customer():
    alice = Customer("Alice")
    latte = Coffee("Latte")
    order = alice.create_order(latte, 4.5)
    assert order.customer is alice
    assert order.coffee is latte

def test_most_aficionado():
    alice = Customer("Alice")
    bob = Customer("Bob")
    latte = Coffee("Latte")
    assert Customer.most_aficionado(latte) is None
    alice.create_order(latte, 4.0)
    bob.create_order(latte, 6.0)
    alice.create_order(latte, 2.0)
    assert Customer.most_aficionado(latte) == bob
    alice.create_order(latte, 10.0)
    assert Customer.most_aficionado(latte) == alice

#https://pybit.es/pytest-fixtures.html

import pytest
from time import sleep

from groceries import Groceries, Item

@pytest.fixture(scope="session")
def cart():
    """Setup code to create a groceries cart object with 6 items in it """
    sleep(1)
    products = 'celery apples water coffee chicken pizza'.split()
    prices = [1, 4, 2, 5, 6, 4]
    cravings = False, False, False, False, False, True

    items = []
    for item in zip(products, prices, cravings):
        items.append(Item(*item))

    return Groceries(items)
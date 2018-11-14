#https://pybit.es/pytest-fixtures.html

from copy import deepcopy
import pytest
from groceries import Item, DuplicateProduct, MaxCravingsReached

def test_add_item(cart):
    cart = deepcopy(cart)
    oranges = Item(product = 'oranges', price = 3, craving = False)
    cart.add(oranges)

    assert len(cart) == 7
    assert cart[-1].product == 'oranges'
    assert cart[-1].price == 3 
    assert cart.due == 25
    assert not cart.num_cravings_reached

def test_add_item_duplicate(cart):
    cart = deepcopy(cart)
    apples = Item(product = 'apples', price = 4, craving=False)
    with pytest.raises(DuplicateProduct):
        cart.add(apples)

def test_add_item_max_cravings(cart):
    cart = deepcopy(cart)
    chocolate = Item('chocolate', 2, True)
    cart.add(chocolate)
    assert cart.num_cravings_reached

    croissants = Item(product='croissants', price=3, craving=True)
    with pytest.raises(MaxCravingsReached):
        cart.add(croissants) 

def test_delete_item(cart):
    cart = deepcopy(cart)
    # not in collection
    croissant = 'croissant'
    with pytest.raises(IndexError):
        cart.delete(croissant)

    # in collection
    assert len(cart) == 6
    apples = 'apples'
    cart.delete(apples)
    # new product at this index
    assert len(cart) == 5
    assert cart[1].product == 'water'
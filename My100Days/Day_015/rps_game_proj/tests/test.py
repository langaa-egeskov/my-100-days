from rps15 import rps15
import pytest
from unittest.mock import patch

#May put all fixtures in conftest.py file

@patch("builtins.input", side_effect=['Zeke the Wizard'])
def test_get_player1_name(input):
    name = rps15.get_player1_name()
    assert name == 'Zeke the Wizard'

def test_get_random_throw():
    assert 1 == 1

def test_get_player1_throw(throws, a_throw):
    assert rps15.get_player1_throw(throws) == a_throw

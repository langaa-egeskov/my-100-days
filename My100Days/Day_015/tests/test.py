from .context import rps15
import pytest
from unittest.mock import patch

#May put all fixtures in conftest.py file

@patch("builtins.input", side_effect=['Zeke the Wizard'])
def test_get_player1_name(input):
    name = get_player1_name()
    assert name == 'Zeke the Wizard'

def test_get_random_throw():
    pass

def test_get_player1_throw(a_throw.name):
    assert get_player1_throw == a_throw

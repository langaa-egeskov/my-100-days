from .context import rps15
from rps15.throws import Throw
from rps15.players import Player
from rps15.rps15 import build_throws, get_player1_name, get_player1_throw
from rps15.rps15 import print_header, player_rounds, get_random_throw
import pytest
from unittest.mock import patch

#May put all fixtures in conftest.py file

@patch("builtins.input", side_effect=['Zeke the Wizard'])
def test_get_player1_name(input):
    name = get_player1_name()
    assert name == 'Zeke the Wizard'

def test_get_random_throw():
    assert 1 == 1

def test_get_player1_throw(throws, a_throw):
    assert get_player1_throw(throws) == a_throw

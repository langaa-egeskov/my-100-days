from throws import Throw
from players import Player
from rps import print_header, build_3_possible_throws, get_player1_name
from rps import get_player1_throw
from unittest.mock import patch
import pytest
import random

def test_Throw():
    item = 'Dragon'
    can_defeat = ['Eagle', 'Sheep']
    dragon = Throw(item, can_defeat)
    eagle = Throw('Eagle',[])
    sheep = Throw('Sheep',[])
    kracken = Throw('Kracken',[])
    assert dragon.name == 'Dragon'
    assert dragon.can_defeat(kracken) == False
    assert dragon.can_defeat(sheep) == True
    assert dragon.can_defeat(eagle) == True


def test_Player():
    name = "Sally"
    player = Player("Sally")
    assert player.name == "Sally"
    assert player.wins == 0
    player.wins += 1
    assert player.wins == 1

def test_print_header():
    pass

def build_3_possible_throws():
    pass

def get_player1_name():
    pass

def get_player1_throw():
    pass

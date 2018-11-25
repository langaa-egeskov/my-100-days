from rps.throws import Throw
from rps.players import Player
from rps.rps import print_header, build_3_possible_throws, get_player1_name
from rps.rps import get_player1_throw
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

def test_print_header(capfd):  #capfd
    print_header()
    output, err = capfd.readouterr()
    expected = ['--------------------------------------------------',
                '               Rock, Paper, Scissors              ',
                '--------------------------------------------------']
    output = output.split('\n')
    for out, exp in zip(output, expected):
        assert out == exp

def test_build_3_possible_throws():
    throws = build_3_possible_throws()
    assert throws['Rock'].name == 'Rock'
    assert throws['Rock'].defeated_throws == ['Scissors']
    assert throws['Paper'].name == 'Paper'
    assert throws['Paper'].defeated_throws == ['Rock']
    assert throws['Scissors'].name == 'Scissors'
    assert throws['Scissors'].defeated_throws == ['Paper']

@patch("builtins.input", side_effect = ["Harry the Great  "])
def test_get_player1_name(inp):
    name = get_player1_name()
    assert name == "Harry the Great"
    
@pytest.fixture
def throws():
    return build_3_possible_throws()
    

# @pytest.mark.parametrize("test_input, expected", [
#     ('r', 'Rock' ),
#     ('p', 'Paper'),
#     ('s', 'Scissors')])
# def test_get_player1_throw_valid(throws, test_input, expected):
#     assert get_player1_throw(throws).name == expected
    

# @pytest.mark.parametrize("test_input, expected", [
#     ('rps',"""** Please enter a single letter: 'r' for rock, 'p' for paper,
#                       or 's' for scissiors **"""),
#     ('None', """** Please enter a single letter: 'r' for rock, 'p' for paper,
#                       or 's' for scissiors **""")])
# def test_get_player1_throw_invalid(throws, test_input, expected, capfd):
#     get_player1_throw(throws)                    
#     output, err = capfd.readouterr()
#     assert output == expected
    
    
# this is main   
def test_game():
    pass
from rps.throws import Throw
from rps.players import Player
from rps.rps import print_header, build_3_possible_throws, get_player1_name
from rps.rps import get_player1_throw
from unittest.mock import patch


def test_Throw():
    item = 'Dragon'
    can_defeat = ['Eagle', 'Sheep']
    dragon = Throw(item, can_defeat)
    eagle = Throw('Eagle', [])
    sheep = Throw('Sheep', [])
    kracken = Throw('Kracken', [])
    assert dragon.name == 'Dragon'
    assert dragon.can_defeat(kracken) is False
    assert dragon.can_defeat(sheep) is True
    assert dragon.can_defeat(eagle) is True


def test_Player():
    player = Player("Sally")
    assert player.name == "Sally"
    assert player.wins == 0
    player.wins += 1
    assert player.wins == 1


def test_print_header(capfd):
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


@patch("builtins.input", side_effect=["Harry the Great  "])
def test_get_player1_name(inp):
    name = get_player1_name()
    assert name == "Harry the Great"

# My fixture did not work; had to fake it
# @pytest.fixture
# def throws():
#     return build_3_possible_throws()


@patch("builtins.input", side_effect=['r', 'p', 's'])
def test_get_player1_throw_valid(inp, throws=build_3_possible_throws()):
    expected = 'Rock'
    assert get_player1_throw(throws).name == expected
    expected = 'Paper'
    assert get_player1_throw(throws).name == expected
    expected = 'Scissors'
    assert get_player1_throw(throws).name == expected


@patch("builtins.input", side_effect=['rps', 'r', None, 'r'])
def test_get_player1_throw_invalid(inp, capfd,
                                   throws=build_3_possible_throws()):
    get_player1_throw(throws)
    output, _ = capfd.readouterr()
    expected = ("** Please enter a single letter: " +
                "'r' for rock, 'p' for paper, or 's' for scissiors **")
    output = output.split('\n')
    output = output[1] + output[2]

    assert output == expected


# Not really sure I can patch my random.choice function
# since it needs to return a specific throw object
# @patch("builtins.input", side_effect = [])
# @patch.object(random, 'choice')
# def test_game():
#     pass
#  pass

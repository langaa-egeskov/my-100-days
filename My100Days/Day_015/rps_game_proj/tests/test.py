from rps15 import (
    Player,
    Throw,
    bt_df,
    print_header,
    build_throws,
    get_player1_name,
    get_random_throw,
    get_player1_throw,
    player_rounds,
    game
)
import pytest
import random
from unittest.mock import patch


# Test the classes
def test_Player():
    player = Player("Sally")
    assert player.name == "Sally"
    assert player.wins == 0
    player.wins += 1
    assert player.wins == 1


def test_Throw():
    item = 'Seagull'
    can_defeat = ['Snail', 'Hermit Crab']
    seagull = Throw(item, can_defeat)
    snail = Throw('Snail', [])
    hermit_crab = Throw('Hermit Crab', [])
    kracken = Throw('Kracken', [])
    assert seagull.name == 'Seagull'
    assert seagull.can_defeat(kracken) is False
    assert seagull.can_defeat(snail) is True
    assert seagull.can_defeat(hermit_crab) is True


# Define a helper function
def equivalent_throw(throw1, throw2):
    cond1 = (throw1.name  == throw2.name)
    cond2 = (throw1.defeated_throws == throw2.defeated_throws)
    return cond1 and cond2


# Test the functions
def test_print_header(capfd):
    print_header()
    output, err = capfd.readouterr()
    expected = ['--------------------------------------------------',
                '        15 Way: Rock, Paper, Scissors             ',
                '--------------------------------------------------']
    output = output.split('\n')
    for out, exp in zip(output, expected):
        assert out == exp


def test_build_throws(data_frame_from_csv, a_throw):
    throws = build_throws(data_frame_from_csv)
    assert throws[a_throw.name].name == a_throw.name
    assert len(throws[a_throw.name].defeated_throws) == 7


@patch("builtins.input", side_effect=['Zeke the Wizard'])
def test_get_player1_name(input):
    name = get_player1_name()
    assert name == 'Zeke the Wizard'


@patch.object(random, 'choice')
def test_get_random_throw(m, throws, a_num):
    m.return_value = a_num
    num_throw = {i:throw for i, throw in enumerate(throws)}
    expected = num_throw[a_num]
    assert get_random_throw(throws).name == expected


def test_get_player1_throw_a_throw(throws, a_throw, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x : a_throw.name)
    assert equivalent_throw(get_player1_throw(throws), a_throw)

def test_get_player1_throw_a_throw_lower(throws, a_throw, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x : a_throw.name.lower())
    assert equivalent_throw(get_player1_throw(throws), a_throw)


def test_get_player1_throw_2_letter(throws, a_throw, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x : a_throw.name[:2])
    assert equivalent_throw(get_player1_throw(throws), a_throw)

def test_get_player1_throw_2_letter_lowere(throws, a_throw, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x : a_throw.name[:2].lower())
    assert equivalent_throw(get_player1_throw(throws), a_throw)
    

def test_player_rounds():
    pass


def test_game():
    pass
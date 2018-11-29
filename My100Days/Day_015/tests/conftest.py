from .context import rps15
from rps15.throws import Throw
from rps15.players import Player
from rps15.rps15 import build_throws, get_player1_name, get_player1_throw
from rps15.rps15 import print_header, player_rounds, get_random_throw
import pytest
import pandas as pd
from unittest.mock import patch

#May put all fixtures in conftest.py file
# This is all so messy
# seems like I shouldnt need 2 copies of the csv file
# one in tests and one in the rps15 file
# TODO check out the link
# link = 'https://github.com/cod3monk3y/' + '
#        'PyImports/blob/master/myimports/tests/test_abs.py'

path_to_csv = r'../rps15/battle-table.csv'
bt_df = pd.read_csv(path_to_csv, index_col = 0)

@pytest.fixture()
def throws():
    throws = build_throws(bt_df) 
    return throws

throw_list = build_throws(bt_df)

@pytest.fixture(params=throw_list)
def a_throw(request):
    return request.param

@pytest.fixture()
def throw_proper_names(throws):
    return [throw.name for throw in throws]

@pytest.fixture()
def throw_2_letter(throw_proper_names):
    return [name[:2] for name in throw_proper_names]

@pytest.fixture()
def throw_2_letter_lower(throw_proper_names):
    return [name[:2].lower for name in throw_proper_names]

    
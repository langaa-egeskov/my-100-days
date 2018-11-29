# -*- coding: utf-8 -*-

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
import pandas as pd
from unittest.mock import patch

@pytest.fixture()
def data_frame_from_csv():
    return(bt_df)

@pytest.fixture()
def throws():
    throws = build_throws(bt_df) 
    return throws

throw_dict = build_throws(bt_df)
defeated_dict = { k : v.defeated_throws for k, v in throw_dict.items()}

@pytest.fixture(params=throw_dict.values())
def a_throw(request):
    return request.param

@pytest.fixture(params=defeated_dict.values())
def a_defeated_throws_list(request):
    return request.param

@pytest.fixture(params=list(range(15)))
def a_num(request):
    return request.param



if __name__ == '__main__':
    main()
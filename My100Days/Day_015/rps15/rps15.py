from throws import Throw
from players import Player
import pandas as pd
import random

def main():
    print_header()
    bt_df = pd.read_csv('battle-table.csv', index_col = 0)
    throws = build_throws(bt_df)  #battle-table dataframe
    name = get_player1_name()
    player1 = Player(name)
    player2 = Player('Computer')
    player_rounds(player1, player2, throws)


def print_header():
    print('--------------------------------------------------')
    print('        15 Way: Rock, Paper, Scissors             ')
    print('--------------------------------------------------')


def build_throws(bt_df):
    '''Dict of throws that the throw can defeat in the form
       "Throw" : Throw('Throw', [list of can defeats])
    '''
    win = 'win'

    can_defeat_dict = {}
    for attacker in bt_df.index:
        can_defeat_list = []
        for opponent in bt_df.columns:
            outcome = bt_df[opponent][attacker]
            if outcome == win:
                can_defeat_list.append(opponent)
        can_defeat_dict[attacker] = can_defeat_list
    
    throws_dict = {}
    for attacker, can_defeat_list in can_defeat_dict.items():
        throws_dict[attacker] = Throw(attacker, can_defeat_list)
    return throws_dict


def get_player1_name():
    name = input('What is your name? ')
    print()
    return str(name.strip())


def get_random_throw(throws):
    throw_by_num = {}
    for i, name_of_throw in enumerate(throws):
        throw_by_num[i]= name_of_throw
    # choosing to write it this way so it is easier to mock the random fx
    num_of_throw = random.choice(list(range(len(throw_by_num))))
    return throws[throw_by_num[num_of_throw]]


def get_player1_throw(throws):
    string = 'Please type your throw: \n'
    for throw in throws:
        string += f'\t[{throw[:2].lower()}]{throw[2:]}\n'
    string += 'Enter your throw:  '
    pick = (input(string).lower()).capitalize()
    
    choice = [(k, v) for k, v in throws.items() if pick[:2] == k[:2]]
    error_string = "\nType the first two letters of the throw you wish to choose.\n"
    error_string += "Or you may type 'q' to quit.\n"
    quit_string = "Quitting the game, thanks for playing."
    
    if choice:
        try: 
            len(choice) == 1
            print(f'You choose {choice[0][0]}\n')
            return choice[0][1]
        except ValueError:
            print(error_string)
            get_player1_throw()
    elif pick == 'quit' or pick == 'q':
        print(quit_string)
        return
    else:
        print(error_string)
        get_player1_throw(throws)


def player_rounds(player1, player2, throws):
    count = 1
    decisive_rounds = 0

    while decisive_rounds < 3 and player1.wins < 2 and player2.wins < 2:
        player2_throw = get_random_throw(throws)
        player1_throw = get_player1_throw(throws)

        player1_win = player1_throw.can_defeat(player2_throw)
        player2_win = player2_throw.can_defeat(player1_throw)

        if player1_win:
            winner = player1
        elif player2_win:
            winner = player2
        elif not player1_win and not player2_win:
            winner = None

        print(f'Round {count}')
        print(f'_____________')
        print(f'{player1.name} threw a {player1_throw.name}')
        print(f'{player2.name} threw a {player2_throw.name}')
        print()

        try:
            print(f'The winner for this round is {winner.name}')
            winner.wins += 1
            decisive_rounds += 1
        except (AttributeError):
            print(f'This round had no winner and is a tie round')

        print()
        count += 1

    if player1.wins > player2.wins:
        overall_winner = player1
    elif player2.wins > player1.wins:
        overall_winner = player2

    print(f'{overall_winner.name} is the winner!')
    print(('{0} won {1} out of {2} rounds that did not end in tie'
           .format(overall_winner.name, overall_winner.wins, decisive_rounds)))

if __name__ == '__main__':
    main()

from rps.throws import Throw
from rps.players import Player
import random


def main():
    print_header()
    throws = build_3_possible_throws()
    name = get_player1_name()
    player1 = Player(name)
    player2 = Player('Computer')
    game_loop(player1, player2, throws)


def print_header():
    print('--------------------------------------------------')
    print('               Rock, Paper, Scissors              ')
    print('--------------------------------------------------')
    return


def build_3_possible_throws():
    Rock = Throw('Rock', ['Scissors'])
    Paper = Throw('Paper', ['Rock'])
    Scissors = Throw('Scissors',  ['Paper'])
    return {'Rock': Rock, 'Paper': Paper, 'Scissors': Scissors}


def get_player1_name():
    name = input('What is your name? ')
    print()
    return str(name.strip())


def get_player1_throw(throws):
    pick = input('Pick [r]ock, [p]aper, or [s]cissors: ')
    print()

    if pick not in ['r', 'p', 's'] or pick is None:
        print("""** Please enter a single letter: 'r' for rock, 'p' for paper,
                      or 's' for scissiors **""")
        return get_player1_throw(throws)
    elif pick == 'r':
        return throws['Rock']
    elif pick == 'p':
        return throws['Paper']
    elif pick == 's':
        return throws['Scissors']


def game_loop(player1, player2, throws):
    count = 1
    decisive_rounds = 0

    while decisive_rounds < 3 and player1.wins < 2 and player2.wins < 2:
        player2_throw = random.choice([throw for throw in throws.values()])
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

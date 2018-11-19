from actors import Creature, Wizard, Dragon
import random


def main():
    print_header()
    game_loop()


def print_header():
    print('------------------------------------------------------')
    print('                     WIZARD GAME                      ')
    print('------------------------------------------------------')
    print()


def game_loop():

    creatures = [
        Creature('Bat', 5),
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Dragon('Black Dragon', 50, scaliness=2, breathes_fire=False),
        Wizard('Evil Wizard', 1000)
    ]


    hero = Wizard('Gandolf', 75)

    while True:

        # Randomly choose a creature
        active_creature = random.choice(creatures)

        print('A {} of level {} has appeared from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?: ')
        print()
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                print('The wizard defeated {}'.format(active_creature.name))
            else:
                print('The wizard has been dealt a defeat')
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!!!')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'
                  .format(hero.name))
            for c in creatures:
                print(" *  {} of level {}".format(c.name, c.level))
        else:
            print('Ok, exiting game...bye!')
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

        print()


if __name__ == '__main__':
        main()

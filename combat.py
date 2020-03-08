import random
import monster
import game


def combat(character):
    enemy = monster.get_monster()


def roll_for_initiative():
    """
    Roll an initiative.

    This function uses decomposition as it uses a helper function.  It is also part of the decomposition process of a
    combat round.
    :precondition: No parameters are inputted into the function.
    :postcondition: Will decide who goes first.
    :return: A boolean value if someone goes first or not.
    """
    while True:
        roll_1 = game.roll_die(1, 20)
        roll_2 = game.roll_die(1, 20)
        if roll_1 > roll_2:
            return True
        if roll_2 > roll_1:
            return False

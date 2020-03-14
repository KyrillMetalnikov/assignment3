"""Run combat functions for the game"""
import monster
import game


def start_combat(character):
    """
    Run an instance of combat.
    :param character: A dictionary representing a character.
    :precondition: Provide the function with a proper argument as stated in the param above.
    :postcondition: The character will fight a monster until one of them dies.
    """
    enemy = monster.get_monster()
    player_first = roll_for_initiative()
    while game.is_alive(enemy) and game.is_alive(character):
        if player_first:
            combat_round(character, enemy)
        else:
            combat_round(enemy, character)
    if game.is_alive(character):
        print("You outlasted your instructor!")
        character["in_combat"] = False
        game.play(character)
    else:
        print("Game over!  You did not manage to survive school.")


def flee(character):
    character["in_combat"] = False
    roll = game.roll_die(1, 10)
    if roll == 1:
        damage = game.roll_die(1, 4)
        character["HP"][0] -= damage
        print("You were late to a pop-quiz and got a 0! Lose " + str(damage) + " sanity.")
    else:
        print("You managed to falsify a doctors note and got excused from class!")
    if game.is_alive(character):
        game.play(character)
    else:
        print("Game over!  You did not manage to survive school.")


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


def combat_round(attacker, defender):
    """
    Do a round of combat between two fighters.
    This function uses decomposition by using a wide variety of helper functions.  It also uses pattern matching by
    demonstrating that multiple attacks are all processed in the exact same way, and so shortens the function. It also
    uses an algorithm to determine if a character is still alive (also using a helper function) in order to continue the
    function if necessary.
    :param attacker: A properly formatted character dictionary.
    :param defender: A different properly formatted character dictionary.
    :precondition: The two parameters must be two different properly formatted characters.
    """
    single_attack(attacker, defender)  # opponent 1 attacks opponent 2
    if game.is_alive(defender):  # if opponent 2 survived, opponent 2 retaliates
        single_attack(defender, attacker)


def single_attack(attacker, defender):
    """
    Complete a single attack attempt.
    This function uses an algorithm to determine what message to display on screen (whether the attack hit, missed or
    killed).  It also uses decomposition by using various helper functions.  It also demonstrates abstraction as it can
    be used with any two character objects.
    :param attacker: A properly formatted character dictionary.
    :param defender: A properly formatted character dictionary.
    :precondition: Both params must be different characters that are properly formatted.
    :postcondition: A single attack will be properly completed.
    """
    attack_attempt = game.roll_die(1, 20)
    if "type" in attacker:
        print(attacker['attack'])
    else:
        print(attacker['name'] + " sniffled in class!")
    if attack_attempt > 8:
        damage = game.roll_die(1, 6)
        defender["HP"][1] -= damage
        if game.is_alive(defender):
            print(defender["name"] + " is going crazy and loses " + str(damage) + " sanity!\n")
        else:
            print(attacker["name"] + " hits " + defender["name"]
                  + " where it hurts and causes them to lose " + str(damage) + " sanity. " + defender["name"]
                  + " has finally lost it and went completely insane.\n")
    else:
        print(defender["name"] + " is living in denial! " + defender["name"] + " doesn\'t lose any sanity!\n")

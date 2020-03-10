"""Run combat functions for the game"""
import monster
import game


def combat(character):
    """
    Run an instance of combat.

    :param character: A dictionary representing a character.
    :precondition: Provide the function with a proper argument as stated in the param above.
    :postcondition: The character will fight a monster until one of them dies.
    """
    enemy = monster.get_monster()
    goes_first = roll_for_initiative()
    while game.is_alive(enemy) and game.is_alive(character):
        if goes_first:
            combat_round(character, enemy)
        else:
            combat_round(enemy, character)


def flee(character):
    roll = game.roll_die(1, 10)
    if roll > 1:
        game.play(character)
    else:
        character["HP"][0] -= 2


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


def combat_round(opponent_one, opponent_two):
    """
    Do a round of combat between two fighters.

    This function uses decomposition by using a wide variety of helper functions.  It also uses pattern matching by
    demonstrating that multiple attacks are all processed in the exact same way, and so shortens the function. It also
    uses an algorithm to determine if a character is still alive (also using a helper function) in order to continue the
    function if necessary.
    :param opponent_one: A properly formatted character dictionary.
    :param opponent_two: A different properly formatted character dictionary.
    :precondition: The two parameters must be two different properly formatted characters.
    """
    single_attack(opponent_one, opponent_two)  # opponent 1 attacks opponent 2
    if game.is_alive(opponent_two):  # if opponent 2 survived, opponent 2 retaliates
        single_attack(opponent_two, opponent_one)

    single_attack(opponent_two, opponent_one)  # if roll_for_initiative returns false: opponent 2 attacks first
    if game.is_alive(opponent_one):
        single_attack(opponent_one, opponent_two)


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
    if attack_attempt > defender["HP"[0]]:
        if 'type' in attacker:
            print(attacker['attack'])
        damage = game.roll_die(1, 6)
        defender["HP"][1] -= damage
        if game.is_alive(defender):
            print(defender["Name"] + " took the hit like a real champ but still took " + str(damage) + " damage!\n")
        else:
            print(attacker["Name"] + " hits " + defender["Name"]
                  + " for " + str(damage) + " damage. " + defender["Name"]
                  + " never stood a chance and now lies dead.\n")
    else:
        print(attacker["Name"] + " misses entirely! " + defender["Name"] + " says: Dude are you even trying?\n")
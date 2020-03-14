import game


def movement(direction, character):
    """
    Update the character position depending on user input and randomly trigger encounters.
    There is a 25% chance that the user encounters combat. If the user does not encounter combat, the user heals health.
    :param direction: a string representing a cardinal direction.
    :param character: a dictionary representing a game character.
    :precondition: provide the function with valid arguments according to the PARAM statements above.
    :postcondition: trigger combat or healing, then allow the user to continue with the game.
    :param character: a dictionary representing a character with a position key.
    """
    horizontal_movement = {"e": 1, "w": -1}
    vertical_movement = {"s": 1, "n": -1}
    if direction in horizontal_movement:
        character["position"][0] += horizontal_movement[direction]
    else:
        character["position"][1] += vertical_movement[direction]
    if game.roll_die(1, 4) > 1:
        heal(character)
        game.play(character)
    else:
        character["in_combat"] = True
        game.play(character)


def heal(character):
    """
    Heal a character for two hit points, up to the hit point maximum.
    :param character: a dictionary representing a game character.
    :precondition: provide the function with a valid argument according to the PARAM statement above.
    :postcondition: update the character's hit points.
    """
    if character["HP"][1] + 2 >= character["HP"][0]:
        character["HP"][1] = character["HP"][0]
    else:
        character["HP"][1] += 2


def user_options(character):
    """
    Generate and return a list of options that a user can take depending on the state of the game.
    :param character: a dictionary representing a game character.
    :precondition: provide the function with a valid argument according the PARAM statement above.
    :postcondition: return an object as defined by the return statement below.
    :return: a list of strings representing the options a user can currently take.
    >>> user_options({"in_combat": True, "position": [4, 3]})
    ['quit', 'fight', 'flee']
    >>> user_options({"in_combat": False, "position": [0, 0]})
    ['quit', 'e', 's']
    >>> user_options({"in_combat": False, "position": [4, 4]})
    ['quit', 'w', 'n']
    >>> user_options({"in_combat": False, "position": [2, 1]})
    ['quit', 'e', 'w', 's', 'n']
    """
    options = ["quit"]
    if character["in_combat"]:
        options.append("fight")
        options.append("flee")
    else:
        if character["position"][0] < 4:
            options.append("e")
        if character["position"][0] > 0:
            options.append("w")
        if character["position"][1] < 4:
            options.append("s")
        if character["position"][1] > 0:
            options.append("n")
    return options

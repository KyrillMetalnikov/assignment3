import random
import map_movement
import combat


def roll_die(number_of_rolls, number_of_sides):
    """
    Simulate rolling dice with a chosen number of sides a chosen number of times.
    :param number_of_rolls: a positive integer representing the number of times the dice should be rolled.
    :param number_of_sides: a positive integer representing the number of sides the dice have.
    :precondition: provide valid arguments to the function as defined by the PARAM statements above.
    :postcondition: return an object as defined by the return statement below.
    :return: a positive integer representing the sum of the dice rolls.
    >>> roll_die(1, 1)
    1
    >>> roll_die(15, 1)
    15
    >>> roll_die(9999, 1)
    9999
    """
    dice_sum = 0
    for i in range(number_of_rolls):
        dice_sum += random.randint(1, number_of_sides)
    return dice_sum


def is_alive(character):
    """
    Determine if a character is alive (1 or more current HP).
    :param character: a dictionary representing a game character.
    :precondition: provide the function with a valid argument according to the PARAM statement above.
    :postcondition: return an object as defined by the return statement below.
    :return: a boolean value representing whether or not the character is alive.
    """
    if character["HP"][1] <= 0:
        print(character["name"] + " has died!")
        alive = False
    else:
        print(character["name"] + " has " + str(character["HP"][1]) + " HP left!")
        alive = True
    return alive


def play(character):
    """
    Trigger game functions based on user input.
    :param character: a dictionary representing a game character.
    :precondition: provide the function with valid arguments according to the PARAM statement above.
    :postcondition: continue the game as directed by user input.
    """
    print(character)
    options = map_movement.user_options(character)
    print(options)  # this will need to be more user friendly
    user_input = input("What will you do?").strip().lower()
    while user_input not in options:
        print(options)  # this will need to be more user friendly
        user_input = input("That is not a valid option, please pick a game option!").strip().lower()
    user_commands = {"quit": print,
                     "flee": combat.flee, "fight": combat.start_combat,
                     "e": map_movement.movement, "w": map_movement.movement,
                     "n": map_movement.movement, "s": map_movement.movement}
    if len(user_input) == 1:
        user_commands[user_input](user_input, character)
    elif user_input == "quit":
        user_commands[user_input]("Game over!  You did not manage to survive school.")
    else:
        user_commands[user_input](character)


def game_start():
    """
    Initialize a character and start the game.
    :precondition: provide the function with no arguments.
    :postcondition: initialize a character and start a game.
    """
    character = {"name": input("Please enter your character name!"),
                 "HP": [10, 10],
                 "position": [2, 2],
                 "in_combat": False}
    play(character)


def main():
    game_start()


if __name__ == "__main__":
    main()
import random
import map_movement


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
    options = map_movement.user_options(character)
    print(options)  # this will need to be more user friendly
    user_input = input("What will you do?").strip().lower()
    while user_input not in options:
        user_input = input("That is not a valid option, please pick a game option!").strip().lower()
        print(options)  # this will need to be more user friendly
    user_commands = {"quit": quit_game(character), "fight": combat(character), "flee": flee(character),
                     "e": map_movement.movement("e", character), "w": map_movement.movement("w", character),
                     "n": map_movement.movement("n", character), "s": map_movement.movement("s", character)}
    user_commands[user_input]
    #  this actually works, and will activate the relevant function based on the the user_input.


def game_start():
    # welcome message, maybe a function?
    character = {"name": input("Please enter your character name!"),
                 "position": [2, 2],
                 "in_combat": False}
    health = 6 + roll_die(1, 6)
    character["HP"] = [health, health]
    play(character)


def main():
    game_start()


if __name__ == "__main__":
    main()

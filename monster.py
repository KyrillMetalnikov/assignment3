import game
import random


def get_monster():
    random_list = [get_chris(), get_amir(), get_janitor(), get_frank()]
    return random.choices(random_list, weights=[1, 25, 25, 25])


def get_amir():
    return {'HP': 10, 'name': 'Amir', 'attack': 'Amir rolls your name on his magic device!'}


def get_chris():
    return {'HP': 1000, 'name': 'Chris', 'attack': 'Chris says "see?  wasn\'t so hard was it?"'}


def get_janitor():
    return {'HP': 10, 'name': 'Jan-Itor', 'attack': 'Jan-Itor removes all paper towels from the sixth floor!'}


def get_frank():
    return {'HP': 10, 'name': 'Frank', 'attack': 'Frank assigns an assignment that\'s 100% fun!'}


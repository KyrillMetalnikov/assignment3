import random


def get_monster():
    value = random.randint(1, 31)
    if value == 1:
        return get_chris()
    elif 1 < value < 11:
        return get_amir()
    elif 10 < value < 21:
        return get_armaan()
    else:
        return get_frank()


def get_amir():
    return {"HP": [10, 10], 'name': 'Amir', 'attack': 'Amir rolls your name on his magic device!', 'type': 'monster'}


def get_chris():
    return {"HP": [1000, 1000], 'name': 'Chris', 'attack': 'Chris says "see?  wasn\'t so hard was it?"',
            'type': 'monster'}


def get_armaan():
    return {"HP": [10, 10], 'name': 'Armaan',
            'attack': 'Armaan says: Studies show students learn best when pushed to the edge!',
            'type': 'monster'}


def get_frank():
    return {"HP": [10, 10], 'name': 'Frank', 'attack': 'Frank assigns an assignment that\'s 100% fun!',
            'type': 'monster'}
import numpy as np
import time
from src.Items import *
from src.Classes import *


# random number generator, returns a vector with n random ints in range [low, high)
def n_random(n, low, high):
    seed = abs(round(time.time())) % 100000
    np.random.seed(seed)
    random_numbers = np.random.randint(low, high, size=n)
    return random_numbers

def random_height():
    h = n_random(1, 130, 201)
    return h[0]/100

# generater n random charachters of rol type in a set
def generate_random_character(type, n):
    character_set = set()
    boots = get_n_random_items( "botas",n)
    helmets = get_n_random_items( "cascos",n)
    armours = get_n_random_items( "pecheras",n)
    gloves = get_n_random_items( "guantes",n)
    weapons = get_n_random_items( "armas",n)
    i = 0
    while i <= n:
        c = Character(type, random_height(), weapons.pop(), helmets.pop(), boots.pop(), gloves.pop(), armours.pop())
        character_set.add(c)
        i += 1

    return character_set


# returns a lists with n random items of type type
def get_n_random_items(type, n):
    item_list = list()
    ids = sorted(n_random(n, 0, 1000000))
    cut = len(ids)
    with open(str(type) + ".tsv") as fp:
        for i, line in enumerate(fp):
            if i-1 in ids:
                line = line[:-1]
                row = line.split('\t')
                item_list.append(Items(row[0], row[1], row[2], row[3], row[4], row[5]))
                cut -= 1
            if cut == 0:
                return item_list


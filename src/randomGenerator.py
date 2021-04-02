import numpy as np
import time
import random
from src.items import *
from src.classes import *


# random number generator, returns a vector with n random ints in range [low, high)
def n_random(n, low, high):
    random_numbers = np.random.randint(low, high, size=n)
    return random_numbers


# generates n random heights
def random_heights(n):
    i = 0
    h_list = list()
    haux = n_random(n, 130, 201)
    for h in haux:
        h_list.append(h/100)
    return h_list


# generater n random charachters of rol type in a set
def generate_random_character(type, n):
    character_list = list() #before : character_set = set()
    boots = get_n_random_items("botas", n)
    helmets = get_n_random_items("cascos", n)
    armours = get_n_random_items("pecheras", n)
    gloves = get_n_random_items("guantes", n)
    weapons = get_n_random_items("armas", n)
    heights = random_heights(n)
    i = 0
    while i < n:
        c = Warrior(heights.pop(), weapons.pop(), helmets.pop(), boots.pop(), gloves.pop(), armours.pop())
        character_list.append(c)
        i += 1

    return character_list


# returns a lists with n random items of type type
def get_n_random_items(type, n):
    item_list = list()
    ids = sorted(random.sample(range(0, 10000), n))
    cut = len(ids)
    with open("/Users/darkovindis/Desktop/Sia tps/sia_tp2/" + str(type) + ".tsv") as fp:
        for i, line in enumerate(fp):
            if i-1 in ids:
                row = line[:-1].split('\t')
                item_list.append(Items(row[0], row[1], row[2], row[3], row[4], row[5]))
                cut -= 1
            if cut == 0:
                return item_list
    return item_list

from src.Classes import *


def cruce_1p(padre1, padre2, n):
    if n > 5:
        raise IndexError("Invalid n parameter, must be <=5")
    index = 0
    # self.armour, self.gloves, self.boots, self.weapon, self.helmet, self.height
    padre1_vec = padre1.vectorize()
    padre2_vec = padre2.vectorize()
    son1 = []
    son2 = []
    while index < n:
        son1.append(padre1_vec[index])
        son2.append(padre2_vec[index])
        index += 1
    while index < 6:
        son1.append(padre2_vec[index])
        son2.append(padre1_vec[index])
        index += 1


    # (role, height, weapon, helmet, boots, gloves, armour)
    char1 = Warrior(son1[0], son1[1], son1[2], son1[3], son1[4], son1[5])
    char2 = Warrior(son2[0], son2[1], son2[2], son2[3], son2[4], son2[5])

    return char1, char2

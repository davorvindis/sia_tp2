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

    return child_creator(padre1, son1, son2)

def cruce_2p(padre1, padre2, punto1, punto2):
    if punto1 > 5 or punto2 > 5 or punto1 > punto2:
        raise IndexError("Invalid parameters, points should be less than 5 and point1 < point2")
    index = 0
    # self.armour, self.gloves, self.boots, self.weapon, self.helmet, self.height
    padre1_vec = padre1.vectorize()
    padre2_vec = padre2.vectorize()
    son1 = []
    son2 = []

    while index < 6:
        if punto1 <= index <= punto2:
            son1.append(padre1_vec[index])
            son2.append(padre2_vec[index])
        else:
            son1.append(padre2_vec[index])
            son2.append(padre1_vec[index])
        index += 1

    return child_creator(padre1, son1, son2)

def cruce_anular(padre1, padre2, p, l):
    index = 0
    # self.armour, self.gloves, self.boots, self.weapon, self.helmet, self.height
    padre1_vec = padre1.vectorize()
    padre2_vec = padre2.vectorize()
    son1 = []
    son2 = []

    while index < p:
        son1.append(padre1_vec[index])
        son2.append(padre2_vec[index])
        index += 1
    while index < p+l:
        if index < 6:
            son1.append(padre2_vec[index])
            son2.append(padre1_vec[index])
        else:
            son1.append(padre2_vec[index-5])
            son2.append(padre1_vec[index-5])
        index += 1
    return


def cruce_uniforme(padre1, padre2):
    index = 0
    # self.armour, self.gloves, self.boots, self.weapon, self.helmet, self.height
    padre1_vec = padre1.vectorize()
    padre2_vec = padre2.vectorize()
    son1 = []
    son2 = []

    while index < 6:
        random = np.random.uniform(0.0, 1.0, None)
        if random < 0.5:
            son1.append(padre1_vec[index])
            son2.append(padre2_vec[index])
        else:
            son1.append(padre2_vec[index])
            son2.append(padre1_vec[index])
        index += 1

    return child_creator(padre1, son1, son2)

def child_creator(parent, son1, son2):
    child1 = ""
    child2 = ""
    if parent.role == "warrior":
        # (role, height, weapon, helmet, boots, gloves, armour)
        child1 = Warrior(son1[0], son1[1], son1[2], son1[3], son1[4], son1[5])
        child2 = Warrior(son2[0], son2[1], son2[2], son2[3], son2[4], son2[5])
    if parent.role == "archer":
        child1 = Archer(son1[0], son1[1], son1[2], son1[3], son1[4], son1[5])
        child2 = Archer(son2[0], son2[1], son2[2], son2[3], son2[4], son2[5])
    if parent.role == "defender":
        child1 = Defender(son1[0], son1[1], son1[2], son1[3], son1[4], son1[5])
        child2 = Defender(son2[0], son2[1], son2[2], son2[3], son2[4], son2[5])
    if parent.role == "infiltrator":
        child1 = Infiltrator(son1[0], son1[1], son1[2], son1[3], son1[4], son1[5])
        child2 = Infiltrator(son2[0], son2[1], son2[2], son2[3], son2[4], son2[5])
    return child1, child2



from src.helpers import *

# Metodos de Cruce  (4/4)
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
    p = int(p)
    l = int(l)
    # self.armour, self.gloves, self.boots, self.weapon, self.helmet, self.height
    padre1_vec = padre1.vectorize()
    padre2_vec = padre2.vectorize()
    son1 = []
    son2 = []

    while index < p:
        son1.append(padre1_vec[index])
        son2.append(padre2_vec[index])
        index += 1
    while index < p + (l+1): #add +1
        if index < 6:
            son1.append(padre2_vec[index])
            son2.append(padre1_vec[index])
        else:
            son1.append(padre2_vec[index - 5])
            son2.append(padre1_vec[index - 5])
        index += 1
    return child_creator(padre1, son1, son2) #add return


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

###################################################################

# [ tipo, padre1, padre2, var1, var2 ]
# [0, 1, 2, 3, 4]
def cruce_wrapper(fn):
    def inner1(*args):
        if args[0] == "1p":
            return cruce_1p(args[1], args[2], int(args[3]))
        elif args[0] == "2p":
            return cruce_2p(args[1], args[2], args[3], args[4])
        elif args[0] == "anular":
            return cruce_anular(args[1], args[2], args[3], args[4])
        elif args[0] == "uniforme":
            return cruce_uniforme(args[1], args[2])

    return inner1

@cruce_wrapper
def cruce(*args):
    print("1")

###################################################################



import numpy as np


class Character:
    def __init__(self, role, height, weapon, helmet, boots, gloves, armour):
        # if height not in range[1.3, 2]:
        #     raise ValueError("Height should be a number between 1,3 and 2")
        self.atm = 0.7 - np.power((3 * height - 5), 4) + np.power((3 * height - 5), 2) + height / 4
        self.dem = 1.9 + np.power((2.5 * height - 4.16), 4) - np.power((2.5 * height - 4.16), 2) - 3 * height / 10
        self.height = height
        self.role = role
        self.weapon = weapon
        self.helmet = helmet
        self.boots = boots
        self.gloves = gloves
        self.armour = armour

    def setHeight(self, height):
        if height not in range[1.3, 2]:
            raise ValueError("Height should be a number between 1,3 and 2")
        self.height = height
        self.atm = 0.7 - np.power((3 * height - 5), 4) + np.power((3 * height - 5), 2) + height / 4
        self.dem = 1.9 + np.powet((2.5 * height - 4.16), 4) - np.power((2.5 * height - 4.16), 2) - 3 * height / 10

    def vectorize(self):
        return [self.height, self.weapon, self.helmet, self.boots, self.gloves, self.armour]

    def setItems(self, weapon, helmet, boots, gloves, armour):
        self.weapon = weapon
        self.helmet = helmet
        self.boots = boots
        self.gloves = gloves
        self.armour = armour

    def attack(self):
        ag_sum = self.boots.ag + self.gloves.ag + self.helmet.ag + self.armour.ag + self.weapon.ag
        ag = np.tanh(0.01 * ag_sum)
        ex_sum = self.boots.ex + self.gloves.ex + self.helmet.ex + self.armour.ex + self.weapon.ex
        ex = 0.6 * np.tanh(0.01 * ex_sum)
        fu_sum = self.boots.fu + self.gloves.fu + self.helmet.fu + self.armour.fu + self.weapon.fu
        fu = 100 * np.tanh(0.01 * fu_sum)
        attack = (ag + ex) * fu * self.atm
        return attack

    def defense(self):
        re_sum = self.boots.re + self.gloves.re + self.helmet.re + self.armour.re + self.weapon.re
        re = np.tanh(0.01 * re_sum)
        ex_sum = self.boots.ex + self.gloves.ex + self.helmet.ex + self.armour.ex + self.weapon.ex
        ex = 0.6 * np.tanh(0.01 * ex_sum)
        vi_sum = self.boots.vi + self.gloves.vi + self.helmet.vi + self.armour.vi + self.weapon.vi
        vi = 100 * np.tanh(0.01 * vi_sum)
        defense = (re + ex) * vi * self.dem
        return defense

    def __eq__(self, o):
        return self.weapon == o.weapon and self.helmet == o.helmet and self.boots == o.boots and \
               self.gloves == o.gloves and self.armour == o.armour and self.role == o.role

    def fitness(self):
        raise NotImplementedError("Please Implement this method")

    def __str__(self):
        return "{ character" + '\n' + '\t' + \
               "type: " + str(self.role) + '\n' + '\t' \
                                                  "height: " + str(self.height) + '\n' + '\t' \
                                                                                         "weapon: " + str(
            self.weapon.id) + ", helmet: " + str(self.helmet.id) + ", boots: " + \
               str(self.boots.id) + ", gloves: " + str(self.gloves.id) + ", armour: " + \
               str(self.armour.id) + '\n' + '\t' \
                                            "attack = " + str(self.attack()) + '\n' + '\t' \
                                                                                      "defense = " + str(
            self.defense()) + '\n' + '\t' \
                                     "performance = " + str(self.fitness()) + '\n' + '\t' \
                                                                                     "}"

    def __hash__(self):
        return hash(hash(self.role) + hash(self.helmet.id) + hash(self.gloves.id) + hash(self.boots.id)
                    + hash(self.weapon.id) + hash(self.armour.id) + hash(self.height))


class Warrior(Character):
    def __init__(self, h, weapon, helmet, boots, gloves, armour):
        if isinstance(h, int) or isinstance(h, float):
            height = h
        else:
            if len(h) > 0:
                height = h.pop()
            else:
                height = 1.70

        self.atm = 0.7 - np.power((3 * height - 5), 4) + np.power((3 * height - 5), 2) + height / 4
        self.dem = 1.9 + np.power((2.5 * height - 4.16), 4) - np.power((2.5 * height - 4.16), 2) - 3 * height / 10
        self.height = height
        self.weapon = weapon
        self.helmet = helmet
        self.boots = boots
        self.gloves = gloves
        self.armour = armour
        self.role = "warrior"

    def fitness(self):
        return 0.6 * self.attack() + 0.6 * self.defense()


class Archer(Character):
    def __init__(self, h, weapon, helmet, boots, gloves, armour):
        if isinstance(h, int) or isinstance(h, float):
            height = h
        else:
            if len(h) > 0:
                height = h.pop()
            else:
                height = 1.70

        self.atm = 0.7 - np.power((3 * height - 5), 4) + np.power((3 * height - 5), 2) + height / 4
        self.dem = 1.9 + np.power((2.5 * height - 4.16), 4) - np.power((2.5 * height - 4.16), 2) - 3 * height / 10
        self.height = height
        self.weapon = weapon
        self.helmet = helmet
        self.boots = boots
        self.gloves = gloves
        self.armour = armour
        self.role = "archer"

    def fitness(self):
        return 0.9 * self.attack() + 0.1 * self.defense()


class Defender(Character):
    def __init__(self, h, weapon, helmet, boots, gloves, armour):
        if isinstance(h, int) or isinstance(h, float):
            height = h
        else:
            if len(h) > 0:
                height = h.pop()
            else:
                height = 1.70

        self.atm = 0.7 - np.power((3 * height - 5), 4) + np.power((3 * height - 5), 2) + height / 4
        self.dem = 1.9 + np.power((2.5 * height - 4.16), 4) - np.power((2.5 * height - 4.16), 2) - 3 * height / 10
        self.height = height
        self.weapon = weapon
        self.helmet = helmet
        self.boots = boots
        self.gloves = gloves
        self.armour = armour
        self.role = "defender"

    def fitness(self):
        return 0.3 * self.attack() + 0.8 * self.defense()


class Infiltrator(Character):
    def __init__(self, h, weapon, helmet, boots, gloves, armour):
        if isinstance(h, int) or isinstance(h, float):
            height = h
        else:
            if len(h) > 0:
                height = h.pop()
            else:
                height = 1.70

        self.atm = 0.7 - np.power((3 * height - 5), 4) + np.power((3 * height - 5), 2) + height / 4
        self.dem = 1.9 + np.power((2.5 * height - 4.16), 4) - np.power((2.5 * height - 4.16), 2) - 3 * height / 10
        self.height = height
        self.weapon = weapon
        self.helmet = helmet
        self.boots = boots
        self.gloves = gloves
        self.armour = armour
        self.role = "infiltrator"

    def fitness(self):
        return 0.8 * self.attack() + 0.3 * self.defense()

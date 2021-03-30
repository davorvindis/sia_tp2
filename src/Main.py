import csv
import time
import json
from src.RandomGenerator import *
from src.Classes import *
from src.Items import *
from src.GeneticOperators import *

# boost para leer archivos de configuracion
f = open('../input/input_parameters', "r")
data = json.load(f)
# print(data["genetic_operator"])
f.close()



# main
# warrior(self, height, weapon, helmet, boots, gloves, armour)
# warrior1 = Warrior(1.5, Items(1, 1, 1, 1, 1, 1), Items(1, 1, 1, 1, 1, 1), Items(1, 1, 1, 1, 1, 1), Items(1, 1, 1, 1, 1, 1), Items(1, 1, 1, 1, 1, 1))
# warrior2 = Warrior(2, Items(2, 2, 2, 2, 2, 2), Items(2, 2, 2, 2, 2, 2), Items(2, 2, 2, 2, 2, 2), Items(2, 2, 2, 2, 2, 2), Items(2, 2, 2, 2, 2, 2))
# hijo1, hijo2 = cruce_1p(warrior1, warrior2, 3)
# print(hijo1)
# print(hijo2)


#c = generate_random_character("warrior", 20)
#print(c.pop())
#print(c.pop())

poblacion = generate_random_character("warrior", 20)
K = 5
seleccion1 = seleccion_ruleta(poblacion, K)


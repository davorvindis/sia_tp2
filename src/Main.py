import csv
import json
from src.Classes import *
from src.Items import Items
from src.Genetic_Operators import *

# boost para leer archivos de configuracion
f = open('../input/input_parameters', "r")
data = json.load(f)
# print(data["genetic_operator"])
f.close()

# boost para leer items de tsv
# with open("armas.tsv") as fd:
#     rd = csv.reader(fd, delimiter="\t", quotechar='"')
#     armas_set = set()
#     header_flag = True
#     for row in rd:
#         if header_flag:
#             header_flag = False
#             continue
#         armas_set.add(Items(row[0], row[1], row[2], row[3], row[4], row[5]))
#     print(len(armas_set))

# main
# warrior(self, height, weapon, helmet, boots, gloves, armour)
warrior1 = Warrior(1.5, Items(1, 1, 1, 1, 1, 1), Items(1, 1, 1, 1, 1, 1), Items(1, 1, 1, 1, 1, 1), Items(1, 1, 1, 1, 1, 1), Items(1, 1, 1, 1, 1, 1))
warrior2 = Warrior(2, Items(2, 2, 2, 2, 2, 2), Items(2, 2, 2, 2, 2, 2), Items(2, 2, 2, 2, 2, 2), Items(2, 2, 2, 2, 2, 2), Items(2, 2, 2, 2, 2, 2))
hijo1, hijo2 = cruce_1p(warrior1, warrior2, 3)
print(hijo1)
print(hijo2)



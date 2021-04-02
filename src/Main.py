import csv
import time
import json
from src.randomGenerator import *
from src.Classes import *
from src.items import *
from src.mutacion import *
from src.seleccion import *
from src.cruce import *
from src.corte import *


# boost para leer archivos de configuracion

f = open('../input/input_parameters', "r")
data = json.load(f)

input_cruce = data["cruce"]
cruce_var1 = 0
cruce_var2 = 0
if input_cruce == "1p":
    cruce_var1 = data["variables_cruce"][0]
elif cruce == ["2p", "anular"]:
    cruce_var1 = data["variables_cruce"][0]
    cruce_var2 = data["variables_cruce"][1]

input_corte = data["corte"]
corte_var=0
if input_corte in ["generaciones", "tiempo"]:
    corte_var = data["corte"][0]

input_seleccion =data["seleccion"]
seleccion_var1 = 0
if input_seleccion == "torneo_deterministico":
    seleccion_var1 = data["variables_seleccion"][0]

input_implementacion = data["implementacion"]

input_mutacion =data["mutacion"]
mutacion_var1 = 0
if input_mutacion == "limitada":
    mutacion_var1 = data["variables_mutacion"][0]


f.close()

N = 10
K = 2
generation_zero = generate_random_character(type, N)
k_sons = list()
next_generation = list()

seleccionados = seleccion(input_seleccion, generation_zero, K, seleccion_var1)
for i in range(len(seleccionados)):
    if len(seleccionados) > 1:
        hijo1, hijo2 = cruce(input_cruce, seleccionados[i], seleccionados[i+1], cruce_var1, cruce_var2)
        k_sons.append(hijo1)
        k_sons.append(hijo2)
        seleccionados.remove(seleccionados[i])
        seleccionados.remove(seleccionados[i])

for i in range(len(k_sons)):
    mutacion(input_mutacion, k_sons[i], mutacion_var1)

if input_implementacion == "fill-all":
    all = list()
    all.extend(generation_zero)
    all.extend(k_sons)
    next_generation = seleccion(input_seleccion, all, N, seleccion_var1)
elif input_implementacion == "fill-parent":
    if K > N:
        next_generation = seleccion(input_seleccion, k_sons, N, seleccion_var1)
    elif K == N:
        next_generation.append(k_sons)
    elif K == N:
        next_generation.append(k_sons)
        next_generation.append(seleccion(input_seleccion, generation_zero, N-K, seleccion_var1))

for i in range(len(generation_zero)):
    print(generation_zero[i])

print("next gen")

for i in range(len(next_generation)):
    print(next_generation[i])
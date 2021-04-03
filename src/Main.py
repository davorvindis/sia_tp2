import csv
import time
import json
from src.randomGenerator import *
from src.classes import *
from src.items import *
from src.mutacion import *
from src.seleccion import *
from src.corte import *
from src.cruce import *

def iterate( generation ,input_cruce, cruce_var1, cruce_var2, input_seleccion, seleccion_var, input_implementacion, input_mutacion, \
             mutacion_var, N, K ):

    k_sons = list()
    next_generation = list()

    seleccionados = seleccion(input_seleccion, generation, K, seleccion_var)
    for i in range(len(seleccionados)):
        if len(seleccionados) > 1:
            hijo1, hijo2 = cruce(input_cruce, seleccionados[i], seleccionados[i+1], cruce_var1, cruce_var2)
            k_sons.append(hijo1)
            k_sons.append(hijo2)
            seleccionados.remove(seleccionados[i])
            seleccionados.remove(seleccionados[i])

    for i in range(len(k_sons)):
        mutacion(input_mutacion, k_sons[i], mutacion_var)

    if input_implementacion == "fill-all":
        all = list()
        all.extend(generation)
        all.extend(k_sons)
        next_generation = seleccion(input_seleccion, all, N, seleccion_var)

    elif input_implementacion == "fill-parent":
        if K > N:
            next_generation = seleccion(input_seleccion, k_sons, N, seleccion_var)
        elif K == N:
            next_generation.append(k_sons)
        elif K <= N:
            next_generation.extends(k_sons)
            next_generation.extends(seleccion(input_seleccion, generation, N-K, seleccion_var))

    for i in range(len(generation)):
        print(generation[i])

    print("next gen")

    for i in range(len(next_generation)):
        print(next_generation[i])



input_cruce, cruce_var1, cruce_var2, input_seleccion, seleccion_var, input_implementacion, input_mutacion, \
mutacion_var, input_corte, corte_var, N, K = read_input()

generation_zero = generate_random_character(type, N)


@corte_wrapper
def corte(*args):
    iterate(generation_zero,input_cruce, cruce_var1, cruce_var2, input_seleccion, seleccion_var, input_implementacion, input_mutacion, \
            mutacion_var, N, K)


corte(input_corte, corte_var)
from src.helpers import *
from src.randomGenerator import *
import random, math, copy, numpy as np


###################################################################

# Metodos de seleccion  (6/6)


def seleccion_ranking(poblacion, K):
    pseudoFitness = pseudo_fitness(poblacion)
    r = np.random.uniform(0, 1, K)
    selected = []

    for ri in r:
        if ri < pseudoFitness[0]:
            selected.append(poblacion[0])
            if len(selected) == K:
                return selected
        for index in range(0, len(pseudoFitness) - 1):
            if pseudoFitness[index] < ri <= pseudoFitness[index + 1]:
                selected.append(poblacion[index + 1])
                if len(selected) == K:
                    return selected


def seleccion_universal(poblacion, K):
    fitnessRelativo = relative_fitness(poblacion)
    fitnessAcumulado = accumulative_fitness(fitnessRelativo)

    # Igual que en ruleta, pero la forma de calcular los rj es la siguiente
    r_ = np.random.uniform(0, 1)
    r = [(r_ + j) / K for j in range(0, K)]
    selected = []

    for ri in r:
        if (ri < fitnessAcumulado[0]):
            selected.append(poblacion[0])
            if len(selected) == K:
                return selected
        for index in range(0, len(fitnessAcumulado) - 1):
            if (fitnessAcumulado[index] < ri <= fitnessAcumulado[index + 1]):
                selected.append(poblacion[index + 1])
                if len(selected) == K:
                    return selected


def seleccion_ruleta(poblacion, K):
    fitnessRelativo = relative_fitness(poblacion)
    fitnessAcumulado = accumulative_fitness(fitnessRelativo)

    r = np.random.uniform(0, 1, K)
    selected = list()

    for ri in r:
        if (ri < fitnessAcumulado[0]):
            selected.append(poblacion[0])
            if len(selected) == K:
                return selected
        for index in range(0, len(fitnessAcumulado) - 1):
            if (fitnessAcumulado[index] < ri <= fitnessAcumulado[index + 1]):
                selected.append(poblacion[index + 1])
                if len(selected) == K:
                    return selected


def seleccion_torneo_deterministico(poblacion, K, M):
    return_list = list()
    selected_positions = sorted(n_random(M * K, 0, len(poblacion)))
    while K > 0:
        cut = 0
        torneo_list = list()
        for individuo in poblacion:
            i = poblacion.index(individuo)
            if poblacion.index(individuo) in selected_positions:
                cut += 1
                selected_positions.remove(i)
                torneo_list.append(individuo)
                if cut == M:
                    break
        torneo_list.sort(reverse=True, key=getFitness)
        return_list.append(torneo_list[0])
        K -= 1
    return return_list


def seleccion_torneo_probabilistico(poblacion, K):
    aux = copy.deepcopy(K)
    result_list = list()
    thresholds_list = n_random(K, 5, 10)
    random_list = n_random(K, 0, 10)
    index = 0
    while K > 0:
        selected_positions = list(random.sample(range(0, len(poblacion)-1), 2))
        torneo_list = list()
        for individuo in poblacion:
            i = poblacion.index(individuo)
            if i in selected_positions:
                selected_positions.remove(i)
                torneo_list.append(individuo)
        torneo_list.sort(reverse=True, key=getFitness)
        K -= 1
        if random_list[index] < thresholds_list[index]:
            result_list.append(torneo_list[0])
        else:
            if len(torneo_list) < 2:
                result_list.append(torneo_list[0])
            else:
                result_list.append(torneo_list[1])
        index += 1

    return result_list


def seleccion_elite(poblacion, k):
    rta = list()
    poblacion_ordenada_por_fitness = list()
    total = 0
    for individuo in poblacion:
        poblacion_ordenada_por_fitness.append((getFitness(individuo), individuo))
        total += 1
    poblacion_ordenada_por_fitness.sort(reverse=False)

    lista_temporal = list()
    aux = 0
    while aux < k:
        if aux == 0 or (aux % total) == 0:
            lista_temporal = poblacion_ordenada_por_fitness.copy()
        rta.append(lista_temporal.pop()[1])
        aux += 1

    return rta


def seleccion_boltzmann(poblacion, K):
    pseudoFitness = boltzmann_fitness(poblacion)
    r = np.random.uniform(0, 1, K)
    selected = []

    for ri in r:
        if ri < pseudoFitness[0]:
            selected.append(poblacion[0])
            if len(selected) == K:
                return selected
        for index in range(0, len(pseudoFitness) - 1):
            if pseudoFitness[index] < ri <= pseudoFitness[index + 1]:
                selected.append(poblacion[index + 1])
                if len(selected) == K:
                    return selected


###################################################################
# [ tipo, poblacion, K, var2 ]
# [0, 1, 2, 3, 4]

# Funcion que se va a wrappear en el criterio de corte, va a correr en loop
def seleccion(input_seleccion_1, input_seleccion_2, seleccion_var_1, seleccion_var_2, generation, K, A):
    pool = copy.deepcopy(generation)
    selected = list()
    ceil = math.ceil(A * K)
    selected_in_method_1 = select(input_seleccion_1, pool, seleccion_var_1, ceil)
    for i in range(len(selected_in_method_1)):
        if selected_in_method_1[i] in pool:
            pool.remove(selected_in_method_1[i])
    selected.extend(selected_in_method_1)
    floor = math.floor((1 - A) * K)
    selected.extend(select(input_seleccion_2, pool, seleccion_var_2, floor))
    return selected


def select(metodo, poblacion, variable, N):
    if metodo == "torneo_deterministico":
        return seleccion_torneo_deterministico(poblacion, N, int(variable))
    elif metodo == "torneo_probabilistico":
        return seleccion_torneo_probabilistico(poblacion, N)
    elif metodo == "universal":
        return seleccion_universal(poblacion, N)
    elif metodo == "ruleta":
        return seleccion_ruleta(poblacion, N)
    elif metodo == "ranking":
        return seleccion_ranking(poblacion, N)
    elif metodo == "boltzmann":
        return seleccion_boltzmann(poblacion, N)
    elif metodo == "elite":
        return seleccion_elite(poblacion, N)

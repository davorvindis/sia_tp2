from src.helpers import *
from src.randomGenerator import *
import random


###################################################################

# Metodos de seleccion  (4/6)
#    * Elite
#    * Boltzmann

def seleccion_ranking(poblacion, K):
    pseudoFitness = pseudo_fitness(poblacion)
    r = np.random.uniform(0, 1, K)
    selected = []

    for ri in r:
        if (ri < pseudoFitness[0]):
            selected.append(poblacion[0])
            if len(selected) == K:
                return selected
        for index in range(0, len(pseudoFitness) - 1):
            if (pseudoFitness[index] < ri <= pseudoFitness[index + 1]):
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


def seleccion_torneo_deterministico(poblacion, K, M):
    return_list = list()
    selected_positions = sorted(n_random(M*K, 0, len(poblacion)))
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
    result_list = list()
    thresholds_list = n_random(5, 10, K)
    random_list = n_random(0, 10, K)
    selected_positions = list(random.sample(range(0, len(poblacion)), 2*K))
    index = 0
    while K > 0:
        cut = 0
        torneo_list = list()
        for individuo in poblacion:
            i = poblacion.index(individuo)
            if poblacion.index(individuo) in selected_positions:
                cut += 1
                selected_positions.remove(i)
                torneo_list.append(individuo)
            if cut == 2:
                break
        torneo_list.sort(reverse=True, key=getFitness)
        K -= 1
        if random_list[index] < thresholds_list[index]:
            result_list.append(torneo_list[0])
        else:
            result_list.append(torneo_list[1])
        index += 1

    return result_list


    #  Metodos de implementacion (0/2)


###################################################################
# [ tipo, poblacion, K, var2, var3 ]
# [0, 1, 2, 3, 4]
def selection_wrapper(fn):
    def inner1(*args):
        if args[0] == "torneo_deterministico":
            return seleccion_torneo_deterministico(args[1], args[2], args[3])
        elif args[0] == "torneo_probabilistico":
            return seleccion_torneo_probabilistico(args[1], args[2])
        elif args[0] == "universal":
            return seleccion_universal(args[1], args[2])
        elif args[0] == "ruleta":
            return seleccion_ruleta(args[1], args[2])
        elif args[0] == "ranking":
            return seleccion_ranking(args[1], args[2])
        # elif args[0] == "boltzmann":
        # elif args[0] == "elite":

    return inner1

# Funcion que se va a wrappear en el criterio de corte, va a correr en loop
@selection_wrapper
def seleccion(*args):
    print("1")
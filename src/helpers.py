from src.classes import *
import json
import math


# Metodos helpers
#    *** Devuelve 2 hijos ***
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


def relative_fitness(poblacion):
    allFitness = [x_i.fitness() for x_i in poblacion]
    totalFitness = sum(allFitness)
    relativeFitness = [x_i.fitness() / totalFitness for x_i in poblacion]
    return relativeFitness


def accumulative_fitness(relativeFitness):
    return np.cumsum(relativeFitness)

def boltzmann_fitness(poblacion):
    rta = list()
    # Temperatura. Debe calcularse con una funcion pero nose como
    T = 100
    counter = 0
    acum_sum = 0
    for individuo in poblacion:
        counter += 1
        acum_sum += math.exp(getFitness(individuo) / T)

    avg = acum_sum / counter

    for individuo in poblacion:
        aux1 = math.exp(getFitness(individuo) / T)
        aux2 = aux1 / avg
        rta.append(aux2)

    return rta

def pseudo_fitness(poblacion):
    N = len(poblacion)
    allFitness = [x_i.fitness() for x_i in poblacion]
    allFitnessSort = allFitness.copy()
    allFitnessSort.sort(reverse=True)  # ranking ordenado de mayor a menor aptitude real.
    # Luego se utiliza RULETA con este pseudo-aptitud redefinida.
    pseudo_apt = [(N - (1 + allFitnessSort.index(x))) / N for x in allFitness]
    return pseudo_apt


def getFitness(e):
    return e.fitness()

def best_fitness(poblacion):
    return max([getFitness(individuo) for individuo in poblacion])


# boost para leer archivos de configuracion
def read_input():
    f = open('../input/input_parameters', "r")
    data = json.load(f)

    input_cruce = data["cruce"]
    cruce_var1 = 0
    cruce_var2 = 0
    if input_cruce == "1p":
        cruce_var1 = data["variables_cruce"][0]
    elif input_cruce == ["2p", "anular"]:
        cruce_var1 = data["variables_cruce"][0]
        cruce_var2 = data["variables_cruce"][1]

    input_corte = data["corte"]
    corte_var = 0
    if input_corte in ["generaciones", "tiempo", "contenido", "aceptable"]:
        corte_var = data["variables_corte"][0]


    input_seleccion_1 = data["seleccion_1"]
    seleccion_var_1 = 0
    if input_seleccion_1 == "torneo_deterministico":
        seleccion_var_1 = data["variables_seleccion_1"][0]

    input_seleccion_2 = data["seleccion_2"]
    seleccion_var_2 = 0
    if input_seleccion_2 == "torneo_deterministico":
        seleccion_var_2 = data["variables_seleccion_2"][0]

    input_seleccion_3 = data["seleccion_3"]
    seleccion_var_3 = 0
    if input_seleccion_3 == "torneo_deterministico":
        seleccion_var_3 = data["variables_seleccion_3"][0]

    input_seleccion_4 = data["seleccion_4"]
    seleccion_var_4 = 0
    if input_seleccion_4 == "torneo_deterministico":
        seleccion_var_4 = data["variables_seleccion_4"][0]

    input_implementacion = data["implementacion"]

    input_mutacion = data["mutacion"]
    mutacion_var = 0
    if input_mutacion == "limitada":
        mutacion_var = data["variables_mutacion"][0]

    N = data["N"]
    K = data["K"]
    A = data["A"]
    B = data["B"]

    f.close()

    return input_cruce, cruce_var1, cruce_var2, input_seleccion_1, seleccion_var_1, input_seleccion_2, seleccion_var_2, \
           input_seleccion_3, seleccion_var_3, input_seleccion_4, seleccion_var_4, \
           input_implementacion, input_mutacion, mutacion_var, input_corte, corte_var, N, K, A, B

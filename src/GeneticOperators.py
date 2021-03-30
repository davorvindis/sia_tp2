from src.Classes import *
from src.RandomGenerator import *

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


def mutacion_gen(individuo):
    # Gen a mutar
    pg = np.random.randint(1, 6, size=None, dtype='l')

    # Probabilidad de mutacion
    pm = 0.3
    # height, weapon, helmet, boots, gloves, armour
    # Hay 2 opciones. 1- Nuevo y random o 2- Modificar el existente con un delta (considerando una distribucion)
    rand = np.random.uniform(0.0, 1.0, None)
    if rand <= pm:
        if pg==1:
            individuo.height = random_height()
        if pg==2:
            individuo.weapon = get_n_random_items( "armas", 1).pop()
        if pg==3:
            individuo.helmet = get_n_random_items( "cascos", 1).pop()
        if pg==4:
            individuo.boots = get_n_random_items( "botas", 1).pop()
        if pg==5:
            individuo.gloves = get_n_random_items( "guantes", 1).pop()
        if pg==6:
            individuo.armour = get_n_random_items( "pecheras", 1).pop()
    return

def mutacion_multigen_limitada(individuo, cantidad_genes):
#PAUSA, LE FALTA TERMINARLO

    

    # Probabilidad de mutacion
    pm = 0.3
    # height, weapon, helmet, boots, gloves, armour
    # Hay 2 opciones. 1- Nuevo y random o 2- Modificar el existente con un delta (considerando una distribucion)
    genes_modificados = 0
    lista_de_genes_modificados = list()

    while genes_modificados < cantidad_genes:
        # Gen a mutar
        pg = np.random.randint(1, 6, size=None, dtype='l')
        rand = np.random.uniform(0.0, 1.0, None)
        if rand <= pm :
            if pg==1:
                individuo.height = random_height()
            if pg==2:
                individuo.weapon = get_n_random_items( "armas", 1).pop()
            if pg==3:
                individuo.helmet = get_n_random_items( "cascos", 1).pop()
            if pg==4:
                individuo.boots = get_n_random_items( "botas", 1).pop()
            if pg==5:
                individuo.gloves = get_n_random_items( "guantes", 1).pop()
            if pg==6:
                individuo.armour = get_n_random_items( "pecheras", 1).pop()
            cantidad_genes += 1

    return

def mutacion_multigen_uniforme(individuo):
    # Probabilidad de mutacion
    pm = 0.3

    if np.random.uniform(0.0, 1.0, None) <= pm:
        individuo.height = random_height()
    if np.random.uniform(0.0, 1.0, None) <= pm:
        individuo.weapon = get_n_random_items( "armas", 1).pop()
    if np.random.uniform(0.0, 1.0, None) <= pm:
        individuo.helmet = get_n_random_items( "cascos", 1).pop()
    if np.random.uniform(0.0, 1.0, None) <= pm:
        individuo.boots = get_n_random_items( "botas", 1).pop()
    if np.random.uniform(0.0, 1.0, None) <= pm:
        individuo.gloves = get_n_random_items( "guantes", 1).pop()
    if np.random.uniform(0.0, 1.0, None) <= pm:
        individuo.armour = get_n_random_items( "pecheras", 1).pop()

    return

def mutacion_completa(set):
    return

def relative_fitness(poblacion):
    allFitness = [x_i.fitness() for x_i in poblacion]
    totalFitness = sum(allFitness)
    relativeFitness = [x_i.fitness()/totalFitness for x_i in poblacion]
    return relativeFitness
	
def accumulative_fitness(relativeFitness):
    return np.cumsum(relativeFitness)

def pseudo_fitness(poblacion):
    N = len(poblacion)
    allFitness = [x_i.fitness() for x_i in poblacion]
    allFitnessSort = allFitness.copy()
    allFitnessSort.sort(reverse=True) #ranking ordenado de mayor a menor aptitude real.
    #Luego se utiliza RULETA con este pseudo-aptitud redefinida.
    pseudo_apt = [(N - (1+allFitnessSort.index(x)))/N for x in allFitness]
    return pseudo_apt

def seleccion_ranking(poblacion, K):
    
    pseudoFitness = pseudo_fitness(poblacion)
    r = np.random.uniform(0, 1, K)
    selected = []

    for ri in r:
        if (ri < pseudoFitness[0]):
            selected.append(poblacion[0])
            if len(selected) == K:
                return selected
        for index in range(0, len(pseudoFitness)-1):
            if (pseudoFitness[index] < ri <= pseudoFitness[index+1]):
                selected.append(poblacion[index+1])
                if len(selected) == K:
		    return selected

def seleccion_universal(poblacion, K):
	
    fitnessRelativo  = relative_fitness(poblacion)
    fitnessAcumulado = accumulative_fitness(fitnessRelativo)

    #Igual que en ruleta, pero la forma de calcular los rj es la siguiente
    r_ = np.random.uniform(0,1)
    r = [(r_ + j)/K for j in range(0, K)]
    selected = []

    for ri in r:
	if (ri < fitnessAcumulado[0]):
	    selected.append(poblacion[0])
	    if len(selected) == K:
                return selected
        for index in range(0, len(fitnessAcumulado)-1):
            if (fitnessAcumulado[index] < ri <= fitnessAcumulado[index+1]):
                selected.append(poblacion[index+1])
                if len(selected) == K:
		    return selected

def seleccion_ruleta(poblacion, K):

    fitnessRelativo  = relative_fitness(poblacion)
    fitnessAcumulado = accumulative_fitness(fitnessRelativo)

    r = np.random.uniform(0, 1, K)
    selected = []

    for ri in r:
	if (ri < fitnessAcumulado[0]):
	    selected.append(poblacion[0])
	    if len(selected) == K:
                return selected
        for index in range(0, len(fitnessAcumulado)-1):
            if (fitnessAcumulado[index] < ri <= fitnessAcumulado[index+1]):
                selected.append(poblacion[index+1])
                if len(selected) == K:
		    return selected

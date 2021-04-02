from src.classes import *
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
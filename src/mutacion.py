from src.helpers import *
from src.randomGenerator import *

# Metodos de Mutacion  (4/4)
def mutacion_gen(individuo):
    # Gen a mutar
    pg = np.random.randint(1, 6, size=None, dtype='l')

    # Probabilidad de mutacion
    pm = 0.3
    # height, weapon, helmet, boots, gloves, armour
    # Hay 2 opciones. 1- Nuevo y random o 2- Modificar el existente con un delta (considerando una distribucion)
    rand = np.random.uniform(0.0, 1.0, None)
    if rand <= pm:
        if pg == 1:
            individuo.height = random_heights(1)
        if pg == 2:
            individuo.weapon = get_n_random_items("armas", 1).pop()
        if pg == 3:
            individuo.helmet = get_n_random_items("cascos", 1).pop()
        if pg == 4:
            individuo.boots = get_n_random_items("botas", 1).pop()
        if pg == 5:
            individuo.gloves = get_n_random_items("guantes", 1).pop()
        if pg == 6:
            individuo.armour = get_n_random_items("pecheras", 1).pop()
    return


def mutacion_multigen_limitada(individuo, cantidad_genes):
    # PAUSA, LE FALTA TERMINARLO

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
        if rand <= pm:
            if pg == 1:
                individuo.height = random_heights(1)
            if pg == 2:
                individuo.weapon = get_n_random_items("armas", 1).pop()
            if pg == 3:
                individuo.helmet = get_n_random_items("cascos", 1).pop()
            if pg == 4:
                individuo.boots = get_n_random_items("botas", 1).pop()
            if pg == 5:
                individuo.gloves = get_n_random_items("guantes", 1).pop()
            if pg == 6:
                individuo.armour = get_n_random_items("pecheras", 1).pop()
            cantidad_genes += 1

    return


def mutacion_multigen_uniforme(individuo):
    # Probabilidad de mutacion
    pm = 0.3

    if np.random.uniform(0.0, 1.0, None) <= pm:
        individuo.height = random_heights(1)
    if np.random.uniform(0.0, 1.0, None) <= pm:
        individuo.weapon = get_n_random_items("armas", 1).pop()
    if np.random.uniform(0.0, 1.0, None) <= pm:
        individuo.helmet = get_n_random_items("cascos", 1).pop()
    if np.random.uniform(0.0, 1.0, None) <= pm:
        individuo.boots = get_n_random_items("botas", 1).pop()
    if np.random.uniform(0.0, 1.0, None) <= pm:
        individuo.gloves = get_n_random_items("guantes", 1).pop()
    if np.random.uniform(0.0, 1.0, None) <= pm:
        individuo.armour = get_n_random_items("pecheras", 1).pop()

    return


def mutacion_completa(individuo):
    '''Aplicar un delta al gen, en algún sentido y con alguna distribución '''
    std = 0.2

    deltaHeight = individuo.height - random.gauss(mu=individuo.height, sigma=std)
    individuo.height += deltaHeight

    deltaWeapon = individuo.weapon - random.gauss(mu=individuo.weapon, sigma=std)
    individuo.weapon += deltaWeapon

    deltaHelmet = individuo.helmet - random.gauss(mu=individuo.helmet, sigma=std)
    individuo.helmet += deltaHelmet

    deltaBoots = individuo.boots - random.gauss(mu=individuo.boots, sigma=std)
    individuo.boots += deltaBoots

    deltaGloves = individuo.gloves - random.gauss(mu=individuo.gloves, sigma=std)
    individuo.gloves += deltaGloves

    deltaArmour = individuo.armour - random.gauss(mu=individuo.armour, sigma=std)
    individuo.armour += deltaArmour

    return


###################################################################
# [ tipo, individuo, var1 ]
# [0, 1, 2, 3]
def mutacion_wrapper(fn):
    def inner1(*args):
        if args[0] == "gen":
            return mutacion_gen(args[1])
        elif args[0] == "limitada":
            return mutacion_multigen_limitada(args[1], args[2])
        elif args[0] == "uniforma":
            return mutacion_multigen_uniforme(args[1])
        elif args[0] == "completa":
            return mutacion_completa(set())

    return inner1

# Funcion que se va a wrappear en el criterio de corte, va a correr en loop
@mutacion_wrapper
def mutacion(*args):
    print("1")
import time as time
from src.seleccion import *


# [tipo, poblacion, var1, var2, var3]
# Recibe: una funcion,  Devuelve: una funcion que se ejecuta hasta un criterio de corte
def selection_wrapper(fn):
    def inner1(*args):
        if args[0] == "torneo_deterministico":
            seleccion_torneo_deterministico(args[1], args[2], args[3])
        elif args[0] == "torneo_probabilistico":
            seleccion_torneo_probabilistico(args[1], args[2])
        elif args[0] == "universal":
            seleccion_universal(args[1], args[2])
        elif args[0] == "ruleta":
            seleccion_ruleta(args[1], args[2])
        elif args[0] == "ranking":
            seleccion_ranking(args[1], args[2])
        # elif args[0] == "boltzmann":
        # elif args[0] == "elite":

    return inner1


# Funcion que se va a wrappear en el criterio de corte, va a correr en loop
@selection_wrapper
def seleccion(*args):
    iter()


def iter():
    print("1")


# Main
seleccion("time", 1, time.time())

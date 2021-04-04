import time as time

# Recibe: una funcion,  Devuelve: una funcion que se ejecuta hasta un criterio de corte
def corte_wrapper(fn):
    def inner1(*args):
        if args[0] == "tiempo":
            start = time.time()
            while time.time() - start < int(args[1]):
                fn()

        if args[0] == "generaciones":
            print(args[1])
            i = int(args[1])
            while i > 0:
                fn()
                i -= 1
                
        if args[0] == "contenido":
            '''El mejor fitness no cambia en una cantidad de generaciones'''
            CtdGeneraciones = int(args[1])
            count = 0
            while True:
                bestFitnessOld, bestFitnessNew = fn()
                delta_Fitness = abs(bestFitnessOld - bestFitnessNew)
                if (delta_Fitness == 0):
                    count += 1
                else:
                    count = 0
                if count == CtdGeneraciones:
                    print("STOP")
                    break
                    
        if args[0] == "aceptable":
            '''|fitness(k-1) - fitness(k)| < treshold -> STOP'''
            treshold = args[1]
            while True:
                bestFitnessOld, bestFitnessNew = fn()
                delta_Fitness = abs(bestFitnessOld - bestFitnessNew)
                if delta_Fitness < treshold:
                    print("STOP")
                    break
    return inner1






# Criterios de corte (0/5)
#    * Tiempo (ok)
#    * Cantidad de generaciones (ok)
#    * Solucion aceptable (ok)
#    * Estructura
#    * Contenido (ok)

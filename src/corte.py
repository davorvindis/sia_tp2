import time as time
from helpers import *

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
					
        if args[0] == "estructura":
            '''Si el delta fitness de K individuos de la poblacion < threshold en N generaciones -> STOP'''
            CtdGeneraciones = int(args[1])
            threshold       = float(args[2])
            K_individuos    = int(args[3])
            count = 0
            while True:
                bestFitnessOld, bestFitnessNew, genOld, genNew = fn()
                Infonew = Info_Generation(genNew, K_individuos)
                Infold = Info_Generation(genOld, K_individuos)
                DeltaGeneration = Diff_Generation(Infold, Infonew, threshold)
                
                if DeltaGeneration: #si DeltaGeneration < threshold
                    count += 1
                else:
                    count = 0
                if count == CtdGeneraciones:
                    print("STOP")
                    break
					
                    
        if args[0] == "aceptable":
        '''|fitness(k-1) - fitness(k)| < treshold -> STOP'''
            threshold = float(args[2])
            while True:
                bestFitnessOld, bestFitnessNew, genOld, genNew = fn()
                delta_Fitness = abs(bestFitnessOld - bestFitnessNew)
                if delta_Fitness < threshold:
                    print("STOP")
                    break
    return inner1


def Info_Generation(generacion, K_individuos):
	#Caracteristicas de K caracteres de una determinada generacion
	DataGeneration = list()
	i = 0
	for individuo in generacion:
		DataGeneration.append(getFitness(individuo))
		i += 1
		if i == K_individuos-1:
			break
	return DataGeneration

def Diff_Generation(generacion_old, generacion_new, threshold):
	#Diferencia de fitness entre caracteres de generaciones distintas.
	for Fit_indv1, Fit_indv2 in zip(generacion_old, generacion_new):
		diff = abs(Fit_indv1 - Fit_indv2)
		if diff > threshold: #Si al menos uno de los deltas es > threshold --> FALSE 
			return False
	return True #Si todos los deltas son menores que threshold -> TRUE


# Criterios de corte (5/5)
#    * Tiempo (ok)
#    * Cantidad de generaciones (ok)
#    * Solucion aceptable (ok)
#    * Estructura (ok)
#    * Contenido (ok)

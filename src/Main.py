from src.mutacion import *
from src.seleccion import *
from src.corte import *
from src.cruce import *
from matplotlib import pyplot as plt


# definicion de funcion que itera
def iterate(generation, input_cruce, cruce_var1, cruce_var2, input_seleccion_1, seleccion_var_1, \
            input_seleccion_2, seleccion_var_2, input_seleccion_3, seleccion_var_3, \
            input_seleccion_4, seleccion_var_4, input_implementacion, input_mutacion, \
            mutacion_var, input_corte, corte_var, threshold_var, individuo_var, N, K, A, B):
    k_sons = list()
    next_generation = list()

    seleccionados = seleccion(input_seleccion_1, input_seleccion_2, seleccion_var_1, seleccion_var_2, generation, K, A)
    for i in range(len(seleccionados)):
        if len(seleccionados) > 1:
            i = 0  # Bug fixed.
            hijo1, hijo2 = cruce(input_cruce, seleccionados[i], seleccionados[i + 1], cruce_var1, cruce_var2)
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
        next_generation = seleccion(input_seleccion_3, input_seleccion_4, seleccion_var_3, seleccion_var_4, all, N, B)

    elif input_implementacion == "fill-parent":
        if K > N:
            next_generation = seleccion(input_seleccion_3, input_seleccion_4, seleccion_var_3, seleccion_var_4, k_sons,
                                        N, B)
        elif K == N:
            next_generation.append(k_sons)
        elif K <= N:
            next_generation.extend(k_sons)
            next_generation.extend(
                seleccion(input_seleccion_3, input_seleccion_4, seleccion_var_3, seleccion_var_4, generation, N - K, B))

    for i in range(len(generation)):
        print(generation[i])

    # Start of Plot
    # Set up
    flag = True
    if flag:
        plt.style.use('seaborn')
        fig1, ax1 = plt.subplots()
        ax1.legend()
        ax1.set_title('Fitness Minimo')
        ax1.set_ylabel('Fitness')
        ax1.set_xlabel('Number of generation')

        fig2, ax2 = plt.subplots()
        ax2.legend()
        ax2.set_title('Fitness Promedio')
        ax2.set_ylabel('Fitness')
        ax2.set_xlabel('Number of generation')

        counter = 0
        flag = False
    # Set up end
    # Expand and scatter one point
    once = True
    if once:
        ax1.set(xlim=(0, len(historic_generations)), ylim=(0, 50))
        ax1.scatter(counter, menor_fitness(generation), color='r', label="F")
        print(menor_fitness(generation))
        ax2.set(xlim=(0, len(historic_generations)), ylim=(0, 50))
        ax2.scatter(counter, avg_fitness(generation), color='b')
        print(avg_fitness(generation))
        counter += 1
        once = False
    # End of plot
    print("next gen")

    for i in range(len(next_generation)):
        print(next_generation[i])

    historic_generations.append(next_generation)


    # Expand and scatter one point
    ax1.set(xlim=(0, len(historic_generations)), ylim=(0, 50))
    ax1.scatter(counter, menor_fitness(next_generation), color='r', label="F")
    print(menor_fitness(next_generation))
    ax2.set(xlim=(0, len(historic_generations)), ylim=(0, 50))
    ax2.scatter(counter, avg_fitness(next_generation), color='b')
    print(avg_fitness(next_generation))
    counter += 1
    # End of plot

    bestFitnessOld = best_fitness(generation)
    bestFitnessNew = best_fitness(next_generation)

    return bestFitnessOld, bestFitnessNew, generation, next_generation


# lector de input
input_cruce, cruce_var1, cruce_var2, input_seleccion_1, seleccion_var_1, \
input_seleccion_2, seleccion_var_2, input_seleccion_3, seleccion_var_3, \
input_seleccion_4, seleccion_var_4, input_implementacion, input_mutacion, \
mutacion_var, input_corte, corte_var, threshold_var, individuo_var, N, K, A, B = read_input()

# primer generacion
generation_zero = generate_random_character(type, N)
historic_generations = list()
historic_generations.append(generation_zero)


# funcion de corte
@corte_wrapper
def corte(*args):
    bestFitnessOld, bestFitnessNew, generation, next_generation = iterate(historic_generations[-1], \
                                                                          input_cruce, cruce_var1, cruce_var2,
                                                                          input_seleccion_1, seleccion_var_1,
                                                                          input_seleccion_2, \
                                                                          seleccion_var_2, input_seleccion_3,
                                                                          seleccion_var_3, input_seleccion_4,
                                                                          seleccion_var_4, \
                                                                          input_implementacion, input_mutacion,
                                                                          mutacion_var, input_corte, corte_var,
                                                                          threshold_var, individuo_var, N, K, A, B)
    return bestFitnessOld, bestFitnessNew, generation, next_generation


# start
corte(input_corte, corte_var, threshold_var, individuo_var)
# Show plot
plt.tight_layout()
plt.show()

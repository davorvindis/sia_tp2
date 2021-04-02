import time as time

# Recibe: una funcion,  Devuelve: una funcion que se ejecuta hasta un criterio de corte
def corte_wrapper(fn):
    def inner1(*args):
        if args[0] == "time":
            start = time.time()
            while time.time() - start < args[1]:
                fn()

        if args[0] == "generation":
            i = args[1]
            while i > 0:
                fn()
                i -= 1
    return inner1

# Funcion que se va a wrappear en el criterio de corte, va a correr en loop
@corte_wrapper
def corte(*args):
    iter()

def iter():
    print("1")



# Criterios de corte (0/5)
#    * Tiempo
#    * Cantidad de generaciones
#    * Solucion aceptable
#    * Estructura
#    * Contenido

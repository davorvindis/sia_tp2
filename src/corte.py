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
    return inner1






# Criterios de corte (0/5)
#    * Tiempo
#    * Cantidad de generaciones
#    * Solucion aceptable
#    * Estructura
#    * Contenido

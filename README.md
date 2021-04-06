README.md
Sistemas de Inteligencia Artificial Repositorio para la materia Sistemas de inteligencia artificial - TP 2

Dentro del repositorio de encontraran carpetas con los distintos trabajos practicos:

Librerias utilizadas:
- Numpy
- MatplotLib

Archivo de configuración de parámetros : ../input/input_parameters

Ejemplo de configuración de ejecución: 

{
  "cruce" : "1p",
  "variables_cruce": ["2"],
  "mutacion": "gen",
  "variables_mutacion": ["1"],
  "seleccion_1": "boltzmann",
  "variables_seleccion_1": [],
  "seleccion_2": "elite",
  "variables_seleccion_2": [],
  "seleccion_3": "torneo_deterministico",
  "variables_seleccion_3": ["3"],
  "seleccion_4": "ruleta",
  "variables_seleccion_4": [],
  "implementacion": "fill-all",
  "corte": "aceptable",
  "variables_corte": ["3"],
  "corte_threshold":["0.001"],
  "k_individuos":["5"],
  "N": 3,
  "K": 2,
  "A": 0.3,
  "B": 0.5
}

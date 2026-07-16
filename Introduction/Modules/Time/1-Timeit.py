""" 
Módulo timeit

El módulo timeit está diseñado para medir con precisión el tiempo
que tarda en ejecutarse un fragmento de código. A diferencia del módulo time,
timeit ejecuta el código varias veces y calcula el tiempo de forma más confiable,
reduciendo la influencia de otros procesos del sistema. Es una herramienta muy
utilizada para comparar el rendimiento de algoritmos, funciones o diferentes
formas de resolver un mismo problema. Sus funciones más importantes son timeit(),
que mide el tiempo de ejecución de un bloque de código repetido varias veces, y
repeat(), que realiza varias mediciones para obtener resultados más consistentes.
"""

from timeit import *


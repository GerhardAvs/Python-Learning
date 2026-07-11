"""Python nos facilita un módulo (un conjunto de funciones
disponibles para su uso) que nos permite generar selecciones
pseudo-aleatorias* entre valores o secuencias."""

"""                from random import *
Nombre del módulo
* = Todos los métodos también pueden importarse de manera independiente aquellos a utilizar.
randint(min, max): devuelve un integer entre dos valores dados (ambos límites
incluidos)
uniform(min, max): devuelve un float entre un valor mínimo y uno máximo
random(sin parámetros): devuelve un float entre 0 y 1
choice(secuencia): devuelve un elemento al azar de una secuencia de valores
(listas, tuples, rangos, etc.)
shuffle(secuencia): toma una secuencia de valores mutable (como una lista), y la
retorna cambiando el orden de sus elementos aleatoriamente."""

from random import *

aleatorio = randint(1,50) # Random del 1 al 50
print(f'Random de int: {aleatorio}')

aleatorio = round(uniform(1,5),1) # Random con decimal del 1 al 5. round() es para redondear
print(f'Random de float: {aleatorio}')

aleatorio = random()
print(f'Random: {aleatorio}') # Elige fracciones de un entero

colores = ['azul','rojo','verde','amarillo']
aleatorio = choice(colores)
print(f'Random de listas: {aleatorio}') # Elige fracciones de un entero

numeros = list(range(5,50,5)) # inicia en 5, da pasos en 5 y acaba en 50
shuffle(numeros) # Mezcla aleatoria
print(f'Random de elementos en listas: {numeros}')
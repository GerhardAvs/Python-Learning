""" 
namedtuple

Una namedtuple es una tupla cuyos elementos tienen nombre.

Devuelve una tupla donde las posiciones de sus elementos tienen un
nombre, además de un número de índice como las tuplas tradicionales.
"""

from collections import namedtuple

tupla = (3,4,7)

print(tupla[1])

instance = namedtuple('Persona',['Nombre','Edad','Peso'])
ariel = instance('Ariel', 29, 74)
print(ariel.Edad)
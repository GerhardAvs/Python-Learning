"""
Counter

Counter es una clase del módulo collections 
diseñada para contar automáticamente cuántas
veces aparece cada elemento dentro de un iterable.

En lugar de recorrer una lista e ir aumentando un
contador manualmente, Counter realiza ese trabajo 
en una sola línea.

Es una subclase del diccionario, usado para contar las
repeticiones de cada elemento en un iterable, en forma de diccionario:
"""
from collections import Counter

serie = [1,1,1,1,1,2,2,2,2,3,4,4,4,5,5,5,6,6]

print(f'Se aplica counter: {Counter(serie)}')


serie = Counter([1,1,1,1,1,2,2,2,2,3,4,4,4,5,5,5,6,6])

print(f'Se aplica metodo most common al counter: {serie.most_common()}')
print(f'Se aplica metodo most common al counter, primeros dos: {serie.most_common(2)}')

print(Counter('Misisipi'))

phrase = 'Al pan, pan, y al vino, vino'
print(Counter(phrase.split()))

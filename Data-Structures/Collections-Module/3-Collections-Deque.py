

from collections import deque


lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

lista_ciudades.pop()#Elimina por la derecha
lista_ciudades.popleft()
lista_ciudades.appendleft('añadido por izq')

print(lista_ciudades)
mi_lista =['a', 'b','c']
print(type(mi_lista))


resultado = len(mi_lista)
print(resultado)

resultado = mi_lista[0]
print(resultado)

resultado = mi_lista[0:2]
print(resultado)

mi_lista2 = ['d','e','f']
print(mi_lista + mi_lista2)

mi_lista3 = mi_lista + mi_lista2
mi_lista3[0] = 'alfa'
print(mi_lista3)

mi_lista3.append('g')
print(mi_lista3)

eliminado = mi_lista3.pop(1) #elimina elementos
print(mi_lista3)
print(eliminado)


lista = ['g','o','b','m','c']
lista.sort()
print('sort',lista) # nontype es el resultado de un objeto que no devuelve nada

lista.reverse()
print(lista)

lista.clear()
print(lista)

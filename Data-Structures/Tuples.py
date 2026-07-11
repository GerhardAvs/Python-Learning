#Los tuples son inmutables, a prueba de daños
# ocupan menos espacio en ram

mi_tuple = (1,2,3,4) # tambien se puede mi_tuple = 1,2,3,4
print(type(mi_tuple))

t = (5, 5.8, 'ff')
print(t[0]) # indexar
print(t[-2]) # indexar
# t[0] = 10
# print(t[0]) No se puede hacer, los tuples no soportan cambiar datos

dos_tuple = (1, 2, (10, 20), 4) # Anidar, poner un tuple dentro de otro tuple
print(dos_tuple[2])
print(dos_tuple[2][0])

mi_tuple = list(mi_tuple)#casting: convertir un tipo de dato a otro
print(type(mi_tuple))

mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

t2 = (100, 200, 300)
x,y,z = t2 #desempaca los valores de t2 en cada variable
print('variable 1: ', x, 'variable 2: ', y, 'variable 3: ', z) 

t3 = (1,2,3,1)
print(len(t3)) #cantidad de elementos en el tuple
print(t3.count(1)) #cuenta la cantidad de valores repetidos
print(t3.index(2)) #se consulta la posición del número 2

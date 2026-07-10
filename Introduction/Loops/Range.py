"""La función range( ) devuelve una secuencia de números dados
3 parámetros. Se utiliza fundamentalmente para controlar el
número de ejecuciones de un loop o para crear rápidamente
una serie de valores.

 range(valor_inicio, valor_final, paso)
 print(list(range(1,13,3)))
  >> [1,4,7,10]"""

lista = [1,2,3,4]

for numero in range(5): # El 5 no esta incluido
    print(numero)         # Va del 1 al 4

print('\n')
for number in range(20, 31 , 3): # Va de 20 a 31 de 3 en 3
    print(number)

print('\n')
list = list(range(1, 101))
print(list)

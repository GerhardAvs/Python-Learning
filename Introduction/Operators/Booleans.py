"""mi_bool = true o mi_bool = false o mi_bool = 5 < 4 , se pueden usar los siguientes:
<=, >=, !=, ==, mi_bool = 5 in mi_lista, 5 not in mi_lista"""

var1 = True
var2 = False
print(type(var1))
print(f'var1: {var1}\nvar2: {var2}')

numero = 5 > 2+3
print('\n',type(numero))
print(numero)

numero2 = bool(5 > 6)
print('\n',type(numero2))
print(numero2)

lista = [1,2,3,4]
control = 5 in lista #5 se encuentra en lista?, not in: 5 no se encuentra en lista?
print('\n',type(control))
print(control)

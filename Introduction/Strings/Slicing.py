texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5] # va desde el hasta el 4, el 5 no se incluye
print(fragmento)
fragmento = texto[2:10:2] # va salteando de 2 en 2 hasta el 9
print(fragmento)
fragmento = texto[::3] # va desde el primer espacio hasta el ultimo, tomando valores de 3 en 3
print(fragmento)

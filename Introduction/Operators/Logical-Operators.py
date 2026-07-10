# and or no
mi_bool = 4 < 5 < 6
print(mi_bool)

mi_bool2 = 4 < 5 > 6
print(mi_bool2)

mi_bool3 = 4 < 5 and 5 > 6
print(mi_bool3)

mi_bool4 = (55 == 55) and ('perro' == 'perro')
print(mi_bool4)

mi_bool5 = 4 == 5 or 5 >= 6
print(mi_bool5)

texto = 'esta frase es breve'
mi_bool6 = ('frase' in texto) and ('breve' in texto)
print(mi_bool6)

mi_bool7 = not 'a' == 'a'
print(mi_bool7)

mi_bool7 = not ('a' != 'a')
print(mi_bool7)

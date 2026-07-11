"""La función min( ) retorna el item con el valor más bajo dentro
de un iterable. La función max( ) funciona del mismo modo,
devolviendo el valor más alto del iterable. Si el iterable contiene
strings, la comparación se realiza alfabéticamente."""


"""ciudades_habitantes = {"Tijuana":1810645,"León":1579803}
lista_valores = [5**5, 12**2, 3050, 475*2]

print(min(ciudades_habitantes.keys()))
>> León
print(max(ciudades_habitantes.values()))
>> 1810645
print(max(lista_valores))
>> 3125"""

menor = min(58,94,59,607,69)
mayor = max(58,94,59,607,69)
print(f'menor: {menor}\nmayor: {mayor}')

print()

lista = [58,94,59,607,69]
print(f'menor {min(lista)}')
print(f'mayor {min(lista)}')

print()

lista_nom = ['juan', 'pablo', 'alicia', 'carlos']
print(min(lista_nom))
print(max(lista_nom))

print()

name = 'carlos'
print(min(name))
print(max(name))

print()

name2 = 'Carlos'
print(min(name2))
print(max(name2))

print()

dict = {'C1':45, 'C2':11}
print(min(dict))
print(max(dict))
print(min(dict.values()))
print(max(dict.values()))
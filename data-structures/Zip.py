"""La función zip( ) crea un iterador formado por los elementos
agrupados del mismo índice provenientes de dos o más
iterables. Zip deriva de zipper (cremallera o cierre), de modo
que es una analogía muy útil para recordar."""


Nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['Lima', 'Madrid', 'Mexico']

combinados = list(zip(Nombres,edades,ciudades))
print(combinados)

print('\n')

for nombres, edades, ciudades in combinados:
    print(f'{nombres} tiene {edades} años y vive en {ciudades}')
    
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

for pais, capital in zip(paises,capitales):
    print(f'la capital de {pais} es {capital}')
    
espanol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
ingles = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(espanol, portugues, ingles))

print(numeros)

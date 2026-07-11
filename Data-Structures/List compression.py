"""La comprensión de listas ofrece una sintaxis más breve en la
creación de una nueva lista basada en valores disponibles en
otra secuencia. Vale la pena mencionar que la brevedad se
logra a costo de una menor interpretabilidad."""


palabra = 'python'
lista = []

for letra in palabra:
    lista.append(letra) # agrega valores a las listas
    
print(f'Metodo mas largo: {lista}')

print('Metodos cortos')

lista2 = [letra for letra in 'python']
print(lista2)

lista3 = [numero for numero in range(0,21,2)]
print(lista3)

lista4 = [n/2 for n in range(0,21,2)]
print(lista4)

lista5 = [n if (n * 2) > 10 else 'no' for n in range(0,21,2)]
print(lista5)

pies = [10,20,30,40,50]
metros = [p * 3.281 for p in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares = [v  for v in valores if v%2 == 0]
print(valores_pares)

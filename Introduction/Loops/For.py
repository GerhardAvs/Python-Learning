lista = ['a', 'b', 'c', 'd']
for letra in lista:
    num_letra = lista.index(letra) + 1
    print(f'Indice {num_letra}, letra: {letra}')

print('\n')
lista = ['Pablo', 'Laura', 'Fede', 'Luis', 'Julia']
for nombre in lista:
    if nombre.startswith('L'): #Si nombre inicia con L
        print(nombre)
    else:
        print('Nombre que no comenza con L')
        
print('\n')     
numeros = [1,2,3,4,5]  
valor = 0
for numero in numeros:
    valor += numero
    print(f'Valores dentro del for {valor}')
print(f'\nValor final {valor}')

print('\n')     
palabra = 'Python'
for letra in palabra:
    print(palabra)
    
print('\n')     
for letra in 'Python':
    print(letra)

print('\n')     
for obj in [[1,2], [3,4], [5,6]]:
    print(obj)
    
print('\n')     
for a, b in [[1,2], [3,4], [5,6]]:
    print(f'Valor a: {a}, valor b: {b}')
    
print('\n')     
dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}
for item,valor in dic.items():
    print(f'item: {item}, valor: {valor}')
    

    

# pablabras clave: brake, continue, pass
monedas = 5
while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -= 1
else:
    print('No tengo mas dinero')
    
print('\n')
respuesta = 'Y'
while respuesta == 'Y':
    respuesta = input('Deseas seguir? (Y/N): ')
else:
    print('Gracias\n')
    
nombre = input('Tu nombre: ')
for letra in nombre:
    if letra == 'r':
        pass
    else:
        print(letra)

"""for elementos in precios_cafe:
    print(elementos)
print()

for cafe, precio in precios_cafe:
    print(cafe, precio)
print()"""
precios_cafe = [('Capuchino',1.5), ('Expresso', 2.7), ('Moka', 1.9)]

def cafe_mas_caro(lista_precios):
    mayor = 0
    cafe_mas_caro = ''
    for cafe,precio in lista_precios:
        if precio > mayor:
            mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return (cafe_mas_caro, mayor)

cafe,precio = cafe_mas_caro(precios_cafe)
print(f'El cafe mas caro es {cafe}, con un precio de {precio}')

"""-----------------------------------------------------------------------"""
from random import shuffle
#lista inicial 
palitos = ['---','-','--']
#mezclar palitos
def mezclar_palitos(lista):
    shuffle(lista)
    return lista
#pedirle intento
def intentos():
    intento = ''
    while intento not in ['1','2','3']:
        intento = input('Elige un numero del 1 al 3: ')
    return int(intento)

#comprobar intento
def comprueba(lista,intento):
    if lista[intento-1] == '-':
        print('Escogiste el mas pequeno')
    else:
        print('Te salvaste')
    print(f'Te ha tocado {lista[intento-1]}')
    
palitos_mezclados = mezclar_palitos(palitos)
seleccion = intentos()
comprueba(palitos_mezclados, seleccion)

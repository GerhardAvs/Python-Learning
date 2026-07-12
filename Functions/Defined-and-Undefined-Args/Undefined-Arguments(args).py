"""En aquellos casos en los que no se conoce de antemano el
número exacto de argumentos que se deben pasar a una
función, se debe utilizar la sintaxis *args para referirse a todos
los argumentos adicionales luego de los obligatorios."""

"""El nombre *args no es mandatorio pero si es sugerido como buena práctica.
Cualquier nombre iniciado en * referirá a estos argumentos de cantidad variable"""

def suma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

def suma2(*args):
    return sum(args)

print(suma(6,5,2,3,4))
print(suma2(6,5,2,3,4))
print()
def suma_cuadrados(*args):
    x=0
    for n in args:  
        x += n**2
    return x
    
print(suma_cuadrados(1,2,3))
print()

def suma_absolutos(*args):
    k = 0
    for n in args:
        if n >= 0:
            k += n
        else:
            k += n*-1
    return k
print(suma_absolutos(-1,-1,-2,-2))
print()
def numeros_persona(nombre,*args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'
print(numeros_persona('Gerardo',1,2,3,4,5))

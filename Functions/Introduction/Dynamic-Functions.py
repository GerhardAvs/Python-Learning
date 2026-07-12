"""La integración de diferentes herramientas de control de flujo,
nos permite crear funciones dinámicas y flexibles. Si debemos
utilizarlas varias veces, lograremos un programa más limpio y
sencillo de mantener, evitando repeticiones de código"""

"""     Funciones
        Loops (for/while)
        Estructuras condicionales
        Palabras clave (return, break, continue, pass)"""
        
def chequear_3cifraspt1(numero):
    return numero in range(100,1000)

number = int(input('Deteccion de numero de tres cifras: '))
resultado = chequear_3cifraspt1(number)
print(resultado)


def chequear_3cifraspt2(lista):
    lista2 = []
    for n in lista:
        if n in range(100,1000):
            lista2.append(n)
        else:
            pass  
    return lista2

resultado2 = chequear_3cifraspt2([555,77,680])
print(resultado2)
print()

from random import *

def lanzar_dados():
    Dado1 = randint(1,6)
    Dado2 = randint(1,6)
    return Dado1, Dado2
    
def evaluar_jugada(resultado1,resultado2):
    
    suma_dados = resultado1 + resultado2
    if suma_dados <= 6:
        mensaje = f'La suma de tus dados es {suma_dados}. Lamentable'
    elif suma_dados > 6 and  suma_dados < 10:
        mensaje = f'La suma de tus dados es {suma_dados}. Tienes buenas chances'
    else:
        mensaje = f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora'
    return mensaje
    
x,y = lanzar_dados()
print(evaluar_jugada(x,y))            

print()
def reducir_lista(lista):
      
    return set(lista)
    
def promedio(lista):
    prom = 0
    i = 0
    for n in lista:
        prom += n
        i += 1
    return prom/i
    
lista_numeros = [1,2,15,7,2]
lista_reducida = reducir_lista(lista_numeros)
print(lista_reducida)
print(promedio(lista_reducida))
print()
def todos_positivos(lista):
    for n in lista:
        if n < 0:
            return False
    return True

lista_numeros = [1, -50, 502, -5000, 755, 600, 33, 61]
print(todos_positivos(lista_numeros))


def cantidad_pares(lista):
    conta = 0
    for numero in lista:
        if numero%2 == 0:
            conta += 1
    return conta
    
    
lista_numeros = [1,2,3,4,5]
print(cantidad_pares(lista_numeros))

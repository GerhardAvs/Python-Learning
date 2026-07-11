""" 
Existen estrategias para capturar y gestionar los errores que
pueden presentarse al ejecutar un programa, a fines de evitar
una falla mayor y controlar la información que es mostrada al
usuario.
"""

def al_cuadrado():
    number = int(input('Ingresa un numero: '))
    result = number**2
    
    print(f'El cuadrado del numero {number} es {result}')
    print('Gracias por calcular el cuadrado')


try:
    #El codigo que puede fallar
    al_cuadrado()
except ValueError:
    #El codigo de se ejecuta si falla
    print('Ese no es un número')
else:
    #Codigo a ejecutar si no falla
    print('Todo correcto')
finally:
    #El codigo que siempre se ejecuta
    print('Eso es todo')
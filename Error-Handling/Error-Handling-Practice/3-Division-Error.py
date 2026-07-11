""" 
Práctica Manejo de Errores 2
Hemos visto en la lección de qué manera 
se implementa el manejo de errores habitualmente 
en Python. En el caso de este ejercicio, sin embargo,
necesitaré que lo hagamos de una forma ligeramente 
distinta para que pueda ser evaluado: deberás implementarlo
DENTRO de la función. En forma de comentario, verás un ejemplo
de resolución. Ten presente, sin embargo, que la forma preferida
es la que hemos visto en clase.

Implementa para la siguiente función cociente(), 
un manejador de errores:

Ante un error de tipo (TypeError), debe imprimir en 
pantalla el mensaje: "Los argumentos a ingresar deben ser números"

Si se generara una división por cero (error del tipo ZeroDivisionError),
[el mensaje mostrado debe ser: "El segundo argumento no debe ser cero"

En caso que no se produzca un error, deberá limitarse a imprimir el 
resultado del cociente (división) entre los dos números entregados
como argumento.
"""
"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""

def cociente(num1,num2):
    try:     
        print(num1/num2)
    
    except TypeError:
        print('Los argumentos a ingresar deben ser números')
 
    except ZeroDivisionError:
        print('El segundo argumento no debe ser cero')

    
cociente(1,1)
cociente(1,'s')
cociente(0,0)
    
    
#MENSAJE EN PANTALLA
"Los argumentos a ingresar deben ser números"
"El segundo argumento no debe ser cero"
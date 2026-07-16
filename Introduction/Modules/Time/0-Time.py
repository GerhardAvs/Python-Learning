""" 
Módulo time

El módulo time permite trabajar con el tiempo de ejecución 
de un programa. Con él es posible obtener la hora actual en
segundos desde una fecha de referencia (timestamp), pausar la
ejecución durante un tiempo determinado y medir cuánto tarda en 
ejecutarse una parte del código. Es muy utilizado para crear temporizadores,
realizar esperas entre procesos, controlar la velocidad de ejecución
de programas y evaluar el rendimiento de algoritmos. 
Algunas de sus funciones más importantes son time(), sleep(), localtime() 
y strftime(), las cuales facilitan el manejo y el formato del tiempo.
"""

from time import *
import Lists_Function

inicio = time() #INICIO del cronometro
Lists_Function.prueba_for(10)
#print(prueba_for(10))
fin = time()

print(f"En la prueba for, transcurrio: {fin-inicio} segundos\n")

inicio = time() #INICIO del cronometro
Lists_Function.prueba_while(10)
#print(prueba_while(10))
fin = time()
print(f"En la prueba while, transcurrio: {fin-inicio} segundos")


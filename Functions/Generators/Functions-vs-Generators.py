""" 
generadores

Los generadores son tipos especiales de funciones que
devuelven un iterador que no almacena su contenido
completo en memoria, sino que "demora" la ejecución de una
expresión hasta que su valor se solicita
"""

def mi_funcion():
    list = [x*10 for x in range(4)]
    return list

def mi_generador():
    for x in range(5):
        yield x*10
    
print(mi_funcion()) 
print(mi_generador())

g = mi_generador()
for _ in range(5):
    print(next(g))

# print(next(g)) 
# StopIteration Error al pedir un valor al generador cuando ya termino

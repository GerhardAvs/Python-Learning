""" 
Práctica Módulo RE 2
Crea una función llamada verificar_saludo para verificar si una 
frase entregada como argumento inicia con la palabra "Hola". Si se
encuentra el patrón, la función debe finalizar mostrando el mensaje
"Ok", pero si detecta que la frase no contiene "Hola", debe informarle
al usuario "No has saludado" imprimiendo el mensaje en pantalla.
"""

import re

def verificar_saludo(frase):
    pattern = r"^Hola"
    search = re.search(pattern, frase)
    
    print ("Ok" if search else "No has saludado")
    
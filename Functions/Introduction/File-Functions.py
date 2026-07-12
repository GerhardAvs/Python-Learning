"""Crea una función llamada abrir_leer() que abra (open)
un archivo indicado como parámetro, y devuelva su contenido (read)."""
def abrir_leer(file):
    archivo = open(file)
    contenido = archivo.read()
    archivo.close()
    return contenido

"""Crea una función llamada sobrescribir() que abra (open) 
un archivo indicado como parámetro, y sobrescriba cualquier 
contenido anterior por el texto: contenido eliminado"""
def sobrescribir(file):
    archivo = open(file, 'w')
    archivo.write('contenido eliminado')
    
"""Crea una función llamada registro_error() que abra (open)
un archivo indicado como parámetro, y lo actualice añadiendo
una línea al final que indique "se ha registrado un error de
ejecución". Finalmente, debe cerrar el archivo abierto."""
def registro_error(file):
    archivo  = open(file, 'a')
    archivo.write("se ha registrado un error de ejecución")
    archivo.close()
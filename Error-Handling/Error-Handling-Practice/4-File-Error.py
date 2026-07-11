""" 
Práctica Manejo de Errores 3
Hemos visto en la lección de qué manera se 
implementa el manejo de errores habitualmente en Python. 
En el caso de este ejercicio, sin embargo, necesitaré que 
lo hagamos de una forma ligeramente distinta para que pueda 
ser evaluado: deberás implementarlo DENTRO de la función. 
En forma de comentario, verás un ejemplo de resolución. 
Ten presente, sin embargo, que la forma preferida es la que hemos visto en clase.

Implementa un manejador de errores dentro de la siguiente 
función, abrir_archivo():
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

def abrir_archivo(nombre_archivo):
    try:
     archivo = open(nombre_archivo)
     
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print ("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")
        
#MENSAJES EN PANTALLA:
"El archivo no fue encontrado"
"Error desconocido"
"Abriendo exitosamente"
"Finalizando ejecución"
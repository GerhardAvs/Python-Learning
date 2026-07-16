""" 
Librería os

La librería os permite a Python interactuar con el sistema operativo. 
Es muy utilizada para obtener información del directorio actual, crear o 
eliminar carpetas, renombrar archivos, verificar si un archivo existe y 
trabajar con rutas. Es una de las librerías más importantes para automatizar
tareas relacionadas con el manejo de archivos y directorios. Algunos métodos 
muy utilizados son os.getcwd(), os.chdir(), os.mkdir(), os.makedirs() y 
os.path.exists().
"""

import os

#Da la direccion del workspace
print(os.getcwd())

file = open(r"Files\Curso.txt","w")
#file = open("Files\\Curso.txt","w")
#file = open(r"Files/Curso.txt","w")
file.write("Texto de prueba")

print(os.listdir())
file.close()

#Eliminar carpetas
"""
   os.unlink()
   os.rmdir()
"""



#Recorre rutas
print(os.walk(r"c:users"))#Tipo generador

#r"" cadena literal sin procesar
path = r"C:\Users\Gerardo AvSn\OneDrive\Programacion\Python-Learning\Introduction"
for carpeta, subcarpetas, archivos in os.walk(path):
    print(f"En la carpeta {carpeta}\n"
          "Las subcarpetas son: ")
    for sub in subcarpetas:
        print(f"\t{sub}")
        
    for arch in archivos:
        print(f"\{arch}")
    
    print("\n")
        
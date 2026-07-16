""" 
Librería shutil

La librería shutil está diseñada para realizar operaciones
de alto nivel sobre archivos y carpetas. A diferencia de os,
ofrece funciones listas para copiar, mover y eliminar directorios 
completos de forma sencilla. Entre sus funciones más importantes se
encuentran shutil.copy(), shutil.copy2(), shutil.move() y shutil.rmtree().
Es la mejor opción cuando necesitas gestionar archivos de manera rápida y 
con menos código.
"""

import shutil

#Mover el archivo mediante shutil.move
#No puedes mover un archivo que esta abierto
shutil.move(r"Files\Curso.txt", r"File-Moved")

#Eliminar archivos
shutil.rmtree() #Elimina una carpeta con todo lo que tiene adentro
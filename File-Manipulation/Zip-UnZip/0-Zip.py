""" 
comprimir y descomprimir archivos


El formato zip permite comprimir archivos sin pérdida de
información, ahorrando espacio de almacenamiento y
manteniendo documentos relacionados en un mismo archivo
.zip.

"""

import zipfile
import os

print(os.getcwd())
path = "Zip_Files.zip"
my_zip = zipfile.ZipFile(path, "w")
my_zip.write("mi_texto_A.txt")
my_zip.write("mi_texto_B.txt")
my_zip.close()
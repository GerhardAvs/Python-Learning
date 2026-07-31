import os
#cwd = current working directory
#chdir = change directory
"""Nos da la ruta del directorio que se tiene actualmente"""
path = os.getcwd()
print(f'ruta: {path}')

"""Cambia el directorio del OS"""
path = os.chdir('C:\\Users\\Gerardo AvSn\\OneDrive\\Programacion\\Python\\Ruta alterna')
print(path)
file = open('Directorios.txt', 'r')
print(file.read())
file.close()

"""No existe la carpeta, la crea
ruta = os.makedirs('C:\\Users\\Gerardo AvSn\\OneDrive\\Programacion\\Python\\Ruta alterna\\otra')
archivo = open('otro_archivo.txt')
print(archivo.read())
archivo.close() """

ruta = 'C:\\Users\\Gerardo AvSn\\OneDrive\\Programacion\\Python\\Ruta alterna\\otra\\otro_archivo.txt'
elemento = os.path.basename(ruta)
print(elemento)
elemento = os.path.dirname(ruta)
print(elemento)
elemento = os.path.split(ruta)
print(elemento)

"""Remover carpetas
os.rmdir('C:\\Users\\Gerardo AvSn\\OneDrive\\Programacion\\Python\\Ruta alterna\\otra')
"""
"""Abrir archivos sin libreria os
otro_archivo = open('C:\\Users\\Gerardo AvSn\\OneDrive\\Programacion\\Python\\Ruta alterna\\otra\\otro_archivo.txt')
print(otro_archivo.read())"""

"""Metodo para que cualquier SO pueda abrir la ruta"""
from pathlib import Path
carpeta = Path('C:/Users/Gerardo AvSn/OneDrive/Programacion/Python/Ruta alterna/otra')
archivo = carpeta / 'otro_archivo.txt'
mi_archivo = open(archivo)
print(mi_archivo.read())
"""Metodo para que cualquier SO pueda abrir la ruta"""
from pathlib import Path, PureWindowsPath
carpeta = Path('C:/Users/Gerardo AvSn/OneDrive/Programacion/Python/Ruta alterna/otra')
archivo = carpeta / 'otro_archivo.txt'
mi_archivo = open(archivo)
print(mi_archivo.read())

file = Path('C:/Users/Gerardo AvSn/OneDrive/Programacion/Python/ManipulacionArchivos/PruebaPathlib.txt')
if not file.exists():
    print('Este archivo no existe')
else:
    print('Genial, existe')
    
print(file.read_text())
print(file.name)
print(file.suffix)
print(file.stem)

ruta_windows = PureWindowsPath(file)
print(ruta_windows)

"""Crear o mover archivos, enumerarlos, rutas basadas en strings"""
from pathlib import Path

base = Path.home() # Directorio principal
guia = Path(base,'Ameria','Mexico',Path('Ciudad_de_Mexico','Estadio_GNP.txt')) # Directorio principal + El creado
guia2 = guia.with_name('la_Pedrera.txt')
print(base)
print(guia)
print(guia.parent) # devuelve el antecesor mas inmediato
print(guia.parent.parent)
print(guia2)

guia3 = Path(Path.home(), 'Europa')
print(guia3)
print()
for txt in Path(guia3).glob('**/*.txt'):
    print(txt)
print()

guia4 = Path('Europa', 'España', 'Barcelona', 'Sagrada_Familia.txt')
en_europa = guia4.relative_to(Path('Europa'))
eN_espania = guia4.relative_to(Path('Europa', 'España'))
print(en_europa)
print(eN_espania)
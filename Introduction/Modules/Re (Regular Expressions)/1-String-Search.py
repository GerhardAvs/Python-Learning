import re

text = "if you need help call (658)-598-9977 they bring 24 hours service"
pattern = "help"
search = re.search(pattern, text)
#<re.Match object; span=(12, 16), match='help'>
print(f"Busqueda: {search}")
print(f"Rango de coincidencia: {search.span()}")
print(f"Inicio de la palabra: {search.start()}")
print(f"Fin de la palabra: {search.end()}")

print()

#Buscar todas las coincidencias de una palabra
text2 = """
Learning Python

Python is a simple and powerful programming language.
It is used for web development, data analysis, artificial intelligence,
and automation. Many beginners choose Python because its syntax is easy
to read and understand. By practicing every day, anyone can improve their
programming skills and create useful applications.
"""

pattern2 = "Python"

for match in re.finditer(pattern2, text2):
    print(f"Se encontraron coincidencias en: {match.span()}")
print(text2[10:16])
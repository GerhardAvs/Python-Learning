r""" 
\d
0 1 2 3 4 5 6 7 8 9

\D
letras, espacios, símbolos, signos de puntuación, etc.

\w 
letras (a-z, A-Z)
Números (0-9)
Guion bajo (_)
"""

import re 

text = "llama al 555-887-4567 ya mismo"
pattern = r"\d{3}-\d{3}-\d{4}"
#pattern = r"\d\d\d-\d\d\d-\d\d\d\d"

search = re.search(pattern,text)
#<re.Match object; span=(9, 21), match='555-123-4567'>
print(f"El numero encontrado es: {search.group()}")
print()

#Buscar en distintos grupos
pattern2 = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
search2 = re.search(pattern2,text)

print(f"Primer grupo: {search2.group(1)}")
print(f"Segundo grupo: {search2.group(2)}")
print(f"Tercero grupo: {search2.group(3)}")



key = input("Introduce una clave: ")
pattern = r"\D{1}\w{7}"

result = re.search(pattern,key)
print(result)
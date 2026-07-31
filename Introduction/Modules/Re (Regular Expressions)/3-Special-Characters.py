r"""
[ ] un set de caracteres
. un carácter cualquiera
^ inicia con
$ finaliza con
* cero o más ocurrencias
+ una o más ocurrencias
{ } un número especificado de ocurrencias
? cero o una ocurrencia
| operador lógico O
"""

import re

text = "No atendemos los martes"

#Busca lunes o martes en el texto
buscar = re.search("lunes|martes",text)
print(f"Aplicando | (or): {buscar.group()}")

#buscar = re.search("demos",text)
#buscar = re.search(r"demos",text)
buscar = re.search(r"...demos",text)#letras que estan antes de demos
print(f"Aplicando . (cada punto imprime una letra atras): {buscar.group()}")

buscar = re.search(r"^\D",text)#palabra que esta antes de demos
print(f"Aplicando ^ con \D (verifica el inicio del texto): {buscar.group()}")

buscar = re.search(r"\D$",text)#palabra que esta antes de demos
print(f"Aplicando $ con \D (verifica el final del texto): {buscar.group()}")

buscar = re.findall(r"[^\s]",text)#palabra que esta antes de demos
print(f"Aplicando [^\s] (devuelve todo menos los espacios vacios): {buscar}")

buscar = re.findall(r"[^\s]+",text)#palabra que esta antes de demos
print(f"Aplicando [^\s]+ (devuelve todo menos los espacios vacios): {buscar}")


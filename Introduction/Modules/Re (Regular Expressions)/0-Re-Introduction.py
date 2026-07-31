r"""  
expresiones regulares

Una expresión regular es una secuencia de caracteres que
forman un patrón de búsqueda determinado. Pueden ser
utilizadas para verificar strings en búsqueda de un contenido
(patrón) específico. Utilizamos el módulo re en Python.

Funciones:

search( ): devuelve un objeto match que contiene información acerca del
hallazgo si se encuentra en algún punto del string

findall( ): devuelve una lista que contiene todos los hallazgos del patrón

[ ] un set de caracteres
. un carácter cualquiera
^ inicia con
$ finaliza con
* cero o más ocurrencias
+ una o más ocurrencias
{ } un número especificado de ocurrencias
? cero o una ocurrencia
| operador lógico O

\d dígito numérico
\D NO numérico
\w caracter alfanumérico
\W NO alfanumérico
\s espacio en blanco
\S NO espacio en blanco
"""

import re

text = "if you need help call (658)-598-9977 they bring 24 hours service"
word = "help" in text

print(word)
print()

pattern = "help"
search = re.search(pattern, text)
#<re.Match object; span=(12, 16), match='help'>
print(search)
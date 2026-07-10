"""upper() pasa a mayusculas
   lower() pasa a minusculas
   split() separarlo en partes(lista)
   join() unir items usando separador
   find() encontrar un sub-string
   replace() reemplazar un substring
"""
texto = "Este es el texto de Gerardo"

result = texto.upper()
print(result)
result = texto[2].upper()
print(result)

result = texto.lower()
print(result)

result = texto.split()
print(result)
result = texto.split("t") # Separa desde las t  y las elimina
print(result)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)

result = texto.find("s")
print(result)

result = texto.replace("Gerardo", "Nadie") # Cambia Gerardo por Nadie
print(result)

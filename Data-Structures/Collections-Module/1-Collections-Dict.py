""" 
defaultdict

defaultdict es un diccionario que crea 
automáticamente un valor cuando una clave aún no existe.

Es una subclase del diccionario, usado para proporcionar valores por
defecto para las claves que no existan, sin generar un mensaje de error. El valor por
defecto puede ser un tipo de dato (int, list, etc.) o una función lambda que proporcione
dicho valor directamente (lambda:
"mi valor").

"""

from collections import defaultdict

mi_dict = {'UNO':'Verde', 'DOS':'Azul','TRES':'Rojo'}
mi_dict = defaultdict(lambda: 'nada', mi_dict)#Para que no se rompa al buscar algo que no hay
print(mi_dict['CUATRO'])
print(mi_dict)
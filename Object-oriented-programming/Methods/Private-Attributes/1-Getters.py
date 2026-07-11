""" 
En Python, un método get se utiliza para obtener (consultar) 
el valor de un atributo de un objeto. 
Es parte del concepto de encapsulamiento, donde los atributos suelen 
hacerse privados y se accede a ellos mediante métodos.
"""

class Persona:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido #__nombre/apellido son valiables privadas
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
Persona1 = Persona('Gerardo', 'Avalos')

print(f'El objeto Persona1, tiene nombre {Persona1.get_nombre()}'
      f' y apellido {Persona1.get_apellido()}')
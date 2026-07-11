""" 
@property es un decorador de Python que permite acceder 
a un método como si fuera un atributo. Se utiliza principalmente
para controlar el acceso a los atributos de una clase sin cambiar
la forma en que se usan.

Un decorador es una forma de modificar o agregar 
comportamiento a una función o método sin cambiar su código interno.
"""

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    @property #Getter
    def nombre(self):
        return self.__nombre
    
    @nombre.setter #setter
    def nuevo_nombre(self, Nuevo_Nombre):
        self.__nombre = Nuevo_Nombre

Persona1 = Persona('Gerardo')
print(Persona1.nombre)#con propery no se usa () para las funciones\

Persona1.nuevo_nombre = 'Luis'
print(Persona1.nombre)#con propery no se usa () para las funciones\

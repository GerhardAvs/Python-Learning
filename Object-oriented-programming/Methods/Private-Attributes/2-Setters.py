class Persona:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido #__nombre/apellido son valiables privadas
        
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_apellido(self, apellido):
        self.__apellido = apellido
    
Persona1 = Persona('Gerardo', 'Avalos')

print(f'El objeto Persona1, tiene nombre {Persona1.get_nombre()}'
      f' y apellido {Persona1.get_apellido()}')

Persona1.set_nombre('Alan')
Persona1.set_apellido('Montes')

print(f'El objeto Persona1, tiene nombre {Persona1.get_nombre()}'
      f' y apellido {Persona1.get_apellido()}')
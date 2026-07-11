"""
herencia

La herencia es el proceso mediante el cual una clase puede
tomar métodos y atributos de una clase superior, evitando
repetición del código cuando varias clases tienen atributos o
métodos en común

Es posible crear una clase "hija" con tan solo pasar como parámetro la clase de la
que queremos heredar:

class Personaje:
    def __init__(self, nombre, herramienta):
    self.nombre = nombre
    self.arma = arma
    
class Mago(Personaje):
    pass

hechicero = Mago("Merlín","caldero")

Una clase "hija" puede sobreescribir los métodos o atributos, así como definir
nuevos, que sean específicos para esta clase.
"""

class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
        
    def nacer(self):
        print('El animal ha nacido')

class Pajaro(Animal):
    pass

class Mamifero(Animal):
    pass

print(Pajaro.__bases__)#Herencia
print(Animal.__subclasses__())
print()
piolin = Pajaro(2, 'Amarillo')
piolin.nacer()
print(piolin.edad)
print(piolin.color)
"""Las clases "hijas" que heredan de las clases superiores, pueden
crear nuevos métodos o sobrescribir los de la clase "padre".
Asimismo, una clase "hija" puede heredar de una o más clases,
y a su vez transmitir herencia a clases "nietas".

Si varias superclases tienen los mismos atributos o métodos, la subclase sólo podrá
heredar de una de ellas. En estos casos Python dará prioridad a la clase que se
encuentre más a la izquierda.
Del mismo modo, si un mismo método se hereda por parte de la clase "padre", e"hija", 
la clase "nieta" tendrá preferencia por aquella más próxima ascendente
(siguiendo nuestro esquema, la tomará de la clase "hija")

class hija:
metodos heredados
metodos modificados
metodos nuevos"""

class Animal:
# Se ejecuta automáticamente cada vez que creas un objeto
# de esa clase y sirve para inicializar sus atributos.
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    
    def nacer(self):
        print('El animal ha nacido')
    
    def hablar(self):
        print('El animal emite sonido')

class Pajaro(Animal):
    
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo
        
    def hablar(self):#sobre escribio el metodo hablar y ahora dice pio
        print('pio')

    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros, con una altura de' +
              f' {self.altura_vuelo} metros')

simba = Animal(12, 'Marron')
piolin = Pajaro(2, 'Amarillo', 50)
piolin.nacer()
piolin.hablar()
piolin.volar(12)
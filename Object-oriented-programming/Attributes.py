class Pajaro:
    alas = True
    
    def __init__(self, mi_color): # Constructor es una funcion
        self.color = mi_color
        
mi_Pajaro = Pajaro('negro')
print(mi_Pajaro.color)

mi_Pajaro.color = 'rojo'
print(mi_Pajaro.color)
print(mi_Pajaro.alas)

"""INIT es una funcion especial que se ejecuta al crear una instancia de la clase
   SELF es una referencia a la instancia actual de la clase"""
 
class Leon:
    hambriento = False
    
    def __init__(self, parametro, especie):
        self.atributo = parametro
        self.especie = especie

mi_leon = Leon('marrón', 'African')

print(f'\n{mi_leon.atributo}')
print(mi_leon.especie)
print(mi_leon.hambriento)

class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


casa_blanca = Casa('blanco', 4)

class Cubo:
    caras = 6
    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo('rojo')

class Personaje:
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico 
        self.edad = edad

harry_potter = Personaje('Humano', True, 17)
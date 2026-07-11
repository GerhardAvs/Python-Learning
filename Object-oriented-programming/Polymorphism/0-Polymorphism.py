"""
El polimorfismo es el pilar de la POO mediante el cual un mismo
método puede comportarse de diferentes maneras según el
objeto sobre el cual esté actuando, en función de cómo dicho
método ha sido creado para la clase en particular    
"""

class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print('mu')    
        
class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        for i in range(3):
            print(f"Beee {i + 1}")
            
vaca1  = Vaca('vaquina')
oveja1 = Oveja('Ovejina')

'''vaca1.hablar()
oveja1.hablar()'''

'''animales_granja = [vaca1, oveja1]

for animal in animales_granja:
    animal.hablar()'''
    
def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)
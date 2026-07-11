class Padre:
    def Hablar(self):
        print('Hola')

class Madre:
    def Reir(self):
        print('ja ja ja')
        
    def Hablar(self):
        print('Que tal?')
        
class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.Hablar()
mi_nieto.Reir()
print()

print(Nieto.__mro__)
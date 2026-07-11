"""
Los métodos estáticos y de clase anteponen
un decorador específico, que indica a Python el
tipo de método que se estará definiendo

-------------------------------------------------------------------------------------------------
     Metodos        l   de instancia   l   de clase @classmethod   l estaticos @staticmethod    l
----------------------------------------------------------------------------------------------- l
acceso a metodos    l      si          l        si                 l        x                   l
y atributos de la   l                  l                           l                            l
clase               l                  l                           l                            l
------------------------------------------------------------------------------------------------l
requiere una        l      si          l        no                 l       no                   l
instancia           l                  l                           l                            l
------------------------------------------------------------------------------------------------l
acceso a métodos y  l      si          l        no                 l       no                   l
atributos de la     l                  l                           l                            l
instancia           l                  l                           l                            l
------------------------------------------------------------------------------------------------l

Así como los métodos de instancia requieren del parámetro self para acceder a
dicha instancia, los métodos de clase requieren del parámetro cls para acceder
a los atributos de clase. Los métodos estáticos, dado que no pueden acceder a
la instancia ni a la clase, no indican un parámetro semejante.
"""

class Pajaro:
    alas = True
    
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f'pio\nMi color es {mi_pajaro.color}')
        
    def volar(self, metros): #Metodo de instancia
        print(f'El pajaro ha volado {metros} metros')
        self.piar()
        
    def pintar_negro(self):
        self.color = 'negro'
        print(f'El pajaro ahora es {self.color}')
    
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} de huevos')
        cls.alas = False
        print(Pajaro.alas)
        
    @staticmethod #Metodos que no se pueden modificar
    def mirar():
        print('El pajaro mira')


mi_pajaro = Pajaro('blanco', 'paloma')
mi_pajaro.piar()
print()
mi_pajaro.volar(270)
print('\nMetodo de instancia')
mi_pajaro.pintar_negro()
print(mi_pajaro.color)
print()
mi_pajaro.alas = False
print(mi_pajaro.alas)
print()
mi_pajaro.poner_huevos(2) 


print('\nMetodo de clase')
Pajaro.poner_huevos(4) #se puede pq es metodo de clase

print('\nMetodo estatico')
Pajaro.mirar()
mi_pajaro.mirar()







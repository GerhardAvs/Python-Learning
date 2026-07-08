'''Práctica Polimorfismo 2
Cuentas con tres clases de personajes en un juego,
los cuales cuentan con sus métodos de ataque específicos.

Crea un iterador que logre un ataque conjugado en el 
siguiente orden: Arquero, Mago, Samurai, llamando al método 
atacar() de cada uno de los personajes. Deberás crear instancias
de cada una de las clases anteriores para construir un iterable 
(una lista llamada personajes) que pueda recorrese en dicho orden.'''

class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
    
    

Personajes = [Arquero(), Mago(), Samurai()]

def atacar(list):
    for i in list:
        i.atacar()
        
atacar(Personajes)
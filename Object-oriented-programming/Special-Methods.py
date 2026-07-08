"""
Puedes encontrarlos con el nombre de métodos mágicos o dunder
methods (del inglés: dunder = double underscore, o doble guión
bajo). Pueden ayudarnos a sobrescribir métodos incorporados de
Python sobre nuestras clases para controlar el resultado devuelto.
"""

class CD:
    def __init__(self,autor,titulo,n_canciones):
        self.autor = autor
        self.titulo = titulo
        self.ncanciones = n_canciones

    def __str__(self): # Cuando imprimimos del objeto, agarra este metodo
        return f"CD {self.autor} de {self.autor} con {self.ncanciones} canciones"
       
    def __len__(self):
        return self.ncanciones 
    
    def __del__(self):
        print(f'El CD de \'{self.autor}\' ha sido eliminado')
        
mi_CD = CD("Pink Floyd", "The wall", 24)
print(mi_CD) # usa __str__
print(len(mi_CD))

del mi_CD #elimina el objeto


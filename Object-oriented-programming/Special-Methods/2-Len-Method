""" 
Práctica Métodos Especiales 2
Dada la clase Libro, implementa el método 
especial __len__ para que cada vez que se ejecute
la función len() sobre el mismo, devuelva el número 
de páginas como número entero.
"""

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return round(self.cantidad_paginas)
        
mi_libro = Libro('Hadas', 'Jeff', 27.4)
print(len(mi_libro))
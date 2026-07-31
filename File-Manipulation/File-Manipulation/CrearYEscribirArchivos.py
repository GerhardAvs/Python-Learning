"""Creacion de archivos"""
archivo = open(r"C:\Users\Gerardo AvSn\OneDrive\Programacion\Python\ManipulacionArchivos\Creado.txt", "w", encoding="utf-8")
archivo.write('Soy el nuevo texto\nHola mundo') # cambias la w por a para escribir desde el final
#archivo.write(['hola','mundo','aqui','estoy']) tambien se puede
archivo.close()

archivo = open(r"C:\Users\Gerardo AvSn\OneDrive\Programacion\Python\ManipulacionArchivos\Creado.txt", "a", encoding="utf-8")
lista = ['hola','mundo','aqui','estoy']
print()    
for p in lista:
    archivo.write(p + '\n')
archivo.close()
"""Lee todo el archivo"""
file = open(r"C:\Users\Gerardo AvSn\OneDrive\Programacion\Python\ManipulacionArchivos\Prueba.txt", "r", encoding="utf-8")
print(file.read()) #Lee todo
print()
file.close()


""""Se muestra con salto de linea"""
file2 = open(r"C:\Users\Gerardo AvSn\OneDrive\Programacion\Python\ManipulacionArchivos\Texto.txt", "r", encoding="utf-8")
una_linea = file2.readline() #Lee una linea, en este caso, la primera
print(una_linea)
una_linea = file2.readline() #Lee una linea, en este caso, la segunda
print(una_linea)
una_linea = file2.readline() #Lee una linea, en este caso, la tercera
print(una_linea)
file2.close()

"""Quita el salto de linea"""
file3 = open(r"C:\Users\Gerardo AvSn\OneDrive\Programacion\Python\ManipulacionArchivos\Notas.txt", "r", encoding="utf-8")
una_linea = file3.readline() #Lee una linea, en este caso, la primera
print(una_linea.lower()) # Pasa todo a minuscula
una_linea = file3.readline() #Lee la segunda y quita el salto de linea
print(una_linea.rstrip())
una_linea = file3.readline() #Lee una linea, en este caso, la tercera
print(una_linea)
file3.close()

print()

"""Lee todas las lineas con un ciclo"""
file = open(r"C:\Users\Gerardo AvSn\OneDrive\Programacion\Python\ManipulacionArchivos\Prueba.txt", "r", encoding="utf-8")
for linea in file:
    print(f'Aqui dice: {linea.rstrip()}')
file.close()

print()

"""Leer todas las lineas y hacerlos lista"""
file = open(r"C:\Users\Gerardo AvSn\OneDrive\Programacion\Python\ManipulacionArchivos\Prueba.txt", "r", encoding="utf-8")
todas = file.readlines()
print(todas)
file.close()
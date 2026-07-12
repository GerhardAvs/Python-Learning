"""Para que una función pueda devolver un valor (y que pueda
ser almacenado en una variable, por ejemplo), utilizamos la
declaración return."""

"""def mi_funcion():
        return [algo]
        
            La declaración return provoca la salida de la función
            Cualquier código que se encuentre después en el bloque de
            la función, no se ejecutará"""
            
"""def multiplicar(x,y):
    total = x*y
    return total  """       
       
def multiplicar(x,y):
    return x*y

resultado = multiplicar(5,200)
print(resultado)

def invertir_palabra(palabra):
    return palabra[::-1].upper()
palabra =  "Curso"
print(invertir_palabra(palabra))

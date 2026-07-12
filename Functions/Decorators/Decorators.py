"""def mayuscula(text):
    print(text.upper())
    
mi_funcion = mayuscula
   mi_funcion('python')  TODO ES UN OBJETO"""
   
""" 
def mayuscula(text):
    print(text.upper())
    
Una funcion puede tener como parametro otra funcion
  
def una_funcion(funcion):
    return funcion

una_funcion(mayuscula('probando'))"""

def cambiar_letra(type):
    def mayuscula(text):
        print(text.upper())
        
    def minuscula(text):
        print(text.lower())   
    
    if type == 'May': return mayuscula
    else: return minuscula 
    
cambiar_letra('May')('Palabra')

#OR

opc = cambiar_letra('Min')
opc('PYTHON')
    
#Example 2

def mi_decorador(funcion):
    def otra_funcion(palabra):
        print('\nHola')
        funcion(palabra)
        print('Adios')
    return otra_funcion

@mi_decorador  
def mayuscula(text):
    print(text.upper())
    
@mi_decorador       
def minuscula(text):
    print(text.lower())
    
mayuscula('EJEMPLO 2 -- ABCDEFG')
minuscula('EJEMPLO 2 -- ABCDEFG')

"""Los argumentos con palabras clave (keyword arguments,
abreviado kwargs), sirven para identificar el argumento por su
nombre, independientemente de la posición en la que se
pasen a su función. Si no se conoce de antemano su cantidad,
se utiliza el parámetro **kwargs que los agrupa en un
diccionario."""

def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += 1
    print(kwargs)
    print(type(kwargs))
    return(total)
    
print(suma(x=3,y=5,z=2))
print()

def prueba(num1,num2,*args,**kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')
    for argumento in args:
        print(f'argumento = {argumento}')
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')
args = [100,200,3004,0,40,32]
kwargs = {'c':'2','r':'3','t':'4','g':'5','n':'-6'}
prueba(15,50,*args,**kwargs) # o tambien prueba(15,50,100,200,3004,0,40,32,c=2,r=3,t=4,g=5,n=-6)
print()

def cantidad_atributos(**kwargs):
    return len(kwargs)
print()

def lista_atributos(**kwargs):
    return list(kwargs.values())

print()
def describir_persona(nombre, **kwargs):
    print(f'Características de {nombre}:')
    for clave,valor in kwargs.items():
        print(f'{clave}: {valor}')

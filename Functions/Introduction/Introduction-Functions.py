"""Una función es un bloque de código que solamente se ejecuta
cuando es llamada. Puede recibir información (en forma de
parámetros), y devolver datos una vez procesados como
resultado"""

def saludar_persona():
    print('hola')

def saludar_persona2(nombre):
    print(f'hola {nombre}')

saludar_persona() #Llama la funcion
saludar_persona2('Fernando')
saludar_persona2('Javier')

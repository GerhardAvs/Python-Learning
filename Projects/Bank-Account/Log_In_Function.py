import os
import Client_Class
from random import randint

def crear_cliente(flag):
    os.system('cls')
    if flag == False:
        nombre = str(input('Deme su nombre: '))
        apellido = str(input('Deme su apellido: '))
        balance = 0
        cuenta = randint(100,1000)
        print(f'Cuenta creada con exito, numero de cuenta {cuenta}')
        
        return Client_Class.cliente(nombre,apellido, cuenta, balance)
    
    else:
        print('La cuenta inicio con exito')
        return Client_Class.cliente('Ger', 'Avs', 90107, 20450)
import sys
import os
from random import randint
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
class cliente(Persona):
    def __init__(self,nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre,apellido)
        self.numero = numero_cuenta
        self.balance = balance
    
    def __str__(self):
        os.system('cls')
        return f'La cuenta {self.numero} tiene un balance de {self.balance}'

    def depositar(self, deposito):
        os.system('cls')
        self.balance += deposito
        print(f'Se depositaron {deposito} pesos a la cuenta {self.numero}')
        print(f'Balance: {self.balance}')

    def retirar(self, retiro):
        os.system("cls")
        if retiro > self.balance: print('No puedes retirar mas de lo que tienes')
        else: 
            self.balance -= retiro
            print(f'Se retiraron {retiro} pesos a la cuenta {self.numero}')
        print(f'Balance: {self.balance}')
        
def crear_cliente(n):
    os.system('cls')
    if n == 0:
        nombre = str(input('Deme su nombre: '))
        apellido = str(input('Deme su apellido: '))
        balance = 0
        cuenta = randint(100,1000)
        print(f'Cuenta creada con exito, numero de cuenta {cuenta}')
        
        return cliente(nombre,apellido, cuenta, balance)
    
    else:
        print('La cuenta inicio con exito')
        return cliente('Ger', 'Avs', 90107, 20450)

while True:
    input('Presiona Enter para continuar...')

    print('\n/////////////////////')
    print('//////  Menu  ///////')
    print('/////////////////////')
    print('1.Crear cliente')
    print('2.Iniciar sesion')
    print('3.Depositar')
    print('4.Retirar')
    print('5.Imprimir datos')
    print('6.Salir')
    opc = int(input('Escoge una opcion: '))

    monto = 0
    
    match opc:
        case 1:
            cuenta = crear_cliente(0)
        case 2:
            cuenta = crear_cliente(1)
        case 3:
            monto = float(input('Monto a depositar: '))
            cuenta.depositar(monto)
        case 4:
            monto = float(input('Monto a retirar: '))
            cuenta.retirar(monto)
        case 5:
            print(cuenta)
        case 6:
            sys.exit()
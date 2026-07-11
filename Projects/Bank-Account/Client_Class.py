import os

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
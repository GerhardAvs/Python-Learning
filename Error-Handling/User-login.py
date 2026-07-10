def pedir_numero():
    while True:
        try:
            numero = int(input('ingresa un numero: '))
        
        except:
            print('Ese no es un numero')
            
        else:
            print(f'Ingresaste {numero}')
            break
        
pedir_numero()
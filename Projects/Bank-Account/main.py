import sys
import Log_In_Function

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
            cuenta = Log_In_Function.crear_cliente(False)
        case 2:
            cuenta = Log_In_Function.crear_cliente(True)
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
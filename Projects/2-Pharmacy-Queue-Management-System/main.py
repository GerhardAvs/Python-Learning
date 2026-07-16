import sys
import os

import Modulos



while True:
    try:
        match Modulos.Menu():
            case 1: 
                
                module = Modulos.Elegir_Modulo()
                if module == 1: Modulos.Medicina()
                elif module == 2: Modulos.Cosmeticos()
                else: Modulos.Farmacia()
                
            case 2:
                pass
            case 3:
                sys.exit()
    except:
        os.system('cls')
        print('\n/////Error inesperado////')
        input('Presiona Enter para reiniciar...')
        os.system('cls')
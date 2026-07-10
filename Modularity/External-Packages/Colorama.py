#pip install colorama
from colorama import Fore, Style, init
init()

nombre = 'Backup diario'
exito = False

if exito:
    print(Fore.GREEN + f'{nombre} completado correctamente' + Style.RESET_ALL)
else: 
    print(Fore.RED + f'{nombre} fallo' + Style.RESET_ALL)
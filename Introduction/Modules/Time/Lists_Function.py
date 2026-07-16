def prueba_for(numero):
    lista = []
    
    for num in range(numero + 1):
        lista.append(num)
        
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    
    while contador <= numero:
        lista.append(contador)
        contador += 1
        
    return lista

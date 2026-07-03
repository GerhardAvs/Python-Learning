"""En Python 3.10, se incorpora la coincidencia de patrones
estructurales mediante las declaraciones match y case. Esto
permite asociar acciones específicas basadas en las formas o
patrones de tipos de datos complejos."""

serie = 'N-02'

match serie:
    case 'N-01':
        print('Samsung')
    case 'N-02':
        print('Nokia')
    case 'N-02':
        print('Motorola')
    case _:
        print('No existe el producto') 
        
cliente = {'name':'Federico',  
           'edad':45, 'ocupacion':'instructor'}
pelicula = {'titulo': 'Matrix',
            'ficha_tecnica': {'protagonista':'Keanu reeves',
                              'director': 'Lana y Lilly wachowski'}}
elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre':nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print('Es un cliente ')
            print(nombre, edad, ocupacion)
        
        case {'titulo': titulo,
              'ficha_tecnica': {'protagonista':protagonista},
                                'director': director}:
            print('Es una pelicula')
            print(titulo,protagonista,director)
            
        case _:
            print('No se que es esto')

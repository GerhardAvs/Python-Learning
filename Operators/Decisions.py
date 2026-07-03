#if elif else

if 10 > 9:
    print('1.Es correcto')
    
if True:
    print('2.Es correcto')
    
x = True
if x:
    print('3.Es correcto')
    
if 5 == 2:
    print('4.Es correcto')
else:
    print('4.No es correcto')

mascota = 'perro'
if mascota == 'gato':
    print('5.Tienes un gato')
elif mascota == 'perro':
    print('5.Tienes un perro')
else:
    print('5.No se que animal tienes')
    
edad = 16
calificacion = 9
if edad < 18:
    print('6.Eres menor de edad')
    if calificacion >= 7:
        print(' 6.1 Aprobado')
    else:
        print(' 6.1 No apronado')
else:
    print('6.Eres un adulto')

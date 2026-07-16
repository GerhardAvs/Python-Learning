""" 
Librería datetime

La librería datetime permite trabajar con fechas y 
horas de forma sencilla en Python. Con ella es posible
obtener la fecha y hora actuales, crear fechas específicas,
realizar operaciones como sumar o restar días, comparar fechas
y darles diferentes formatos para mostrarlas al usuario. 
Es una de las librerías más utilizadas en aplicaciones que 
necesitan registrar eventos, generar reportes, manejar calendarios o 
calcular períodos de tiempo. Sus clases más importantes son date, time, 
datetime y timedelta, cada una enfocada en un aspecto diferente del manejo 
del tiempo.
"""

import datetime 
#para evidar datetime.date
#from datetime import date

"""Establecer Hora"""
print("Hora establecida manualmente: ")
mi_hora = datetime.time(17,35) #17hrs, 35min
print(type(mi_hora))
print(mi_hora)
print(mi_hora.hour)
print(mi_hora.minute)
print()

print("Segunda Hora establecida manualmente: ")
mi_hora = datetime.time(17,35,15,1220) #17hrs, 35min 15sec 1220 milisec
print(mi_hora)
print()

"""Establecer Dia"""
print("Dia establecido manualmente: ")
mi_dia = datetime.date(2026, 7, 15) #ano, mes, dia
print(mi_dia)
print(mi_dia.year)
print(mi_dia.ctime())#Muestra un mejor formato para la hora
print()

"""Establecer Dia"""
print("Dia establecido automaticamente: ")
mi_dia = datetime.date.today()
print(mi_dia)
print()

"""Establecer Dia"""
print("Dia establecido manuealmente con .datetime(): ")
mi_fecha = datetime.datetime(2026, 11, 11, 18, 20, 2, 3000)
print(mi_fecha)

#reemplazar fecha
mi_fecha = mi_fecha.replace(month=3)
print(mi_fecha)
print()

"""Diferencia Entre Fechas"""
print("Diferencia entre fechas: ")
nacimiento = datetime.date(1995,3,5)
muerte = datetime.date(2095,6,19)
tiempo_vivo = muerte - nacimiento

print(f"Nacimiento: {nacimiento}")
print(f"Muerte: {muerte}")
print(f"Tiempo vivo: {tiempo_vivo}")
print()


"""Tiempo Despierto"""
print("Diferencia entre fechas: ")
Despierto = datetime.datetime(2026,4,11,7,30)
Duerme = datetime.datetime(2026,4,11,23,45)
tiempo_despierto = Duerme - Despierto

print(f"Despierto: {Despierto}")
print(f"Durmiendo: {Duerme}")
print(f"Tiempo despierto: {tiempo_despierto}")
print()

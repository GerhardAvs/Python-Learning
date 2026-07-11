# set(1,2,3,4,5) o {1,2,3,4,5} o mi_set = (['a', 'b', 'c'])

#Los sets son mutables, no son ordenados en indices (index) y no admite duplicados
#Los sets no admiten listas dentro de ellos ni diccionarios

mi_set = set([1,2,3,4,5,6,7])
print(type(mi_set), )
print(mi_set, '\n')

#otro_set = {1,2,3,1,1,[2,4],2,2,2,3,3} no se pueden poner listas
otro_set = {1,2,3,1,1,1,1,2,2,2,3,3} #python elimina las repeticiones
print(type(otro_set))
print(otro_set, '\n')

otrotro_set = set([1,2,(1,2,3)]) #si admite tuples
print(type(otrotro_set))
print(otrotro_set, '\n')

mi2_set = {1,2,3,4}
print(len(mi2_set))
print(2 in mi2_set, '\n')

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3,'\n')

s4 = {1,2,3,4}
s4.add(5) #agrega
print(s4)
s4.remove(3) #quita 
print(s4)
s4.discard(3) #descarta
print(s4)
s4.pop() #elimina un elemento aleatorio
print(s4)
s4.clear() #limpia el set
print(s4)



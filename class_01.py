#Crear lista
Lista = [1, 5, 25, 100, 500]
print("inicial: ", Lista)

#Agregra un dato al final de la lista

Lista.append(250)
print("append: ", Lista)

#extend = Toma una segunda lista y agrega sus datos a la primera 
Lista2 = [75, 125]
Lista.extend(Lista2)
print("extend :", Lista)

#Insert = agregamos datos en la posicion indicada

Lista.insert(2,400)
print("insert :", Lista)

#Remove = Busca y elimina el dato entregado

Lista.remove(400)
print("remove :", Lista)

#pop = Elimina el ultimo registro

Lista.pop()
print("pop :", Lista)

#pop(posci.) elimina la posicion indicada

Lista.pop(5)
print("pop :", Lista)

#reverse = Invierte el orden de la lista

Lista.reverse()
print("reverse :", Lista)

#sort = es para ordenar de menor a mayor

Lista.sort()
print("sort :", Lista)

#sort(reverse=True) = ordena de mayor a menor

Lista.sort(reverse=True)
print("sort(r) :", Lista)
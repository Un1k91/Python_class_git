#Array son tipos de arreglos y tienen 3 tipos de dimenciones, (1D = arreglos unidimencionales), (2D = arreglos bidimencionales), (3D = arreglos multidimencionales).
#Contro + shift + n = terminal

import numpy as np
lista = [1,2,3,4,5]
arreglo = np.array(lista)
print(arreglo)

#ndim = indica cuantas dimenciones posee el arreglo
print(f"El arreglo es de {arreglo.ndim} dimension")

#Len = indica el largo del arreglo
print(f"El arreglo es de largo {len(arreglo)}")

#Slice
#star,stop,step = indica cuanto quiero mostrar del arreglo
#Start = indica desde donde vamos a consultar, stop = indica hasta donde vamos a consultar, step = indica en cuanto en cuanto vamos a consultar

print(arreglo[::2])

#Rellenar arreglo
#for
lista2 = [i for i in range(1,11)]
arreglo2 = np.array(lista2)
print(arreglo2)

#arange(Star,Stop,Step) = rellenar el arreglo con valores segun lo indicamos

arreglo3 = np.arange(1,11)
print(arreglo3)
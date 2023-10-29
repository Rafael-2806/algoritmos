#Ordena de forma de selección directa n^2


#recorro la lista busco el mas pequeño y lo pongo el primero, recorro la lista busco el 2º más pequeño y lo pongo el segundo 

def selection_sort(lista):
    # Recorre todos los elementos de la lista
    for i in range(len(lista)):
        # Encuentra el mínimo en la lista[i..len(lista)-1]
        idx_min = i
        for j in range(i+1, len(lista)):
            if lista[idx_min] > lista[j]:
                idx_min = j

        # Intercambia el mínimo encontrado con el primer elemento
        lista[i], lista[idx_min] = lista[idx_min], lista[i]

    return lista

# Prueba
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
selection_sort(lista)
print("Lista ordenada:", lista)
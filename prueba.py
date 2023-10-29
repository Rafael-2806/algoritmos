

def selection_sort(lista):
    # Recorre todos los elementos de la lista
    for i in range(len(lista)):
        # Encuentra el mínimo en la lista[i..len(lista)-1]
        minimo = i
        print(minimo)
       
# Prueba
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
selection_sort(lista)
print("Lista ordenada:", lista)
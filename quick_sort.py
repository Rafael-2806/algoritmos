#quick sort 
#Mejor caso: cuando el pivote seleccionado divide siempre la lista en dos partes aproximadamente iguales log2 n
#Peor caso: Si el pivote es siempre el menor o el mayor elemento de la lista, la partición es muy desigual n^2

# La idea básica del QuickSort es elegir un elemento llamado "pivote" y particionar la lista en dos sub-listas: la primera con elementos menores 
# que el pivote y la segunda con elementos mayores que el pivote. Luego, QuickSort se aplica recursivamente a estas dos sub-listas.

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        # Tomamos el primer elemento como pivote
        pivote = lista[0]
        # Crear una sub-lista de elementos menores que el pivote
        menores = [x for x in lista[1:] if x <= pivote]
        # Crear una sub-lista de elementos mayores que el pivote
        mayores = [x for x in lista[1:] if x > pivote]
        # Combina las listas y aplica quicksort recursivamente
        return quicksort(menores) + [pivote] + quicksort(mayores)

# Prueba
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
lista_ordenada = quicksort(lista)
print("Lista ordenada:", lista_ordenada)
#insert sort n^2

#De ordenación. Como cuando ordenas las cartas coges carta y la metes en la posición correcta comparando con las que tienes

def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1

        # Mueve los elementos de la lista[0..i-1] que son mayores que la clave
        # a una posición adelante de su posición actual
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave

    return lista

# Prueba
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
insertion_sort(lista)
print("Lista ordenada:", lista)

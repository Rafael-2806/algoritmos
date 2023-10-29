#

#Imaginamos que nuestro array esta tumbado. Las burbujas  mas pequeñas van subiendo:compara con el de arriba y si es mas 
# pequeña se cambian. En la primera pasada el mas pequeño esta arriba 3
def ordenacion_burbuja(lista):

    for i in range(len(lista)):
        # Comparar el elemento actual con el siguiente
        for j in range(0, len(lista)-i-1):
            if lista[j] > lista[j+1]:
                # Si el elemento actual es mayor que el siguiente, los intercambiamos
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
ordenacion_burbuja(lista)
print("Lista ordenada:", lista)
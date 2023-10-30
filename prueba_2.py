


def quicksort(lista):
    
    if len(lista)<=1:
        return lista
    else:
        pivote= lista[0]
        
        menores= [x for x in lista[1:] if x <=pivote]
        mayores= [x for x in lista[1:] if x >pivote]
        return quicksort(menores)+ [pivote]+ quicksort(mayores)

# Prueba
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
lista_ordenada = quicksort(lista)
print("Lista ordenada:", lista_ordenada)
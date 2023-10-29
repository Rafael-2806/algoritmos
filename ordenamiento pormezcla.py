#merge sort  t= log2 n

#voy dividiendo  por la mitad y voy ordenando en subgrupos y subiendo y ordenando grupo


def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    # División de la lista en mitades
    mitad = len(lista) // 2
    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])

    # Combinar las mitades ordenadas
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    if not izquierda:
        return derecha
    if not derecha:
        return izquierda

    if izquierda[0] < derecha[0]:
        return [izquierda[0]] + merge(izquierda[1:], derecha)
    return [derecha[0]] + merge(izquierda, derecha[1:])

# Prueba
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)

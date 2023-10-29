#busqueda binaria  log n

#DividoSi lo de la izquierda es mas grande me desplazo a la derecha y voy partiendo el espacio de búsqueda

def busqueda_binaria(arr, x):
    l = 0
    h = len(arr) - 1
    mid = 0

    while l <= h:
        mid = (h + l) // 2

        # Si el elemento está presente en el medio
        if arr[mid] < x:
            l = mid + 1

        # Si el elemento es más pequeño, ignora la mitad derecha
        elif arr[mid] > x:
            h = mid - 1

        # x está presente en mid
        else:
            return mid

    # Si no encontramos el elemento
    return -1
# Prueba
lista = [12, 22, 34, 64, 90]
x = 64

# Resultado
resultado = busqueda_binaria(lista, x)
if resultado != -1:
    print(f"El elemento {x} está presente en el índice {resultado}.")
else:
    print(f"El elemento {x} no se encuentra en la lista.")
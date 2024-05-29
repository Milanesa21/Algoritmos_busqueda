""" Busqueda lineal
Si 'x' esta en la lista, devuelve su posicion
si no esta, devuelve '-1'
"""

# Se recorren uno a uno los elementos de la lista 
# y se los compara con el valor buscado

def busqueda_lineal(lista, x):
    i = 0 # i tiene la posicion actual en la lista, la cual comienza en 0

    # El ciclo recorre todos los elementos de la lista
    for z in lista:

        # Si z es igual a x, devuelve el valor de i
        if z == x:
            return i
        i = i+1
    # Si salio del ciclosin haber encontrado el valor, devuelve -1
    return -1


"""
Resultados de ejemplo:
 >>> busqueda_lineal([1, 4, 54, 3, 0, 34, 23, 12], 2)
-1
>>> busqueda_lineal([1, 4, 54, 3, 0, 34, 23, 12], 23)
6
>>> busqueda_lineal([1, 4, 54, 3, 0, 34, 23, 12], 4)
1
"""
print(busqueda_lineal([1, 4, 54, 3, 0, 34, 23, 12], 2))
print(busqueda_lineal([1, 4, 54, 3, 0, 34, 23, 12], 23))
print(busqueda_lineal([1, 4, 54, 3, 0, 34, 23, 12], 4))
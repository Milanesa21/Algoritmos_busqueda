""" Busqueda lineal
Si 'x' esta en la lista, devuelve su posicion
si no esta, devuelve '-1'
"""

# Se importa la libreria time para medir el tiempo de ejecucion
import time

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


# Se crea una funcion para medir el tiempo de ejecucion
def medir_tiempo(func, *args):
    # Se toma el tiempo de inicio
    inicio = time.time()
    # Se ejecuta la funcion con los argumentos
    resultado = func(*args)
    # Se toma el tiempo de finalizacion
    fin = time.time()
    # Se muestra el resultado y el tiempo de ejecucion  
    tiempo_transcurrido = fin - inicio
    print(f"Resultado: {resultado}, Tiempo de ejecución: {tiempo_transcurrido:.8f} segundos")


"""
Resultados de ejemplo:
Resultado: -1, Tiempo de ejecución: 0.00000286 segundos
Resultado: 6, Tiempo de ejecución: 0.00000191 segundos
Resultado: 1, Tiempo de ejecución: 0.00000167 segundos
"""



medir_tiempo(busqueda_lineal, [1, 4, 54, 3, 0, 34, 23, 12], 2)
medir_tiempo(busqueda_lineal, [1, 4, 54, 3, 0, 34, 23, 12], 23)
medir_tiempo(busqueda_lineal, [1, 4, 54, 3, 0, 34, 23, 12], 4)
import time

"""
Busqueda Binaria.
"""

def busqueda_binaria(vector, numero):
    # La variable puntero será el inicio del vector, que es 0
    puntero = 0

    # VectorLen contiene la longitud del vector
    vectorLen = len(vector) - 1

    # La variable encontrado cambiará su valor, y así el algoritmo sabrá qué hacer
    encontrado = False

    # Creamos un bucle que no se detenga hasta que encontrado deje de ser False
    # y que puntero sea menor o igual que vectorLen
    while not(encontrado) and puntero <= vectorLen:

        # Creamos la variable mitad
        mitad = int((puntero + vectorLen) / 2)

        # Si numero es igual que el índice mitad en vector
        if numero == vector[mitad]:
            # Cambiamos el valor de encontrado a True
            encontrado = True
        elif numero < vector[mitad]:
            # vectorLen será igual a mitad - 1
            vectorLen = mitad - 1
        else:
            # Puntero será igual a mitad + 1
            puntero = mitad + 1

    # Si encontrado es true
    if encontrado:
        # Devolvemos la posición del dato en el vector
        return mitad + 1
    else:
        # Devolvemos -1 indicando que el número no se encuentra en el vector
        return -1

# Función para medir el tiempo de ejecución
def medir_tiempo(func, *args):
    # Se toma el tiempo de inicio
    inicio = time.time()
    # Se ejecuta la función con los argumentos
    resultado = func(*args)
    # Se toma el tiempo de finalización
    fin = time.time()
    # Se muestra el resultado y el tiempo de ejecución
    tiempo_transcurrido = fin - inicio
    print(f"Resultado: {resultado}, Tiempo de ejecución: {tiempo_transcurrido:.8f} segundos")

# Resultados de ejemplo con medición de tiempo
vector = [3, 5, 8, 9, 10, 22, 45, 500, 900, 4253]

medir_tiempo(busqueda_binaria, vector, 8)
medir_tiempo(busqueda_binaria, vector, 69)
medir_tiempo(busqueda_binaria, vector, 500)

""" Resultados de ejemplo:
Resultado: 3, Tiempo de ejecución: 0.00000429 segundos
Resultado: -1, Tiempo de ejecución: 0.00000286 segundos
Resultado: 8, Tiempo de ejecución: 0.00000167 segundos
"""
"""
Busqueda Binaria.
"""


# Este es el vector que el algoritmo usara para buscar cualqiuer dato
vector = [3, 5, 8, 9, 10, 22, 45, 500, 900, 4253]

# La variable puntero sera el inicio del vector, que es 0
puntero = 0

# VectorLen contiene la longitud del vector
vectorLen = len(vector)

# La variable encontrado cambiara su valor, y asi el algoritmo sabra que hacer
encontrado = False

# Le pedimos al usuario una entrada de un entero
numero = int(input("Ingrede el numero que desea buscar: "))

# Creamos un bucle que no se detenga hasta que encontrado deje de ser False
# Y que puntero sea menor o igual que vectorLen
while not(encontrado) and puntero <= vectorLen:

    #Creamos la variable mitad
    mitad = int((puntero + vectorLen)/2)

    #Si numero es igual que el indice mitad en vector
    if numero == vector[mitad]:
        # Cambiamos el valor de encontrado a True
        encontrado = True

    elif numero < vector[mitad]:
        #vectorLen sera igual a mitad -1
        vectorLen = mitad - 1

    else:
        #Puntero sera igual a mitad + 1
        puntero = mitad +1

# Si encontrado es true
if(encontrado):

    #mostrams el mensaje con la posicion del dato en el vector

    print(" El numero se encuentra en la posicion: ", str(mitad+1))

    #Mostramosel vector ordenado
    print(vector)
#De lo contrario
else:
    #Mostramos un mensaje de fallo
    print("El numero no se encuentra en el vector")

""" 
Resultados de ejemplo:

Ingresar el dato que desea buscar: 8
El dato se encuentra en la posición  3
[3, 5, 8, 9, 10, 22, 45, 500, 900, 4253]

Ingrede el numero que desea buscar: 69
El numero no se encuentra en el vector
"""
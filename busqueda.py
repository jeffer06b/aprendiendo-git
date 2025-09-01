
# Programa 1: Búsqueda en Arreglo Multidimensional

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j
    return None

# Matriz de ejemplo 3x3
matriz = [
    [4, 7, 1],
    [9, 3, 5],
    [8, 2, 6]
]

print("Matriz:")
for fila in matriz:
    print(fila)

# Valor a buscar
valor = int(input("Ingrese el número que desea buscar: "))
posicion = buscar_valor(matriz, valor)

if posicion:
    print(f"El valor {valor} se encontró en la posición: fila {posicion[0]}, columna {posicion[1]}")
else:
    print(f"El valor {valor} NO se encontró en la matriz.")

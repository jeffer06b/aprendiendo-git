
# Programa 2: Ordenación en Arreglo Multidimensional (Bubble Sort en una fila)

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    return fila

# Matriz 3x3 de ejemplo
matriz = [
    [4, 7, 1],
    [9, 3, 5],
    [8, 2, 6]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

fila_a_ordenar = int(input("Ingrese el número de fila a ordenar (0, 1 o 2): "))

if 0 <= fila_a_ordenar < len(matriz):
    matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])
    print("\nMatriz con la fila ordenada:")
    for fila in matriz:
        print(fila)
else:
    print("Número de fila inválido.")

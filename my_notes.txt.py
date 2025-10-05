# Escritura de archivo de texto
with open("my_notes.txt", "w") as file:
    file.write("Nota 1: Hoy aprendí a manejar archivos en Python.\n")
    file.write("Nota 2: El método 'with open' es muy útil.\n")
    file.write("Nota 3: Es importante cerrar los archivos después de usarlos.\n")

# Lectura de archivo de texto
with open("my_notes.txt", "r") as file:
    for linea in file:
        print(linea.strip())  # strip() elimina saltos de línea al imprimir
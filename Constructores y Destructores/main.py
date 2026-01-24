from servicios.biblioteca_service import main

def main():
    biblioteca = main()

    biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez")
    biblioteca.agregar_libro("1984", "George Orwell")

    biblioteca.mostrar_libros()

if _name_ == "_main_":
    main()
from modelos.libro import Libro

class BibliotecaService:
    def _init_(self):
        # Constructor: estado inicial del servicio
        self.libros = []
        print("🏛️ Biblioteca iniciada")

    def agregar_libro(self, titulo, autor):
        libro = Libro(titulo, autor)
        self.libros.append(libro)

    def mostrar_libros(self):
        print("\n📚 Libros en la biblioteca:")
        if not self.libros:
            print("- (vacía)")
            return
        for libro in self.libros:
            print(f"- {libro.titulo} ({libro.autor})")

    def _del_(self):
        # Destructor: “cierre” del servicio
        print("🔒 Cerrando biblioteca y liberando recursos")
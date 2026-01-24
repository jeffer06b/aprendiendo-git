class Libro:
    def _init_(self, titulo, autor):
        """
        Constructor:
        Inicializa los atributos obligatorios del objeto Libro.
        Se ejecuta cuando se crea una instancia.
        """
        self.titulo = titulo
        self.autor = autor
        print(f"📘 Libro creado: {self.titulo} - {self.autor}")

    def _del_(self):
        """
        Destructor:
        Se ejecuta cuando el objeto deja de existir.
        Aquí simulamos la liberación de recursos.
        """
        print(f"🗑️ Libro eliminado: {self.titulo}")
# services/gestor_vehiculos.py

class GestorVehiculos:
    """
    Clase de servicios (lógica del sistema).
    Aquí manejamos una lista de vehículos y mostramos su información.
    """

    def __init__(self):
        self.vehiculos = []  # Lista para almacenar objetos Vehiculo o Auto

    def agregar(self, vehiculo) -> None:
        """Agrega un vehículo (puede ser Vehiculo o cualquier clase que herede)."""
        self.vehiculos.append(vehiculo)

    def mostrar_todos(self) -> None:
        """
        POLIMORFISMO:
        Llamamos descripcion() sin importar si es Vehiculo o Auto.
        Python ejecuta la versión correcta según el objeto.
        """
        print("\n--- LISTA DE VEHÍCULOS ---")
        for v in self.vehiculos:
            print(v.descripcion())

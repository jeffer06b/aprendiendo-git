# models/vehiculo.py

class Vehiculo:
    """
    Clase base: Vehiculo
    Aquí aplicamos ENCAPSULACIÓN usando atributos privados (__marca, __anio).
    """

    def __init__(self, marca: str, anio: int):
        # Atributos privados (encapsulación)
        self.__marca = marca
        self.__anio = anio

    # Getter y Setter para marca
    def get_marca(self) -> str:
        return self.__marca

    def set_marca(self, nueva_marca: str) -> None:
        self.__marca = nueva_marca

    # Getter y Setter para año
    def get_anio(self) -> int:
        return self.__anio

    def set_anio(self, nuevo_anio: int) -> None:
        self.__anio = nuevo_anio

    def descripcion(self) -> str:
        """
        Método pensado para POLIMORFISMO:
        Las clases hijas lo pueden sobrescribir para dar una descripción distinta.
        """
        return f"Vehículo marca {self.__marca}, año {self.__anio}"

    def encender(self) -> str:
        """Método común a todos los vehículos."""
        return "El vehículo está encendido."
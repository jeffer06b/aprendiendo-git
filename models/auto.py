# models/auto.py

from models.vehiculo import Vehiculo

class Auto(Vehiculo):
    """
    Clase derivada: Auto (HEREDA de Vehiculo)
    Agrega un atributo propio: __puertas (también encapsulado).
    """

    def __init__(self, marca: str, anio: int, puertas: int):
        super().__init__(marca, anio)  # Herencia: reutilizamos constructor de Vehiculo
        self.__puertas = puertas       # Encapsulación: atributo privado

    def get_puertas(self) -> int:
        return self.__puertas

    def set_puertas(self, nuevas_puertas: int) -> None:
        self.__puertas = nuevas_puertas

    # POLIMORFISMO: sobrescribimos el método descripcion()
    def descripcion(self) -> str:
        return f"Auto marca {self.get_marca()}, año {self.get_anio()}, puertas: {self.__puertas}"

    # Otro ejemplo de comportamiento propio
    def tocar_bocina(self) -> str:
        return "¡Piiii piiii!"
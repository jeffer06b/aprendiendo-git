# main.py

from models.vehiculo import Vehiculo
from models.auto import Auto
from services.gestor_vehiculos import GestorVehiculos

def main():
    # Crear instancias (objetos)
    vehiculo1 = Vehiculo("Yamaha", 2020)
    auto1 = Auto("Toyota", 2022, 4)

    # Probar getters/setters (encapsulación)
    vehiculo1.set_marca("Honda")
    auto1.set_puertas(2)

    # Crear el gestor y agregar objetos
    gestor = GestorVehiculos()
    gestor.agregar(vehiculo1)
    gestor.agregar(auto1)

    # Mostrar resultados (demostración + polimorfismo)
    gestor.mostrar_todos()

    # Probar métodos
    print("\n--- PRUEBAS DE MÉTODOS ---")
    print(vehiculo1.encender())
    print(auto1.encender())          # Heredado
    print(auto1.tocar_bocina())      # Propio de Auto

if __name__ == "__main__":
    main()
import json
import os


# -------------------------
# Clase Producto
# -------------------------
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(
            data["id"],
            data["nombre"],
            data["cantidad"],
            data["precio"]
        )


# -------------------------
# Clase Inventario
# -------------------------
class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.productos = {}  # Diccionario {id: Producto}
        self.archivo = archivo
        self.cargar_archivo()

    # Añadir producto
    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("❌ El producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_archivo()
            print("✅ Producto agregado correctamente.")

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_archivo()
            print("✅ Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    # Actualizar producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            self.guardar_archivo()
            print("✅ Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    # Buscar producto por nombre
    def buscar_producto(self, nombre):
        encontrados = [
            p for p in self.productos.values()
            if p.nombre.lower() == nombre.lower()
        ]

        if encontrados:
            for p in encontrados:
                print(p.to_dict())
        else:
            print("❌ Producto no encontrado.")

    # Mostrar todos
    def mostrar_productos(self):
        if not self.productos:
            print("📦 Inventario vacío.")
        else:
            for p in self.productos.values():
                print(p.to_dict())

    # Guardar en archivo
    def guardar_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                json.dump(
                    {id_: p.to_dict() for id_, p in self.productos.items()},
                    f,
                    indent=4
                )
        except Exception as e:
            print("Error al guardar:", e)

    # Cargar desde archivo
    def cargar_archivo(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r") as f:
                    data = json.load(f)
                    for id_, prod in data.items():
                        self.productos[id_] = Producto.from_dict(prod)
            except Exception as e:
                print("Error al cargar archivo:", e)


# -------------------------
# Menú interactivo
# -------------------------
def menu():
    inventario = Inventario()

    while True:
        print("\n--- SISTEMA DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_ = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_ = input("ID a eliminar: ")
            inventario.eliminar_producto(id_)

        elif opcion == "3":
            id_ = input("ID a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")

            inventario.actualizar_producto(
                id_,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Nombre del producto: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida.")


# Ejecutar programa
if __name__ == "__main__":
    menu()
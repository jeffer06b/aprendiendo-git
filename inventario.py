import os

class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Formato para guardar en archivo
        return f"{self.codigo},{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_desde_archivo()

    # ===============================
    # CARGAR INVENTARIO DESDE ARCHIVO
    # ===============================
    def cargar_desde_archivo(self):
        try:
            if not os.path.exists(self.archivo):
                # Si el archivo no existe, lo crea vacío
                open(self.archivo, "w").close()
                print("Archivo de inventario creado automáticamente.")
                return

            with open(self.archivo, "r") as f:
                for linea in f:
                    try:
                        codigo, nombre, cantidad, precio = linea.strip().split(",")
                        self.productos[codigo] = Producto(
                            codigo,
                            nombre,
                            int(cantidad),
                            float(precio)
                        )
                    except ValueError:
                        print("⚠ Línea corrupta ignorada:", linea.strip())

            print("Inventario cargado correctamente.")

        except PermissionError:
            print("❌ Error: No hay permisos para leer el archivo.")
        except Exception as e:
            print("❌ Error inesperado al cargar:", e)

    # ===============================
    # GUARDAR INVENTARIO EN ARCHIVO
    # ===============================
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(str(producto) + "\n")
            print("✔ Cambios guardados en el archivo.")
        except PermissionError:
            print("❌ Error: No hay permisos para escribir en el archivo.")
        except Exception as e:
            print("❌ Error inesperado al guardar:", e)

    # ===============================
    # OPERACIONES CRUD
    # ===============================
    def agregar_producto(self, codigo, nombre, cantidad, precio):
        if codigo in self.productos:
            print("❌ El producto ya existe.")
            return

        self.productos[codigo] = Producto(codigo, nombre, cantidad, precio)
        self.guardar_en_archivo()
        print("✔ Producto agregado correctamente.")

    def actualizar_producto(self, codigo, cantidad=None, precio=None):
        if codigo not in self.productos:
            print("❌ Producto no encontrado.")
            return

        if cantidad is not None:
            self.productos[codigo].cantidad = cantidad
        if precio is not None:
            self.productos[codigo].precio = precio

        self.guardar_en_archivo()
        print("✔ Producto actualizado correctamente.")

    def eliminar_producto(self, codigo):
        if codigo not in self.productos:
            print("❌ Producto no encontrado.")
            return

        del self.productos[codigo]
        self.guardar_en_archivo()
        print("✔ Producto eliminado correctamente.")

    def mostrar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
            return

        print("\n--- INVENTARIO ACTUAL ---")
        for p in self.productos.values():
            print(f"Código: {p.codigo} | Nombre: {p.nombre} | Cantidad: {p.cantidad} | Precio: ${p.precio}")
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = []
        self.nombre_archivo = "inventario.txt"  # Nombre del archivo donde se va a guardar el inventario
        self.cargar_inventario()

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.actualizar_archivos()

    def actualizar_archivos(self):
        try:
            with open(self.nombre_archivo, "w") as archivo:
                for producto in self.productos:
                    archivo.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n")
            print("Inventario actualizado en el archivo correctamente.")
        except PermissionError:
            print("No se tiene permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al actualizar el archivo: {e}")

    def cargar_inventario(self):
        try:
            with open(self.nombre_archivo, "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id, nombre, cantidad, precio = datos
                        producto = Producto(id, nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
            print("Inventario cargado desde el archivo correctamente.")
        except FileNotFoundError:
            print("El archivo de inventario no existe. Se creará uno nuevo.")
        except PermissionError:
            print("No se tiene permisos para leer el archivo.")
        except Exception as e:
            print(f"Error al cargar el inventario desde el archivo: {e}")

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                self.actualizar_archivos()
                return True
        return False

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id == id:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.actualizar_archivos()
                return True
        return False

    def buscar_producto_por_nombre(self, nombre):
        return [producto for producto in self.productos if nombre.lower() in producto.nombre.lower()]

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print("ID:", producto.id)
                print("Nombre:", producto.nombre)
                print("Cantidad:", producto.cantidad)
                print("Precio:", producto.precio)
                print("-------------------------")


# Interfaz de usuario en la consola
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto por ID")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos en el inventario")
    print("6. Salir")


if __name__ == "__main__":
    inventario = Inventario()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
            print("Producto agregado con éxito.")

        elif opcion == "2":
            id = input("Ingrese el ID del producto que desea eliminar: ")
            if inventario.eliminar_producto(id):
                print("Producto eliminado con éxito.")
            else:
                print("No se encontró un producto con ese ID.")

        elif opcion == "3":
            id = input("Ingrese el ID del producto que desea actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco para no modificar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco para no modificar): ")
            if cantidad == "":
                cantidad = None
            else:
                cantidad = int(cantidad)
            if precio == "":
                precio = None
            else:
                precio = float(precio)
            if inventario.actualizar_producto(id, cantidad, precio):
                print("Producto actualizado con éxito.")
            else:
                print("No se encontró un producto con ese ID.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre (o parte del nombre) del producto: ")
            productos_encontrados = inventario.buscar_producto_por_nombre(nombre)
            if productos_encontrados:
                print("Productos encontrados:")
                for producto in productos_encontrados:
                    print("ID:", producto.id)
                    print("Nombre:", producto.nombre)
                    print("Cantidad:", producto.cantidad)
                    print("Precio:", producto.precio)
                    print("-------------------------")
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

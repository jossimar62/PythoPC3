class Producto:
    def _init_(self, nombre, marca, año, precio):
        self.nombre = nombre
        self.marca = marca
        self.año = año
        self.precio = precio
    
    def _str_(self):
        return f"{self.nombre} - Marca: {self.marca}, Año: {self.año}, Precio: ${self.precio:.2f}"


class Catalogo:
    def _init_(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el catálogo.")
            return
        print("Lista de Productos:")
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if not productos_filtrados:
            print(f"No se encontraron productos del año {año}.")
        else:
            print(f"Productos del año {año}:")
            for producto in productos_filtrados:
                print(producto)

    def filtrar_por_precio(self, precio_max):
        productos_filtrados = [producto for producto in self.productos if producto.precio <= precio_max]
        if not productos_filtrados:
            print(f"No se encontraron productos con un precio menor o igual a ${precio_max:.2f}.")
        else:
            print(f"Productos con precio menor o igual a ${precio_max:.2f}:")
            for producto in productos_filtrados:
                print(producto)


# Ejemplo de uso
catalogo = Catalogo()

# Crear productos
producto1 = Producto("Freno de disco", "ACME", 2021, 150.00)
producto2 = Producto("Batería", "Energizer", 2020, 75.50)
producto3 = Producto("Aceite de motor", "LubriMax", 2023, 25.00)

# Agregar productos al catálogo
catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

# Mostrar todos los productos
catalogo.mostrar_productos()

# Filtrar productos por año
catalogo.filtrar_por_año(2021)

# Filtrar productos por precio
catalogo.filtrar_por_precio(80.00)
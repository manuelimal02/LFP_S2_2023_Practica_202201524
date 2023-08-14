from inventario import Producto

class inventario_DAO:
    def __init__(self):
        self.lista_productos = []

    def agregar_producto(self, nombre, cantidad, precio, ubicacion):
        producto_nuevo = Producto(nombre, cantidad, precio, ubicacion)
        self.lista_productos.append(producto_nuevo)
        print("El producto "+nombre +" ha sido ingresado correctamente al inventario.")
        return True
    
    def encontrar_producto(self, nombre, ubicacion):
        for producto in self.lista_productos:
            if producto.nombre == nombre and producto.ubicacion == ubicacion:
                return producto
        return None

    def agregar_stock(self, nombre, ubicacion, cantidad):
        producto_existente = self.encontrar_producto(nombre, ubicacion)
        if producto_existente is not None:
            producto_existente.cantidad += cantidad
            print("La cantidad producto "+nombre +" ha sido actualizada correctamente en el inventario.")
        else:
            print("ERROR: El producto "+nombre+" no existe en la ubicación "+ubicacion+".")


    def vender_producto(self, nombre, ubicacion, cantidad):
        producto_existente = self.encontrar_producto(nombre, ubicacion)
        if producto_existente is not None:
            if cantidad < producto_existente.cantidad:
                producto_existente.cantidad -= cantidad
                print("El producto "+nombre +" ha sido vendido correctamente. Inventario Actualizado.")
            elif cantidad >= producto_existente.cantidad:
                print("ERROR: La cantidad a vender de "+nombre+" en la ubicación "+ubicacion+" es mayor o igual que la existencia.")
        else:
            print("ERROR: El producto "+nombre+" no existe en la ubicación "+ubicacion+".")


    def crear_informe(self, nombre_archivo):
        try:
            with open(nombre_archivo, "w") as archivo:
                linea1="Informe de Inventario:" + "\n"+ "\n" 
                archivo.write(linea1)
                for producto in self.lista_productos:
                    valor_total=producto.cantidad*producto.precio
                    linea = "Nombre: "+producto.nombre+", "+"Cantidad: "+str(producto.cantidad)+", "+"Precio: "+str(producto.precio)+", "+"Valor Total: "+str(valor_total)+", "+"Ubicacion: "+producto.ubicacion + "\n"
                    archivo.write(linea)
            print("Archivo",nombre_archivo," Creado Correctamente")
        except Exception as e:
            print("Error al crear el archivo:",e)


    def imprimir_productos(self):
        for producto in self.lista_productos:
            print(producto)

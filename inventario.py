class Producto:
    def __init__(self, nombre, cantidad, precio, ubicacion):
        self.nombre = nombre
        self.cantidad = int(cantidad)
        self.precio = float(precio)
        self.ubicacion = ubicacion

    def __str__(self):
        return f"{self.nombre}, {self.cantidad}, {self.precio}, {self.ubicacion}"

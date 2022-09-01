class Carrito():
    def __init__(self) -> None:
        self.productos = []

    def agregar_producto(producto):
        pass  
             
class Venta():

    def __init__(self,producto,cliente) -> None:
        self.producto= producto
        self.precio_total= 0
        self.cantidad = 0
        self.cliente = cliente

class Producto():

    def __init__(self,codigo,nombre,precio,stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
      
        
    def __str__(self) -> str:
        return f"""
            Producto Codigo: {self.codigo} 
            Nombre: {self.nombre} 
            Precio: ${self.precio}
            Stock: {self.stock}
            """

    def vender(self):
        pass

    def descontar_stock(self):
        self.stock=self.stock-1
    
#instanciamos
producto_uno = Producto('xx2','Peras','333',4)
print(producto_uno)
producto_uno.descontar_stock()
print(producto_uno)

listado_producto = [producto_uno]
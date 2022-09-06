class Producto():

    def __init__(self,codigo,nombre,precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
      
        
    def __str__(self) -> str:
        return f"""
            Producto Codigo: {self.codigo} 
            Nombre: {self.nombre} 
            Precio: ${self.precio}"""

    def vender(self):
        pass

    def descontar_stock(self):
        pass
    

producto_uno = Producto('xx2','Peras','333')
print(producto_uno)

from herencia.producto import Producto


class Alimento(Producto):

    def __init__(self, codigo, nombre, precio,marca,fecha_vencimiento):
        super().__init__(codigo, nombre, precio)
        self.marca = marca
        self.fecha_vencimiento = fecha_vencimiento


    def __str__(self) -> str:
        return super().__str__()+f'\nMarca: {self.marca} \nFecha Ven.: {self.fecha_vencimiento}'
    

class Libro(Producto):

    def __init__(self, codigo, nombre, precio,autor,editorial):
        super().__init__(codigo, nombre, precio)
        self.autor = autor
        self.editorial = editorial

    def __str__(self) -> str:
        return super().__str__()+f'\nAutor: {self.autor} \nEditorial: {self.editorial}'


    
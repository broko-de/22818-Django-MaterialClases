
from polimorfismo.persona import Persona

class Programador(Persona):

    def __init__(self, nombre,lenguaje) -> None:
        super().__init__(nombre)
        self.lenguaje = lenguaje

    def trabajar(self):
        print(f'Yo trabajo de programador - {self.lenguaje}')

    
class Contador(Persona):

    def __init__(self, nombre) -> None:
        super().__init__(nombre)

    def trabajar(self):
        print('Yo trabajo de contador')
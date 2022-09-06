from abstractas.abstracta import Animal

class Gato(Animal):

    def mover(self):
        print('El gato se mueve')

    def emitir_sonido(self):
        super().emitir_sonido()
        print('Miau miau')

    def correr(self):
        print('Estoy corriendo')
        
class Perro(Animal):

    def mover(self):
        print('El perro se mueve')

    def emitir_sonido(self):
        super().emitir_sonido()
        print('Guauu! Guauuu!')
    


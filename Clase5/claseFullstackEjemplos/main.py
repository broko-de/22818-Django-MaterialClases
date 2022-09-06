from abstractas.abstracta import Animal
from abstractas.subclase import Gato, Perro
from encapsulamiento.cliente import Cliente
from herencia.producto import Producto
from herencia.subclase import Alimento, Libro
from herenciamultiple.spiderverse import SpiderVerse
from polimorfismo.persona import Persona
from polimorfismo.subclases import Contador, Programador

def main():
    #ENCAPSULAMIENTO
    # cliente_uno = Cliente()
    # #SETTER
    # cliente_uno.nombre = 'Roberto'
    # #GETTER
    # print(cliente_uno.nombre)
    # print(cliente_uno)

    # cliente_uno.email = 'robertocarlos@gmail.com'
    # print(cliente_uno)
    
    # # HERENCIA 
    # p_uno = Producto('1','Escritorio',13000)

    # print(p_uno)
    # print('.---.---')
    # p_dos = Alimento('2','Galletas surtido',200,'Bagley','30/06/2022')

    # print(p_dos)
    # print('.---.---')
    # p_tres = Libro('3','Harry potter',7000,'xxx','kapeluz')
    # print(p_tres)

    #HERENCIA MULTIPLE
    # spider_verse = SpiderVerse()
    # spider_verse.bailar()
    # spider_verse.mis_villanos()
    # spider_verse.hablar()

    #POLIMORFISMO
    # persona = Persona('Lucas')
    # print(persona)
    # persona.trabajar()
    
    # programador = Programador('Felipe','Python')
    # print(programador)
    # programador.trabajar()

    # contador = Contador('Maria')
    # print(contador)
    # contador.trabajar()

    #CLASE ABSTRACTA
    #animal = Animal() ERROR!
    perro = Perro()
    perro.mover()
    perro.emitir_sonido()
    
    gato = Gato()
    gato.mover()
    gato.emitir_sonido()
    gato.correr()
    pass


if __name__ == "__main__":
    main()
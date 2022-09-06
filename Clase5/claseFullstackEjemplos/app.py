class Persona:
    def inicializar(self, nom):
        self.nombre= nom

    def mostrar(self):
        print ("Nombre:", self.nombre)

# Programa ppal
# creamos una instancia
persona1= Persona()
persona1.inicializar("Juan")
persona1.mostrar()
# creamos una instancia
persona2= Persona()
persona2.inicializar("Sofía")
persona2.mostrar()

class Contacto:

    def init(self,nombre,tel,email) -> None:
        self.nombre = nombre
        self.telefono = tel
        self.email = email

    def mostrar(self):
        print(f'Contacto: {self.nombre} - {self.email} ({self.telefono})')

class Agenda:

    def __init__(self) -> None:
         pass
    
    def menu(self):
        print('algo')

agenda = Agenda()
agenda.menu()
class Persona:

    def __init__(self,nombre) -> None:
        self.nombre = nombre

    def __str__(self) -> str:
        return f'Hola soy: {self.nombre}'
    
    def trabajar(self):
        print('hola estoy trabajando')
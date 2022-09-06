from abc import ABC, abstractmethod
""" 
Definicion de la superclase
"""
class Empleado(ABC):

    def __init__(self,nombre,apellido):
        self.__nombre = nombre
        self.__apellido = apellido


    @property
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    #GETTER
    @property
    def nombre(self):
        return self.__nombre

    @property
    @abstractmethod
    def salario(self):
        pass

#empleado = Empleado('Pepe','Argento') NO SE PUEDE

"""
Definicion de las subclases
"""
class EmpleadoFullTime(Empleado):

    def __init__(self, nombre, apellido,salario):
        #constructor de la superclase
        super().__init__(nombre, apellido)
        #atributo de la subclase
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario


empleado_uno = EmpleadoFullTime('Argento','Pepe',100000)
#print(empleado_uno.nombre)


class EmpleadorPorHora(Empleado):

    def __init__(self, nombre, apellido,horas_trabajadas,valor_hora):
        super().__init__(nombre, apellido)
        self.__horas_trabajadas= horas_trabajadas
        self.__valor_hora = valor_hora

    @property
    def salario(self):    
        return self.__horas_trabajadas*self.__valor_hora

    #metodo privado
    def __mostrar(self):
        print('Hola!')

    #metodo publico
    def algo(self):
        self.__mostrar()


empleado_dos = EmpleadorPorHora('Mony','Argento',100,1000)
#empleado_dos.algo()    


class Nomina:

    def __init__(self):
        self.__lista_empleados = []


    def agregar_empleado(self,empleado):
        self.__lista_empleados.append(empleado)

    def print(self):
        for empleado in self.__lista_empleados:
            if isinstance(empleado,Empleado):
                print(f"{empleado.nombre_completo} y el salario: ${empleado.salario}")
            else:
                print(f"En la nomina hay un NO empleado: {empleado}")


nomina_empleado = Nomina()

nomina_empleado.agregar_empleado(empleado_uno)
nomina_empleado.agregar_empleado(empleado_dos)
nomina_empleado.agregar_empleado(EmpleadoFullTime('Mario','Lobo',150000))
nomina_empleado.agregar_empleado(44)
nomina_empleado.agregar_empleado(EmpleadorPorHora('Gustavo','Balvorin',40,500))

nomina_empleado.print()


class Estudiante:

    def __init__(self,legajo) -> None:
        self.__legajo = legajo

    @property
    def legajo(self):
        return self.__legajo

    def __str__(self) -> str:
        return f"Legajo: {self.__legajo}"


class EstudiantePasante(Empleado,Estudiante):

    def __init__(self, nombre, apellido,legajo):
        Empleado.__init__(self,nombre, apellido)
        Estudiante.__init__(self,legajo)


    @property
    def salario(self):
        return 0
    
    def __str__(self) -> str:
        return f"{self.nombre_completo} Legajo: {self.legajo}"


estudiante_uno = EstudiantePasante('Franco','Sosa','IN-23456')
print(estudiante_uno)
nomina_empleado.agregar_empleado(estudiante_uno)
nomina_empleado.print()
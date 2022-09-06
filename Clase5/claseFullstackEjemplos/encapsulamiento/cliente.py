class Cliente:

    def __init__(self) -> None:
        self.__nombre = ''
        self.__email = ''


    def __str__(self) -> str:
        return 'Nombre:'+self.__nombre+' - ('+self.__email+')'

    #GETTER
    @property
    def nombre(self):
        return f'Nombre: {self.__nombre}'

    #SETTER
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

    #GETTER
    @property
    def email(self):
        return f'Email: {self.__email}'

    #SETTER
    @email.setter
    def email(self,nuevo_email):
        self.__email = nuevo_email

    

    

    

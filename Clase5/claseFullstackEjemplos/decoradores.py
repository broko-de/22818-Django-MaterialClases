def funcion_decoradora(funcion_parametro):

    def funcion_interior():
        #definir acciones que decoren
        print('se inicia el calculo')
        funcion_parametro()
        #seguir ejecutando más cosas
        print('Se ha finalizado calculo')

    return funcion_interior

@funcion_decoradora
def suma():
    print(10+2)

@funcion_decoradora
def resta():
    print(7-3)

suma()
resta()
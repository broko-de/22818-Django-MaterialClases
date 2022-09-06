#funcion A                  #funcion B
def funcion_decoradora(funcion_parametro):
    #funcion C
    def funcion_interior():

        #acciones adicionales que decoran
        print('Se inicia el calculo')
        funcion_parametro()
        #acciones adicionales que decoran
        print('Se ha terminado con el calculo')
    
    return funcion_interior


@funcion_decoradora
def suma():
    #print(a+b)
    print(10+2)

@funcion_decoradora
def resta():
    #print(a-b)
    print(23-4)

suma()
resta()
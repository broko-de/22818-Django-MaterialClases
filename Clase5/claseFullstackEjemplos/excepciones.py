def division(a,b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print('Error! No se puede realizar la division por 0')

def division_excepciones(a):
    try:
        divisor = input('Ingrese el divisor: ')
        resultado = a/divisor
        print(resultado)
    except TypeError:
        print('Error! no se puede operar int con str')
    except ValueError:
        print('Error! Debe ingresar un formato numerico')
    except ZeroDivisionError:
        print('Error! No se puede realizar la division por 0')

#SIN Excepcion
def division_sin_excp(a,b):
    return a/b

def main():
    #a = 20/0
    #n= int(input('Ingrese un numero: '))
    #print('hola')
    # division(10,0)
    # division(10,2)
    #division_excepciones(10)

    # try:
    #     print(division_sin_excp(10,0))
    # except Exception as e:
    #     print('Algo raro paso',e)

    while True:
        try:
            total = 0
            sumandos = input('Ingresa numeros separados por espacios: ')
            sumandos = sumandos.split()
            for num in sumandos:
                if num.isnumeric():
                    total += float(num)
                else:
                    raise ValueError('El valor ingresado no es numerico')
        except ValueError as e:
            print(e)
            print('Vuelva a ingresar los numeros: ')
        else:
            print(f'La suma es: {total}')
            break
        finally:
            print('Ha terminado el proceso, se vimos!')
            
    print('Fin del main')
    pass

if __name__ == '__main__':
    main()
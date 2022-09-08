import sys

class DivisorNegativoError(Exception):
    """ 
        Excepcion lanzada se divide por un numero negativo
    """
    pass

def mostrar_division_entera(dividendo,divisor):
    try:
        assert divisor >= 0, "Mandaron un número negativo"

        print('Intentando realizar la división')
        if divisor<0:
            raise DivisorNegativoError("Mandaron un número negativo ojo!")

        resultado = dividendo / divisor
        print(f'El resultado de la división es: {resultado}')
    except AssertionError as assert_error:
        print(assert_error)
        print('Se ingreso un numero negativo para el divisor')

    except TypeError:
        print('Revisar los operandos hay datos incorrectos')
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(exc_type)
        print(exc_value)
        print(exc_traceback)
    except ZeroDivisionError:
         print('No se puede dividir por cero..')
    except DivisorNegativoError as dne:
        print(f'Error divisor nevagativo: {dne}')
    except Exception as ex:
        print(f'Algo anda mal: {ex}')
    else:
        print('La division se ejecuto correctamente')
    finally:
        print('La funcion se terminó!')

mostrar_division_entera(2,-1)
# mostrar_division_entera(2,'-1')
# mostrar_division_entera(2,0)


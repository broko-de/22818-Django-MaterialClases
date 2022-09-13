import ejercicio_integrador_1

def mcm(n, m):
    """Función que calcula el mínimo común múltiplo de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El mínimo común múltiplo de n y m.
    """
    if n > m:
        mayor = n
    else:
        mayor = m
    while (mayor % n != 0) or (mayor % m != 0):
        mayor += 1
    return mayor


print(mcm(1032,180))

def mcm_2(n,m):
    """
        Funcion de calculo de mcm utilizando el cálculo del MCD 
        Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
        Devuelve:
            El mínimo común múltiplo de n y m.
    """
    mcd_aux = ejercicio_integrador_1.mcd(n,m)
    return n*m//mcd_aux

print(mcm_2(1032,180))    
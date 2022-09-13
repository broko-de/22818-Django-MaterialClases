"""
Ejercicio 1
"""

num1=int(input("Ingrese un número: "))
num2=int(input("Ingrese otro número: "))

def maximo_comun_divisor(num1,num2):
  '''
    Debe ingresar dos números distintos de 0
  '''
  if num1==num2:
    max_divisor=num1
  else:
    if abs(num1)<abs(num2):
      menor_numero=abs(num1)
      mayor_numero=abs(num2)
    else:
      menor_numero=abs(num2)
      mayor_numero=abs(num1)

    mcd=False
    divisor=menor_numero

    while mcd==False:
      if (mayor_numero % divisor == 0 and menor_numero % divisor == 0):
        max_divisor=divisor
        mcd=True
      else:
        divisor-=1
  return max_divisor
  
  print(f"El máximo común divisor entre {num1} y {num2} es {maximo_comun_divisor(num1,num2)}")
  
  
  
"""
Ejercicio 3
"""

caracteres=[".",",","¡","!","¿","?","-"]
cadena="Hola,.?¿¡- Mundo Hola mundo MuNdo programacion!"
nuevaCadena=cadena
for i in caracteres:  
  nuevaCadena=nuevaCadena.replace(i,"")
nuevaCadena=nuevaCadena.lower()

arr=nuevaCadena.split(" ")
diccionario={}

for i in arr:
  if i in diccionario:
    diccionario[i]+=1
  else:
    diccionario[i]=1

print(diccionario)




"""
Ejercicio 1
"""
def MCD(num1, num2):
    if num1 == 0:
        print(
            f"El máximo común divisor de {num1} y {num2} es: {num2}")

    while (num2 != 0):
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1

    return num1


num1 = int(input("Ingrese el primero número: "))
num2 = int(input("Ingrese el segundo número: "))

resultado = MCD(num1, num2)

print(f"El máximo común divisor de {num1} y {num2} es: {resultado}")



print(
    "Ingrese dos números enteros para calcular el mínimo común múltiplo entre ellos.\n")

"""
Ejercicio 2
"""
def MCM(num1, num2):

    if num1 > num2:
        max = num1
    else:
        max = num2

    while (True):
        if max % num1 == 0 and max % num2 == 0:
            valor = max
            break
        max += 1
    return valor


num1 = int(input("Ingrese el primero número: "))
num2 = int(input("Ingrese el segundo número: "))

valor = MCM(num1, num2)

print(f"El mínimo común múltiplo de {num1} y {num2} es: {valor}")



"""
Ejercicio 4
"""

# Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def count_words(string: str):
    # Creo un diccionario vacío donde voy a guardar las palabras y la frecuencia de cada una
    count_words = {}
    string = string.strip().lower()
    words = string.split(" ")
    for i in words:
        count_words[i] = i
        count_words[i] = string.count(i)
    # Imprimo los resultados
    result = count_words
    return result

# Nueva función que llama a la anterior y busca la palabra más repetida

def most_frequent(string: str):
    dict = count_words(string)
    # Busca la llave con el valor más alto
    max_key = max(dict, key=dict.get)
    # El resultado es una tupla con la llave y el valor
    result = max_key, dict[max_key]
    print(result)
    return result

    # Llamo a la nueva función
most_frequent(
    "uno cuatro seis seis dos tres seis cuatro dos cuatro seis cuatro seis seis tres tres")

"""
Ejercicio 5 (version 1)
"""

def get_int():
    
    try:
        numero= int(input("ingrese un numero: "))
    
    except ValueError:
        print("Ingreso no valido")
        get_int()
    else: print("ingreso valido. El programa finaliza")

get_int()



"""
Ejercicio 5 (version 2)
"""


# Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.

# Método iterativo
def get_int_i():
    result = None
    while result is None:
        try:
            value = input("Por favor introduzca un valor entero: ")
            result = int(value)
            print(result)
        except ValueError:
            print("Formato incorrecto, pruebe de nuevo.")
        else:
            print("Ingreso válido!")
            return result


# Método recursivo
def get_int_r():
    value = input("Por favor introduzca un valor entero: ")
    try:
        result = int(value)
        print("Ingreso válido!")
        print(result)
        return result
    except ValueError:
        print("Formato incorrecto, pruebe de nuevo.")
        get_int_r()


get_int_i()
# get_int_r()

"""
Ejercicio 1
"""

# Escribir una función que calcule el máximo común divisor entre dos números.

def calcula_mcd(a: int, b: int) -> int:
    """Calcula máximo común divisor entre dos números
    enteros utilizando el algoritmo de Euclides.
    Args:
        a (int): entero distinto de cero.
        b (int): entero distinto de cero.
    Returns:
        int: máximo común divisor entre a y b.
    """

    ap, bp = a, b

    if b > a:
        a, b = b, a

    while a % b != 0:
        a, b = b, a % b

    mcd = b

    if __name__ == "__main__":
        return f"El MCD entre {ap} y {bp} es: {mcd}"
    else:
        return mcd


# print(calcula_mcd(17, 23))
# print(calcula_mcd(60, 48))
# print(calcula_mcd(55, 89))
# print(calcula_mcd(15, 25))
# print(calcula_mcd(42, 56))
"""
Ejercicio 2
"""

from ejercicio1 import calcula_mcd

# Escribir una función que calcule el mínimo común múltiplo entre dos números.


def calcula_mcm(a: int, b: int) -> int:
    """Calcula el mínimo común múltiplo entre dos números
    enteros a partir del máximo común divisor.
    MCM(a, b) = a * b / MCD(a, b)
    Args:
        a (int): entero distinto de cero.
        b (int): entero distinto de cero.
    Returns:
        int: mínimo común múltiplo entre a y b.
    """

    mcm = int((a * b) / calcula_mcd(a, b))

    if __name__ == "__main__":
        return f"El MCM entre {a} y {b} es: {mcm}"
    else:
        return mcm


# print(calcula_mcm(72, 50))
# print(calcula_mcm(6, 33))
# print(calcula_mcd(42, 56))

"""
Ejercicio 3
"""
# Escribir un programa que reciba una cadena de caracteres
# y devuelva un diccionario con cada palabra que contiene
# y la cantidad de veces que aparece (frecuencia).


def contador(cadena: str) -> dict:
    """Recibe una cadena de caracteres y devuelve
    un diccionario con cada palabra[key] que contiene 
    y la frecuencia[value] con que aparece.
    Args:
        cadena (str): la cadena de caracteres.
    Returns:
        contador (dict): un diccionario donde palabra[key]: frecuencia[value].
    """

    # Remover caracteres especiales, puntuación y mayúsculas de la cadena
    chars = "¿?¡!#$%^&*()"
    for ch in chars:
        cadena = cadena.replace(ch, '')
    cadena = cadena.replace(',', '').replace('.', '').replace('\n', ' ')
    cadena = cadena.lower()

    # Inicializar el diccionario vacio
    contador_dict = {}

    for palabra in cadena.split(' '):
        if palabra not in contador_dict:
            contador_dict.update({palabra: 1})
        else:
            contador_dict[palabra] += 1

    if __name__ == '__main__':
        return print(contador_dict)
    else:
        return contador_dict
      
      
"""
Ejercicio 4
"""

from ejercicio3 import contador

# Escribir un programa que reciba una cadena de caracteres
# y devuelva un diccionario con cada palabra que contiene
# y la cantidad de veces que aparece (frecuencia).
# Escribir otra función que reciba el diccionario generado
# con la función anterior y devuelva una tupla con la palabra
# más repetida y su frecuencia.


def mas_repetida(dict_palabras: dict) -> tuple:
    """Recibe un diccionario de frecuencias de aparición de
    palabras y devuelve una tupla con la(s) palabra(s) más 
    repetida(s) y su(s) frecuencia(s).
    Args:
        contador (dict): diccionario de palabras[key] y sus
        respectivas frecuencias[value].
    Returns:
        mas_freq (tuple): tupla con la(s) palabra(s) más repetida(s) y su(s) frecuencia(s).
    """

    mas_freq = ['', 0]
    for k, v in dict_palabras.items():
        if v > mas_freq[1]:
            mas_freq[0], mas_freq[1] = k, v
        elif v == mas_freq[1]:
            mas_freq.append(k)
            mas_freq.append(v)

    mas_freq = tuple(mas_freq)

    if __name__ == '__main__':
        return print(f'la(s) palabra(s) más repetida(s) del diccionario: {mas_freq}')
    else:
        return mas_freq


"""
EJERCICIO 8
"""
class Persona():

    def __init__(self):
        self.nombre=""
        self.edad=0
        self.dni=0
    
    
    def set_nombre(self):
        while True:
            try:
                nombre = str(input("Escribe tu nombre: "))
            except ValueError:
                print("Debes escribir letras solamente.")
                continue

            if nombre.isalpha() == False:
                print("Ingresa sólo letras.")
                continue
            elif len(nombre) < 3:
                print("El nombre es demasiado corto")
            else:
                self.nombre = nombre
                break
        

    def set_edad(self):
        while True:
            try:
                edad = int(input("Escribe tu edad: "))
            except ValueError:
                print("Debes escribir un número.")
                continue

            if edad < 0:
                print("Debes escribir un número positivo.")
                continue
            elif edad > 120:
                print("Ingresa una edad válida [entre 0 y 120 años]")
                continue
            else:
                self.edad = edad
                break

        

    def set_dni(self):
        while True:
            try:
                dni = int(input("Escribe tu número de DNI: "))
            except ValueError:
                print("Debes escribir un número.")
                continue

            if dni < 0:
                print("Debes escribir un número positivo.")
                continue
            elif dni < 999999:
                print ("Debes ingresar un número de DNI válido.")
            else:
                self.dni = dni
                break

    def get_nombre(self):
        print("Nombre: {}".format(self.nombre))

    def get_edad(self):
        print("Edad: {}".format(self.edad))

    def get_dni(self):
        print("DNI: {}".format(self.dni))

    def mostrar(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))
        print("DNI: {}".format(self.dni))

    def es_mayor_de_edad(self):
        return (self.edad > 17)


persona1=Persona()
persona1.set_nombre()
persona1.set_edad()
persona1.set_dni()
persona1.mostrar()
print(persona1.es_mayor_de_edad())


"""
    def __init__(self, nombre, edad, dni):
        nom = str(nombre)
        if nom.isalpha() == False:
            print("El nombre ingresado no es válido [no se aceptan números o caracteres especiales]")
            self.set_nombre()
        elif len(nombre) < 3:
            print("El nombre ingresado es demasiado corto")
            self.set_nombre()
        else:
            self.nombre=nom

        while True:
            try:
                age = int(edad)
            except ValueError:
                print("La edad recibida no tiene un formato válido")
                self.set_edad()
            if edad < 0:
                print("La edad recibida fue un número negativo.")
                self.set_edad()
                break
            elif edad > 120:
                print("La edad recibida fue demasiado alta. Ingresa una edad válida [entre 0 y 120 años]")
                self.set_edad()
                break
            else:
                self.edad = age
                break
        
        self.dni=dni
""" 


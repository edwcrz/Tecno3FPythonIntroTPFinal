import string
from secrets import choice
# import sys

# les paso un diccionario donde cada valor tendra una cadena, es decir letras tiene una cadena del alfabeto en mayusculas y minusculas, numeros tiene la cadena de numeros del 0 al 9 y lo mismo con caracteres

# print (string.digits)
# print (string.ascii_lowercase)
# print (string.ascii_uppercase)
# print (string.punctuation)

def validar_int (numero: int) -> tuple [bool, int]:
    largo_computado : int = 0
    if numero.isdigit() == True:
        largo_computado = int(numero)
        largo_validado = True
    else:
        largo_validado = False
    return (largo_validado, largo_computado)

dict_permitido  = {
                    'caracteres': string.punctuation,
                    'numeros': string.digits,
                    'letras_mayusculas': string.ascii_uppercase,
                    'letras_minusculas': string.ascii_lowercase
                  }


largo_min : int = 12

largo_caracteres_min = 2
largo_numeros_min = 3
largo_letras_mayusculas_min = 2
# largo_letras_minusculas_min = 5

lista_acumulador_caracteres : list = []
lista_acumulador_numeros : list = []
lista_acumulador_letras_mayusculas : list = []
lista_acumulador_letras_minusculas : list = []

password : str = ""

error_int : bool = True
largo_password_validado = False
salir : bool = False

largo_password_computado : int = 0

lista_acumulador : list = []
password_list : list = []

print ("bienvenido al programa de generación de password")
print ("la password generada tendrá al menos una letra mayúscula, al emnos un caracter especial y al menos un numero")
print ("ingrese Exit para salir")


while salir == False:
    
    while error_int == True:

        # Seccion largo del password
        largo_password = input("ingrese la longitud de la password a generar de al menos 12 caracteres : ")
        if largo_password == "Exit":
            print ("saliendo del programa")
            continue
        
        largo_password_validado, largo_password_computado = validar_int(largo_password)
        
        if not largo_password_validado:
            print("ingreso una longitud de password diferente a un numero entero : ")
            continue    
        largo_password = int(largo_password)
                
        if largo_password < largo_min:
            print("ingreso una longitud de password menor de 12 caracteres : ")
            continue
        error_int = False

        # seccion cantidad de caracteres especiales
        largo_caracteres = input(f"ingrese la longitud de caracteres especiales de al menos {largo_caracteres_min} caracteres : ")
        if largo_caracteres == "Exit":
            print ("saliendo del programa")
            continue
        
        largo_caracteres_validado, largo_caracteres_computado = validar_int(largo_caracteres)
        
        if not largo_password_validado:
            print("ingreso una longitud de caracteres diferente a un numero entero : ")
            continue    
        largo_caracteres = int(largo_caracteres)
                
        if largo_caracteres < largo_caracteres_min:
            print(f"ingreso una longitud de caracteres menor de {largo_caracteres_min} caracteres : ")
            continue
        error_int = False

        # seccion cantidad de numeros
        largo_numeros = input(f"ingrese la longitud de numeros de al menos {largo_numeros_min } numeros : ")
        if largo_numeros == "Exit":
            print ("saliendo del programa")
            continue
        
        largo_numeros_validado, largo_numeros_computado = validar_int(largo_numeros)
        
        if not largo_numeros_validado:
            print("ingreso una longitud de numeros diferente a un numero entero : ")
            continue    
        largo_numeros = int(largo_numeros)
                
        if largo_numeros < largo_numeros_min:
            print(f"ingreso una longitud de numeros menor de {largo_numeros_min} caracteres : ")
            continue
        error_int = False

        # seccion letras mayusculas
        largo_letras_mayusculas = input(f"ingrese la longitud de letras mayusculas de al menos {largo_letras_mayusculas_min } letras mayusculas : ")
        if largo_numeros == "Exit":
            print ("saliendo del programa")
            continue
        
        largo_letras_mayusculas_validado, largo_letras_mayusculas_computado = validar_int(largo_letras_mayusculas)
        
        if not largo_letras_mayusculas_validado:
            print("ingreso una longitud de letras mayusculas diferente a un numero entero : ")
            continue    
        largo_letras_mayusculas = int(largo_letras_mayusculas)
                
        if largo_letras_mayusculas < largo_letras_mayusculas_min:
            print(f"ingreso una longitud de letras mayusculas menor de {largo_letras_mayusculas_min} caracteres : ")
            continue
        error_int = False

        largo_letras_minusculas = largo_password - largo_caracteres - largo_numeros - largo_letras_mayusculas

    salir = True
# print (largo_password)

"""
caracteres_permitidos = dict_permitido['letras_minusculas'] + dict_permitido['letras_mayusculas'] + dict_permitido ['numeros'] + dict_permitido['caracteres']
# print(caracteres_permitidos)

for i in range (largo_password):
    lista_acumulador.append (choice(caracteres_permitidos))
# print (lista_acumulador)

password = "".join(lista_acumulador)
print (password)

"""
caracteres_permitidos = dict_permitido['caracteres'] + dict_permitido ['numeros'] + dict_permitido['letras_mayusculas'] + dict_permitido['letras_minusculas']
# print(caracteres_permitidos)

for i in range (largo_caracteres):
    lista_acumulador_caracteres.append (choice(dict_permitido['caracteres']))
# print (lista_acumulador)

for i in range (largo_numeros):
    lista_acumulador_numeros.append (choice(dict_permitido['numeros']))
# print (lista_acumulador)

for i in range (largo_letras_mayusculas):
    lista_acumulador_letras_mayusculas.append (choice(dict_permitido['letras_mayusculas']))
# print (lista_acumulador)

for i in range (largo_letras_minusculas):
    lista_acumulador_letras_minusculas.append (choice(dict_permitido['letras_minusculas']))
# print (lista_acumulador)

"""
password = "".join(lista_acumulador_caracteres)
print (password)
password = "".join(lista_acumulador_numeros)
print (password)
password = "".join(lista_acumulador_letras_mayusculas)
print (password)
password = "".join(lista_acumulador_letras_minusculas)
print (password)

"""

acumulador = "".join(lista_acumulador_caracteres) + "".join(lista_acumulador_numeros) + "".join(lista_acumulador_letras_mayusculas) + "".join(lista_acumulador_letras_minusculas)
# print (acumulador)
i : int = 0

# control de eleccion no repetida
while i in range(largo_password_computado):
    caracter_elegido = choice(acumulador)
    lista_acumulador = list(acumulador)
    password_list.append(caracter_elegido)
    lista_acumulador.remove(caracter_elegido)
    acumulador = "".join(lista_acumulador)
    i += 1
    """
    if caracter_elegido not in password_barre:
        password_barre.append (caracter_elegido)
        i += 1
    """

password = "".join(password_list)
print (f"La password generada aleatoriamente es {password}")
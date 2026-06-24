from random import randint

from PantallasEC02 import pantalla_inicial

# funcion controlar que no haya caracteres especiales en un string
def controlar_caracteres_especiales(texto: str, caracteres_especiales: tuple) -> bool:
    encontrado : bool = False
    texto = list()
    texto_list = list(texto)
    for caracter in texto_list:
        for char_especial in caracteres_especiales:
            if caracter == char_especial:
                encontrado = True
                return encontrado

def normalizar_string(texto):
    try:
        return int(texto)
    except ValueError:
        try:
            return float(texto)
        except ValueError:
            texto = str(texto)
            texto = texto.strip()
            return texto

def control_ingreso_string (texto) -> tuple[str, bool, bool]:
    salir : bool = False
    error_verificacion_string : bool = False
    if texto.strip().lower() == "exit":
        salir = True
   #     break
    elif texto.strip() == "":
        print("Ingreso no válido, no se permiten entradas vacías. ingrese nuevamente.")
        error_verificacion_string = True
    #    continue
    elif not texto.find(".") == -1 and texto.replace(".","").isdigit():
        print("Ingreso no válido, ingresó un número decimal. ingrese nuevamente")
        error_verificacion_string = True
    #    continue
    elif not texto.find(",") == -1 and texto.replace(",","").isdigit():
        print("Ingreso no válido, ingresó un número separado por comas. ingrese nuevamente")
        error_verificacion_string = True
    #    continue
    elif texto.isdigit():
        print(".Ingresó un número entero. ingrese nuevamente")
        error_verificacion_string = True
    #    continue
    elif controlar_caracteres_especiales(texto, caracteres_especiales):
        print("Ingreso no válido, ingresó un caracter especial. Ingrese nuevamente.")
        error_verificacion_string = True
    #    continue
    elif isinstance(normalizar_string(texto), str):
        error_verificacion_string = False
    #    break
    else:
        print ("error de ingreso. ingrese un nombre")
        error_verificacion_string = True
    #    break
    return texto, salir, error_verificacion_string

def control_ingreso_string_reduced (texto) -> tuple[str, bool, bool]:
    salir : bool = False
    if texto.strip().lower() == "exit":
        salir = True
   #     break
    elif texto.strip() == "":
        print("Ingreso no válido, no se permiten entradas vacías. ingrese nuevamente.")
        error_verificacion_string = True
    #    continue
    elif not texto.find(".") == -1 and texto.replace(".","").isdigit():
        print("Ingreso no válido, ingresó un número decimal. ingrese nuevamente")
        error_verificacion_string = True
    #    continue
    elif not texto.find(",") == -1 and texto.replace(",","").isdigit():
        print("Ingreso no válido, ingresó un número separado por comas. ingrese nuevamente")
        error_verificacion_string = True
    #    continue
    elif texto.isdigit():
        print(".Ingresó un número entero. ingrese nuevamente")
        error_verificacion_string = True
    #    continue
    elif isinstance(normalizar_string(texto), str):
        error_verificacion_string = False
    #    break
    else:
        print ("error de ingreso. ingrese un nombre")
        error_verificacion_string = True
    #    break
    return texto, salir, error_verificacion_string

def validar_numero_random (numero_ticket_generado : int ) -> bool:
    coincide_random : bool = False
    for ticket in tickets:
        if numero_ticket_generado == ticket["numero_ticket"]:
            coincide_random = True
    return coincide_random

def ingresar_ticket ():

    error_verificacion_string = False
    salir = False

    while salir == False: 

        while error_verificacion_string == False and salir == False:
        
            nombre_ingresado = input("ingrese su Nombre (Exit para salir):")
            # print(f"el nombre ingresado es :{nombre_ingresado}")
            nombre_ingresado_validado, salir, error_verificacion_string = control_ingreso_string (nombre_ingresado)

            nombre_ingresado_validado = nombre_ingresado_validado.strip()
            nombre_ingresado_validado = nombre_ingresado_validado.lower()
            nombre_ingresado_validado = nombre_ingresado_validado.capitalize()

            if error_verificacion_string == True:
                error_verificacion_string = False
                continue
            if salir == True:
                break
            break
        # print(type(nombre_ingresado_validado))
        # print(f"el nombre ingresado es : {nombre_ingresado_validado}")

        while error_verificacion_string == False and salir == False:
            sector_ingresado = input("ingrese su Sector (Exit para salir):")
            # print(f"el sector ingresado es :{sector_ingresado}")
            sector_ingresado_validado, salir, error_verificacion_string = control_ingreso_string (sector_ingresado)
            if error_verificacion_string == True:
                error_verificacion_string = False
                continue
            if salir == True:
                break
            break
        # print(type(sector_ingresado_validado))
        # print(f"el sector ingresado es : {sector_ingresado_validado}")


        while error_verificacion_string == False and salir == False:
            asunto_ingresado = input("ingrese el Asunto (Exit para salir):")
            # print (f"el asunto ingresado es :{asunto_ingresado}")
            asunto_ingresado_validado, salir, error_verificacion_string = control_ingreso_string_reduced (asunto_ingresado)
            if error_verificacion_string == True:
                error_verificacion_string = False
                continue
            if salir == True:
                break
            break
        # print(type(asunto_ingresado_validado))
        # print(f"el asunto ingresado es : {asunto_ingresado_validado}")


        while error_verificacion_string == False and salir == False:
            problema_ingresado = input("ingrese la descripcion del problema (Exit para salir):")
            # print (f"el problema ingresado es :{problema_ingresado}")
            problema_ingresado_validado, salir, error_verificacion_string = control_ingreso_string_reduced (problema_ingresado)
            if problema_ingresado_validado == True:
                error_verificacion_string = False
                continue
            if salir == True:
                break
            break
        # print(type(problema_ingresado_validado))
        # print(f"el problema ingresado es : {problema_ingresado_validado}")
    
        if salir == True:
            continue

        coincide_random = True
        while coincide_random == True:
            numero_ticket_generado : int = randint(numeros_random[0], numeros_random[1])
            coincide_random = validar_numero_random(numero_ticket_generado)
    
        numero_ticket_validado = numero_ticket_generado

        ticket = {  
                    "numero_ticket" : numero_ticket_validado, 
                    "nombre" : nombre_ingresado_validado,
                    "sector" : sector_ingresado_validado,
                    "asunto" : asunto_ingresado_validado,
                    "problema" : problema_ingresado_validado,
                 }
        tickets.append(ticket)
        print (tickets)
        salir = True
    return

def leer_ticket (numero_ticket_leer : int) :
    # lista_numero_tickets : list = []
    for numero_ticket_barre in tickets:
        if numero_ticket_leer == numero_ticket_barre["numero_ticket"]:
            return numero_ticket_barre

def validar_ticket_entero (numero_ticket_leido : int) -> bool:
    if numero_ticket_leido.split() == "" :
        print ("no se permite un ingreso vacio")
        error_verificacion_entero = True
    elif not numero_ticket_leido.find(".") == -1 and numero_ticket_leido.replace(".","").isdigit() :
        print ("no se permite un numero decimal")
        error_verificacion_entero = True
    elif not numero_ticket_leido.find(",") == -1 and numero_ticket_leido.replace(",","").isdigit() :
        print ("no se permite un numero decimal")
        error_verificacion_entero = True
    elif not numero_ticket_leido.isdigit() :
        print ("no se permite letras")
        error_verificacion_entero = True
    elif numero_ticket_leido.isdigit() :
        error_verificacion_entero = False
    else:
        print("error de ingreso")
        error_verificacion_entero = True
    return error_verificacion_entero


def pantalla_leer_ticket (ticket : dict):
    print(f"Ticket nro : {ticket["numero_ticket"]}")
    print(f"Su nombre : {ticket["nombre"]}")
    print(f"Su sector : {ticket["sector"]}")
    print(f"Asunto : {ticket["asunto"]}")
    print(f"Descripción : {ticket["problema"]}")
    return

def salir_ticket () -> bool:
    salir = True
    return salir

""" inicializo variables"""
tickets : list = []
# print(type(tickets))
ticket : dict[str:int, str:str, str:str, str:str, str:str]= {}
# print(type(ticket))

numeros_random : tuple = (int, int)
numeros_random = (1000, 9999)

caracteres_especiales : tuple = ()
caracteres_especiales = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", '"', ",", ".", "<", ">", "/", "?")

ticket = {
            "numero_ticket" : "999",
            "nombre" : "prueba",
            "sector" : "grip",
            "asunto" : "BGP unreachable",
            "problema" : "la sesion BGP con le peer 209.217.24.13 se encuntra unreachable",
         }

"""
for clave, valor in ticket.items():
    print(f"imprimo clave : valor {clave}:{valor}")
"""

tickets.append(ticket)
# print(tickets)

error_verificacion_string : bool = False
error_verificacion_entero : bool = False
error_verificacion_ticket : bool = True

salir : bool = False

while salir == False:

    pantalla_inicial ()
    ingreso_pantalla_inicial = str(input())
    # print (f"el codigo de ingreso de pantalla inicial ingresado es :{ingreso_pantalla_inicial}")
 
    if ingreso_pantalla_inicial == str(1) and salir == False:
        ingresar_ticket ()
    elif ingreso_pantalla_inicial == str(2) and salir == False:
        error_verificacion_ticket = True
        while error_verificacion_ticket == True:
            ticket_leido = input("ingrese el numero de ticket a leer :")
            error_verificacion_ticket = validar_ticket_entero(ticket_leido)
        
        ticket_leido = int(ticket_leido)
        ticket= leer_ticket (ticket_leido)
        print (f"el ticket leido fue {ticket_leido}")
        if ticket:
            pantalla_leer_ticket(ticket)
        else:
            print(f"no se encontro el ticket {ticket_leido}")   
    elif ingreso_pantalla_inicial == str(3) and salir == False:
        salir = salir_ticket ()
    else:
        print("ingreso un código no permitido")
    
    # print(tickets)
print ("fin del programa. Gracias por confiar en Tecno3F")

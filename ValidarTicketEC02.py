"""Funcion para validar ticket entero"""

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
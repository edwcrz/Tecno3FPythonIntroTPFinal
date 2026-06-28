""" importo archivos .py con funciones"""
from PantallasEC02 import pantalla_inicial
from PantallasEC02 import pantalla_leer_ticket

from IngresarTicketEC02 import ingresar_ticket_test
from IngresarTicketEC02 import ingresar_ticket

from LeerTicketEC02 import leer_ticket

from MostrarTicketEC02 import mostrar_tickets

from SalirTicketEC02 import salir_ticket

from ValidarTicketEC02 import validar_ticket_entero

#import sys
# import os
# import random
# import subprocess

"""
import sys, os, random, subprocess
    # Ejecuta el comando de forma segura
    subprocess.run([comando], shell=True)
numero_random = random.randrange(1000, 9999) #con esto crean un numero random
os.path.isfile(ruta) # la palabra ruta obtendra el nombre del archivo y verificara que exista
sys.exit() #con este comando cierra la ejecucion del programa
"""

""" inicializo variables"""
tickets : list = []
# print(type(tickets))
ticket_list : list = []
# print(type(ticket_list))

ticket : dict[str:int, str:str, str:str, str:str, str:str]= {}
# print(type(ticket))

error_verificacion_string : bool = False
error_verificacion_entero : bool = False
error_verificacion_ticket : bool = True
salir : bool = False

while salir == False:

    pantalla_inicial ()
    ingreso_pantalla_inicial = str(input())
    # print (f"el codigo de ingreso de pantalla inicial ingresado es :{ingreso_pantalla_inicial}")

    if ingreso_pantalla_inicial == str(0) and salir == False:
        ingresar_ticket_test ()
    elif ingreso_pantalla_inicial == str(1) and salir == False:
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
        ticket_list = mostrar_tickets()
        print (f"la lista de tickets ingresada hasta el momento es {ticket_list}")
    elif ingreso_pantalla_inicial == str(4) and salir == False:
        salir = salir_ticket ()
    else:
        print("ingreso un código no permitido")
    
    # print(tickets)
print ("fin del programa. Gracias por confiar en Tecno3F")

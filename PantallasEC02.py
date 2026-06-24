from os import system, name
from time import sleep

""" pantalla inicial """
def pantalla_inicial ():
    pantalla_limpiar()
    print("\r", end="")
    print("Bienvenido al sistema de Tickets")
    print("\r", end="")
    print("1 - Generar un Ticket.")
    print("2 - Leer un Ticket.")
    print("3 - Listar Tickets.")
    print("4 - Salir.")
    print("Seleccione: ")
    return

""" pantalla de lectura de tickets """
def pantalla_leer_ticket (ticket : dict):
    pantalla_limpiar()
    print(f"Ticket nro : {ticket["numero_ticket"]}")
    print(f"Su nombre : {ticket["nombre"]}")
    print(f"Su sector : {ticket["sector"]}")
    print(f"Asunto : {ticket["asunto"]}")
    print(f"Descripción : {ticket["problema"]}")
    return

""" funcion para limpiar pantalla"""
def pantalla_limpiar ():
    sleep(3)
    if name == 'nt':
        system('cls')
    else:
        system('clear')

    
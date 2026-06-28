from JsonEC02 import leer_json

"""Funcion para mostrar los identificadores de los tickets registrados"""
def mostrar_tickets () -> list:
    ticket_list : list = []
    ticket_barre : dict = {}
    tickets = leer_json ("Tickets.json")
    for ticket_barre in tickets:
        ticket_list.append(ticket_barre["numero_ticket"])
    # print (f"la lista de tickets es :{ticket_list}")
    return ticket_list

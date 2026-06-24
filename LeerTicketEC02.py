from JsonEC02 import leer_json

"""Funcion para leer ticket"""
def leer_ticket (numero_ticket_leer : int) :
    # lista_numero_tickets : list = []
    tickets = leer_json("Tickets.json")
    ticket_barre : dict = {}
    for ticket_barre in tickets:
        if numero_ticket_leer == ticket_barre["numero_ticket"]:
            return ticket_barre
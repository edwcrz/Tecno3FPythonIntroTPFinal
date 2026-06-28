
""" Funcion de validaciòn de numero random para avisar si es repetido"""
def validar_numero_random (numero_ticket_generado : int , tickets : dict) -> bool:
    coincide_random : bool = False
    for ticket in tickets:
        if numero_ticket_generado == ticket["numero_ticket"]:
            coincide_random = True
    return coincide_random
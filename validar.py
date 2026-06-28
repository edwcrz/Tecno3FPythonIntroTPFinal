# funcion para validar que el parametro recibido es entero
# salida informa True-False si es entero y computar el largo
def validar_int (numero: int) -> tuple [bool, int]:
    largo_computado : int = 0
    if numero.isdigit() == True:
        largo_computado = int(numero)
        largo_validado = True
    else:
        largo_validado = False
    return (largo_validado, largo_computado)

"""Declaro Tupla de caracteres especiales inmutable"""
caracteres_especiales : tuple = ()
caracteres_especiales = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", '"', ",", ".", "<", ">", "/", "?")

"""Funcion Controlar que no haya caracteres especiales en un string"""
def controlar_caracteres_especiales(texto: str, caracteres_especiales: tuple) -> bool:
    encontrado : bool = False
    texto = list()
    texto_list = list(texto)
    for caracter in texto_list:
        for char_especial in caracteres_especiales:
            if caracter == char_especial:
                encontrado = True
                return encontrado

"""Funcion para normalizar un string"""
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

"""Funcion para controlar el ingreso de un string. incluye caracteres especiales"""
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


"""Funcion para controlar el ingreso de un string. no incluye caracteres especiales"""
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


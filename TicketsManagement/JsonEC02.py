import json
import sys
from os.path import isfile
from os.path import abspath
# from subprocess import run
# from os import getcwd

code = "utf-8"

def leer_json (archivo: str) -> list:
    # path = getcwd()
    # print (path.stdout)
    ruta = abspath(archivo)
    if not isfile(archivo):
        print(f"el archivo : {archivo} no existe in {ruta}")
        sys.exit()
    with open(archivo,'r', encoding= code) as f:
        
        tickets = json.load(f)
    return tickets

def guardar_json (archivo: str, tickets: list) -> None:
    with open(archivo,"w",encoding= code) as f:
        json.dump(tickets, f, indent= 4)
    return
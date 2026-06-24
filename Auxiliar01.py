"""
texto : str = "holacomoestas"
print(type(texto))
binario  = texto.find(".")
print (f"texto.find(.) devuelve :{binario}")
print(type(binario))
if texto.find(".") == 1:
    print("encontrado")
else:
    print("no encontrado")
"""

from subprocess import run
from os.path import isfile
from os import getcwd


# routes =run(["dir"], capture_output=True, text=True)
# print (f"las rutas son : {routes.stdout}")
"""
path = getcwd()
print (f"el directorio de trabajo es : {path}")
"""
# routes =run(["dir"], capture_output=True, text=True)
# print (f"las rutas son : {routes.stdout}")

# changedir =run(["cd .."], )


path = getcwd()
print (f"el directorio de trabajo es : {path}")

# changedir = run(["cd Users\Eduardo\Mi unidad (edwcrz@gmail.com)\edwcrzdev\PythonProjects\Tecno3F\PythonIntro"])

"""
directorio = run(["dir"], capture_output=True, text=True, shell=True)
print (directorio.stdout)
"""

"""
path = run(["pwd"], capture_output=True, text=True, shell=True)
print (path.stdout)
"""

"""
for items in directorio:
    if items == "Tickets.json":
        print(items)
    else: print(items)
"""
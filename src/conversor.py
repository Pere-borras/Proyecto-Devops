import os
from recopilador_datos import recopilador_datos
from recopilador_datos import json_arr


def conversor():
    file = open(
        "//Users/pere/Desktop/CFGS_21_22/Proyecto_devops/Proyecto_Dan_Pere/prueba.md", "w")
    input = recopilador_datos(json_arr)
    for element in input:
        file.write(element + os.linesep)
    file.close()


conversor()

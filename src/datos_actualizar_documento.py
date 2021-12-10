from conectar_con_mongo import conectar_con_mongo
from recopilar_datos_documento import recopilar_datos_documento


def datos_actualizar_documento():
    nombre_documento = input(
        'Introduzca el nombre del pack que quiere actualizar\n')

    colleccion = conectar_con_mongo()

    documento = colleccion.find_one({"Nombre pack": nombre_documento})

    if documento:
        print('Ahora escriba el documento, cambiando los valores para actualizar')
        nombre_pack, calidad_pack, stock_pack, dimensiones_pack, contenido = recopilar_datos_documento()
        return nombre_pack, calidad_pack, stock_pack, dimensiones_pack, contenido, documento
    else:
        return

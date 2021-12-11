from eliminar_documentos.sanear_query_borrar import sanear_query_borrar
from eliminar_documentos.borrar_documentos import borrar_documentos
from eliminar_documentos.borrar_un_documento import borrar_un_documento


def query_D():

    pregunta = input(
        '¿Desea borrar uno o varios documentos? Introduzca "1" para borrar un documento y "2" para borrar varios: ')

    if pregunta == '1':
        query = input('Introduzca el nombre del pack: ')

        query = sanear_query_borrar(query)
        borrar_un_documento(query)

    elif pregunta == '2':
        query_campo = input(
            'Introduzca el campo por el que quiere borrar los documentos. Por ejemplo, "calidad": ')
        query_valor = input(
            'Introduzca el valor por el que quiere borrar los documentos. Por ejemplo, "basic": ')

        query = {query_campo: query_valor}

        borrar_documentos(query)

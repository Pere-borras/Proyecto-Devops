from encontrar_documentos.query import sanear_query
from encontrar_documentos.request_query import query_request
from encontrar_documentos.app import app
from encontrar_documentos.reiniciar_hugo import reiniciar_hugo
from mongo_archivos.mongo_find import mongo_find
from insertar_documentos.insertar_documento import insertar_documento
from actualizar_documentos.actualizar_documento import actualizar_documento
from eliminar_documentos.query_borrar_documentos import query_D

print()
print()
pregunta = input('¡Bienvenido! Si deseas crear documentos en la base de datos, introduce "1". Si deseas encontrar datos en la base de datos, introduce "2". Si deseas actualizar algún campo en la base de datos, introduce "3". Si deseas eliminar algún documento en la base de datos, introduce "4": ')

if pregunta == '1':
    # insertar un documento nuevo en la BD
    try:
        insertar_documento()
    except:
        print('Ha introducido los datos de manera incorrecta. Inténtelo de nuevo.')

elif pregunta == '2':
    # obtener documentos de la BD
    reiniciar_hugo()
    consulta = sanear_query(query_request())
    json_files = mongo_find(print(consulta))
    app(json_files)

elif pregunta == '3':
    # actualizar algún campo de los documentos en la BD
    try:
        actualizar_documento()
    except:
        print('El documento no se ha podido actualizar,asegurese de que ha introducido bien todos los datos.')

elif pregunta == '4':
    query_D()

else:
    print('Ha introducido un dato incorrecto, por favor, introdúzcalo de nuevo')

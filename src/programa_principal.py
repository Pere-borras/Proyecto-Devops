from query import query
from request_query import query_request
from app import app
from mongo_find import mongo_find

print()
print()
pregunta = input('¡Bienvenido! Si deseas crear documentos en la base de datos, introduce "1". Si deseas encontrar datos en la base de datos, introduce "2". Si deseas actualizar algún campo en la base de datos, introduce "3". Si deseas eliminar algún documento en la base de datos, introduce "4": ')

if pregunta == '1':
    print('Actualmente esta función no está disponible')

elif pregunta == '2':
    consulta = query(query_request())
    json_files = mongo_find(print(consulta))
    app(json_files)

elif pregunta == '3':
    print('Actualmente esta función no está disponible')

elif pregunta == '4':
    print('Actualmente esta función no está disponible')

else:
    print('Ha introducido un dato incorrecto, por favor, introdúzcalo de nuevo')

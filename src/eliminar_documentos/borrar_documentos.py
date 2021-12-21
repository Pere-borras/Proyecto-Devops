import os, sys
p = os.path.abspath('src')
sys.path.insert(1,p)
from mongo_archivos.conectar_con_mongo import conectar_con_mongo

def borrar_documentos (query):

    archivos = []

    collection = conectar_con_mongo()
    encontrado = collection.find(query)

    for archivo in encontrado:
        archivos.append(archivo)

    if len(archivos) > 0:
        collection.delete_many(query)
        print('Los documentos ' + str(query) + ' han sido borrados')

    else:
        print('No se han podido encontrar los documentos ' + str(query) + ' que queria eliminar.')

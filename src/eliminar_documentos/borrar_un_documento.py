import os, sys
p = os.path.abspath('src')
sys.path.insert(1,p)
from mongo_archivos.conectar_con_mongo import conectar_con_mongo

def borrar_un_documento (query):
    try:
        archivos = []

        collection = conectar_con_mongo()
        encontrado = collection.find(query)

        for archivo in encontrado:
            archivos.append(archivo)

        if len(archivos) > 0:
            collection.delete_one(query)

    except:
        print('No se ha podido encontrar el documento ' + str(query) + ' que queria eliminar.')
    else:
        print('El documento ' + str(query) + ' ha sido borrado.')


from conectar_con_mongo import conectar_con_mongo

def borrar_un_documento (query):
    try:
        collection = conectar_con_mongo()
        encontrado = collection.find(query)
        if len(encontrado) > 0:
            collection.delete_one(query)
    except:
        print('No se ha podido encontrar el documento ' + str(query) + ' que queria eliminar.')
    else:
        print('El documento ' + str(query) + ' ha sido borrado.')


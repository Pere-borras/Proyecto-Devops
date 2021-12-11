from mongo.conectar_con_mongo import conectar_con_mongo

def borrar_documentos (query):
    try:
        collection = conectar_con_mongo()
        encontrado = collection.find_one(query)
        if len(encontrado) > 0:
            collection.delete_many(query)
    except:
        print('No se han podido encontrar los documentos ' + str(query) + ' que queria eliminar.')
    else:
        print('Los documentos ' + str(query) + ' han sido borrados')

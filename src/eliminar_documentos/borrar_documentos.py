from mongo_archivos.conectar_con_mongo import conectar_con_mongo

def borrar_documentos (query):
    try:
        archivos = []

        collection = conectar_con_mongo()
        encontrado = collection.find(query)

        for archivo in encontrado:
            archivos.append(archivo)

        if len(archivos) > 0:
            collection.delete_many(query)
    except:
        print('No se han podido encontrar los documentos ' + str(query) + ' que queria eliminar.')
    else:
        print('Los documentos ' + str(query) + ' han sido borrados')

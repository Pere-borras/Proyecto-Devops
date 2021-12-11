from mongo.conectar_con_mongo import conectar_con_mongo

def mongo_find(query):
    collection = conectar_con_mongo()
    documents = collection.find(query)
    json_files= []
    for document in documents:
        json_files.append(document)
    return json_files
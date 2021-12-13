from conectar_con_mongo import conectar_con_mongo

def mongo_find(query):
    
    collection = conectar_con_mongo()
    
    #Se le pasa la query para buscar todos los documentos que tengan esa query
    documents = collection.find(query)
    
    json_files= []
    
    #Se van introduciendo todos los documentos en una lista
    for document in documents:
        json_files.append(document)
    return json_files
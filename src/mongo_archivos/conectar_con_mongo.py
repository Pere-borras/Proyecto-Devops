from pymongo import MongoClient

def conectar_con_mongo():
    try:
        uri = "mongodb+srv://DanPere:DawDual20212022@proyectodevops.oqpis.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        client = MongoClient(uri)
        db = client.Proyecto_Dual
        collection = db.packs
        print('La conexión con la base de datos ha sido un éxito.')
        return collection
    except:
        print('La conexión con la base de datos ha fallado.')
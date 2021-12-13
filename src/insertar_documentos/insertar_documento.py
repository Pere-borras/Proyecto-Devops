import os, sys
p = os.path.abspath('src')
sys.path.insert(1,p)
from mongo_archivos.conectar_con_mongo import conectar_con_mongo
from recopilar_datos_documento import recopilar_datos_documento

def insertar_documento ():
    try:
        documento = recopilar_datos_documento()

        colleccion = conectar_con_mongo()
    
        colleccion.insert_one(documento)
        
        print("Se ha introducido el documento.")
    
    except:
        return 'No se ha conseguido insertar el documento, intentelo de nuevo'
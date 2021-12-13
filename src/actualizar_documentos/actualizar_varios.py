import os, sys
p = os.path.abspath('src')
sys.path.insert(1,p)
from mongo_archivos.conectar_con_mongo import conectar_con_mongo
from insertar_documentos.recopilar_datos_documento import recopilar_datos_documento

def actualizar_varios(nombre_documento):
    #Se recogen todos los datos nuevamente para actualizar el documento al completo 
    documento = recopilar_datos_documento()

    colleccion = conectar_con_mongo()
            
    #Y aqui se actualiza campo a campo
    for item in reversed(documento.items()):
        item = [item]
        colleccion.update_one(nombre_documento, {"$set":dict(item)})

    print("Se han actualizado los valores")
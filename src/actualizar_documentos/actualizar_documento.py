import os, sys

p = os.path.abspath('src')
sys.path.insert(1,p)
from mongo_archivos.conectar_con_mongo import conectar_con_mongo
from insertar_documentos.recopilar_datos_documento import recopilar_datos_documento

def actualizar_documento():
    
    try:
        nombre_documento = {'Nombre pack':input('Introduzca el nombre del pack que quiere actualizar\n')}
    
        cantidad_actualizar = input("Si quiere actualizar un solo campo del documento escriba 1\n\
Si quiere actualizar varios campos escriba varios\n")
    
        colleccion = conectar_con_mongo()
        
        # Una vez se decide si va a cambiar un campo o varios se decide que se hace
        if cantidad_actualizar == "1":
            
            #Primero se escribe el campo para que se quiere actualizar
            campo = {input("Introduzca el campo que quiere actualizar\n"):input("Introduzca el valor cambiado\n")}

            #Ahora se actualiza el campo indicandole pirmero a update_one el nombre del documento al cual le vamos a actualizar el campo
            colleccion.update_one(nombre_documento,{"$set":campo})

            print("Se ha actualizado el campo")
    
        elif cantidad_actualizar == "varios":
            
            #Se recogen todos los datos nuevamente para actualizar el documento al completo 
            documento = recopilar_datos_documento()
            
            #Y aqui se actualiza campo a campo
            for item in reversed(documento.items()):
                item = [item]
                colleccion.update_one(nombre_documento, {"$set":dict(item)})

            print("Se han actualizado los valores")

        else:
            print("Se ha producido un error, por favor inserte bien la cantidad de campos que quiere actualizar.")
    except:
        print('Ha introducido mal algun valor, por favor intentelo de nuevo')

    
            

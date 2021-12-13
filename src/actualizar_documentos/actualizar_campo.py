import os, sys
p = os.path.abspath('src')
sys.path.insert(1,p)
from mongo.conectar_con_mongo import conectar_con_mongo

def actualizar_campo(nombre_documento):

    colleccion = conectar_con_mongo()

    #Primero se escribe el campo para que se quiere actualizar
    campo = {input("Introduzca el campo que quiere actualizar\n"):input("Introduzca el valor cambiado\n")}

    #Ahora se actualiza el campo indicandole pirmero a update_one el nombre del documento al cual le vamos a actualizar el campo
    colleccion.update_one(nombre_documento,{"$set":campo})

    print("Se ha actualizado el campo")
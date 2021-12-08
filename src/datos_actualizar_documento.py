from conectar_con_mongo import conectar_con_mongo
from recopilar_datos_documento import recopilar_datos_documento

def datos_actualizar_documento():
    try:
        nombre_documento =input('Introduzca el nombre del pack que quiere actualizar\n')
        
        colleccion = conectar_con_mongo()
        
        documento = colleccion.find_one({"Nombre pack":nombre_documento})
        
        print('Ahora escriba el documento, cambiando los valores para actualizar')
        
        nombre_pack,calidad_pack,precio_pack,stock_pack,dimensiones_pack,contenido = recopilar_datos_documento()
        
        if len(nombre_documento) > 0:
            return nombre_pack,calidad_pack,precio_pack,stock_pack,dimensiones_pack,contenido,documento
        else:
            return False
    
    except:
        print('El documento que busca actualizar no existe.')

import os, sys
p = os.path.abspath('src')
sys.path.insert(1,p)
from mongo.conectar_con_mongo import conectar_con_mongo
from actualizar_varios import actualizar_varios
from actualizar_campo import actualizar_campo

def actualizar_documento():
    
    try:
        nombre_documento = {'Nombre pack':input('Introduzca el nombre del pack que quiere actualizar\n')}
    
        cantidad_actualizar = input("Si quiere actualizar un solo campo del documento escriba 1\n\
Si quiere actualizar varios campos escriba varios\n")
    
        colleccion = conectar_con_mongo()
        
        # Una vez se decide si va a cambiar un campo o varios se decide que se hace
        if cantidad_actualizar == "1":
            
            actualizar_campo(nombre_documento)
    
        elif cantidad_actualizar == "varios":
            
            actualizar_varios(nombre_documento)

        else:
            print("Se ha producido un error, por favor inserte bien la cantidad de campos que quiere actualizar.")
    except:
        print('Ha introducido mal algun valor, por favor intentelo de nuevo')

    
            

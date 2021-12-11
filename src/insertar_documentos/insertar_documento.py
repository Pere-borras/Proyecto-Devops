from insertar_documentos.recopilar_datos_documento import recopilar_datos_documento
from insertar_documentos.insertar_documento_basic import insertar_documento_basic
from insertar_documentos.insertar_documento_standard import insertar_documento_standard
from insertar_documentos.insertar_documento_premium import insertar_documento_premium

def insertar_documento ():
    try:
        nombre_pack,calidad_pack,stock_pack,dimensiones_pack,contenido = recopilar_datos_documento()
    
        if calidad_pack.lower() == 'basic':
            insertar_documento_basic(nombre_pack,stock_pack,dimensiones_pack,contenido)
    
        elif calidad_pack.lower() == 'standard':
            insertar_documento_standard(nombre_pack,stock_pack,dimensiones_pack,contenido)
    
        elif calidad_pack.lower() == 'premium':
            insertar_documento_premium(nombre_pack,stock_pack,dimensiones_pack,contenido)
    
        else:
            print('Ha introducido mal la calidad del pack')
    except:
        return  
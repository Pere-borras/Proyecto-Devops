from actualizar_documentos.datos_actualizar_documento import datos_actualizar_documento
from actualizar_documentos.actualizar_basic import actualizar_basic
from actualizar_documentos.actualizar_standard import actualizar_standard
from actualizar_documentos.actualizar_premium import actualizar_premium

def actualizar_documento():
    try:
        nombre_pack,calidad_pack,stock_pack,dimensiones_pack,contenido,documento = datos_actualizar_documento()
    
        if calidad_pack.lower() == 'basic':
            actualizar_basic(nombre_pack,stock_pack,dimensiones_pack,contenido,documento)
    
        elif calidad_pack.lower() == 'standard':
            actualizar_standard(nombre_pack,stock_pack,dimensiones_pack,contenido,documento)
    
        elif calidad_pack.lower() == 'premium':
            actualizar_premium(nombre_pack,stock_pack,dimensiones_pack,contenido,documento)
    
        else:
            print('Ha introducido mal la calidad del pack')
    
    except:
        return

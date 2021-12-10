from conectar_con_mongo import conectar_con_mongo

def actualizar_standard(nombre_pack,stock_pack,dimensiones_pack,contenido,documento):
    
    contenidos = {"contenidos":{
        contenido[0]:{
            "caracteristicas":{
                "Precio":str(contenido[1]),
                "Calidad":contenido[2],
                "Material":contenido[3],
                "Cantidad":contenido[4],
                "Stock":contenido[5],
                "Demanda":contenido[6]
            }
        },
        contenido[7]:{
            "caracteristicas":{
                "Precio":str(contenido[8]),
                "Calidad":contenido[9],
                "Material":contenido[10],
                "Cantidad":contenido[11],
                "Stock":contenido[12],
                "Demanda":contenido[13]
            }
        },
        contenido[14]:{
            "caracteristicas":{
                "Precio":str(contenido[15]),
                "Calidad":contenido[16],
                "Material":contenido[17],
                "Cantidad":contenido[18],
                "Stock":contenido[19],
                "Demanda":contenido[20]
            }
        }}}
    
    colleccion = conectar_con_mongo()
    
    documento_actualizado ={"Nombre pack":nombre_pack,
    "calidad":"Standard",
    "precio":str(contenido[1]+contenido[8]+contenido[15]),
    "stock":stock_pack,
    "dimensiones":{
        "altura":dimensiones_pack[0],
        "ancho":dimensiones_pack[1]
    },
    "contenidos":contenidos["contenidos"]
    }

    colleccion.update_one(documento, documento_actualizado)
    print('El documento ha sido actualizado con exito')
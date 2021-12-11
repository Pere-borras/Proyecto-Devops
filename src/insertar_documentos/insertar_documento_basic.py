from mongo.conectar_con_mongo import conectar_con_mongo

def insertar_documento_basic(nombre_pack,stock_pack,dimensiones_pack,contenido):
    
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
        }}}
    
    colleccion = conectar_con_mongo()
    
    colleccion.insert_one({"Nombre pack":nombre_pack,
    "calidad":"Basic",
    "precio":str(contenido[1] + contenido[8]),
    "stock":stock_pack,
    "dimensiones":{
        "altura":dimensiones_pack[0],
        "ancho":dimensiones_pack[1]
    },
    "contenidos":contenidos["contenidos"]
    })
    
    print("Se ha introducido el documento.")
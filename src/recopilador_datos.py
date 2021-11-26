json_arr = {
    "Nombre pack": "Pack Squanchy Style",
    "calidad": "Basic",
    "precio": "7",
    "stock": "25",
    "dimensiones": {
        "altura": "3 cm",
        "ancho": "6 cm"
    },
    "contenidos": {
        "Rifle de pulso": {
            "caracteristicas": {
                "Precio": "5",
                "Calidad": "30",
                "Material": "normal",
                "Cantidad": "1",
                "Stock": "25",
                "Demanda": "10"
            }
        },
        "Poción del arcoiris": {
            "caracteristicas": {
                "Precio": "2",
                "Calidad": "20",
                "Material": "consumible",
                "Cantidad": "1",
                "Stock": "50",
                "Demanda": "63"
            }
        }
    }
}


def recopilador_datos(json_arr):
    output = []
    json_contenidos = json_arr['contenidos']
    llaves_contenidos = json_contenidos.keys()
    list(llaves_contenidos)

    output.append('## ' + 'Nombre pack')
    output.append('- ' + str(json_arr["Nombre pack"]))
    output.append('#### ' + 'Calidad')
    output.append('- ' + str(json_arr["calidad"]))
    output.append('#### ' + 'Precio')
    output.append('- ' + str(json_arr["precio"]))
    output.append('#### ' + 'Stock')
    output.append('- ' + str(json_arr["stock"]))
    output.append('#### ' + 'Dimensiones')
    output.append('- ' + 'Altura: ' + str(json_arr['dimensiones']['altura']))
    output.append('- ' + 'Ancho: ' + str(json_arr['dimensiones']['ancho']))
    output.append('### ' + 'Contenidos')

    for item in llaves_contenidos:
        output.append('### ' + str(item))
        output.append('#### ' + 'Caracteristicas')
        output.append('    ' + '- ' + 'Precio: ' +
                      str(json_arr['contenidos'][str(item)]['caracteristicas']['Precio']))
        output.append('    ' + '- ' + 'Calidad: ' +
                      str(json_arr['contenidos'][str(item)]['caracteristicas']['Calidad']))
        output.append('    ' + '- ' + 'Material: ' +
                      str(json_arr['contenidos'][str(item)]['caracteristicas']['Material']))
        output.append('    ' + '- ' + 'Cantidad: ' +
                      str(json_arr['contenidos'][str(item)]['caracteristicas']['Cantidad']))
        output.append('    ' + '- ' + 'Stock: ' +
                      str(json_arr['contenidos'][str(item)]['caracteristicas']['Stock']))
        output.append('    ' + '- ' + 'Demanda: ' +
                      str(json_arr['contenidos'][str(item)]['caracteristicas']['Demanda']))

    return output

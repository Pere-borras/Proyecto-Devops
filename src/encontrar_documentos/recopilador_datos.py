def recopilador_datos(json_arr):

    output = []
    json_contenidos = json_arr['contenidos']
    llaves_contenidos = json_contenidos.keys()
    list(llaves_contenidos)
    # información necesaria para Hugo
    output.append('---')
    output.append('title: ' + '"' + str(json_arr["Nombre pack"]) + '"')
    output.append('draft: true')
    output.append('tags: ' + '[' + '"' + str(json_arr["calidad"]) + '"' + ']')
    output.append('---')
    # fin información necesaria para Hugo
    output.append('## ' + str(json_arr["Nombre pack"]))
    output.append('#### ' + 'Calidad: ' + str(json_arr["calidad"]) + '.')
    output.append('#### ' + 'Precio: ' + str(json_arr["precio"]) + '.')
    output.append('#### ' + 'Stock: ' + str(json_arr["stock"]) + '.')
    output.append('#### ' + 'Dimensiones')
    output.append('**' + 'Altura' + '**' + ': ' +
                  str(json_arr['dimensiones']['altura']) + '.')
    output.append('')
    output.append('**' + 'Ancho' + '**' + ': ' +
                  str(json_arr['dimensiones']['ancho']) + '.')
    output.append('## ' + 'Contenidos')

    for item in llaves_contenidos:
        output.append('- ' + str(item))
        output.append('    ' + '- ' + 'Caracteristicas')
        output.append('        ' + '- ' + 'Precio: ' +
                      str(json_arr['contenidos'][str(item)]['caracteristicas']['Precio']))
        output.append('        ' + '- ' + 'Calidad: ' +
                      str(json_arr['contenidos'][str(item)]['caracteristicas']['Calidad']))
        output.append('        ' + '- ' + 'Material: ' +
                      str(json_arr['contenidos'][str(item)]['caracteristicas']['Material']))
        output.append('        ' + '- ' + 'Cantidad: ' +
                      str(json_arr['contenidos'][str(item)]['caracteristicas']['Cantidad']))
        output.append('        ' + '- ' + 'Stock: ' +
                      str(json_arr['contenidos'][str(item)]['caracteristicas']['Stock']))
        output.append('        ' + '- ' + 'Demanda: ' +
                      str(json_arr['contenidos'][str(item)]['caracteristicas']['Demanda']))

    return output

from encontrar_documentos.conversor import conversor
from encontrar_documentos.recopilador_datos import recopilador_datos


def app(json_files):

    counter = 0

    if len(json_files) <= 0:
        print('No se ha encontrado ningún archivo. ¿Ha introducido la query de forma correcta?')
        return

    for entrance in json_files:
        counter += 1
        json_arr = entrance
        output = recopilador_datos(json_arr)
        conversor(output)
    print('Todos los archivos han sido convertidos (total de archivos -> ' +
          str(counter) + ')')
def sanear_query_borrar(query):

    if query == '':
        return print(
            'El nombre del pack no puede ser una string vacía, por favor, inténtelo de nuevo')

    else:
        query_return = {'Nombre pack': query}
        return query_return

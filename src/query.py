from pprint import pprint


def query():
    schema = {
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
    print()
    print('El siguiente diccionario es un ejemplo del esquema a seguir para realizar una búsqueda correcta en la base de datos de MongoDB:')
    print()

    pprint(schema)
    print()
    print()

    query = input(
        'Indique los campos que quiera buscar con la sintaxis "campo":"valor", recuerde que si quiere consultar campos que están dentro de otros campos, debe ajustarse al esquema. Si quiere buscar todos los documentos de la colección, simplemente pulse Enter: ')

    if query == '':
        query = '{' + query + '}'
        return

    if query[0] != '{':
        query = '{' + query

    if query[-1] != '}':
        query = query + '}'

    return query

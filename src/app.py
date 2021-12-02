from Conectar_py_mongo import conectar_pymongo
from conversor import conversor
from recopilador_datos import recopilador_datos

counter = -1
json_files = conectar_pymongo()

for entrance in json_files:
    if counter >= len(json_files):
        break
    else:
        counter += 1
    json_arr = json_files[counter]
    output = recopilador_datos(json_arr)
    conversor(output)
print('Todos los archivos han sido convertidos (total de archivos -> ' +
      str(counter + 1) + ')')

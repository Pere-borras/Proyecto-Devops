import os

n_archivo = 1


def conversor(output, carpeta):

    global n_archivo
    ext_archivo = '.md'
    file = open(
        os.path.join(os.getcwd(), 'hugo','content',str(carpeta),str(n_archivo) + ext_archivo), "w")

    for element in output:
        file.write(str(element) + os.linesep)
    file.close()

    print('¡Archivo ' + str(n_archivo) + ' convertido correctamente!')
    n_archivo += 1

    return

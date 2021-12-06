def datos_insertar_documento():
    
    nombre_pack = input('Escriba el nombre del pack...')
    
    calidad_pack = input('Escriba la calidad del pack, eligiendo entre: Basic, Standard y Premium\n')
    
    precio_pack = input('Introduzca el valor del pack al completo\n\
Recuerde que la suma de los precios del contenido del pack tiene que ser el mismo que el del pack\n')
    
    stock_pack = input('Introduzca el numero de packs que hay\n')
    
    altura_pack = input('Introduzca la altura con centimetros\n')
    
    ancho_pack = input('Introduzca el ancho con cm\n')
    
    dimensiones_pack = [altura_pack, ancho_pack]
    
    cantidad_contenidos = {'basic':2,'standard':3,'premium':4}
    
    contenido = {}
    contador = 0
    if calidad_pack in cantidad_contenidos.keys():
        for number in range(0,cantidad_contenidos[calidad_pack.lower()]):
    
            contenido[contador]= input('Escriba el nombre del contenido\n')
            contador += 1
    
            contenido[contador]= input('Introduzca el precio del contenido\n')
            contador += 1
    
            contenido[contador]= input('Escriba la calidad del contenido\n')
            contador += 1
    
            contenido[contador]= input('Escriba el material del contenido\n')
            contador += 1
    
            contenido[contador]= input('Introduzca la cantidad del contenido \n')
            contador += 1
    
            contenido[contador]= input('Introduzca el stock del contenido\n')
            contador += 1
    
            contenido[contador]= input('Introduzca la demanda del contenido\n')
            contador += 1
    
        return nombre_pack,calidad_pack,precio_pack,stock_pack,dimensiones_pack,contenido
    else:
        print('Se ha producido un error, por favor intentelo de nuevo.')
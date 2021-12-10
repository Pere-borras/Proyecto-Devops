def recopilar_datos_documento():
    
    nombre_pack = input('Escriba el nombre del pack...\n')
    
    calidad_pack = input('Escriba la calidad del pack, eligiendo entre: Basic, Standard y Premium\n')
    
    stock_pack = input('Introduzca el stock del pack\n')
    
    altura_pack = input('Introduzca la altura en centimetros\n')
    
    ancho_pack = input('Introduzca el ancho en cm\n')
    
    dimensiones_pack = [altura_pack, ancho_pack]
    
    cantidad_contenidos = {'basic':2,'standard':3,'premium':4}
    
    contenido = {}
    contador = 0
    if calidad_pack in cantidad_contenidos.keys():
        # Al entrar al for se decide las vueltas que dara dependiendo de la calidad del pack. Cada vuelta es un contenido
        for number in range(0,cantidad_contenidos[calidad_pack.lower()]):
    
            contenido[contador]= input('Escriba el nombre del contenido\n')
            contador += 1

            # Aqui se hace un try except para que si o si ese contenido sea un numero ya que el precio del pack es la suma del precio de los contenidos
            try:
                contenido[contador]= float(input('Introduzca el precio del contenido\n'))
                contador += 1
            except:
                print('Por favor introduzca solo numeros\nIntentelo de nuevo')
                return
    
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
    
        return nombre_pack,calidad_pack,stock_pack,dimensiones_pack,contenido
    else:
        print('Se ha producido un error, por favor intentelo de nuevo.')
def recopilar_datos_documento():
    
    #Recoge todos los valores para poder cumplir con el squema de la base de datos
    nombre_pack = {"Nombre pack":input('Escriba el nombre del pack\n')}
    
    calidad_pack = {"calidad":input('Escriba la calidad del pack, eligiendo entre: Basic, Standard y Premium\n')}

    stock_pack = {"stock":input('Introduzca el stock del pack\n')}
    
    dimensiones_pack = {"dimensiones":{
        "altura":input("Introduzca la altura del pack en cm\n"),
        "ancho":input("Introduzca el ancho del pack en cm\n")
    }}
    
    #Dependiendo de la calidad entrara en un if u otro ya que tienen difente cantidad de contenidos cada calidad
    contenido = {}
    
    if calidad_pack["calidad"] == 'Basic':
        contenido.update({"contenidos": 
        {input("Introduzca el nombre del contenido\n"):{"caracteristicas":
            {"Precio":input("Introduzca el precio del contenido\n"),
             "Calidad":input("Introduzca la calidad del contenido\n"),
             "Material":input("Introduzca el material del que esta hecho\n"),
             "Cantidad":input("Introduzca la cantidad de veces que viene este contenido en el pack\n"),
             "Stock":input("Introduzca el stock del contenido\n"),
             "Demanda":input("Introduzca la demanda del contenido\n")}},
        input("Introduzca el nombre del contenido\n"):{"caracteristicas":
            {"Precio":input("Introduzca el precio del contenido\n"),
             "Calidad":input("Introduzca la calidad del contenido\n"),
             "Material":input("Introduzca el material del que esta hecho\n"),
             "Cantidad":input("Introduzca la cantidad de veces que viene este contenido en el pack\n"),
             "Stock":input("Introduzca el stock del contenido\n"),
             "Demanda":input("Introduzca la demanda del contenido\n")}}}})
    
    elif calidad_pack["calidad"] == "Standard":
        contenido.update({"contenidos":
        {input("Introduzca el nombre del contenido\n"):{"caracteristicas":
            {"Precio":input("Introduzca el precio del contenido\n"),
             "Calidad":input("Introduzca la calidad del contenido\n"),
             "Material":input("Introduzca el material del que esta hecho\n"),
             "Cantidad":input("Introduzca la cantidad de veces que viene este contenido en el pack\n"),
             "Stock":input("Introduzca el stock del contenido\n"),
             "Demanda":input("Introduzca la demanda del contenido\n")}},
        input("Introduzca el nombre del contenido\n"):{"caracteristicas":
            {"Precio":input("Introduzca el precio del contenido\n"),
             "Calidad":input("Introduzca la calidad del contenido\n"),
             "Material":input("Introduzca el material del que esta hecho\n"),
             "Cantidad":input("Introduzca la cantidad de veces que viene este contenido en el pack\n"),
             "Stock":input("Introduzca el stock del contenido\n"),
             "Demanda":input("Introduzca la demanda del contenido\n")}},
        input("Introduzca el nombre del contenido\n"):{"caracteristicas":
            {"Precio":input("Introduzca el precio del contenido\n"),
             "Calidad":input("Introduzca la calidad del contenido\n"),
             "Material":input("Introduzca el material del que esta hecho\n"),
             "Cantidad":input("Introduzca la cantidad de veces que viene este contenido en el pack\n"),
             "Stock":input("Introduzca el stock del contenido\n"),
             "Demanda":input("Introduzca la demanda del contenido\n")}}
             }})
    elif calidad_pack["calidad"] == "Premium":
        contenido.update({"contenidos":
        {input("Introduzca el nombre del contenido\n"):{"caracteristicas":
            {"Precio":input("Introduzca el precio del contenido\n"),
             "Calidad":input("Introduzca la calidad del contenido\n"),
             "Material":input("Introduzca el material del que esta hecho\n"),
             "Cantidad":input("Introduzca la cantidad de veces que viene este contenido en el pack\n"),
             "Stock":input("Introduzca el stock del contenido\n"),
             "Demanda":input("Introduzca la demanda del contenido\n")}},
        input("Introduzca el nombre del contenido\n"):{"caracteristicas":
            {"Precio":input("Introduzca el precio del contenido\n"),
             "Calidad":input("Introduzca la calidad del contenido\n"),
             "Material":input("Introduzca el material del que esta hecho\n"),
             "Cantidad":input("Introduzca la cantidad de veces que viene este contenido en el pack\n"),
             "Stock":input("Introduzca el stock del contenido\n"),
             "Demanda":input("Introduzca la demanda del contenido\n")}},
        input("Introduzca el nombre del contenido\n"):{"caracteristicas":
            {"Precio":input("Introduzca el precio del contenido\n"),
             "Calidad":input("Introduzca la calidad del contenido\n"),
             "Material":input("Introduzca el material del que esta hecho\n"),
             "Cantidad":input("Introduzca la cantidad de veces que viene este contenido en el pack\n"),
             "Stock":input("Introduzca el stock del contenido\n"),
             "Demanda":input("Introduzca la demanda del contenido\n")}},
        input("Introduzca el nombre del contenido\n"):{"caracteristicas":
            {"Precio":input("Introduzca el precio del contenido\n"),
             "Calidad":input("Introduzca la calidad del contenido\n"),
             "Material":input("Introduzca el material del que esta hecho\n"),
             "Cantidad":input("Introduzca la cantidad de veces que viene este contenido en el pack\n"),
             "Stock":input("Introduzca el stock del contenido\n"),
             "Demanda":input("Introduzca la demanda del contenido\n")}}
             }})
    else:
        print("Ha introducido mal la clase, Por favor intentelo de nuevo")
    
    try:
        #Aqui suma el precio de todos los contenidos para calcualar el precio del pack
        suma_precio_pack = 0
        valores_contenido = contenido.values()
            
        for s in valores_contenido:
            for x in s:
                caracteristicas = s[x]
                suma_precio_pack += int(caracteristicas["caracteristicas"]["Precio"])
        precio_pack = {"precio":str(suma_precio_pack)}
    except:
            print("Ha introducido mal el precio de los contenidos\n\
                Por favor intentelo de nuevo")
    else:
        #Aqui se añaden todos los campos a la variable documento
        documento = {}
        documento.update(nombre_pack)
        documento.update(calidad_pack)
        documento.update(precio_pack)
        documento.update(stock_pack)
        documento.update(dimensiones_pack)
        documento.update(contenido)
        return documento
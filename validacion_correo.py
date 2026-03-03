validacion_correo = input("ingrese correo: ").lower()
if validacion_correo.count("@") == 1:
    despues = validacion_correo.split("@")[1]
    if "." in despues:
        print("el correo {} es valido".format(validacion_correo))
    elif "." not in despues:
        print("no se encontro en {} el . del vinculo".format(despues))
    else:
        print("error")    
else:
    print("error")

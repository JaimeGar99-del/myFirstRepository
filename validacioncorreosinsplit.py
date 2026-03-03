validacion_correo = input("ingrese correo: ").lower()

if validacion_correo.count("@") == 1:
    posicion = validacion_correo.find("@")
    despues = validacion_correo[posicion + 1:]
    if "." in despues:
        print("el correo {} es valido".format(validacion_correo))
        print("dominio", despues)
        print("usuario", validacion_correo[:posicion])
    else:
        print("correo no valido, falta el punto")
else:
    print("error")
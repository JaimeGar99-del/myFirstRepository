
validacion_password = input("ingrese contraseña: ")
if len(validacion_password) < 8:
    print("Minimo 8 caracteres")
    exit()
mayuscula = False
numero = False
time_especial = False
especial = "@$_&!*-+.,"
for caracteres in validacion_password:
    if caracteres.isupper():
        mayuscula = True
    if caracteres.isnumeric():
        numero = True
    if caracteres in especial:
        time_especial = True

if not mayuscula:
    print("Debe tener almenos una mayuscula")
if not numero:
    print("Debe tener almenos un numero")
if not especial:
    print("Debe tener almenos un caracter especial @,$,_")
else:
    print("contraseña valida")
    




"""if not any(c.isupper() )for c in validacion_password:
    print("no tiene mayuscula")
if not any(c.isdigit() and c.isupper() and c in "@$_" and len(validacion_password) > 8 for c in validacion_password):
    print("contraseña no valida falta debe contener mayuscula, numero, algun caracter especial @,$,_ y minimo 8 caracteres")
if not any(c in "@$_" for c in validacion_password):
    print("agrega algun caracter especial : @,$,,_")  
if not len(validacion_password) >= 8:
    print("minimo 8 caracteres")
else:
    print("valida")"""

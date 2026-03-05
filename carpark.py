
car_in_parking = 5
total_entradas = 0
total_salidas = 0


door_parking = ""

print("Bienvenido a nuestro parqueadero")

while door_parking != '3':
    print(f"\nCarros en el parqueadero: {car_in_parking}")
    print(f"Entradas: {total_entradas} | Salidas: {total_salidas}")
    print("1. Confirmar ingreso")
    print("2. Confirmar salida")
    print("3. Salir")

    door_parking = int(input("Confirmar accion: ")).strip()
    
    if door_parking == "1":
        if car_in_parking < 10:
            car_in_parking += 1
            total_entradas += 1
            print(f"Bienvenido! Carros actuales: {car_in_parking}")
        elif car_in_parking == 10:
            print("Tenemos el maximo de capacidad en este momento, porfavor vuelva pronto: ")

    elif door_parking == "2":
        if car_in_parking > 0:
            car_in_parking -= 1
            total_salidas += 1
            print(f"Vuelva pronto! Carros actuales: {car_in_parking}")
        else:
            print("No hay carros en el parqueadero")

    elif door_parking == "3":
        print(f"\nResumen de la sesion:")
        print(f"  Entradas totales : {total_entradas}")
        print(f"  Salidas totales  : {total_salidas}")
        print(f"  Carros finales   : {car_in_parking}")
        print("Cerrando sistema...")
        break

    else:
        print("Opcion no valida, intente de nuevo")



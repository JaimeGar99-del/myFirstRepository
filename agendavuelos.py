vuelos = {
    "AV101": ("Bogota", 5, 300),
    "AV202": ("Medellin", 3, 200),
    "AV303": ("Cartagena", 4, 250),
    "AV404": ("Cali", 2, 220)
}

reservas = []
opcion = 'si'
print('Bienvenido')

while opcion == 'si':
    print('\nVuelos disponibles:')
    for codigo, datos in vuelos.items():
        print(f'{codigo} - {datos[0]} - Asientos: {datos[1]} - Precio: {datos[2]}')

    nombre_pasajero = input('\ningrese el nombre del pasajero\n').strip().capitalize()
    codigo_vuelo = input('ingrese el codigo del vuelo\n').strip().upper()

    if vuelos.get(codigo_vuelo):
        cantidad_asientos = int(input('ingrese la cantidad de asientos\n'))
        destino, asientos, precio = vuelos[codigo_vuelo]

        if cantidad_asientos <= asientos:
            reservas.append((nombre_pasajero, codigo_vuelo, cantidad_asientos))
            vuelos[codigo_vuelo] = (destino, asientos - cantidad_asientos, precio)
            print("Reserva realizada con exito!")
        else:
            print(f'no hay asientos suficientes, disponibles: {asientos}')
    else:
        print('el vuelo no esta registrado')

    opcion = input('\ndesea hacer otra reserva? si/no\n').strip().lower()
if opcion == 'no':
    print("Gracias por preferir nuestra aerolinea")
else:
    print("error, respuesta no valida")

print(reservas)

dinero_total = 0
print('\n\n')
for item in reservas:
    print('-'*50)
    nombre_cliente = item[0]
    codigo_vuelos = item[1]
    cantidad_asientos = item[2]
    precio_vuelos_tupla = vuelos[codigo_vuelos]
    precio_vuelo = precio_vuelos_tupla[2]
    subtotal = cantidad_asientos * precio_vuelo
    dinero_total += subtotal
    print(f'{nombre_cliente}    {codigo_vuelo}    {cantidad_asientos} asientos    precio: {precio_vuelo}    subtotal: {subtotal}')
    print('-'*50)

print(f'El total recaudado es: {dinero_total}')
conteo = {}
for item in reservas:
    codigo_vuelos = item[1]
    if codigo_vuelos in conteo:
        conteo[codigo_vuelos] += 1
    else:
        conteo[codigo_vuelos] = 1

if conteo:
    vuelo_top = max(conteo, key=conteo.get)
    print(f'El vuelo con mas reservas es: {vuelo_top} con {conteo[vuelo_top]} reservas')
else:
    print('No se realizaron reservas')

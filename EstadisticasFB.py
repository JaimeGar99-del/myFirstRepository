"""
Estadisticas de YUYU
Cantidad de partidos del yuyu
resultado del partido:
    goles en el partido:
        goles en contra
        goles a favor

puntos
PJ
PG
PE
PP
GF(goles a favor)
GC(goles en contra)
DG(diferencia de goles)
"""
# primero pedimos el numero de partidos que va a jugar el yuyu

# por cada partido pedimos goles a favor los goles en contra
# dependiendo del resultado el yuyu gana o el yuyu pierde
# contar los partidos ganados
# contar los partidos empatados
# contar partidos perdidos
# calcular puntos partido ganado = 3 puntos partido perdido = 0, partido empatado =1
# goles totales a favor
# goles totales en contra
# diferencia de goles
partidos_jugados = int(input("Numero de partidos a jugar: "))
goles_a_favor = 0
goles_en_contra = 0
goles_diferencia = 0
partido_ganado = 0
partido_perdido = 0
partido_empatado = 0
puntos = 0
total_goles_afavor = 0
total_goles_encontra = 0
total_diferencia = 0

for i in range(1,partidos_jugados+1):
    print(f"partido # {i} del YUYU")
    goles_a_favor = int(input("ingresar los goles que marco el yuyu: "))
    goles_en_contra = int(input("ingresar los goles que le metieron al yuyu: "))
    goles_diferencia = goles_a_favor - goles_en_contra
    print(f"la diferencia de goles en el partido fue de {goles_diferencia}")
    total_goles_afavor += goles_a_favor
    total_goles_encontra += goles_en_contra
    total_diferencia = total_goles_afavor - total_goles_encontra
    if goles_diferencia ==0:
        print("el yuyu empata")
        partido_empatado += 1
    elif goles_diferencia >0:
        print("gano el yuyu")
        partido_ganado += 1
    else:
        print("perdio el yuyu")
        partido_perdido += 1
print("\n")
print("="*40)
print(f"Estadisticas del yuyu")
print("="*40)
print("\n")
print(f"el yuyu gano {partido_ganado}, perdio {partido_perdido} y empato {partido_empatado}")
puntos =(partido_ganado*3) +(partido_empatado*1)+(partido_perdido*0)
print(f"puntos acumulados: {puntos}")
print(f"goles a favor acumulado: {total_goles_afavor}")
print(f"goles en contra acumulado: {total_goles_encontra }")
print(f"la diferencia de goles es de : {total_diferencia}")
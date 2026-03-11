heroes = [
    # Dragon Ball
    {"nombre": "Goku",             "universo": "DragonBall",     "poder": "Ki",              "nivel": 99},
    {"nombre": "Vegeta",           "universo": "DragonBall",     "poder": "Ki",              "nivel": 98},
    {"nombre": "Gohan",            "universo": "DragonBall",     "poder": "Ki",              "nivel": 96},
    {"nombre": "Piccolo",          "universo": "DragonBall",     "poder": "Energia",         "nivel": 94},
    {"nombre": "Trunks",           "universo": "DragonBall",     "poder": "Espada",          "nivel": 93},
    # Naruto
    {"nombre": "Naruto Uzumaki",   "universo": "Naruto",         "poder": "Chakra",          "nivel": 98},
    {"nombre": "Sasuke Uchiha",    "universo": "Naruto",         "poder": "Sharingan",       "nivel": 97},
    {"nombre": "Sakura Haruno",    "universo": "Naruto",         "poder": "Fuerza",          "nivel": 90},
    {"nombre": "Kakashi Hatake",   "universo": "Naruto",         "poder": "Sharingan",       "nivel": 92},
    {"nombre": "Itachi Uchiha",    "universo": "Naruto",         "poder": "Genjutsu",        "nivel": 95},
    # Boku no Hero
    {"nombre": "Izuku Midoriya",   "universo": "MyHeroAcademia", "poder": "One For All",     "nivel": 96},
    {"nombre": "Katsuki Bakugo",   "universo": "MyHeroAcademia", "poder": "Explosion",       "nivel": 94},
    {"nombre": "Shoto Todoroki",   "universo": "MyHeroAcademia", "poder": "Hielo/Fuego",     "nivel": 93},
    {"nombre": "All Might",        "universo": "MyHeroAcademia", "poder": "Super Fuerza",    "nivel": 99},
    {"nombre": "Endeavor",         "universo": "MyHeroAcademia", "poder": "Fuego",           "nivel": 95},
    # One Punch Man
    {"nombre": "Saitama",          "universo": "OnePunchMan",    "poder": "Fuerza",          "nivel": 100},
    {"nombre": "Genos",            "universo": "OnePunchMan",    "poder": "Tecnologia",      "nivel": 93},
    {"nombre": "Tatsumaki",        "universo": "OnePunchMan",    "poder": "Telequinesis",    "nivel": 97},
    {"nombre": "Bang",             "universo": "OnePunchMan",    "poder": "Artes Marciales", "nivel": 92},
    # Jujutsu Kaisen
    {"nombre": "Yuji Itadori",     "universo": "JujutsuKaisen",  "poder": "Energia Maldita", "nivel": 94},
    {"nombre": "Satoru Gojo",      "universo": "JujutsuKaisen",  "poder": "Infinito",        "nivel": 99},
    {"nombre": "Megumi Fushiguro", "universo": "JujutsuKaisen",  "poder": "Sombras",         "nivel": 92},
    {"nombre": "Nobara Kugisaki",  "universo": "JujutsuKaisen",  "poder": "Hechiceria",      "nivel": 90},
    {"nombre": "Ryomen Sukuna",    "universo": "JujutsuKaisen",  "poder": "Maldicion",       "nivel": 100},
    # Marvel
    {"nombre": "Captain Marvel",   "universo": "Marvel",         "poder": "Energia",         "nivel": 97},
    {"nombre": "Scarlet Witch",    "universo": "Marvel",         "poder": "Magia",           "nivel": 96},
    {"nombre": "Wolverine",        "universo": "Marvel",         "poder": "Regeneracion",    "nivel": 92},
    {"nombre": "Captain America",  "universo": "Marvel",         "poder": "Liderazgo",       "nivel": 84},
    {"nombre": "Doctor Strange",   "universo": "Marvel",         "poder": "Magia",           "nivel": 94},
    {"nombre": "Black Panther",    "universo": "Marvel",         "poder": "Combate",         "nivel": 87},
    {"nombre": "Hulk",             "universo": "Marvel",         "poder": "Fuerza",          "nivel": 97},
    {"nombre": "Thor",             "universo": "Marvel",         "poder": "Electricidad",    "nivel": 95},
    {"nombre": "Spider-Man",       "universo": "Marvel",         "poder": "Agilidad",        "nivel": 85},
    {"nombre": "Iron Man",         "universo": "Marvel",         "poder": "Tecnologia",      "nivel": 90},
    {"nombre": "Deadpool",         "universo": "Marvel",         "poder": "Regeneracion",    "nivel": 91},
    {"nombre": "Storm",            "universo": "Marvel",         "poder": "Clima",           "nivel": 94},
    {"nombre": "Jean Grey",        "universo": "Marvel",         "poder": "Telepatia",       "nivel": 96},
    {"nombre": "Cyclops",          "universo": "Marvel",         "poder": "Rayos Opticos",   "nivel": 89},
    {"nombre": "Nightcrawler",     "universo": "Marvel",         "poder": "Teletransporte",  "nivel": 88},
    {"nombre": "Silver Surfer",    "universo": "Marvel",         "poder": "Energia Cosmica", "nivel": 98},
    {"nombre": "Vision",           "universo": "Marvel",         "poder": "Intangibilidad",  "nivel": 93},
    {"nombre": "Ant-Man",          "universo": "Marvel",         "poder": "Cambio de Tamaño","nivel": 87},
    {"nombre": "Wasp",             "universo": "Marvel",         "poder": "Vuelo",           "nivel": 86},
    {"nombre": "Star-Lord",        "universo": "Marvel",         "poder": "Estrategia",      "nivel": 85},
    # DC
    {"nombre": "Green Lantern",    "universo": "DC",             "poder": "Constructs",      "nivel": 89},
    {"nombre": "Cyborg",           "universo": "DC",             "poder": "Tecnologia",      "nivel": 83},
    {"nombre": "Shazam",           "universo": "DC",             "poder": "Magia",           "nivel": 90},
    {"nombre": "Martian Manhunter","universo": "DC",             "poder": "Telepatia",       "nivel": 95},
    {"nombre": "Green Arrow",      "universo": "DC",             "poder": "Precision",       "nivel": 80},
    {"nombre": "Batman",           "universo": "DC",             "poder": "Inteligencia",    "nivel": 88},
    {"nombre": "Superman",         "universo": "DC",             "poder": "Fuerza",          "nivel": 98},
    {"nombre": "Wonder Woman",     "universo": "DC",             "poder": "Combate",         "nivel": 93},
    {"nombre": "Flash",            "universo": "DC",             "poder": "Velocidad",       "nivel": 91},
    {"nombre": "Aquaman",          "universo": "DC",             "poder": "Hidrocinesis",    "nivel": 86},
    {"nombre": "Nightwing",        "universo": "DC",             "poder": "Acrobacia",       "nivel": 88},
    {"nombre": "Robin",            "universo": "DC",             "poder": "Combate",         "nivel": 84},
    {"nombre": "Batgirl",          "universo": "DC",             "poder": "Tecnologia",      "nivel": 85},
    {"nombre": "Raven",            "universo": "DC",             "poder": "Magia",           "nivel": 94},
    {"nombre": "Starfire",         "universo": "DC",             "poder": "Energia",         "nivel": 92},
    {"nombre": "Beast Boy",        "universo": "DC",             "poder": "Transformacion",  "nivel": 89},
    {"nombre": "Supergirl",        "universo": "DC",             "poder": "Fuerza",          "nivel": 96},
    {"nombre": "Zatanna",          "universo": "DC",             "poder": "Magia",           "nivel": 93},
    {"nombre": "Blue Beetle",      "universo": "DC",             "poder": "Armadura",        "nivel": 87},
    {"nombre": "Hawkman",          "universo": "DC",             "poder": "Vuelo",           "nivel": 88},
]

equipo = []
opcion = 'si'
print("=== HEROES DISPONIBLES ===\n")
for i, h in enumerate(heroes, start=1):
    numero   = str(i).rjust(2)
    nombre   = h['nombre'].ljust(17)
    universo = h['universo'].ljust(14)
    poder    = h['poder'].ljust(16)
    nivel    = str(h['nivel'])
    print(f"{numero}. Heroe: {nombre} | Universo: {universo} | Poder: {poder} | Nivel: {nivel}")
while opcion == 'si':
    numero = int(input("\nElige el número del héroe (1-64): "))
    if numero < 1 or numero > len(heroes):
        print(" Número inválido, elige entre 1 y 64.")
        continue
    heroe_elegido = heroes[numero - 1]
    if heroe_elegido in equipo:
        print(f"{heroe_elegido['nombre']} ya está en tu equipo, elige otro.")
        continue
    equipo.append(heroe_elegido)
    print(f"{heroe_elegido['nombre']} agregado al equipo.")

    opcion = input("¿Agregar otro héroe? (si/no): ").lower()

    if opcion == 'no':
        print("\nEquipo confirmado.")
    elif opcion != 'si':
        print("Opción inválida, escribe 'si' o 'no'.")
        opcion = 'si'
print("\n=== TU EQUIPO ===\n")
for i, h in enumerate(equipo, start=1):
    numero   = str(i).rjust(2)
    nombre   = h['nombre'].ljust(18)
    universo = h['universo'].ljust(6)
    poder    = h['poder'].ljust(14)
    nivel    = str(h['nivel'])
    print(f"{numero}. Heroe: {nombre} | Universo: {universo} | Poder: {poder} | Nivel: {nivel}")

nivel_de_poder_equipo = sum(h['nivel'] for h in equipo)
marvel = sum(1 for h in equipo if h['universo'] == 'Marvel')
dc     = sum(1 for h in equipo if h['universo'] == 'DC')
db = sum(1 for h in equipo if h['universo'] == 'DragonBall')
naruto     = sum(1 for h in equipo if h['universo'] == 'Naruto')
mha = sum(1 for h in equipo if h['universo'] == 'MyHeroAcademia')
opm     = sum(1 for h in equipo if h['universo'] == 'OnePunchMan')
JujutsuKaisen     = sum(1 for h in equipo if h['universo'] == 'JujutsuKaisen')


print("\n=== RESUMEN EQUIPO DE HEROES ===\n")
print(f"Total de nivel del equipo : {nivel_de_poder_equipo}")
print(f"Heroes de Marvel          : {marvel}")
print(f"Heroes de DC              : {dc}")
print(f"Heroes de Dragon Ball     : {db}")
print(f"Heroes de Naruto          : {naruto}")
print(f"Heroes de Boku no hero    : {mha}")
print(f"Heroes de one punch man   : {opm}")
print(f"Heroes de jujutsu kaisen  : {JujutsuKaisen}")
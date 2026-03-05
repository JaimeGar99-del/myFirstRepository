numero_de_estudiantes = int(input("Ingresar el número de estudiantes: "))
estudiantes = []
notas = []
aprobados = 0
reprobados = 0

if numero_de_estudiantes > 0:
    for i in range(numero_de_estudiantes):
        nombre = input(f"Ingresar nombre del estudiante {i+1}: ")
        nota1 = -1  
        nota2 = -1
        nota3 = -1
        while not (0 <= nota1 <= 5):
            nota1 = float(input(f"  Ingresar nota 1 de {nombre}: "))
            if not (0 <= nota1 <= 5):
                print("  Nota inválida, debe estar entre 0 y 5")

        while not (0 <= nota2 <= 5):
            nota2 = float(input(f"  Ingresar nota 2 de {nombre}: "))
            if not (0 <= nota2 <= 5):
                print("  Nota inválida, debe estar entre 0 y 5")

        while not (0 <= nota3 <= 5):
            nota3 = float(input(f"  Ingresar nota 3 de {nombre}: "))
            if not (0 <= nota3 <= 5):
                print("  Nota inválida, debe estar entre 0 y 5")

        promedio = (nota1 + nota2 + nota3) / 3
        estudiantes.append(nombre)
        notas.append(promedio)

    print("\n--- Resultados ---")
    for i in range(len(estudiantes)):
        estado = "Aprobado" if notas[i] >= 3 else "Reprobado"
        print(f"{estudiantes[i]} → Promedio: {notas[i]:.1f} | {estado}")
        if estado == "Aprobado":
            aprobados +=1
        else:
            reprobados +=1

    promedio_general = sum(notas) / len(notas)
    print(f"\n El promedio general es: {promedio_general:.1f}")
    print(f"Aprobados: {aprobados}, Reprobados: {reprobados}")

else:
    print("El numero de estudiantes debe ser mayor a 0")
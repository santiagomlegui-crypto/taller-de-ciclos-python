vuelta = 0
acumulado = 0
nAprobados = 0
nReprobados = 0
cantidadAlumnos = int(input("Digite el numero de estudiantes a evaluar: "))
while vuelta < cantidadAlumnos:
    puntos = float(input("Digite la nota del estudiante: "))
    if puntos < 0 or puntos > 5.0:
        print("Nota no valida")
    else:
        if puntos >= 3.0:
            print("Aprobado")
            nAprobados = nAprobados + 1
        else:
            print("Reprobado")
            nReprobados = nReprobados + 1
    vuelta = vuelta + 1
    acumulado = acumulado + puntos
resultadoMedio = acumulado / cantidadAlumnos
print("El numero de estudiantes evaluados fueron:", cantidadAlumnos)
print("Aprobados:", nAprobados)
print("Reprobados:", nReprobados)
print("Promedio:", resultadoMedio)

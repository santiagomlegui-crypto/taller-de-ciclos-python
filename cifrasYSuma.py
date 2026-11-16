valorEntrada = int(input("digite un numero: "))

if valorEntrada > 0:
    temporal = valorEntrada
    ultimo = 0
    sumaPot = 0
    longitud = 0
    while temporal > 0:
        ultimo = temporal % 10
        temporal = temporal // 10
        sumaPot = sumaPot + ultimo
        longitud = longitud + 1
    print("La cantidad de cifras de:", valorEntrada, "son", longitud)
    print("La sumatoria es:", sumaPot)
else:
    print("El numero no es positivo")

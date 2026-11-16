entero = int(input("Ingrese un número: "))
if entero < 0:
    print("el número no posee factorial.")
else:
    producto = 1
    multiplicador = 1
    while True:
        if entero > 0:
            producto = producto * multiplicador
            multiplicador = multiplicador + 1
        if multiplicador > entero:
            break
    print("El factorial de", entero, "es:", producto)

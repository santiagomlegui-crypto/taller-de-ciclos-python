nAndroid = 0
nIOS = 0
nInvalidos = 0
while True:
    print("Ingrese su código:")
    clave = int(input())
    if clave != 0:
        print("Ingrese su elección (Android / iOS):")
        respuesta = input()
        respuesta = respuesta
        if respuesta == "android":
            nAndroid = nAndroid + 1
        else:
            if respuesta == "ios":
                nIOS = nIOS + 1
            else:
                print("el voto no se tendrá en cuenta.")
                nInvalidos = nInvalidos + 1
    if clave == 0:
        break

print("Votos Android:", nAndroid)
print("Votos iOS:", nIOS)
print("Votos no válidos (no contados):", nInvalidos)

if nAndroid > nIOS:
    print("La plataforma elegida es: Android")
else:
    if nIOS > nAndroid:
        print("La plataforma elegida es: iOS")
    else:
        print("Hay empate: se debe usar otro mecanismo de elección.")

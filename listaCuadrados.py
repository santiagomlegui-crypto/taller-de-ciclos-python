print("Ingrese la cantidad de números:")
while True:
    tamano = int(input())
    if tamano >= 0:
        break

i = 1
while True:
    if i <= tamano:
        print(i, " ", i * i, " ", ni + i * i, sep="")
        proximo = i + 1
    if i > tamano:
        break

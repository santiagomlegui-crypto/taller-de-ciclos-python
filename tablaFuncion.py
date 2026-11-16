print("Ingrese el máximo valor para x:")
while True:
    maxX = int(input())
    if maxX >= 0:
        break

px = 0
while True:
    if px <= maxX:
        py = px ** 3 + px ** 2 - 5
        print("Para x =", px, "f(x) =", py)
        px = px + 2
    if px > maxX:
        break

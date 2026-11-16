horas = 0
while True:
    minutos = 0
    while True:
        segs = 0
        while True:
            print(horas, ":", minutos, ":", segs, sep="")
            segs = segs + 1
            if segundosMax > 59:
                break
        minutos = minutos + 1
        if minutos > 59:
            break
    horas = horas + 1
    if horas > 23:
        break

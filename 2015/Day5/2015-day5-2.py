file = open("input.txt", "r")
linie = file.read().splitlines()

nice = 0

for linia in linie:
    slowa = []
    podwojne = False
    palindrom = False

    for i in range(len(linia) - 1):
        slowo = linia[i:i+2]
        slowa.append(slowo)

    for i in range(len(slowa)-2):
        ilosc = slowa.count(slowa[i])
        if ilosc == 2:
            if slowa[i] == slowa[i+1] and slowa[i] != slowa[i+2]:
                podwojne = False
                break
            else:
                podwojne = True
                break
        elif ilosc > 2:
            podwojne = True
            break

    for i in range(len(linia)-2):
        if linia[i] == linia[i+2]:
            palindrom = True
            break

    if podwojne and palindrom:
        nice += 1

print(nice)

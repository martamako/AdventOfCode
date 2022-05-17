file = open("input.txt", "r")
linie = file.read().splitlines()

for i in range(0, len(linie)):
    linie[i] = linie[i].split('x')
    for j in range(3):
        linie[i][j] = int(linie[i][j])

powierzchnia = 0

for linia in linie:
    objetosc = linia[0] * int(linia[1]) * int(linia[2])

    if linia[0] < linia[2] and linia[1] < linia[2]:
        powierzchnia += linia[0] + linia[0] + linia[1] + linia[1]
    elif linia[0] < linia[1] and linia[2] < linia[1]:
        powierzchnia += linia[0] + linia[0] + linia[2] + linia[2]
    elif linia[1] < linia[0] and linia[2] < linia[0]:
        powierzchnia += linia[1] + linia[1] + linia[2] + linia[2]

    powierzchnia += objetosc

print(powierzchnia)

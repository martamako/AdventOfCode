file = open("input.txt", "r")
linie = file.read().splitlines()

pole_swiatel = []

for i in range(1000):
    wiersz = [False] * 1000
    pole_swiatel.append(wiersz)

for i in range(len(linie)):
    linie[i] = linie[i].replace(',', ' ')
    linie[i] = linie[i].split(' ')

x1 = 0
y1 = 0
x2 = 0
y2 = 0

for linia in linie:
    if linia[0] == "turn":
        x1 = int(linia[2])
        y1 = int(linia[3])
        x2 = int(linia[5])
        y2 = int(linia[6])

        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                if linia[1] == "on":
                    pole_swiatel[i][j] = True
                elif linia[1] == "off":
                    pole_swiatel[i][j] = False

    elif linia[0] == "toggle":
        x1 = int(linia[1])
        y1 = int(linia[2])
        x2 = int(linia[4])
        y2 = int(linia[5])
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                pole_swiatel[i][j] = not pole_swiatel[i][j]

zapalone_swiatla = 0
for i in range(1000):
    for j in range(1000):
        zapalone_swiatla += pole_swiatel[i][j]

print(zapalone_swiatla)
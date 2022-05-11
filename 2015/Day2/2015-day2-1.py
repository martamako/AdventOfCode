file = open("input.txt", "r")
linie = file.read().splitlines()

for i in range(len(linie)):
    linie[i] = linie[i].split('x')
    for j in range(3):
        linie[i][j] = int(linie[i][j])

powierzchnia = 0
for linia in linie:
    powierzchnia += 2 * linia[0] * linia[1] + 2 * linia[1] * linia[2] + 2 * linia[0] * linia[2]
    powierzchnia += min(linia[0]*linia[1], linia[1]*linia[2], linia[0]*linia[2])

print(powierzchnia)

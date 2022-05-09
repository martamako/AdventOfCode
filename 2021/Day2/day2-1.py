file = open("input.txt", "r")
linie = file.read().splitlines()

for i in range(0, len(linie)):
    linie[i] = linie[i].split(' ')
    linie[i][1] = int(linie[i][1])

depth = 0
horizontal = 0

for linia in linie:
    if linia[0] == 'forward':
        horizontal += linia[1]
    elif linia[0] == 'up':
        depth -= linia[1]
    elif linia[0] == 'down':
        depth += linia[1]


print(horizontal * depth)
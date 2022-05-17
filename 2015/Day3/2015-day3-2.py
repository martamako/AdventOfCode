file = open("input.txt", "r")
linie = file.read()

x = 0
y = 0
robo_x = 0
robo_y = 0

koordynaty = {(0, 0)}
indeks = 0
for char in linie:
    if char == '>':
        if indeks % 2 == 0:
            x += 1
        else:
            robo_x += 1
    elif char == 'v':
        if indeks % 2 == 0:
            y += 1
        else:
            robo_y += 1
    elif char == '<':
        if indeks % 2 == 0:
            x -= 1
        else:
            robo_x -= 1
    elif char == '^':
        if indeks % 2 == 0:
            y -= 1
        else:
            robo_y -= 1

    if indeks % 2 == 0:
        para = (x, y)
    else:
        para = (robo_x, robo_y)

    koordynaty.add(para)
    indeks += 1


print(len(koordynaty))

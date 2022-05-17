file = open("input.txt", "r")
linie = file.read()

x = 0
y = 0

koordynaty = {(0, 0)}

for char in linie:
    if char == '>':
        x += 1
    elif char == 'v':
        y += 1
    elif char == '<':
        x -= 1
    elif char == '^':
        y -= 1
    para = (x, y)

    koordynaty.add(para)

print(len(koordynaty))
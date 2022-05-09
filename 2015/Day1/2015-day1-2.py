file = open("input.txt", "r")

pietro = 0
indeks = 1

for znak in file.read():
    if znak == '(':
        pietro += 1
    elif znak == ')':
        pietro -= 1

    if pietro == -1:
        break

    indeks += 1

print(indeks)
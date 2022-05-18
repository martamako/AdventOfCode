import Gate

file = open("input.txt", "r")
linie = file.read().splitlines()

gates = []

for i in range(len(linie)):
    linie[i] = linie[i].split(' ')
    print(linie[i])
file = open("input.txt", "r")
linie = file.read().splitlines()

for i in range(0, len(linie)):
    linie[i] = int(linie[i])

pierwszy = linie[0]
ilosc = 0
for i in range(1, len(linie)):
    drugi = linie[i]
    if drugi > pierwszy:
        ilosc += 1
    pierwszy = drugi

print(ilosc)
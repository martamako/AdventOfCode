file = open("input.txt", "r")
linie = file.read().splitlines()

for i in range(0, len(linie)):
    linie[i] = int(linie[i])

ilosc = 0
for i in range(0, len(linie)-3):
    pierwszy = linie[i] + linie[i+1] + linie[i+2]
    drugi = linie[i+1] + linie[i+2] + linie[i+3]
    if drugi > pierwszy:
        ilosc += 1
    pierwszy = drugi

print(ilosc)
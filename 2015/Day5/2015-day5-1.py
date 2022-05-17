file = open("input.txt", "r")
linie = file.read().splitlines()

bad_letters = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']
podwojne_znaki = []

for i in range(26):
    litery = chr(ord('a') + i) + chr(ord('a') + i)
    podwojne_znaki.append(litery)


nice = 0

for linia in linie:
    przerwij = False
    podwojne = False
    ilosc_samoglosek = 0
    for znak in bad_letters:
        if znak in linia:
            przerwij = True
            break

    if not przerwij:
        for znak in podwojne_znaki:
            if znak in linia:
                podwojne = True
                break

        if podwojne:
            for litera in linia:
                for samogloska in vowels:
                    if litera == samogloska:
                        ilosc_samoglosek += 1

    if ilosc_samoglosek >= 3:
        nice += 1

print(nice)
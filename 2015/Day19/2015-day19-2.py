text = ""

with open('input.txt') as file:
    data = file.read().splitlines()

    text = data.pop()
    data.pop()

    for i in range(len(data)):
        data[i] = data[i].split(" => ")


med = text
count = 0
while med != 'e':
    for src, repl in data:
        if repl in med:
            med = med.replace(repl, src, 1)
            count += 1

print(count)
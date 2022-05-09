file = open("input.txt", "r")

pietro = 0

for znak in file.read():
    if znak == '(':
        pietro += 1
    elif znak == ')':
        pietro -= 1

print(pietro)
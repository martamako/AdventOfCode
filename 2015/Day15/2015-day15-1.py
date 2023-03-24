file = open("input.txt", "r")

lines = file.read().splitlines()

ingredients = []

for i in range(len(lines)):
    new_list = []
    elements = lines[i].split()
    new_list.append(int(elements[2].strip(",")))
    new_list.append(int(elements[4].strip(",")))
    new_list.append(int(elements[6].strip(",")))
    new_list.append(int(elements[8].strip(",")))
    new_list.append(int(elements[10]))
    lines[i] = new_list

t = lines

score = 0
maximum = 0

for i in range(100):
    for j in range(100-i):
        for k in range(100-j):
            l = 100-i-j-k
            capacity = t[0][0] * i + t[1][0] * j + t[2][0] * k + t[3][0] * l
            durability = t[0][1] * i + t[1][1] * j + t[2][1] * k + t[3][1] * l
            flavor = t[0][2] * i + t[1][2] * j + t[2][2] * k + t[3][2] * l
            texture = t[0][3] * i + t[1][3] * j + t[2][3] * k + t[3][3] * l
            calories = t[0][4] * i + t[1][4] * j + t[2][4] * k + t[3][4] * l

            if not calories == 500:
                continue

            if capacity <= 0 or durability <= 0 or flavor <= 0 or texture <= 0:
                score = 0
                continue

            score = capacity * durability * flavor * texture
            if score > maximum:
                maximum = score

print(maximum)
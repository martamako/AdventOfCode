file = open("input.txt", "r")

lines = file.read().splitlines()

ingridients = dict()

for l in lines:
    elements = l.split(":")
    elements[1] = elements[1].strip(" ")
    elements[1] = elements[1].split(", ")
    for i in range(len(elements[1])):
        elements[1][i] = elements[1][i].split(" ")
        elements[1][i] = {elements[1][i][0]: int(elements[1][i][1])}
    ingridients[elements[0]] = elements[1]


for key in ingridients.keys():
    lst = ingridients[key]
    new_dict = {}
    for l in lst:
        for k in l.keys():
            new_dict[k] = l[k]
    ingridients[key] = new_dict

for key in ingridients.keys():
    print(ingridients[key])
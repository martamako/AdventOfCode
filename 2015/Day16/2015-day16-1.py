file = open("input.txt", "r")

lines = file.read().splitlines()

tape = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

for l in lines:
    l = l.replace(":", "")
    l = l.replace(",", "")
    l = l.split()
    if tape[l[2]] == int(l[3]) and tape[l[4]] == int(l[5]) and tape[l[6]] == int(l[7]):
        print(l[1])

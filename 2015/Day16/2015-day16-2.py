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
indexes = [2, 4, 6]

for l in lines:
    l = l.replace(":", "")
    l = l.replace(",", "")
    l = l.split()
    agree = 0
    for i in indexes:
        if l[i] == 'cats' or l[i] == 'trees':
            if tape[l[i]] < int(l[i+1]):
                agree += 1
        elif l[i] == 'pomeranians' or l[i] == 'goldfish':
            if tape[l[i]] > int(l[i+1]):
                agree += 1
        else:
            if tape[l[i]] == int(l[i+1]):
                agree += 1
    if agree == 3:
        print(l[1])


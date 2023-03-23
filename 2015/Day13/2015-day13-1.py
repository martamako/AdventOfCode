file = open("input.txt", "r")
lines = file.read().splitlines()

people = set()

for i in range(len(lines)):
    lines[i] = lines[i].split()
    people.add(lines[i][0])


people = list(people)
people.sort()
print(people)



matrix = [[0] * len(people) for i in range(len(people))]

for line in lines:
    i = people.index(line[0])
    j = people.index(line[-1][:-1])
    distance = 0
    if line[2] == 'gain':
        distance = int(line[3])
    elif line[2] == 'lose':
        distance = -1 * int(line[3])

    matrix[i][j] = distance


perm = [*range(len(people))]


# Python function to print permutations of a given list
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


maxim = 0
lista_sum = []
for p in permutation(perm):
    suma = 0
    for i in range(len(p)):
        if i == 0:
            suma += matrix[p[i]][p[-1]]
            suma += matrix[p[i]][p[i + 1]]
        elif i == len(p) - 1:
            suma += matrix[p[i]][p[0]]
            suma += matrix[p[i]][p[i - 1]]
        else:
            suma += matrix[p[i]][p[i + 1]]
            suma += matrix[p[i]][p[i - 1]]
    if suma > maxim:
        maxim = suma

print(maxim)

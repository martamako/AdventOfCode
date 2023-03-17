file = open("input.txt", "r")
lines = file.read().splitlines()

distances = list()
cities = set()


def get_cities_permutation(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = []

    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]

        for p in get_cities_permutation(remLst):
            l.append([m] + p)
    return l


for line in lines:
    line = line.split(" ")
    distances += [(line[0], line[2], line[4])]
    distances += [(line[2], line[0], line[4])]
    cities.add(line[0])
    cities.add(line[2])

cities_list = list(cities)
permutations = get_cities_permutation(cities_list)

longest_distance = 0
for per in permutations:
    distance = 0
    for i in range(len(per)-1):
        for dist in distances:
            if per[i] == dist[0] and per[i+1] == dist[1]:
                distance += int(dist[2])
    if distance >= longest_distance:
        longest_distance = distance

print(longest_distance)



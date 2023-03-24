def calculate_distance(reindeer: dict, second: int) -> str:
    rest = second % (reindeer["flying time"] + reindeer["resting time"])
    if rest < reindeer["flying time"]:
        reindeer["distance"] += reindeer["speed"]


f = open("input.txt", "r")

lines = f.read().splitlines()

data = []

for i in range(len(lines)):
    lines[i] = lines[i].split()
    data.append({"name": lines[i][0], "speed": int(lines[i][3]), "flying time": int(lines[i][6]),
                 "resting time": int(lines[i][-2]), "distance": 0, "points": 0})

time = 2503

for i in range(time):
    maximum = 0
    indeks = 0
    for j in range(len(data)):
        calculate_distance(data[j], i)
        if data[j]["distance"] > maximum:
            maximum = data[j]["distance"]
            indeks = j
    data[indeks]["points"] += 1

maximum = 0
for i in range(len(data)):
    if data[i]["points"] > maximum:
        maximum = data[i]["points"]

print(maximum)

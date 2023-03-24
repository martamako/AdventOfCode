def calculate_distance(reindeer: dict, time: int) -> (str, int):
    current_time = 0
    distance = 0
    while current_time <= time:
        for i in range(reindeer["flying time"]):
            distance += reindeer["speed"]
            current_time += 1
            if current_time > time:
                return reindeer["name"], distance
        current_time += reindeer["resting time"]
        if current_time > time:
            return reindeer["name"], distance


f = open("input.txt", "r")

lines = f.read().splitlines()

data = []

for i in range(len(lines)):
    lines[i] = lines[i].split()
    data.append({"name": lines[i][0], "speed": int(lines[i][3]), "flying time": int(lines[i][6]),
                 "resting time": int(lines[i][-2])})

reindeer_list = []
time = 2503
for i in range(len(data)):
    reindeer_list.append(calculate_distance(data[i], time))

maximum = reindeer_list[0][1]
for i in range(1, len(reindeer_list)):
    if reindeer_list[i][1] > maximum:
        maximum = reindeer_list[i][1]

print(maximum)

def part1():
    with open("input-2024-day1.txt", "r") as input:
        lines = input.readlines()
        list1 = []
        list2 = []
        for line in lines:
            locations = line.split("   ")
            list1.append(int(locations[0]))
            list2.append(int(locations[1]))

        list1.sort()
        list2.sort()
        total_distance = 0
        for i in range(len(list1)):
            total_distance += abs(list1[i] - list2[i])
        print(total_distance)


def part2():
    with open("input-2024-day1.txt", "r") as input:
        lines = input.readlines()
        list1 = []
        list2 = []
        for line in lines:
            locations = line.split("   ")
            list1.append(int(locations[0]))
            list2.append(int(locations[1]))

        familiarity = 0
        for num in list1:
            familiarity += list2.count(num) * num
        print(familiarity)

part2()
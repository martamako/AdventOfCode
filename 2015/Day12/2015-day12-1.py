import json


def get_numbers(data, number):
    if isinstance(data, int):
        return data
    elif isinstance(data, str):
        return 0
    elif isinstance(data, list):
        sum = 0
        for el in data:
            sum += get_numbers(el, number)
        return sum
    elif isinstance(data, dict):
        # Added for part 2
        for key in data:
            if data[key] == "red":
                return 0
        # End for part 2
        sum = 0
        for key in data:
            sum += get_numbers(data[key], number)
        return sum


f = open("input.txt", "r")

data = json.load(f)

number = 0
for el in data:
    number += get_numbers(el, number)

# Closing file
f.close()

print(number)

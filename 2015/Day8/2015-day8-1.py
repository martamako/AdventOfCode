file = open("input.txt", "r")
lines = file.read().splitlines()


def count_characters(text: str) -> int:
    number = 0
    i = 0
    while i < len(text):
        if text[i] == "\\":
            if text[i + 1] == "\"" or text[i + 1] == "\\":
                i = i + 1
                number += 1
            elif text[i + 1] == "x":
                i += 3
                number += 1
        elif text[i] == "\"":
            pass
        else:
            number += 1
        i += 1
    return number


suma = 0
for line in lines:
    suma += len(line) - count_characters(line)

print(suma)

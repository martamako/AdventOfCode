file = open("input.txt", "r")
lines = file.read().splitlines()


def new_text(text: str) -> str:
    newText = "\""
    for i in range(len(text)):
        if text[i] == "\\":
            newText += "\\\\"
        elif text[i] == "\"":
            newText += "\\\""
        else:
            newText += text[i]
    newText += "\""
    return newText


suma = 0
for line in lines:
    suma += len(new_text(line)) - len(line)

print(suma)

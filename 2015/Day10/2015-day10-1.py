

def look_and_day(text: str) -> str:
    new_string = ""
    digit = text[0]
    numberOfCopies = 0

    for i in range(len(text)):
        if digit != text[i]:
            new_string += str(numberOfCopies) + digit
            numberOfCopies = 1
            digit = text[i]
        else:
            numberOfCopies += 1

    new_string += str(numberOfCopies) + digit

    return new_string


text = "1113222113"
for i in range(40):
    text = look_and_day(text)

print(len(text))
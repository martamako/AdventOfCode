def rule1(text: str) -> bool:
    number = 0
    for i in range(len(text) - 1):
        if ord(text[i + 1]) - ord(text[i]) == 1:
            number += 1
            if number >= 2:
                return True
        else:
            number = 0

    return number > 2


def rule2(text: str) -> bool:
    for c in text:
        if c == 'i' or c == 'l' or c == 'o':
            return False
    return True


def rule3(text: str) -> bool:
    first_pair = ""
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            if first_pair == "":
                first_pair += text[i] + text[i + 1]
            elif first_pair != "":
                second_pair = text[i] + text[i+1]
                if first_pair != second_pair:
                    return True
    return False


def next_combination(text: str, index: int) -> str:
    first_part = text[:index]
    letter = text[index]
    second_part = text[index+1:]

    if letter == 'z':
        letter = 'a'
    else:
        letter = chr(ord(letter) + 1)
    return first_part + letter + second_part


def find_new_password(text: str) -> str:
    turns = [0] * len(text)
    index = len(text) - 1
    turns[index] += 1
    text = next_combination(text, index)

    depth_cur = len(text) - 1
    depth_all = len(text) - 1

    while not (rule1(text) and rule2(text) and rule3(text)):
        text = next_combination(text, index)

        turns[index] += 1

        if turns[index] == 25:
            turns[index] = 0
            index -= 1
        elif index < len(text) - 1:
            index += 1

        if index < depth_cur:
            depth_cur = index

        if depth_cur < depth_all:
            depth_all = depth_cur

    return text


old_password = "hxbxwxba"

new_password = find_new_password(old_password)

print(find_new_password(new_password))

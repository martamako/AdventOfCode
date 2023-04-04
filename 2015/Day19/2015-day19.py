def main():
    file = open("input.txt", "r")
    data = file.read().splitlines()

    molecules = set()

    text = data.pop()
    data.pop()

    for i in range(len(data)):
        data[i] = data[i].split(" => ")

    for before, after in data:
        loc = -1
        i = 0
        indexes = []
        while True:
            i += 1
            loc = text.find(before, loc + 1)
            if loc != -1:
                indexes.append(loc)
            else:
                break

        for current in indexes:
            molecules.add(text[0:current] + after + text[current+len(before):])

    print(len(molecules))


if __name__ == '__main__':
    main()

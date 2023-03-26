def subsets(numbers):
    if not numbers:
        return [[]]
    x = subsets(numbers[1:])
    return x + [[numbers[0]] + y for y in x]


# wrapper function
def subsets_of_given_size(numbers, n):
    return [x for x in subsets(numbers) if len(x) == n]


if __name__ == '__main__':
    file = open("input.txt", "r")

    data = file.read().splitlines()

    integer_map = map(int, data)

    data = list(integer_map)
    n = len(data)

    for i in range(n):
        subset = subsets_of_given_size(data, i)
        suma = 0
        for s in subset:
            if sum(s) == 150:
                suma += 1
        if suma > 0:
            print(suma)
            break

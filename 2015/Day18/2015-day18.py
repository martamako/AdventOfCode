# # on
# . off

def million_lights(grid: list) -> list:
    new_grid = [["."] * len(grid[0]) for i in range(len(grid[0]))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbours = 0
            if 0 < i < len(grid) - 1 and 0 < j < len(grid) - 1:
                if grid[i-1][j-1] == "#":
                    neighbours += 1
                if grid[i-1][j] == "#":
                    neighbours += 1
                if grid[i-1][j+1] == "#":
                    neighbours += 1
                if grid[i][j-1] == "#":
                    neighbours += 1
                if grid[i][j+1] == "#":
                    neighbours += 1
                if grid[i+1][j-1] == "#":
                    neighbours += 1
                if grid[i+1][j] == "#":
                    neighbours += 1
                if grid[i+1][j+1] == "#":
                    neighbours += 1
            if i == 0 and j == 0:
                if grid[i][j+1] == "#":
                    neighbours += 1
                if grid[i+1][j] == "#":
                    neighbours += 1
                if grid[i+1][j+1] == "#":
                    neighbours += 1

            if i == 0 and 0 < j < len(grid[i]) - 1:
                if grid[i][j-1] == "#":
                    neighbours += 1
                if grid[i][j+1] == "#":
                    neighbours += 1
                if grid[i+1][j-1] == "#":
                    neighbours += 1
                if grid[i+1][j] == "#":
                    neighbours += 1
                if grid[i+1][j+1] == "#":
                    neighbours += 1

            if i == 0 and j == len(grid[i]) - 1:
                if grid[i][j-1] == "#":
                    neighbours += 1
                if grid[i+1][j-1] == "#":
                    neighbours += 1
                if grid[i+1][j] == "#":
                    neighbours += 1

            if 0 < i < len(grid) - 1 and j == 0:
                if grid[i-1][j] == "#":
                    neighbours += 1
                if grid[i-1][j+1] == "#":
                    neighbours += 1
                if grid[i][j+1] == "#":
                    neighbours += 1
                if grid[i+1][j] == "#":
                    neighbours += 1
                if grid[i+1][j+1] == "#":
                    neighbours += 1

            if 0 < i < len(grid) - 1 and j == len(grid[i])-1:
                if grid[i-1][j-1] == "#":
                    neighbours += 1
                if grid[i-1][j] == "#":
                    neighbours += 1
                if grid[i][j-1] == "#":
                    neighbours += 1
                if grid[i+1][j-1] == "#":
                    neighbours += 1
                if grid[i+1][j] == "#":
                    neighbours += 1

            if i == len(grid) - 1 and j == 0:
                if grid[i-1][j] == "#":
                    neighbours += 1
                if grid[i-1][j+1] == "#":
                    neighbours += 1
                if grid[i][j+1] == "#":
                    neighbours += 1

            if i == len(grid) - 1 and 0 < j < len(grid) - 1:
                if grid[i-1][j-1] == "#":
                    neighbours += 1
                if grid[i-1][j] == "#":
                    neighbours += 1
                if grid[i-1][j+1] == "#":
                    neighbours += 1
                if grid[i][j-1] == "#":
                    neighbours += 1
                if grid[i][j+1] == "#":
                    neighbours += 1

            if i == len(grid) - 1 and j == len(grid) - 1:
                if grid[i-1][j-1] == "#":
                    neighbours += 1
                if grid[i-1][j] == "#":
                    neighbours += 1
                if grid[i][j-1] == "#":
                    neighbours += 1

            if grid[i][j] == "#" and 2 <= neighbours <= 3:
                new_grid[i][j] = "#"
            if grid[i][j] == "." and neighbours == 3:
                new_grid[i][j] = "#"
    return new_grid


def count_lights(grid: list) -> int:
    lights_turned_on = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                lights_turned_on += 1

    return lights_turned_on


def print_grid(grid: list):
    for i in range(len(grid)):
        print(grid[i])


if __name__ == '__main__':
    file = open("input.txt", "r")

    data = file.read().splitlines()

    for i in range(len(data)):
        data[i] = [j for j in data[i]]

    grid = data

    for i in range(100):
        grid[0][0] = "#"
        grid[0][len(grid) - 1] = "#"
        grid[len(grid) - 1][0] = "#"
        grid[len(grid) - 1][len(grid) - 1] = "#"
        grid = million_lights(grid)

    print(count_lights(grid))

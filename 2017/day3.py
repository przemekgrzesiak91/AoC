# Day 3 (2017)
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 3     #Edit this
year = 2017 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.readlines()
    return int(input[0])

def solve_part1(input):
    """Solve part 1."""
    def check_neighbours(spiral, current_pos):
        directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        sum = 0
        for direction in directions:
            neighbour = (current_pos[0] + direction[0], current_pos[1] + direction[1])
            if neighbour in spiral:
                sum += spiral[neighbour]
        return sum

    k = 1
    while k ** 2 < input:
        k += 2

    if k == 1:
        return 0

    start = k // 2
    cords = [start, -start]

    #
    if input >= k ** 2 - (k - 1):
        cords = [start - (k ** 2 - input), -start]
    elif input >= k ** 2 - 2 * (k - 1):
        cords = [-start, -start + (k ** 2 - k - 1 - input)]
    elif input >= k ** 2 - 3 * (k - 1):
        cords = [-start + (k ** 2 - 2 * (k - 1) - input), start]
    elif input > k ** 2 - 4 * (k - 1):
        cords = [start, start - (k ** 2 - 3 * (k - 1) - input)]

    return (abs(cords[0]) + abs(cords[1]))


def solve_part2(input):
    """Solve part 2."""
    def check_neighbours(spiral, current_pos):
        directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        sum = 0
        for direction in directions:
            neighbour = (current_pos[0] + direction[0], current_pos[1] + direction[1])
            if neighbour in spiral:
                sum += spiral[neighbour]
        return sum

    spiral = {(0, 0): 1}

    r = 1
    current_pos = (0, 0)
    while True:
        current_pos = (current_pos[0] + 1, current_pos[1])
        spiral[current_pos] = check_neighbours(spiral, current_pos)
        # while current_pos!=r or current_pos!=-r:
        while current_pos[1] < r:
            current_pos = (current_pos[0], current_pos[1] + 1)
            value = check_neighbours(spiral, current_pos)
            if value > input:
                return value
            else:
                spiral[current_pos] = value

        while current_pos[0] > -r:
            current_pos = (current_pos[0] - 1, current_pos[1])
            value = check_neighbours(spiral, current_pos)
            if value > input:
                return value
            else:
                spiral[current_pos] = value

        while current_pos[1] > -r:
            current_pos = (current_pos[0], current_pos[1] - 1)
            value = check_neighbours(spiral, current_pos)
            if value > input:
                return value
            else:
                spiral[current_pos] = value
        while current_pos[0] < r:
            current_pos = (current_pos[0] + 1, current_pos[1])
            value = check_neighbours(spiral, current_pos)
            if value > input:
                return value
            else:
                spiral[current_pos] = value
        r += 1


def result(day,year):
    input = parse()
    rp1 = solve_part1(input)
    rp2 = solve_part2(input)


    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + str(year)+ Fore.YELLOW + ' *')
    print('Result for ' + Fore.CYAN + 'Day ' + str(day))
    print(Fore.CYAN + str(rp1))
    print(Fore.CYAN + str(rp2))


if __name__ == "__main__":
    result(day,year)

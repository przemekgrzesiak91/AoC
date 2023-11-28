# Day 5 (2017)
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 5     #Edit this
year = 2017 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.readlines()
        input = [int(line.strip()) for line in input]
    return input

def solve_part1(input):
    """Solve part 1."""
    maze1 = input.copy()
    current_pos = 0
    steps = 0

    while current_pos < len(maze1):
        next_pos = maze1[current_pos]
        maze1[current_pos] += 1
        current_pos += next_pos
        steps += 1

    return steps


def solve_part2(input):
    """Solve part 2."""
    maze2 = input.copy()
    current_pos = 0
    steps = 0

    while current_pos < len(maze2):
        next_pos = maze2[current_pos]
        if maze2[current_pos] >= 3:
            maze2[current_pos] -= 1
        else:
            maze2[current_pos] += 1
        current_pos += next_pos
        steps += 1

    return steps


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

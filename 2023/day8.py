# Day 8 (2023)
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 8     #Edit this
year = 2023 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.readlines()

    return input

def solve_part1(input):
    """Solve part 1."""
    nav = input[0]
    nodes = {}
    len_nav = len(nav)

    for row in input[2:]:
        key, value = row.strip().split(' = ')
        nodes[key] = value[1:-1].split(', ')

    current = 'AAA'
    i=0
    steps = 0
    while current != 'ZZZ':
        if nav[i] == 'L': current = nodes[current][0]
        elif nav[i] == 'R': current = nodes[current][1]

        steps += 1
        i += 1

        if i >= len_nav-1: i = 0


    return steps

def solve_part2(input):
    """Solve part 2."""
    return 0

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

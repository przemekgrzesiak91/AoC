# Day 8 (2023)
from colorama import Fore, init
import math

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
    nav = input[0]
    nodes = {}
    len_nav = len(nav)
    current = []
    n_steps_Z = [0,0,0,0,0,0]
    steps = 0
    i= 0
    for row in input[2:]:
        key, value = row.strip().split(' = ')
        nodes[key] = value[1:-1].split(', ')

    for key in nodes.keys():
        if key[2] == 'A': current.append(key)

    last_letters = ''.join([x[2] for x in current])

    while 0 in n_steps_Z:
        for j in range(0, len(current)):
            if nav[i] == 'L':
                current[j] = nodes[current[j]][0]
            elif nav[i] == 'R':
                current[j] = nodes[current[j]][1]

            if current[j][2] == 'Z' and n_steps_Z[j] == 0:
                n_steps_Z[j] = steps+1
        steps += 1
        i += 1

        if i >= len_nav - 1: i = 0

    return math.lcm(*n_steps_Z)


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

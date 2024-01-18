# Day 15 (2023)
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 15     #Edit this
year = 2023 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.read().strip().split(',')
    return input

def solve_part1(input):
    """Solve part 1."""
    rp1 = 0

    for i in input:
        start = 0
        for char in i:
            start = ((start + ord(char)) * 17) % 256
        rp1 += start
    return rp1

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

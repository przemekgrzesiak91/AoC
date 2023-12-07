# Day 5 (2023)
from colorama import Fore, init
import numpy as np

# Initialize colorama
init(autoreset=True)

day = 5    #Edit this
year = 2023 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    
    with open(filepath, 'r') as f:
        input = f.readlines()



    return input

def solve_part1(input):
    """Solve part 1."""
    print(input)
    return 0

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

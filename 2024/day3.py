from IPython.utils.text import marquee
from colorama import Fore, init
import re

from sympy.strategies.branch import condition

# Initialize colorama
init(autoreset=True)

day = 3     #Edit this
year = 2024 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.readlines()
    return input

def solve_part1(input):
    """Solve part 1."""
    result = 0
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, str(input))

    for match in matches:
        #print(match)
        x,y = [int(i) for i in re.findall(r'\d+', match)]
        result += x*y

    return result

def solve_part2(input):
    """Solve part 2."""
    result = 0

    #poprawic pattern
    print(input)
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, str(input))
    print(matches)
    condition = True
    for match in matches:
        if match == 'don\'t()': condition = False
        elif match == 'do()': condition = True
        elif condition:
        # print(match)
            x, y = [int(i) for i in re.findall(r'\d+', match)]
            result += x * y

    return result

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

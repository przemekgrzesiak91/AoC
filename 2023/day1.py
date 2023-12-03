# Day 1 (2017)
from colorama import Fore, init
import re

# Initialize colorama
init(autoreset=True)

day = 1     #Edit this
year = 2017 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.readlines()
    return input

def solve_part1(input):
    """Solve part 1."""
    part1 = 0
    for row in input:
        digits = re.findall('\d',row)
        value = int(digits[0] + digits[-1])
        part1 += value

    return part1

def solve_part2(input):
    """Solve part 2."""
    part2 = 0
    pattern = r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))'
    str_to_num = {'one':'1',
                 'two':'2',
                 'three':'3',
                 'four':'4',
                 'five':'5',
                 'six':'6',
                 'seven':'7',
                 'eight':'8',
                 'nine':'9'}

    for row in input:
        digits = re.findall(pattern,row )

        if digits[0] in str_to_num.keys():
            digits[0] = str_to_num[digits[0]]
        if digits[-1] in str_to_num.keys():
            digits[-1] = str_to_num[digits[-1]]

        value = int(digits[0] + digits[-1])
        part2 += value

    return part2

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

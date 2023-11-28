# Day 1 (2017)
from colorama import Fore, init

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
    digits = list(str(input))
    rp1 = 0

    for i in range(0, len(digits)):
        if i == len(digits) - 1:
            if digits[i] == digits[0]: rp1 += int(digits[i])
        else:
            if digits[i] == digits[i + 1]: rp1 += int(digits[i])

    return rp1

def solve_part2(input):
    """Solve part 2."""
    digits = list(str(input))
    rp2 = 0
    dist = int(len(digits) / 2)

    for i in range(0, len(digits)):
        if i + dist > len(digits) - 1:
            break
        else:
            if digits[i] == digits[i + dist]: rp2 += 2 * (int(digits[i]))
    return rp2

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

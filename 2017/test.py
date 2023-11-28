# Day 7 (2017)
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 7     #Edit this
year = 2017 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.readlines()

    map = {}

    for row in input:
        row = row.strip().replace(',', '').split(' ')
        if len(row) == 2:
            value = int(row[1].replace('(', '').replace(')', ''))
            map[row[0]] = [value]
        else:
            map[row[0]] = [value, row[3:]]
    return map

def solve_part1(input):
    """Solve part 1."""
    for key in input.keys():
        seen = 0
        for value in input.values():
            if len(value) > 1:
                if key in value[1]:
                    seen = 1
        if seen == 0:
            return key


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

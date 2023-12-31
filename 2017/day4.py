# Day 4 (2017)
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 4     #Edit this
year = 2017 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.readlines()
    return input

def solve_part1(input):
    """Solve part 1."""
    n_valid = 0
    for row in input:
        row = row.strip().split(' ')
        if len(row) == len(set(row)): n_valid += 1
    return n_valid


def solve_part2(input):
    """Solve part 2."""
    n_valid = 0
    for row in input:
        row = row.strip().split(' ')

        new_row = [''.join(sorted(list(word))) for word in row]
        if len(new_row) == len(set(new_row)): n_valid += 1
    return n_valid


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

# Day 2 (2017)
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 2     #Edit this
year = 2017 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.readlines()

    return input

def solve_part1(input):
    """Solve part 1."""
    rp1 = 0
    for row in input:
        row = row.replace('\t', ' ').strip().split(' ')
        row = [int(i) for i in row]

        # Part1
        row = sorted(row, reverse=True)
        max, min = row[0], row[-1]
        rp1 += max - min

    return rp1

def solve_part2(input):
    """Solve part 2."""
    rp2=0
    for row in input:
        row = row.replace('\t', ' ').strip().split(' ')
        row = [int(i) for i in row]

        row = sorted(row, reverse=True)

        # Part2
        for i in row:
            for j in row:
                if i != j and i % j == 0:
                    rp2 += i // j

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

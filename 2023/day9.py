# Day 9 (2023)
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 9     #Edit this
year = 2023 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.readlines()
    return input

def solve_part1(input):
    """Solve part 1."""
    rp1 = 0

    for row in input:
        map = []

        row = [int(x) for x in row.strip().split(' ')]
        map.append(row)

        while not all(element == 0 for element in map[-1]):
        #while sum(map[-1]) != 0:
            #print(map[-1])
            new_row = []
            for i in range(0,len(map[-1])-1):
                new_row.append(map[-1][i+1]-map[-1][i])
            map.append(new_row)
        #print(map)
        for x in map:
            rp1 += x[-1]

    return rp1

def solve_part2(input):
    """Solve part 2."""
    rp2 = 0

    for row in input:
        map = []
        row = [int(x) for x in row.strip().split(' ')]
        row = row[::-1]
        map.append(row)

        while not all(element == 0 for element in map[-1]):
            # while sum(map[-1]) != 0:
            # print(map[-1])
            new_row = []
            for i in range(0, len(map[-1]) - 1):
                new_row.append(map[-1][i + 1] - map[-1][i])
            map.append(new_row)
        # print(map)
        for x in map:
            rp2 += x[-1]

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


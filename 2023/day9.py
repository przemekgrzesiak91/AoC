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
        new_value = 0
        row = [int(x) for x in row.strip().split(' ')]
        map.append(row)

        while sum(map[-1]) != 0:
            #print(map[-1])
            new_row = []
            for i in range(0,len(map[-1])-1):
                new_row.append(map[-1][i+1]-map[-1][i])
            map.append(new_row)

        for x in map:
            new_value += x[-1]
        print(new_value)

        rp1+=new_value
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
    print(1743490457)


if __name__ == "__main__":
    result(day,year)



# row 107 (1) i row 168 (-2)
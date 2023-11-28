# Day 6 (2017)
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 6     #Edit this
year = 2017 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.readline().strip().split('\t')
        input = [int(x) for x in input]

    return input

def solve_part1(banks, part = 1):
    """Solve part 1."""

    def find_max(banks):
        max_value = max(banks)
        id = banks.index(max_value)

        return id

    seen = []
    current = banks.copy()
    cycle = 0
    n = len(banks)

    while current not in seen:

        seen.append(current.copy())
        id = find_max(current)
        value = current[id]
        # print('--',id)
        j = id
        current[id] = 0

        for i in range(value):
            if j + 1 < n:
                j += 1
            else:
                j = 0

            current[j] += 1
        cycle += 1

    if part == 1:   return cycle
    if part == 2:
        cycle = -1

        repeated = current.copy()
        seen = []

        while seen.count(repeated) < 2:

            seen.append(current.copy())
            id = find_max(current)
            value = current[id]
            # print('--',id)
            j = id
            current[id] = 0

            for i in range(value):
                if j + 1 < n:
                    j += 1
                else:
                    j = 0

                current[j] += 1
            cycle += 1
        return cycle


def solve_part2(input):
    """Solve part 2."""
    pass


def result(day,year):
    input = parse()
    rp1 = solve_part1(input)
    rp2 = solve_part1(input,2)


    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + str(year)+ Fore.YELLOW + ' *')
    print('Result for ' + Fore.CYAN + 'Day ' + str(day))
    print(Fore.CYAN + str(rp1))
    print(Fore.CYAN + str(rp2))


if __name__ == "__main__":
    result(day,year)

from colorama import Fore, init
from collections import Counter
# Initialize colorama
init(autoreset=True)

day = 1     #Edit this
year = 2024 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.readlines()

    return input


def solve_part1(input):
    """Solve part 1."""
    x = []
    y = []
    result = 0

    for row in input:
        row = row.strip().split()
        x.append(int(row[0]))
        y.append(int(row[1]))


    x.sort()
    y.sort()

    col3 = [abs(y[i]-x[i]) for i in range(len(x))]
    result = sum(col3)

    return result

def solve_part2(input):
    """Solve part 2."""
    x = []
    y = []
    result = 0

    for row in input:
        row = row.strip().split()
        x.append(int(row[0]))
        y.append(int(row[1]))

    x_count = Counter(x)
    y_count = Counter(y)

    for i in x_count:
        if i in y_count:
            result += i * x_count[i] * y_count[i]

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

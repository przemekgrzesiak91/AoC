from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 1     #Edit this
year = 2018 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = [line.strip() for line in f.readlines()]
    return input

def solve_part1(input):
    """Solve part 1."""
    result = 0

    for line in input:
        op = line[0]
        value = int(line[1:])

        if op == "+":
            result += value
        else:
            result -= value

    return result

def solve_part2(input):
    """Solve part 2."""
    result = 0
    freq = set([0])

    while True:
        for line in input:
            op = line[0]
            value = int(line[1:])

            if op == "+":
                result += value
            else:
                result -= value

            if result in freq:
                return result
            freq.add(result)

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

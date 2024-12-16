from colorama import Fore, init
from itertools import product


# Initialize colorama
init(autoreset=True)

day = 7     #Edit this
year = 2024 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = [list(map(int, x.replace(':', '').strip().split())) for x in f.readlines()]

    #print(input)
    return input

def generate_combinations(k,n):
    return list(product(list(range(k)), repeat=n))

def solve_part1(input):
    """Solve part 1."""
    sum = 0
    #print(list(range(2)))
    for row in input:
        result, values =row[0], row[1:]
        n = len(values) - 1

        combs = generate_combinations(2,n)

        for comb in combs:
            check = values[0]
            for i in range(0,n):
                if comb[i] == 0: check+=values[i+1]
                elif comb[i] == 1: check*=values[i+1]

            if result == check:
                sum += result
                break


    return sum

def solve_part2(input):
    """Solve part 2."""
    sum = 0
    # part 2 very slow

    for row in input:
        result, values = row[0], row[1:]
        n = len(values) - 1

        combs = generate_combinations(3, n)

        for comb in combs:
            check = values[0]
            for i in range(0, n):
                if comb[i] == 0:
                    check += values[i + 1]
                elif comb[i] == 1:
                    check *= values[i + 1]
                elif comb[i] == 2:
                    check = int(str(check)+str(values[i+1]))

            if result == check:
                sum += result
                break

    return sum

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

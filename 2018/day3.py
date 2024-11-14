from colorama import Fore, init
import numpy as np

# Initialize colorama
init(autoreset=True)

day = 3     #Edit this
year = 2018 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = [[int(x) for x in
                  line.strip().replace('#', '').replace(' @ ', ' ')
                  .replace(',', ' ').replace(':', '')
                  .replace('x',' ').split(' ')] for line in f.readlines()]

    print(input)
    return input

def solve_part1(input):
    """Solve part 1."""

    fabric = np.zeros((1000,1000))

    for claim in input:
        fabric[claim[2]:claim[2]+claim[4], claim[1]:claim[1]+claim[3]] += 1

    count = np.sum(fabric > 1)
    return count

def solve_part2(input):
    """Solve part 2."""

    fabric = np.zeros((1000, 1000))

    for claim in input:
        fabric[claim[2]:claim[2] + claim[4], claim[1]:claim[1] + claim[3]] += 1

    for claim in input:
        size = claim[3]*claim[4]

        if np.sum( fabric[claim[2]:claim[2] + claim[4], claim[1]:claim[1] + claim[3]]) == size:
            result = claim[0]

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

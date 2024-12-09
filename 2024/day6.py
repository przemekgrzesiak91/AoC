from adodbapi.ado_consts import directions
from colorama import Fore, init
import numpy as np

# Initialize colorama
init(autoreset=True)

day = 6     #Edit this
year = 2024 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = [list(line.strip()) for line in f]

    input = np.array(input)

    return input

def solve_part1(input):
    """Solve part 1."""
    result = 0
    n,m = np.shape(input)

    # finding start
    start = [int(cord) for cord in np.where(input == "^")]
    pos = start
    direction = ('^')

    while pos[0] in range(0,n-1) and pos[1] in range(0,m-1):
        #print(pos, direction, input[tuple(pos)])
        if direction == '^':
            pos[0]-=1
            if input[tuple(pos)] == '.':
                input[tuple(pos)] = 'X'
                result += 1
            elif input[tuple(pos)] == '#':
                pos[0] += 1
                direction = '>'

        elif direction == '>':
            pos[1]+=1
            if input[tuple(pos)] == '.':
                input[tuple(pos)] = 'X'
                result += 1
            elif input[tuple(pos)] == '#':
                pos[1] -= 1
                direction = 'v'

        elif direction == 'v':
            pos[0]+=1
            if input[tuple(pos)] == '.':
                input[tuple(pos)] = 'X'
                result += 1
            elif input[tuple(pos)] == '#':
                pos[0] -= 1
                direction = '<'

        elif direction == '<':
            pos[1]-=1
            if input[tuple(pos)] == '.':
                input[tuple(pos)] = 'X'
                result += 1
            elif input[tuple(pos)] == '#':
                pos[1] += 1
                direction = '^'

    return result
# test +1, my puzzle -1 ??? add animation



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

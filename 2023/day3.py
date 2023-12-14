# Day 3 (2023)
from colorama import Fore, init
import numpy as np

# Initialize colorama
init(autoreset=True)

day = 3     #Edit this
year = 2023 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.read()
    return input

def solve_part1(input):
    """Solve part 1."""
    #print(set(input)) #what with '\n'
    symbols = {'+', '=', '#', '*', '@', '&', '-', '%', '/', '$'}
    nums = [str(x) for x in range(0,10)]
    gears = []

    def check_adjacent(value_pos,value):
        adj_pos = []

        min_i = value_pos[0][0] - 1
        if min_i < 0: min_i = 0
        min_j = value_pos[0][1] - 1
        if min_j < 0: min_j = 0

        max_i = value_pos[0][0] + 2
        if max_i > ncol-1: max_i = ncol
        max_j = value_pos[-1][1] + 2
        if max_j > ncol-1: max_j = ncol

        #print(matrix[min_i:max_i,min_j:max_j])
        for i in range(min_i,max_i):
            for j in range(min_j,max_j):
                adj_pos.append((i,j))
        #print (adj_pos)

        for pos in adj_pos:
            value_adj_pos = matrix[pos]
            if value_adj_pos in symbols:
                if value_adj_pos =='*':
                    gears.append((pos,value))
                return True

        return False

    rp1 = 0
    nrow = input.count('\n')
    ncol = int((len(input) - nrow)/nrow)

    #print(ncol,nrow)
    matrix = np.matrix(list(''.join(input.replace('\n',''))))
    matrix = np.reshape(matrix,(nrow,ncol))


    for i in range(0,nrow):
        value_pos = []
        value = ''
        for j in range(0,ncol):
            if matrix[i,j] in nums:
                value_pos.append((i,j))
                value += matrix[i,j]

            else:
                if value_pos != []:
                    #print(value_pos, value)
                    if check_adjacent(value_pos, value): rp1 += int(value)
                    value_pos = []
                    value = ''
        if value_pos != []:
            if check_adjacent(value_pos, value): rp1 += int(value)
            value_pos = []
            value = ''

    # Part 2
    rp2 = 0

    while gears:
        current = gears.pop()

        for gear in gears:
            if current[0] == gear[0]:
                rp2 += (int(current[1])*int(gear[1]))



    return rp1, rp2

def solve_part2(input):
    """Solve part 2."""
    return 0

def result(day,year):
    input = parse()
    rp1, rp2 = solve_part1(input)


    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + str(year)+ Fore.YELLOW + ' *')
    print('Result for ' + Fore.CYAN + 'Day ' + str(day))
    print(Fore.CYAN + str(rp1))
    print(Fore.CYAN + str(rp2))


if __name__ == "__main__":
    result(day,year)

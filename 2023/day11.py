# Day 11 (2023)
from colorama import Fore, init
import numpy as np
from itertools import combinations

# Initialize colorama
init(autoreset=True)

day = 11     #Edit this
year = 2023 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.read()
    return input

def solve_part1(input):
    """Solve part 1."""
    rp1 = 0
    #print(input)
    nrow = input.count('\n') + 1
    ncol = input.find('\n')

    #print(ncol,nrow)
    matrix = np.matrix(list(''.join(input.replace('\n', ''))))
    matrix = np.reshape(matrix, (nrow, ncol))



    matrix2 = matrix.copy()

    def line_to_str(element):
        return str(element).replace('[','').replace(']','').replace("'","").replace(' ','').replace('\n','')

    #double 'empty' rows:
    # for row in matrix:
    #     if line_to_str(row) == '.'*ncol:
    n_double = 0
    for i in range(nrow):
        line = matrix[i,:]
        if line_to_str(line) == '.'*ncol:
            n_double += 1
            matrix2 = np.insert(matrix2, i+n_double, line, axis=0)

    matrix = matrix2.copy()
    n_double = 0
    nrow = matrix.shape[0]

    for i in range(ncol):
        line = matrix[:,i]
        if line_to_str(line) == '.' * nrow:
            n_double += 1
            matrix2 = np.insert(matrix2, i + n_double, np.array(['.']*nrow), axis=1)

    for row in matrix2:
        print(line_to_str(row))

    matrix = matrix2.copy()
    ncol = matrix.shape[1]
    points = []

    for i in range(nrow):
        for j in range(ncol):
            if matrix[i,j] == '#':
                points.append((i,j))

    n_points = len(points)

    combs_result = list(combinations(points, 2))
    n_combs = len(combs_result)
    print(n_points,n_combs)

    for comb in combs_result:
        rp1 += abs(comb[0][0]-comb[1][0]) + abs(comb[0][1]-comb[1][1])

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


if __name__ == "__main__":
    result(day,year)

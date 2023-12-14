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

def solve(input, x):
    """Solve part 1."""
    result = 0

    # print(input)
    nrow = input.count('\n') + 1
    ncol = input.find('\n')

    # print(ncol,nrow)
    matrix = np.matrix(list(''.join(input.replace('\n', ''))))
    matrix = np.reshape(matrix, (nrow, ncol))

    matrix2 = matrix.copy()

    def line_to_str(element):
        return str(element).replace('[', '').replace(']', '').replace("'", "").replace(' ', '').replace('\n', '')

    # double 'empty' rows:
    # for row in matrix:
    #     if line_to_str(row) == '.'*ncol:
    empty_rows, empty_cols = [],[]
    n_double = 0
    for i in range(nrow):
        line = matrix[i, :]
        if line_to_str(line) == '.' * ncol:
            empty_rows.append(i)

    for i in range(ncol):
        line = matrix[:, i]
        if line_to_str(line) == '.' * nrow:
            empty_cols.append(i)

    points = []

    for i in range(nrow):
        for j in range(ncol):
            if matrix[i, j] == '#':
                points.append((i, j))


    combs_result = list(combinations(points, 2))

    for comb in combs_result:
        row_value, col_value = 0,0
        row_range = range(min(comb[0][0], comb[1][0]), max(comb[0][0], comb[1][0] + 1))
        col_range = range(min(comb[0][1], comb[1][1]), max(comb[0][1], comb[1][1] + 1))

        for i in empty_rows:
            if i in row_range: row_value += x

        for i in empty_cols:
            if i in col_range: col_value += x

        result += abs(comb[0][0] - comb[1][0]) + row_value + abs(comb[0][1] - comb[1][1]) + col_value
    return result

def result(day,year):
    input = parse()
    rp1 = solve(input,1)
    rp2 = solve(input,999999)


    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + str(year)+ Fore.YELLOW + ' *')
    print('Result for ' + Fore.CYAN + 'Day ' + str(day))
    print(Fore.CYAN + str(rp1))
    print(Fore.CYAN + str(rp2))


if __name__ == "__main__":
    result(day,year)

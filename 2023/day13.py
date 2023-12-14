# Day 13 (2023)
from colorama import Fore, init
import numpy as np

# Initialize colorama
init(autoreset=True)

day = 13    #Edit this
year = 2023 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.read()
        input = input.split('\n\n')
    return input

def solve_part1(input):
    """Solve part 1."""
    rp1 = 0

    def check_rest_row(i,j,nrow):
        # compare previous and next row and so on until row =0  or row > nrows!
        while i>=0 and j<nrow:
            if np.any(matrix[i,] != matrix[j,]): return False
            i-=1
            j+=1
        return True

    def check_rest_col(i,j,ncol):
        i -= 1
        j += 1

        while i>=0 and j<ncol:
            if np.any(matrix[:,i] != matrix[:,j]): return False
            i -= 1
            j += 1

        return True


    for pattern in input:
        nrow = pattern.count('\n') + 1
        ncol = pattern.find('\n')

        matrix = np.matrix(list(''.join(pattern.replace('\n', ''))))
        matrix = np.reshape(matrix, (nrow, ncol))

        for i in range(nrow):
            j=i+1
            if j<nrow:
                if np.all(matrix[i,] == matrix[j,]):
                    if check_rest_row(i,j,nrow): rp1 += 100*(i+1)

        for i in range(ncol):
            j=i+1
            if j<ncol:
                if np.all(matrix[:,i] == matrix[:,j]):
                    if check_rest_col(i,j,ncol): rp1 += i+1



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

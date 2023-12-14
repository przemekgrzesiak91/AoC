# Day 10 (2023)
from colorama import Fore, init
import numpy as np

# Initialize colorama
init(autoreset=True)

day = 10     #Edit this
year = 2023 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.read()
    return input

def solve_part1(input):
    """Solve part 1."""
    rp1 = 0 # steps
    nrow = input.count('\n')+1
    ncol = input.find('\n')

    matrix = np.matrix(list(''.join(input.replace('\n', ''))))
    matrix = np.reshape(matrix, (nrow, ncol))

    matrix2 = matrix.copy()


    xS,yS = np.argwhere(matrix == 'S')[0]
    print(xS,yS)

    def show_neighbours(x,y):
        neighbours = [(0,1),(1,0),(0,-1),(-1,0)]
        neighbours = [(x+dx,y+dy) for dx, dy in neighbours]
        return neighbours

    neighbours = show_neighbours(xS,yS)
    if matrix[neighbours[0]] in ('-','J','7'): current = neighbours[0]
    elif matrix[neighbours[1]] in ('|','J','L'): current = neighbours[1]
    elif matrix[neighbours[2]] in ('-','L','F'): current = neighbours[2]
    elif matrix[neighbours[3]] in ('|','F','7'): current = neighbours[3]

    last = (xS,yS)
    current_symbol = matrix[current]

    rp1 += 1

    while current_symbol != 'S':
        #print(last, current, current_symbol)
        if current_symbol == 'J':
            if last[0]==current[0]:
                last = current
                current = (current[0]-1,current[1])
            else:
                last = current
                current = (current[0], current[1]-1)

        if current_symbol == 'F':
            if last[0]==current[0]:
                last = current
                current = (current[0]+1,current[1])
            else:
                last = current
                current = (current[0], current[1]+1)

        if current_symbol == '7':
            if last[0]==current[0]:
                last = current
                current = (current[0]+1,current[1])
            else:
                last = current
                current = (current[0], current[1]-1)

        if current_symbol == 'L':
            if last[0]==current[0]:
                last = current
                current = (current[0]-1,current[1])
            else:
                last = current
                current = (current[0], current[1]+1)

        if current_symbol == '-':
            if last[1]<current[1]: current = (current[0],current[1]+1)
            else: current = (current[0],current[1]-1)

        if current_symbol == '|':
            if last[0]<current[0]: current = (current[0]+1,current[1])
            else: current = (current[0]-1,current[1])

        rp1 += 1
        current_symbol = matrix[current]
        matrix2[current] = 'O'


    for row in matrix2:
        print(''.join(str(row).replace('\n','').replace("[", "").replace("]", "").replace("'", "").replace(" ", "")))
    return int(rp1/2)

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

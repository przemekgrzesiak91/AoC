from colorama import Fore, init
import numpy as np
from collections import Counter


# Initialize colorama
init(autoreset=True)

day = 8     #Edit this
year = 2024 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = [list(line.strip()) for line in f]

    input = np.array(input)
    return input

def solve_part1(input):
    """Solve part 1."""
    antinodes = np.copy(input)
    print(input.shape)
    max_x, max_y = input.shape

    unique_values = np.unique(input)

    for val in unique_values:
        if val != '.':
            points = list(np.argwhere(input==val))
            # Iteracja po parach punktów
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    # Pobieranie współrzędnych punktów

                    x1, y1 = points[i]
                    x2, y2 = points[j]

                    new_x1 = 2*x2-x1
                    new_y1 = 2*y2-y1

                    new_x2 = 2*x1-x2
                    new_y2 = 2*y1-y2


                    # Sprawdzanie, czy punkty mieszczą się w zakresie
                    if 0 <= new_x1 <= max_x-1 and 0 <= new_y1 <= max_y-1:
                        antinodes[new_x1,new_y1] = '#'
                    if 0 <= new_x2 <= max_x-1 and 0 <= new_y2 <= max_y-1:
                        antinodes[new_x2,new_y2] = '#'

    result = np.sum(antinodes == '#')
    return result

def solve_part2(input):
    """Solve part 2."""
    antinodes = np.copy(input)
    print(input.shape)
    max_x, max_y = input.shape

    unique_values = np.unique(input)

    for val in unique_values:
        if val != '.':
            points = list(np.argwhere(input == val))
            # Iteracja po parach punktów
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    # Pobieranie współrzędnych punktów

                    x1, y1 = points[i]
                    x2, y2 = points[j]

                    new_x1 = 2 * x2 - x1
                    new_y1 = 2 * y2 - y1
                    diff_x1 = new_x1-x2
                    diff_y1 = new_y1-y2

                    new_x2 = 2 * x1 - x2
                    new_y2 = 2 * y1 - y2

                    # Sprawdzanie, czy punkty mieszczą się w zakresie
                    while 0 <= new_x1 <= max_x - 1 and 0 <= new_y1 <= max_y - 1:
                        antinodes[new_x1, new_y1] = '#'
                        new_x1 += diff_x1
                        new_y1 += diff_y1
                    while 0 <= new_x2 <= max_x - 1 and 0 <= new_y2 <= max_y - 1:
                        antinodes[new_x2, new_y2] = '#'
                        new_x2 -= diff_x1
                        new_y2 -= diff_y1

    result = np.sum(antinodes == '.')
    result = (max_x*max_y) - result

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

from colorama import Fore, init
import numpy as np

# Initialize colorama
init(autoreset=True)

day = 10     #Edit this
year = 2024 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = [list(line.strip()) for line in f]

    input = np.array(input)
    return input

def solve_part1(input):
    """Solve part 1."""
    start_positions = list(np.argwhere(input == '0'))
    max_x, max_y = input.shape
    print("Pozycje startowe:", start_positions)

    for start in start_positions:
        current = np.array(start)  # Zamiana na tablicę NumPy
        height = 0

        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        # Bezpieczne kroki w kierunkach
        steps = [
            (height + 1, tuple(current + np.array(x)))
            for x in directions
            if 0 <= (current + np.array(x))[0] < max_x
            and 0 <= (current + np.array(x))[1] < max_y
            and input[tuple(current + np.array(x))] == str(height + 1)
        ]
        print(f"Pozycja startowa {start}: {steps}")

        while steps != []:
            for step in steps:
                height = step[0]
                current = np.array(step[1])  # Zamiana na tablicę NumPy

                steps = [
                    (height + 1, tuple(current + np.array(x)))
                    for x in directions
                    if 0 <= (current + np.array(x))[0] < max_x
                    and 0 <= (current + np.array(x))[1] < max_y
                    and input[tuple(current + np.array(x))] == str(height + 1)
                ]
                print(steps)

    return 0



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

# Day 2 (2023)
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 2     #Edit this
year = 2023  #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.readlines()
    return input

def solve_part1(input):
    """Solve part 1."""
    rp1 = 0
    max_green = 13
    max_blue = 14
    max_red = 12

    for row in input:
        row=row.strip().split(':')
        game_ID = int(row[0].split(' ')[-1])
        max_values = {'blue':0, 'red':0, 'green':0}

        sets = row[1].split(';')
        for set in sets:
            set = set.split(',')

            for cube in set:
                value, color = cube[1:].split(' ')
                value = int(value)
                if max_values[color] < value: max_values[color] = value
        if max_values['green'] <= max_green and max_values['red'] <= max_red and max_values['blue'] <= max_blue:
            rp1 += game_ID


    return rp1

def solve_part2(input):
    """Solve part 2."""
    #CHANGE TO USE SOME LINES FROM PART1

    rp2=0
    for row in input:
        row=row.strip().split(':')
        game_ID = int(row[0].split(' ')[-1])
        max_values = {'blue':0, 'red':0, 'green':0}

        sets = row[1].split(';')
        for set in sets:
            set = set.split(',')

            for cube in set:
                value, color = cube[1:].split(' ')
                value = int(value)
                if max_values[color] < value: max_values[color] = value

        rp2 += (max_values['green']*max_values['red']*max_values['blue'])
    return rp2

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

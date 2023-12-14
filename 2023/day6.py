# Day 6 (2023)

from colorama import Fore, init
import re
# Initialize colorama
init(autoreset=True)

day = 6     #Edit this
year = 2023 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.readlines()
    return input

def solve_part1(input):
    """Solve part 1."""
    rp1 = 1
    times = [int(x) for x in re.findall('\d+',input[0])]
    distances = [int(x) for x in re.findall('\d+',input[1])]


    for i in range(0,len(times)):
        n_wins = 0
        time = times[i]
        distance = distances[i]
        for j in range(1,time):
            if j*(time-j) > distance: n_wins+=1
        rp1 *= n_wins


    return rp1

def solve_part2(input):
    """Solve part 2."""
    rp2 = 0
    time = int(''.join([x for x in re.findall('\d', input[0])]))
    distance = int(''.join([x for x in re.findall('\d', input[1])]))

    for j in range(1, time):
        if j * (time - j) > distance: rp2 += 1

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

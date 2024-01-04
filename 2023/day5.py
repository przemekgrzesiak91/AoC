# Day 5 (2023)
'''
Seed > Soil > ... > location
seeds: 79 14 55 13

seed-to-soil map:
50 98 2 (50 - destination range, 98 - source range, 2 - range length)
52 50 48

'''
from colorama import Fore, init
import numpy as np

# Initialize colorama
init(autoreset=True)

day = 5    #Edit this
year = 2023 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    
    with open(filepath, 'r') as f:
        input = f.readlines()
        seeds  = [int(x) for x in input[0].strip().split(' ')[1:]]
        mapping = []
        current = []
        for row in input[2:]:

            if row[0].isdigit():
                dest,source,length = [int(x) for x in row.split(' ')]
                #print(dest,source,length)
                current.append([(source,source+length),(dest,dest+length)])
            elif row =='\n':
                #print(current)
                mapping.append(current)
                current = []
        mapping.append(current)
        current = []
        input = [seeds,mapping]
    return input

def solve_part1(input):
    """Solve part 1."""
    rp1 = 9999999999

    for start in input[0]:
        #print('----')
        #print(start)
        for step in input[1]:
            for change in step:
                source_range = change[0]
                destination_range = change[1]

                if start >= source_range[0] and start <= source_range[1]:
                    start = start - source_range[0] + destination_range[0]
                    break
        #print(start)
        if start < rp1: rp1 = start

    return rp1

def solve_part2(input):
    """Solve part 2."""
    rp2 = 9999999999
    seed_ranges = []
    for i in range(0, len(input[0]), 2):
        seed_ranges.append(range(input[0][i], input[0][i + 1]+input[0][i]))

    #print(seed_ranges)

    for pair in seed_ranges:
        print('----')
        for start in list(pair):

            #print(start)
            for step in input[1]:
                for change in step:
                    source_range = change[0]
                    destination_range = change[1]

                    if start >= source_range[0] and start <= source_range[1]:
                        start = start - source_range[0] + destination_range[0]
                        break
            #print(start)
            if start < rp2: rp2 = start
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

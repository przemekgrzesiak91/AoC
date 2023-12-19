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
        print(mapping)
        input = [seeds,mapping]
    return input

def solve_part1(input):
    """Solve part 1."""
    print(len(input[1]))
    rp1 = 0
    for start in input[0]:
        print('----')
        print(start)
        for step in input[1]:
            for change in step:
                source_range = range(*change[1])
                destination_range = list(range(*change[0]))

                # print(source_range, destination_range)
                if start in destination_range:
                    if start == 38:
                        print(source_range,destination_range)
                        print(destination_range.index(38))
                    id = destination_range.index(start)
                    start = source_range[id]
                    print(start,'>',id,sep=" ")
        print(start)

        '''example 2 - light should be 42 check this'''


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

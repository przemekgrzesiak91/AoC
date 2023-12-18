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
        print(seeds)
        mapping = [[(98,100),(50,52)],[(50,98),(52,100)]]


        for start in seeds:
            print(start)

            for step in mapping:
                print(step)
                for new_range in step:
                    print(new_range)
                    if start in x[0]:
                        print(start, x.index([start]))

                        #loop over and take value from 2nd range


            for x in soil:
                if seed in x: print(seed)




    return input

def solve_part1(input):
    """Solve part 1."""
    print(input)
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

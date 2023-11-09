# Day 1 (2017)
from aocd import get_data
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def result(day,year,rp1, rp2):
    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + str(year)+ Fore.YELLOW + ' *')
    print('Result for ' + Fore.CYAN + 'Day ' + str(day))
    print(Fore.CYAN + str(rp1))
    print(Fore.CYAN + str(rp2))

day = 2    #Edit this
year = 2017 #Edit this

input = get_data(day = day,year = year)
#print(input)

# Result for part 1 & 2
rp1, rp2 = 0, 0

### Code here

result(day,year,rp1,rp2)

print(input)

import itertools as iter

with open('data/day2.txt') as f:
    input = f.readlines()

part1_result = 0
for row in input:
    row = row.replace('\t',' ').strip().split(' ')
    row = [int(i) for i in row]

    min, max = row[0],row[0]
    for i in row[1:]:
        if min>i: min = i
        elif max<i: max = i
    part1_result += max-min

print(part1_result)


#part 2
part2_result = 0
for row in input:
    row = row.replace('\t',' ').strip().split(' ')
    row = [int(i) for i in row]

    x = iter.combinations(row,2)
    print(x)

    #for i in row[1:]:



    part2_result += max-min

print(part1_result)



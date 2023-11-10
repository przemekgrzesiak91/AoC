# Day 2 (2017)
from aocd import get_data
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def result(day,year,rp1, rp2):
    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + str(year)+ Fore.YELLOW + ' *')
    print('Result for ' + Fore.CYAN + 'Day ' + str(day))
    print(Fore.CYAN + str(rp1))
    print(Fore.CYAN + str(rp2))

day = 2     #Edit this
year = 2017 #Edit this

filepath = 'data/day' + str(day) + '.txt'
with open(filepath, 'r') as f:
    input = f.readlines()

# Result for part 1 & 2
rp1, rp2 = 0, 0

for row in input:
    row = row.replace('\t',' ').strip().split(' ')
    row = [int(i) for i in row]

    #Part1
    row = sorted(row, reverse=True)
    max, min = row[0],row[-1]
    rp1 += max-min

    #Part2
    for i in row:
        for j in row:
            if i != j  and i % j == 0:
                rp2 += i//j

result(day,year,rp1,rp2)




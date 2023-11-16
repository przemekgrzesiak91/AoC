# Day 3 (2017)
from aocd import get_data
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def result(day,year,rp1, rp2):
    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + str(year)+ Fore.YELLOW + ' *')
    print('Result for ' + Fore.CYAN + 'Day ' + str(day))
    print(Fore.CYAN + str(rp1))
    print(Fore.CYAN + str(rp2))

day = 3     #Edit this
year = 2017 #Edit this

filepath = 'data/day' + str(day) + '.txt'
with open(filepath, 'r') as f:
    input = f.readlines()[0].strip()

# Result for part 1 & 2
rp1, rp2 = 0, 0

### Code here

def count_steps(number):
    k = 1
    while k ** 2 < number:
        k += 2

    if k == 1:
        return 0

    start = k // 2
    cords = [start,-start]

    #
    if number >= k**2 - (k-1):
        cords = [start - (k**2 - number), -start]
    elif number >= k**2 - 2*(k-1):
        cords = [-start,-start+(k**2 - k-1 - number)]
    elif number >= k**2 - 3*(k-1):
        cords = [-start +(k**2- 2*(k-1) - number),start]
    elif number > k**2 - 4*(k-1):
        cords = [start,start - (k**2 - 3*(k-1) - number)]

    return (abs(cords[0])+abs(cords[1]))



#count_steps(int(input))
rp1 = count_steps(int(input))

result(day,year,rp1,rp2)
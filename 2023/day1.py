# Day 1 (2023)
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def result(day,year,rp1, rp2):
    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + str(year)+ Fore.YELLOW + ' *')
    print('Result for ' + Fore.CYAN + 'Day ' + str(day))
    print(Fore.CYAN + str(rp1))
    print(Fore.CYAN + str(rp2))

day = 1     #Edit this
year = 2023 #Edit this

filepath = 'data/day' + str(day) + '.txt'
with open(filepath, 'r') as f:
    input = f.readlines()

# Result for part 1 & 2
rp1, rp2 = 0, 0

### Code here

result(day,year,rp1,rp2)
# Day 4 (2017)
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def result(day,year,rp1, rp2):
    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + str(year)+ Fore.YELLOW + ' *')
    print('Result for ' + Fore.CYAN + 'Day ' + str(day))
    print(Fore.CYAN + str(rp1))
    print(Fore.CYAN + str(rp2))

day = 4    #Edit this
year = 2017 #Edit this

filepath = 'data/day' + str(day) + '.txt'
with open(filepath, 'r') as f:
    input = f.readlines()

# Result for part 1 & 2
rp1, rp2 = 0, 0

### Code here
def check_valid(input):
    n_valid = 0
    for row in input:
        row = row.strip().split(' ')
        if len(row) == len(set(row)): n_valid+=1
    return n_valid

def check_valid2(input):
    n_valid = 0
    for row in input:
        row = row.strip().split(' ')

        new_row = [''.join(sorted(list(word))) for word in row]
        if len(new_row) == len(set(new_row)): n_valid += 1
    return n_valid


rp1 = check_valid(input)
rp2 = check_valid2(input)

result(day,year,rp1,rp2)
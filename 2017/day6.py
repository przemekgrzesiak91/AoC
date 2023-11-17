# Day 6 (2017)
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def result(day,year,rp1, rp2):
    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + str(year)+ Fore.YELLOW + ' *')
    print('Result for ' + Fore.CYAN + 'Day ' + str(day))
    print(Fore.CYAN + str(rp1))
    print(Fore.CYAN + str(rp2))

day = 6     #Edit this
year = 2017 #Edit this

filepath = 'data/day' + str(day) + '.txt'
with open(filepath, 'r') as f:
    input = f.readline().strip().split('\t')

# Result for part 1 & 2
rp1, rp2 = 0, 0

### Code here
input = [int(x) for x in input]
print(input)

n = len(input)
def find_max(banks):
    max_value = max(banks)
    id = banks.index(max_value)

    return id

def distribute(banks):
    seen = []
    seen.append(banks)
    current = banks.copy()

    while current != seen:
        id = find_max(banks)
        value = banks[id]

        blocks = value % n-1
        print(value, n-1)
        banks = [banks[i]+blocks for i in range(0,len(banks)) if i != id]
        print(banks)


print(distribute(input))

result(day,year,rp1,rp2)
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

#input = [0,2,7,0]

n = len(input)
def find_max(banks):
    max_value = max(banks)
    id = banks.index(max_value)

    return id

def distribute(banks):
    seen = []
    current = banks.copy()
    cycle = 0

    while current not in seen:
        seen.append(current)
        id = find_max(current)
        value = current[id]

        blocks = value // (n-1)
        print(id,blocks)

        current = [current[i]+blocks if i!=id else current[i]-blocks*(n-1) for i in range(0,len(current))]
        print(current)
        print(seen)
        cycle += 1
    return cycle

rp1 = (distribute(input))

result(day,year,rp1,rp2)
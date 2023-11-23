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

def distribute(banks,part=1):
    seen = []
    current = banks.copy()
    cycle = 0
    n = len(banks)

    while current not in seen:

        seen.append(current.copy())
        id = find_max(current)
        value = current[id]
        #print('--',id)
        j = id
        current[id] = 0

        for i in range(value):
            if j+1 < n: j+=1
            else: j=0

            current[j] += 1
        cycle += 1

    if part == 1:   return cycle
    if part == 2:
        cycle = -1

        repeated = current.copy()
        seen = []

        while seen.count(repeated) < 2:

            seen.append(current.copy())
            id = find_max(current)
            value = current[id]
            # print('--',id)
            j = id
            current[id] = 0

            for i in range(value):
                if j + 1 < n:
                    j += 1
                else:
                    j = 0

                current[j] += 1
            cycle += 1
        return cycle

rp1 = distribute(input)
rp2 = distribute(input,2)

result(day,year,rp1,rp2)
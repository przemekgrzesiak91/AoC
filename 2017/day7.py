# Day 7 (2017)

'''Info
library - NetworkX - https://www.reddit.com/r/adventofcode/comments/7i44pg/comment/dqw0f0c/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

'''

from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def result(day,year,rp1, rp2):
    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + str(year)+ Fore.YELLOW + ' *')
    print('Result for ' + Fore.CYAN + 'Day ' + str(day))
    print(Fore.CYAN + str(rp1))
    print(Fore.CYAN + str(rp2))

day = 7     #Edit this
year = 2017 #Edit this

filepath = 'data/day' + str(day) + '.txt'
with open(filepath, 'r') as f:
    input = f.readlines()

# Result for part 1 & 2
rp1, rp2 = 0, 0

### Code here
map = {}

for row in input:
    row = row.strip().replace(',','').split(' ')
    if len(row) == 2:
        value = int(row[1].replace('(','').replace(')',''))
        map[row[0]] = [value]
    else:
        map[row[0]] = [value,row[3:]]

#print(map)
def find_bottom(map):
    for key in map.keys():
        seen = 0
        for value in map.values():
            if len(value) > 1:
                if key in value[1]:
                    seen = 1
        if seen == 0:
            return key

rp1 = find_bottom(map)

result(day,year,rp1,rp2)
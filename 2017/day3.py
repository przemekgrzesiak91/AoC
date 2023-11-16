# Day 3 (2017)
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


def check_neighbours(spiral, current_pos):
    directions = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    sum = 0
    for direction in directions:
        neighbour = (current_pos[0]+direction[0],current_pos[1]+direction[1])
        if neighbour in spiral:
            sum += spiral[neighbour]
    return sum

def create_spiral(number):
    spiral = {(0,0):1}

    r = 1
    current_pos = (0,0)
    while True:
        current_pos = (current_pos[0] + 1, current_pos[1])
        spiral[current_pos] = check_neighbours(spiral,current_pos)
        #while current_pos!=r or current_pos!=-r:
        while current_pos[1]< r:
            current_pos = (current_pos[0],current_pos[1]+1)
            value=check_neighbours(spiral, current_pos)
            if value > number:
                return value
            else:
                spiral[current_pos] = value

        while current_pos[0]>-r:
            current_pos = (current_pos[0]-1, current_pos[1])
            value = check_neighbours(spiral, current_pos)
            if value > number:
                return value
            else:
                spiral[current_pos] = value

        while current_pos[1]>-r:
            current_pos = (current_pos[0], current_pos[1]-1)
            value = check_neighbours(spiral, current_pos)
            if value > number:
                return value
            else:
                spiral[current_pos] = value
        while current_pos[0]<r:
            current_pos = (current_pos[0]+1, current_pos[1])
            value = check_neighbours(spiral, current_pos)
            if value > number:
                return value
            else:
                spiral[current_pos] = value
        r += 1



rp1 = count_steps(int(input))
rp2 = create_spiral(int(input))


result(day,year,rp1,rp2)
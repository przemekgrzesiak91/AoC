# Day 5 (2017)
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def result(day,year,rp1, rp2):
    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + str(year)+ Fore.YELLOW + ' *')
    print('Result for ' + Fore.CYAN + 'Day ' + str(day))
    print(Fore.CYAN + str(rp1))
    print(Fore.CYAN + str(rp2))

day = 5    #Edit this
year = 2017 #Edit this

filepath = 'data/day' + str(day) + '.txt'
with open(filepath, 'r') as f:
    input = f.readlines()
    input = [int(line.strip()) for line in input]

# Result for part 1 & 2
rp1, rp2 = 0, 0

### Code here

def walk_maze(maze):
    maze1 = maze.copy()
    current_pos = 0
    steps = 0

    while current_pos<len(maze1):
        next_pos = maze1[current_pos]
        maze1[current_pos] += 1
        current_pos += next_pos
        steps += 1

    return steps

def walk_maze2(maze):
    maze2 = maze.copy()
    current_pos = 0
    steps = 0

    while current_pos<len(maze2):
        next_pos = maze2[current_pos]
        if maze2[current_pos] >= 3:
            maze2[current_pos] -= 1
        else:
            maze2[current_pos] += 1
        current_pos += next_pos
        steps += 1

    return steps

rp1 = walk_maze(input)
rp2 = walk_maze2(input)

result(day,year,rp1,rp2)
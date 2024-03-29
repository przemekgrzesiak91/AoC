# Day 14 (2023)
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 14    #Edit this
year = 2023 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = []
        for line in f:
            input.append(line.strip())
    return input

def solve_part1(input):
    """Solve part 1."""
    n = len(input)
    m = len(input[0])
    rp1 =0

    for i in range(0,m):
        col = [row[i] for row in input]
        for j in range(0,n):
            while j>0 and col[j]=='O':

                if col[j-1]=='.':
                    col[j],col[j-1] = col[j-1],col[j]
                j -= 1

        for j in range(0,n):
            if col[j]=='O':
                rp1 += n-j


    return rp1

def solve_part2(input):
    """Solve part 2."""
    return 0

def result(day,year):
    input = parse()
    rp1 = solve_part1(input)
    rp2 = solve_part2(input)


    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + str(year)+ Fore.YELLOW + ' *')
    print('Result for ' + Fore.CYAN + 'Day ' + str(day))
    print(Fore.CYAN + str(rp1))
    print(Fore.CYAN + str(rp2))


if __name__ == "__main__":
    result(day,year)

from colorama import Fore, init
from jupyter_core.version import pattern

# Initialize colorama
init(autoreset=True)

day = 2     #Edit this
year = 2025 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.read().replace('\n','').split(',')
    return input

def solve_part1(input):
    """Solve part 1."""
    invalid = []

    for i in input:
        min, max = [int(num) for num in i.split('-')]

        for x in range(min, max+1):
            new_x = list(str(x))
            len_x = len(new_x)

            a = new_x[:(len_x//2)]
            b = new_x[(len_x//2):]

            if a == b:
                invalid.append(x)



    return sum(invalid)

def solve_part2(input):
    """Solve part 2."""

    invalid = [0,]

    for i in input:
        min, max = [int(num) for num in i.split('-')]

        for x in range(min, max + 1):
            new_x = list(str(x))
            len_x = len(new_x)

            for y in range((len_x//2)):
                pattern = new_x[:y+1]
                len_p = len(pattern)
                if len_x % len_p != 0: continue
                else:
                    if all(new_x[z:z + len_p] == pattern for z in range(0, len_x, len_p)):

                        if invalid[-1] != x:
                            #print(x)
                            invalid.append(x)
                            continue

    return sum(invalid)

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

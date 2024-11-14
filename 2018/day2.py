from colorama import Fore, init
from collections import Counter

# Initialize colorama
init(autoreset=True)

day = 2     #Edit this
year = 2018 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = [line.strip() for line in f.readlines()]
    print(input)
    return input

def solve_part1(input):
    """Solve part 1."""
    result = 0
    twice = 0
    triple = 0

    for row in input:
        elem_count = Counter(row)
        if 2 in elem_count.values(): twice += 1
        if 3 in elem_count.values(): triple += 1


    return twice*triple

def solve_part2(input):
    """Solve part 2."""


    for i in range(0,len(input)):
        k = i
        for j in range(i+1,len(input)):
            result = ''
            diff_count = 0
            list1 = list(input[i])
            list2 = list(input[j])

            min_len = min(len(list1),len(list2))
            for k in range(min_len):
                if list1[k] != list2[k]:
                    diff_count += 1
                else:
                    result += list1[k]

            if diff_count == 1:
                return result

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

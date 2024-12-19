from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 9     #Edit this
year = 2024 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = [int(x) for x in list(f.read())]
    return input

def solve_part1(input):
    """Solve part 1."""
    #print(input)
    disk = []
    id = 0
    result = 0

    for i in range(len(input)):
        digit = input[i]

        if (i+1)%2 != 0:
            disk.extend(digit*[id])
            id+=1

        else:
            disk.extend(digit*['.'])

    #print(disk)

    for i in range(len(disk)):
        if all(c == '.' for c in disk[i:]): break
        block = disk[i]
        if block == '.':
            for j in range(1,len(disk)):
                rev_block = disk[-j]
                if rev_block != '.':
                    disk[i],disk[-j] = disk[-j],disk[i]
                    result += i * disk[i]
                    break
        else:
            result += i * block

    # VEEEEEERY SLOW
    return result

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

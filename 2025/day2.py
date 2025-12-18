from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 2     #Edit this
year = 2025 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.read().replace('\n','').split(',')
    return input

def is_double(s: str) -> bool:
    mid = len(s) // 2
    return s[:mid] == s[mid:]


def solve_part1(ranges):
    invalid = set()
    for r in ranges:
        lo, hi = map(int, r.split('-'))
        for x in range(lo, hi + 1):
            if is_double(str(x)):
                invalid.add(x)
    return sum(invalid)


def solve_part2(input_ranges):
    invalid = set()

    for r in input_ranges:
        lo, hi = map(int, r.split('-'))

        for x in range(lo, hi + 1):
            s = str(x)
            n = len(s)

            for size in range(1, n//2 + 1):
                if n % size != 0:
                    continue
                pattern = s[:size]
                if pattern * (n // size) == s:
                    invalid.add(x)
                    break  # nie musimy sprawdzać większych wzorców

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

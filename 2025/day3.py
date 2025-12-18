from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 3     #Edit this
year = 2025 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with (open(filepath, 'r') as f):
        input = f.read().splitlines()

    return input

def solve_part1(input_lines):
    """Solve part 1."""
    total = 0
    for line in input_lines:
        digits = list(map(int, line))
        max_joltage = max(int(str(a) + str(b)) for i, a in enumerate(digits) for b in digits[i + 1:])
        total += max_joltage
    return total


def solve_part2(input_lines):
    total = 0
    n = 12  # liczba cyfr do włączenia

    for line in input_lines:
        digits = list(map(int, line))
        result = []
        to_pick = n

        for i, d in enumerate(digits):
            while result and d > result[-1] and len(result) - 1 + len(digits) - i >= to_pick:
                result.pop()
            if len(result) < to_pick:
                result.append(d)

        max_joltage = int(''.join(map(str, result)))
        total += max_joltage

    return total


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

from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 1     #Edit this
year = 2025 #Edit this

def parse():
    filepath = f"data/day{day}.txt"
    with open(filepath, 'r') as f:
        return f.read().strip().splitlines()

def solve_part1(data):
    start = 50
    count_zero = 0

    for line in data:
        direction, value = line[0], int(line[1:])

        if direction == "R":
            start = (start + value) % 100
        else:
            start = (start - value) % 100

        if start == 0:
            count_zero += 1

        #print(line, "-", start, "-", count_zero)

    return count_zero


def solve_part2(data):
    start = 50
    hits = 0

    for line in data:
        direction = line[0]
        value = int(line[1:])

        if direction == "R":
            first = (100 - start) % 100
            if first == 0:
                first = 100

            if first <= value:
                hits += 1 + (value - first) // 100

            start = (start + value) % 100

        else:  # L
            first = start % 100
            if first == 0:
                first = 100

            if first <= value:
                hits += 1 + (value - first) // 100

            start = (start - value) % 100

    return hits


def result(day,year):
    data = parse()
    rp1 = solve_part1(data)
    rp2 = solve_part2(data)


    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + str(year)+ Fore.YELLOW + ' *')
    print('Result for ' + Fore.CYAN + 'Day ' + str(day))
    print(Fore.CYAN + str(rp1))
    print(Fore.CYAN + str(rp2))


if __name__ == "__main__":
    result(day,year)

from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 1     #Edit this
year = 2025 #Edit this

def parse():
    filepath = f"data/day{day}.txt"
    with open(filepath, 'r') as f:
        return f.read().strip().splitlines()

def solve_part1(data: list[str]) -> int:
    pos = 50
    hits = 0

    for line in data:
        step = int(line[1:])
        pos += step if line[0] == "R" else -step
        pos %= 100

        if pos == 0:
            hits += 1

    return hits



def solve_part2(data: list[str]) -> int:
    pos = 50
    hits = 0

    for line in data:
        step = int(line[1:])
        direction = 1 if line[0] == "R" else -1

        distance_to_zero = (100 - pos) % 100 if direction == 1 else pos % 100
        if distance_to_zero == 0:
            distance_to_zero = 100

        if distance_to_zero <= step:
            hits += 1 + (step - distance_to_zero) // 100

        pos = (pos + direction * step) % 100

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

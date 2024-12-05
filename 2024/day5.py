from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 5     #Edit this
year = 2024 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        pages,orders = f.read().strip().split('\n\n')

    pages = list(pages.split('\n'))

    pages_dict = {}

    for x in pages:
        a,b = [int(i) for i in x.split('|')]

        if a not in pages_dict:
            pages_dict[a] = []

        pages_dict[a].append(b)

    orders = [list(map(int, line.split(','))) for line in orders.strip().splitlines()]

    return pages_dict, orders

def solve_part1(input):
    """Solve part 1."""
    pages_dict, orders = input
    result = 0

    for order in orders:
        correct = True
        n=len(order)
        order = order[::-1]
        for i in range(n-1):
            check = order[i+1:]
            if order[i] in pages_dict:
                common_elements = set(order[i+1:]) & set(pages_dict[order[i]])
                if common_elements:
                    correct=False

        if correct:
            mid_id = round(n//2)
            result += order[mid_id]


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

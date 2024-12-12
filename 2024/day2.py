from colorama import Fore, init
from django.contrib.sitemaps.views import index

# Initialize colorama
init(autoreset=True)

day = 2     #Edit this
year = 2024 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = [list(map(int, line.split())) for line in f]
        #print(input)
    return input

def solve_part1(input):
    """Solve part 1."""
    result = 0
    for x in input:
        n_diff = 0
        if x[0]>x[1]:
            #decreasing
            x = x[::-1]

        for i in range(len(x)-1):
            diff = x[i+1]-x[i]

            if diff not in (1,2,3): n_diff += 1
        if n_diff==0:
            result+=1


    return result


def solve_part2(input):
    """Solve part 2."""
    result = 0

    for x in input:
        print()
        print(input.index(x), x,end=' ')
        # Sprawdzamy różnice między kolejnymi elementami
        n_diff = 0

        # Jeśli lista jest malejąca, odwracamy ją
        if x[0] > x[1] :
            x = x[::-1]

        # Sprawdzamy, czy różnice między wszystkimi kolejnymi elementami są w zakresie 1, 2, 3
        for i in range(len(x) - 1):
            diff = x[i + 1] - x[i]
            if diff not in (1, 2, 3):
                n_diff += 1
        # Jeśli żadna różnica nie jest poza zakresem (1, 2, 3), dodajemy wynik
        if n_diff == 0:
            print('OK - ')
            result += 1
        else:
            # Spróbuj usunąć jeden element i sprawdź ponownie
            x = x[::-1]
            for j in range(len(x)):
                temp_x = x[:j] + x[j + 1:]  # Usuwamy element z indeksu j
                if temp_x[0] > temp_x[1]:
                    temp_x = temp_x[::-1]
                print(temp_x)
                n_diff = 0
                for i in range(len(temp_x) - 1):
                    diff = temp_x[i + 1] - temp_x[i]
                    if diff not in (1, 2, 3):
                        n_diff += 1

                if n_diff == 0:
                    print('OK - ')
                    result += 1
                    break
                #print('bad - ', n_diff, temp_x)

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

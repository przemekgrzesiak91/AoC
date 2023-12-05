# Day 4 (2023)
from colorama import Fore, init
import re

# Initialize colorama
init(autoreset=True)

day = 4     #Edit this
year = 2023 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        input = f.readlines()
    return input

def solve_part1(input):
    """Solve part 1."""
    rp1 = 0
    cards = {}
    for card in input:
        numbers = re.findall(' \d+',card)
        n_card, winning, your_numbers = int(numbers[0]),[int(x) for x in numbers[1:11]],[int(x) for x in numbers[11:]]
        card_point = 0
        n_winning = 0
        for win_num in winning:
            if win_num in your_numbers:
                n_winning +=1
                if card_point==0:
                    card_point = 1
                else:
                    card_point *= 2

        cards[n_card] = [n_winning,1]
        rp1 += card_point

    return rp1, cards

def solve_part2(input):
    """Solve part 2."""
    rp2 = 0
    for card in input.keys():
        copies = input[card][0]
        print(card, ' --',copies)
        for i in range(card+1,copies+2):
            input[i][1] += 1
    print(input)

    for card in input.keys():
        rp2 += input[card][1]

    return rp2

def result(day,year):
    input = parse()
    rp1, cards  = solve_part1(input)
    rp2 = solve_part2(cards)


    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + str(year)+ Fore.YELLOW + ' *')
    print('Result for ' + Fore.CYAN + 'Day ' + str(day))
    print(Fore.CYAN + str(rp1))
    print(Fore.CYAN + str(rp2))


if __name__ == "__main__":
    result(day,year)
